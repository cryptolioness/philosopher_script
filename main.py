import openai
import os

# Load your API key from an environment variable\
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ["OPENAI_API_KEY"]


def get_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0
    )

    message = response.choices[0].message.content.strip()
    return message


def add_prompt_to_messages(messages, prompt):
    messages.append({"role": "user", "content": prompt})
    return messages


def init_prompt_list():
    messages = [
        {"role": "system", "content": "You are an expert on ethics as it applies to artificial intelligence. You are having a conversation with a philosopher about the ethics of artificial intelligence. Be collaborative and concise, but imaginative with liberal use of metaphors."},
    ]
    return messages


def add_response_to_messages(messages, response):
    messages.append({"role": "assistant", "content": response})
    return messages


def get_prompt_from_user():
    prompt = input("Ask the philosopher chatbot a question: ")
    return prompt


def main():
    messages = init_prompt_list()

    while True:
        prompt = get_prompt_from_user()
        messages = add_prompt_to_messages(messages, prompt)
        response = get_response(messages)
        messages = add_response_to_messages(messages, response)
        print(response)

        if prompt == "quit":
            break


if __name__ == "__main__":
    main()

