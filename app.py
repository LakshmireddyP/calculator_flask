from flask import Flask,request,render_template

obj=Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to the flask"
obj.route("/cal",methods=['GET'])
def math_operations(operation,num1,num2):
    if operation=="add":
        result=num1+num2
    elif operation=="sub":
        result=num1-num2
    elif operation=="mul":
        result=num1*num2
    return f'The {operation} of {num1},{num2} is {result}'
if __name__=="__main__":
    obj.run(debug=True)

