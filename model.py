import numpy as np 
import pandas as pd 
import statsmodels.api as sm 
#import matplotlib.pyplot as plt 
from patsy import dmatrices 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 
from sklearn import metrics
from sklearn.model_selection import cross_val_score
import pickle
#import seaborn as sns



from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model  import Ridge,Lasso,RidgeCV, LassoCV, ElasticNet, ElasticNetCV, LogisticRegression
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor 
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score

#import scikitplot as skl



train = sm.datasets.fair.load_pandas().data

#########################################
def covert_occ(occ):
    if occ == 1:
        return 'student1'
    elif occ == 2:
        return 'unskilled worker2'
    elif occ == 3:
        return 'white-colloar3'
    elif occ == 4:
        return 'skilled worker4'
    elif occ == 5:
        return 'managerial5'
    else:
        return'advanced degree6'

def education(occ):
    if occ == 9:
        return 'grade school1'
    elif occ == 12:
        return 'High school2'
    elif occ == 14:
        return 'some college3'
    elif occ == 16:
        return 'college graduate4'
    elif occ == 17:
        return 'some graduate school5'
    else:
        return'advanced degree6'        




# Done some EDA
train['children'] = train['children'].astype(int)
train['affair'] = (train.affairs>0).astype(int)
train['new_marriage'] = train.apply(lambda x :1 if (x['yrs_married'])<3 else 0,axis=1)
train['no_children'] = train.apply(lambda x:1 if (x['children'])==0 else 0,axis=1)
train['named_occ_wife'] = train.apply(lambda x:covert_occ(x['occupation']),axis=1)
train['named_occ_huband'] = train.apply(lambda x:covert_occ(x['occupation_husb']),axis=1)
train['education_name'] = train.apply(lambda x:education(x['educ']),axis=1)
train['wifemore'] = train.apply(lambda x:1 if (x['occupation']>x['occupation_husb']) else 0,axis=1)
train['husbandmore'] = train.apply(lambda x:1 if (x['occupation']<x['occupation_husb']) else 0,axis=1)

###################################################

# Dropping the unnecessary affairs column
train.drop(['affairs'],axis=1,inplace=True)

##################################################

#converting target type from int to Object
convert_dict = {
                'affair': object
                
               } 
  
train = train.astype(convert_dict)

#################################################

#building model with selected columns along with 
train1 = train[['rate_marriage','age','religious','new_marriage','no_children']]
labels = train[['affair']]

#################################################

# Splitting the data set in train and test
labels=labels.astype('int')
X_train,X_test,y_train,y_test = train_test_split(train1,labels,test_size=0.2)

######################################################

# Applying logistic regression
model = LogisticRegression()
model.fit(X_train,y_train.values.ravel())

#####################################################

# Dumping the data
pickle.dump(model,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

##########################################
