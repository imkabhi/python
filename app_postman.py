from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/postman_action', methods = ['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if ops == 'add':
            r = num1 + num2
            result = 'The Sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if ops == 'subtract':
            r = num1 - num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if ops == 'multiply':
            r = num1 * num2
            result = 'The multiply of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if ops == 'divide':
            r = num1 / num2
            result = 'The division of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r) 
        return jsonify(result)       

if __name__=="__main__":
    app.run(host="0.0.0.0")
