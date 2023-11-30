from hugchat import hugchat
from hugchat.login import Login
import clsResponse


def ask_hugging_chat(isNewChat: bool, question: str)-> clsResponse.Response:
    try:
        # Log in to huggingface and grant authorization to huggingchat
        print("Before singin")
        #sign = Login('christoskarathanasisac@gmail.comtest', 'Mai23021@uom.edu.gr')
        sign = Login('christoskarathanasisac@gmail.com', 'Mai23021@uom.edu.gr')
        
        cookies = sign.login()

        print("sing in ok")
        # Save cookies to the local directory
        cookie_path_dir = "./cookies_snapshot"
        sign.saveCookiesToDir(cookie_path_dir)

        print("cookies ok")

        # Load cookies when you restart your program:
        # sign = login(email, None)
        # cookies = sign.loadCookiesFromDir(cookie_path_dir) # This will detect if the JSON file exists, return cookies if it does and raise an Exception if it's not.

        # Create a ChatBot
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"

        print("chatbot ok")

        if(isNewChat):
           # Create a new conversation
            print("Is new CHAT")
            id = chatbot.new_conversation()
            chatbot.change_conversation(id)
        

        query_result = chatbot.query(question)
        print(query_result)

        response = clsResponse.Response(True,'',query_result.text)
        return response
    except Exception as e:
        #If connection to db is still open --> Close
        response = clsResponse.Response(False,e,None)
        return response