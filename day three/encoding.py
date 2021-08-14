#importing dependencies
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder # one hot encoding
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

'''
Handling Categorical Variables
1. Nominal (independent like car companies)
2. Ordinal (1st,2nd,3rd)

We need to convert it into numerical varibales

BMW | AUDI | BENZ | SellPrice | Age
----------------------------
1   |   0  |   0  |   18000   | 6
0   |   1  |   0  |   32000   | 5

for that we can use
1. pd.get_dummies() (pandas)
2. One Hot Encoding (sklearn) [label encoding: assigning each catagory a numerical value]
'''
# Loading Dataset
dataset = pd.read_csv("/home/aswnss/Coding/Python/Machine-Learning-Projects/ras ml/datasets/car_models.csv",sep=',')
print(dataset)
# pd.get_dummies()
dummy_val = pd.get_dummies(dataset['Car Model'])
print(dummy_val)

merge_dataset = pd.concat([dummy_val,dataset],axis=1)
merge_dataset = merge_dataset.drop(['Car Model'],axis=1)
print(merge_dataset)
'''
dummy variable trap :
we can determine the value of one variable with the values of other two

    Audi A5  BMW X5  Mercedez Benz C class  Mileage  Sell Price($)  Age(yrs)
0         0       1                      0    69000          18000         6
1         0       1                      0    35000          34000         3
2         0       1                      0    57000          26100         5
3         0       1                      0    22500          40000         2
4         0       1                      0    46000          31500         4

here when Audi is 0 and BMW is 0 we know MErc is also 0
'''

#dropping one column to get rid or dummy variable trap
merge_dataset = merge_dataset.drop(['Audi A5'],axis=1)

# Splitting data
# y- what we need to find , x - all other
y = merge_dataset['Sell Price($)']
X = merge_dataset.drop(['Sell Price($)'],axis=1)
x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,y,test_size=0.1)

# Training Model
Model = linear_model.LinearRegression()
Model.fit(x_train,y_train)

# One Hot Encoding
# Label_Encode = LabelEncoder()
# dataset_cpy = dataset

# dataset_cpy['Car Model'] = Label_Encode.fit_transform(dataset_cpy['Car Model'])
# print(dataset_cpy)

# # ColumnTransformer([(Column_name , transformation_function() , [index of column])], remainder = 'passthrough')
# ct = ColumnTransformer([('Car Model', OneHotEncoder(), [0])], remainder = 'passthrough')
# dataset_cpy = ct.fit_transform(dataset_cpy)

# print(dataset_cpy)