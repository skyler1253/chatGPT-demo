# chatGPT-demo

Quick Start:

1. Grab your bearer token from: https://chat.openai.com/chat
2. Open the Network Tab in Developer Tools
3. Type something in the chat and enter
4. Look for fetch to https://chat.openai.com/backend-api/conversation
5. In the request header look for authorization then get the Bearer Token


```
export CHATGPT_BEARER=<your_bearer_token>
python test_chatgpt.py
```


