import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)


def chat_with_gpt(
    model, user_message, top_p=1, frequency_penalty=0, presence_penalty=0,temperature=0
):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful conversational AI expert.",
                },
                {"role": "user", "content": user_message},
            ],
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            temperature=temperature
        )
        return response
    except Exception as e:
        return str(e)
    
# Example usage
response = chat_with_gpt(
    "gpt-3.5-turbo",
    "Suggest a good name for a customer support chatbot working for a holiday company",
    top_p=0.9,
    frequency_penalty=-0.5,
    presence_penalty=0.6,
)
