import openai

def run(prompt):
    # Your OpenAI API key here
    api_key = ""

    # Initialize the OpenAI API client
    openai.api_key = api_key

    # Make the API call to get the code
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message['content']