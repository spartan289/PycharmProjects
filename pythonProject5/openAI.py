import os
import openai
openai.api_key = "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"

user_input=input("Ask me Anything: ")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": user_input}
  ],
    temperature=0.2,
    max_tokens=100
)
#print(completion)
#print(completion.usage)
print(completion.choices[0].message.content)
#print(completion.choices[0].content)

