from flask import Flask,request

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to the flask"
@obj.route("/cal",methods=['GET'])
def math_operations():
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]
    if operation=="add":
        result=int(num1)+int(num2)
    elif operation=="sub":
        result=int(num1)-int(num2)
    elif operation=="mul":
        result=int(num1)*int(num2)
    return f' the {operation} of {num1},{num2} is {result}'
if __name__=="__main__":
    obj.run(debug=True)

