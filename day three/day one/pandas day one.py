import pandas as pd

students = pd.read_csv('/home/aswnss/Coding/Python/Machine-Learning-Projects/ras ml/datasets/students.csv',sep=',')
print("Original Dataset\n",students)

new = pd.DataFrame([{"ID":11,"Name":"Kiran","Age":20,"Semester":2,"Marks":80},
                    {"ID":12,"Name":"Rahul","Age":25,"Semester":8,"Marks":60}])

students = students.append(new,ignore_index=True)
print("\nNew datas appended\n",students)
#dropping Age
students = students.drop('Age',axis=1)
print("\nAfter deleting the Age Column : \n",students)
# Mean of Marks
mean = students.mean(axis=0)
print("Mean of Marks = ",mean.Marks)
