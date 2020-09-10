from flask import Flask,render_template,request,jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


def new_marriage_func(years_married):
    if years_married < 3:
        return 1
    else:
        return 0 

def no_children_func(number_of_children):
    if number_of_children == 0:
        return 1
    else:
        return 0


@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        #operation=request.form['operation']
        rate_marriage=float(request.form['num1'])
        age =float(request.form['num2'])
        religious =float(request.form['num3'])
        years_married = int(request.form['num4'])
        number_of_children = int(request.form['num5'])

        new_marriage = new_marriage_func(years_married)
        no_children = no_children_func(number_of_children)








        int_features = []
        int_features.append(rate_marriage)
        int_features.append(age)
        int_features.append(religious)
        int_features.append(new_marriage)
        int_features.append(no_children)

        print(int_features)

        final_features = [np.array(int_features)]

        print(final_features)



        prediction = model.predict_proba(final_features)

        not_cheating = prediction[0][0]
        cheating = prediction[0][1]

        if not_cheating > cheating:
            verdict = int(not_cheating*100)
            predict = 'not cheating'
        else:
            verdict = int(cheating*100)   
            predict = 'cheating' 

        prediction = [verdict, predict]   



        print(prediction)

        #output = num1+num2+num3



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
        return render_template('results.html',result=prediction)  


if __name__ == '__main__':
    app.run(debug=True)          