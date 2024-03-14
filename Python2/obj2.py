class Calculator:

    def __init__(self):

        self.result = 0
    def add(self,b,d):

        self.result =b+d
        return self.result
    def subtract(self,b,d):
        self.result=b-d
        return self.result

    def multiply(self,b,d):
        self.result=b*d
        return self.result

    def divide(self ,b,d):
        self.result=b / d
        return self.result

calc = Calculator()

