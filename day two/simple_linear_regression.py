#importing dependencies
import pandas as pd
import numpy as np
from sklearn import model_selection, linear_model
import matplotlib.pyplot as plt

#Collecting the data
dataset = pd.read_csv("/home/aswnss/Coding/Python/Machine-Learning-Projects/ras ml/datasets/Salary_Data.csv",sep=',')

#Selecting the data
X = np.array(dataset.drop('Salary',axis=1))
Y = np.array(dataset['Salary'])

#Splitting data , 80-20 train-test
x_train, x_test, y_train, y_test = model_selection.train_test_split(X,Y,test_size=0.2)

#Training model
Jarvis = linear_model.LinearRegression()
Jarvis.fit(x_train,y_train)

#Testing the model
accuracy = Jarvis.score(x_test, y_test)
prediction = Jarvis.predict(x_test)
print("Model Accuracy : ",accuracy*100,"%")
for i in range(len(prediction)):
    print("predicted Salary - ",prediction[i],"Actual Salary - ", y_test[i], " loss - ",y_test[i]-prediction[i])

#Plotting the result
plt.scatter(x_test,y_test,label="Given",color='green')
plt.scatter(x_test,prediction,label="Predicted",color='red')
plt.legend()
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
