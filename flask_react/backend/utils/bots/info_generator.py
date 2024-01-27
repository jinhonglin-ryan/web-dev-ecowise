import imp
import re
import time
import concurrent.futures
import openai
from .object_detection import localize_objects

openai.api_key = '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'
total_threads = 1


def make_request(keyword):
    try:
        system_message = ("You are an environmentally-friendly AI chatbot. Your major task is to provide users with"
                            "environmentally-friendly information based on their input (usually the name of an energy"
                            "consumption device).")

        user_message = (f"What is the general energy consumption information about a general {keyword} and your "
                        f"advice to save energy with respect to the use of this device (keep it short within 75 "
                        f"words)")

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=700, top_p=0.1,
                                                frequency_penalty=0, presence_penalty=0, stop=None, timeout=20)
        result = [response['choices'][0]['message']['content'], keyword]
        # Save result for each response
        # print(result)
        return result

    except Exception as e:
        print(f"Request failed with {str(e)}, retrying...")
        # If the request failed, sleep for a while before retrying
        time.sleep(1)


def multi_threading(keyword):
    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=total_threads) as executor:

        def wrapper(keyword):
            try:
                return make_request(keyword)
            except Exception as e:
                print(f"Error in thread: {str(e)}")

        # Submit tasks and store Future objects in a dictionary
        futures = {executor.submit(wrapper, keyword): i for i in range(total_threads)}

        # Wait for all threads to complete
        for future in concurrent.futures.as_completed(futures):
            try:
                index = futures[future]
                result = future.result()
                results[index] = result
            except Exception as e:
                print(f"Error getting result: {str(e)}")

    return results[0]


def info_generator_interaction(binary_info):
    keyword = localize_objects(binary_info)
    print(keyword)
    if keyword is None:
        raise ValueError("Keyword is None. Handling exception.")
    return multi_threading(keyword)
