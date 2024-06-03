import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)



def chat_with_gpt(
    messages, user_message, top_p=1, frequency_penalty=0, presence_penalty=0,temperature=0
):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            temperature=temperature
        )
        print(str(response.choices[0].message))
        return response.choices[0].message["content"]
        return response
    except Exception as e:
        return str(e)

    
messages =  [  
{'role':'system', 'content':'You are travel agency chatbot.'},
{'role':'user', 'content':'Hi, my name is Adrian'},
{'role':'assistant', 'content': "Hi Adrian! \
Is there anything I can help you with today?"},
{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
response = get_completion_from_messages(messages, temperature=1)

    
# Example usage
response = chat_with_gpt(
    messages,
    "gpt-3.5-turbo",
    top_p=0.9,
    frequency_penalty=-0.5,
    presence_penalty=0.6,
)
print(str(response.choices[0].message))