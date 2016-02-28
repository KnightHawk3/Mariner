class Trigger:
    def __init__(self, message, response):
        self.message = message
        self.response = response

    def is_triggered(self, message):
        if self.message in message:
            return True
        return False
    
    def output(self, message):
        return self.message
