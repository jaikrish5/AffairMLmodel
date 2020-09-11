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

def rate_marriage_mapping(rate_marriage):
    if rate_marriage == 'very poor':
        return 1
    elif rate_marriage == 'poor':
        return 2
    elif rate_marriage == 'fair':
        return 3
    elif rate_marriage == 'good':
        return 4
    else:
        return 5

def religious_mapping(religious):
    if religious == 'not':
        return 1
    elif religious == 'mildly':
        return 2
    elif religious == 'fairly':
        return 3
    else:
        return 4           




@app.route('/affair', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        #operation=request.form['operation']
        rate_marriage=(request.form['rate_marriage'])
        age =float(request.form['age'])
        religious =(request.form['Religious'])
        years_married = int(request.form['years_married'])
        number_of_children = int(request.form['Children'])

        rate_marriage = rate_marriage_mapping(rate_marriage)
        religious = religious_mapping(religious)

        

        new_marriage = new_marriage_func(years_married)
        no_children = no_children_func(number_of_children)








        int_features = []
        int_features.append(rate_marriage)
        int_features.append(age)
        int_features.append(religious)
        int_features.append(new_marriage)
        int_features.append(no_children)

        

        final_features = [np.array(int_features)]

        



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



        

        
        return render_template('results.html',result=prediction)  


if __name__ == '__main__':
    app.run(debug=True)          