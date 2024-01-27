import time
import concurrent.futures
import openai
"""
接收path
读keyword
根据图片生成问题
返回一个问题
"""

openai.api_key = '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'
total_threads = 1


def make_request(keyword):
    try:
        system_message = ("You are an environmentally-friendly AI chatbot. Your major task is to generate a "
                            "environment-related multiple-choice question based on a specific object inputted by "
                            "the user and gives a correct answer. The question you generated needs to be meaningful "
                            "and have educational purposes.")

        user_message = (f"Please give me one environment-related, meaningful, energy-consumption-related "
                        f"multiple-choice quiz"
                        f"regarding a general {keyword}. With the format Question: A) B) C) D) E); Correct Answer:")

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages, max_tokens=700, top_p=0.1,
                                                frequency_penalty=0, presence_penalty=0, stop=None, timeout=20)
        generated_content = response['choices'][0]['message']['content']
        return extract_question_and_answer(generated_content)

    except Exception as e:
        print(f"Request failed with {str(e)}, retrying...")
        # If the request failed, sleep for a while before retrying
        time.sleep(1)


def extract_question_and_answer(generated_content):
    # Split the GPT output into lines
    lines = generated_content.split('\n')

    # Extract the question
    question_line = next((line for line in lines if line.startswith("Question: ")), None)
    question = question_line[len("Question: "):] if question_line else ""

    # Extract the answer choices
    answer_choice_lines = [line for line in lines if line.startswith(("A) ", "B) ", "C) ", "D) ", "E) "))]
    answer_choices = [choice.strip() for choice in answer_choice_lines]

    # Extract the correct answer
    correct_answer_line = next((line for line in lines if line.startswith("Correct Answer: ")), None)
    correct_answer = correct_answer_line[len("Correct Answer: "):].strip()[0] if correct_answer_line else ""

    # Create the dictionary
    result_dict = {"question": question, "choices": "\n".join(answer_choices), "answer": correct_answer}

    return result_dict


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


def game_bot_interaction(keyword):
    if keyword is None:
        raise ValueError("Keyword is None. Handling exception.")
    return multi_threading(keyword)
