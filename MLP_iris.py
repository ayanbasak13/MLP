# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('iris.csv')
x= dataset.iloc[:, :-1].values.astype(float)
y= dataset.iloc[:, 4].values
#y=y.reshape((-1,1))


# Encoding the Categorical Variable
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_y = LabelEncoder()
y= labelencoder_y.fit_transform(y)


# Convert integers to dummy variables (one hot encoded)
y=y.reshape((-1,1))
onehotencoder=OneHotEncoder(categorical_features=[0])
y=onehotencoder.fit_transform(y).toarray()
#y=y[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# ANN Model

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers


# Initialising the ANN
classifier = Sequential()


# Adding the input layer and the hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 4))


# Adding the output layer
classifier.add(Dense(output_dim = 3, init = 'uniform', activation = 'sigmoid'))


# Compiling the ANN
sgd= optimizers.SGD(lr=0.9)
classifier.compile(optimizer =sgd, loss = 'mean_squared_error', metrics = ['accuracy'])


# Fitting the ANN to the Training set
classifier.fit(x_train, y_train, batch_size = 15,epochs = 25000)


# Predicting the Test set results
N=30
y_pred = classifier.predict(x_test)
for i in range (0,N):
    for j in range (0,2):
        index=0
        if(y_pred[i,j]>y_pred[i,j+1]):
            index=j
            if(j!=index):
                y_pred[i,j]=0
                y_pred[i,index]=1
            



