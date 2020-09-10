from flask import Flask,render_template,request,jsonify
#import numpy as np
import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        #operation=request.form['operation']
        num1=float(request.form['num1'])
        num2 =float(request.form['num2'])
        num3 =float(request.form['num3'])
        int_features = []
        int_features.append(num1)
        int_features.append(num2)
        int_features.append(num3)

        output = num1+num2+num3



        # if(operation=='add'):
        #     r=num1+num2
        #     result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        # if (operation == 'subtract'):
        #     r = num1 - num2
        #     result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        # if (operation == 'multiply'):
        #     r = num1 * num2
        #     result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        # if (operation == 'divide'):
        #     r = num1 / num2
        #     result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=output)  


if __name__ == '__main__':
    app.run(debug=True)          