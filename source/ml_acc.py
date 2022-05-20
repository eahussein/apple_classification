import numpy as np
from sklearn.model_selection import GridSearchCV, cross_val_score, KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import *
from sklearn import metrics
from sklearn.model_selection import RandomizedSearchCV

def cv (m, itr, p, xtrain, ytrain, xtest, ytest):
    inner_cv = StratifiedKFold(n_splits=3)
    # clf = GridSearchCV(m, p, scoring='accuracy', n_jobs=-1, cv=inner_cv, refit=True, verbose=0)
    clf = RandomizedSearchCV(estimator = m, param_distributions = p, n_iter = itr, cv = 3, verbose=0, random_state=42, n_jobs = -1)
    clf.fit(X = np.array(xtrain), y=np.array(ytrain).reshape(len(ytrain)).ravel())
    pred = clf.predict(xtest)
    return precision_score(ytest, pred), clf


def get_accuracy_ml (m, itr, p, xTrain, yTrain, xTest, yTest):
    accTot, clfTot = cv(m, itr, p, xTrain, yTrain, xTest, yTest)
    jackTrainArr = []
    jackTestArr = []
    for i in range(0, len(xTrain), 3):
        x_train = np.delete(np.array(xTrain), i, 0)
        y_train = np.delete(np.array(yTrain), i, 0)
        
        scoreTrain, clf1 = cv(m, itr, p, x_train, y_train, xTest, yTest)
        
        jackTrainArr.append(scoreTrain)
            
    for t in range (len(xTest)):
        x_test = np.delete(np.array(xTest), t, 0)
        y_test = np.delete(np.array(yTest), t, 0)
            
        y_predict = clfTot.predict(x_test)
        
        jackTestArr.append(precision_score(y_test, y_predict))  
    return  accTot, jackTrainArr, jackTestArr, clfTot