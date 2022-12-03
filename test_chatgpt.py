from chatgpt import ChatGPT
import os
bearer = os.getenv('CHATGPT_BEARER')
assert bearer, "Please set the CHATGPT_BEARER environment variable"
cgpt = ChatGPT(bearer)

print('chatting with chatGPT...')
query = "I'm planning for a bike trip.  What should I bring and where are the best places in the world to go?"
response = cgpt.chat(query)
query_2 = "If I choose Morocco, where would be a good place to go?"
response_2 = cgpt.chat(query_2)

for i, response in enumerate(cgpt.response_history):
    print(cgpt.prompt_history[i])
    print(cgpt.response_history[i])