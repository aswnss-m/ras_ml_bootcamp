import pandas as pd
dataset = pd.read_csv("datasets/weather_dict.csv",sep=',')
print(dataset.head())

max_temp = dataset['Temperature'].max() # Returns the max temp
mx_temp_date = dataset['EST'][dataset['Temperature']==50] #returns the EST data of specified temp
print(dataset.isnull())
print(dataset.loc[:,dataset.isnull().any()]) # returns the column with null value
data_final = dataset.drop(['SeaLevelPressureIn','VisibilityMiles','WindSpeedMPH','PrecipitationIn','CloudCover','Events','WindDirDegrees'],axis=1)

print(data_final.Humidity.mean())

import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [1,2,6,8,10]
# plt.plot(x,y,color='green',marker='o',linestyle='dashed')
# plt.show()

# data_final.plot.bar()
# plt.show()

import seaborn as sns
sns.set_theme()
flights = sns.load_dataset("flights")
print(flights)
sns.heatmap(flights.corr(),annot=True)
plt.show()