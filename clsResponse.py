class Response:
   def __init__(self, success: bool, errorMsg: str,data,conversation_id):
        # Instance attributes
        self.success = success
        self.error = errorMsg
        self.data = data
        self.conversation_id = conversation_id