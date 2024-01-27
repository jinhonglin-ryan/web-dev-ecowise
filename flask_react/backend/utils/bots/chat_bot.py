import openai
import concurrent.futures

openai.api_key = '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'


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()


def process_user_input(user_input):
    prompt = f"User: {user_input}\nAI:"
    return generate_response(prompt)


def chatbot_interaction(user_full_input):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            if check_ended(user_full_input):
                return "Conversation ended."

            # Submit user input for processing in a separate thread
            future = executor.submit(process_user_input, user_full_input)

            # Wait for the result
            ai_response = future.result()

            return ai_response


def check_ended(user_full_input):
    if user_full_input == 'exit':
        return 1

