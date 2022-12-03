import json
import requests
import uuid

class ChatGPT():
    def __init__(self, bearer):
        self.bearer = bearer
        self.task_sleep_seconds = 3
        self.parent_message_id = None
        self.conversation_id = None
        self.prompt_history = []
        self.response_history = []

    def chat(self, query):
        self.prompt_history.append(query)
        response = self.get_response(query, parent_message_id=self.parent_message_id, conversation_id=self.conversation_id)
        if response.status_code == 200:
            chatGPT_response = json.loads(response.text.split('\n\ndata: ')[-2])
            self.conversation_id = chatGPT_response['conversation_id']
            self.parent_message_id = chatGPT_response['message']['id']
            
            self.response_history.append(chatGPT_response['message']["content"]["parts"]) 
            return chatGPT_response['message']["content"]["parts"]

        else:
            print(response.text)
            print(response.status_code)
            return None

    def get_response(self, query, parent_message_id=None, conversation_id=None):

        message_id = str(uuid.uuid4()) #generate a random message id

        #parent message id is the id of the message that chatGPT responds with.  If this is the first message, it is random
        if not parent_message_id:
            parent_message_id = str(uuid.uuid4()) 

        body = {
                "action":"next",
                "messages":[
                    {
                        "id":message_id,
                        "role":"user",
                        "content":{
                            "content_type":"text",
                            "parts":[
                            query
                            ]
                        }
                    }
                ],
                "parent_message_id":parent_message_id,
                "model":"text-davinci-002-render"
                }
        
        #conversation id is only included if this message is a response to a previous message
        if conversation_id:
            body['conversation_id'] = conversation_id

        url = "https://chat.openai.com/backend-api/conversation"
        headers = {
            'Authorization': "Bearer " + self.bearer,
            'Content-Type': "application/json",
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))
        return response