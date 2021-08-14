#importing dependencies
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
#for saving the model
import pickle

dataset = pd.read_csv('/home/aswnss/Coding/Python/Machine-Learning-Projects/ras ml/datasets/student/student-mat.csv',sep=';')
student_dataset = dataset[['G1','G2','G3','failures','absences']]

predict = 'G3'
X = np.array(student_dataset.drop([predict],axis=1))
Y =np.array(student_dataset[predict])
x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
# max =0
# for _ in range(10000):
#     x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
#     Ultron = linear_model.LinearRegression()
#     Ultron.fit(x_train,y_train)
#     accuracy = Ultron.score(x_test,y_test)
#     if accuracy>max:
#         max = accuracy
#     with open('Ultron_Model.pickle','wb') as f:
#         pickle.dump(Ultron,f)


pickle_in = open("Ultron_Model.pickle",'rb')
Ultron = pickle.load(pickle_in)
# print("Ultron is at ",accuracy*100,"% Accurate")

# print("Coefficients : ",Ultron.coef_)
# print("Intercept : ",Ultron.intercept_)


prediction = Ultron.predict(x_test)
for i in range(len(prediction)):
    print("predicted G3 - ",prediction[i],"Actual G3 - ", y_test[i], " loss - ",y_test[i]-prediction[i])

# plt.scatter(student_dataset['absences'], student_dataset['G3'])
# plt.xlabel("Absence")
# plt.ylabel("G3")
# plt.show()

