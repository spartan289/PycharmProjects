from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()

#split it in features and labels
X=iris.data
y=iris.target

classes=['Iris Setosa','Iris Versicolor','Iris Virginica']
from sklearn import svm


print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
model = svm.SVC()
model.fit(X_train,y_train)
print(model)

prediction=model.predict(X_test)
acc = accuracy_score(y_test,prediction)
print("prediction",prediction)
print("actual: ",y_test)
print("accuracy",acc)
-0
for i in range(len(prediction)):
    print(classes[prediction[i]])