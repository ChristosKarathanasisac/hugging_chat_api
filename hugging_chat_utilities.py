from hugchat import hugchat
from hugchat.login import Login
import clsResponse


def ask_hugging_chat(isNewChat: bool, question: str,id)-> clsResponse.Response:
    try:
        #By default ID -999 for new conversation
        conversation_id = "-999"
        # Log in to huggingface and grant authorization to huggingchat
        sign = Login('christoskarathanasisac@gmail.com', 'Mai23021@uom.edu.gr')
        
        cookies = sign.login()

        #print("sing in ok")
        # Save cookies to the local directory
        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)

        # Create a ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

        #print("chatbot ok")

        if(isNewChat):
           # Create a new conversation
            #print("Is new CHAT")
            conversation_id = chatbot.new_conversation()
            chatbot.change_conversation(conversation_id)
        else:
            #conversation_list = chatbot.get_conversation_list()
            conversation_list = chatbot.get_remote_conversations(replace_conversation_list=True)
            found_object = None
            flag = False
            for item in conversation_list:
             if item.id == id:
              found_object = item
              conversation_id = found_object.id
              chatbot.change_conversation(found_object)
              flag = True
              break
            if(flag != True):
                response = clsResponse.Response(False,'conversation missing. Create a new one!','','-999')
                return response 
            
        

        query_result = chatbot.query(question)
        #If I remove the print query_result.text will be empty
        print(query_result)

        response = clsResponse.Response(True,'',query_result.text,conversation_id.id)
        return response
    except Exception as e:
        #If connection to db is still open --> Close
        response = clsResponse.Response(False,e,None,-999)
        return response