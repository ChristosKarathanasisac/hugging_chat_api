from flask import Flask,request
import hugging_chat_utilities
import clsResponse

# Create a Flask web server
app = Flask(__name__)

@app.route('/use_hagging_chat', methods=['POST'])
def use_hagging_chat():
    try:   
      requestDataDict = request.get_json()
      newChatFlag = requestDataDict['newChat']
      inputQuestion = requestDataDict['inpout']
      conversation_id = requestDataDict['conversation_id']

      respData = hugging_chat_utilities.ask_hugging_chat(newChatFlag,inputQuestion,conversation_id)
      obj_dict = vars(respData)
      return obj_dict
    except Exception as e:
         response = clsResponse.Response(False,e,None)
         obj_dict = vars(response)
         return response  

# Run the Flask app on localhost, port 5000
if __name__ == '__main__':
    app.run(host='localhost', port=5001)