import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import r2_score
# read the data from Excel table , using header=0 because there are labels on columns
xlsx = pd.read_excel("ENB2012_data.xlsx",header=0)
# replacement of missing values with the mean of all column values
xlsx.fillna(xlsx.mean())
# I use a LinearRegression object for extimation. I use this object
# to select the features.
estimator = LinearRegression()
# selection of the target variable y and the 8 indipendent variables X.
# With iloc(:,:8) I select all the values of the first 8 columns while with iloc(:,8) 
# I select all the values for the 9th column
X = xlsx.iloc[:,:8]
y = xlsx.iloc[:,8]
# Selection of 4 from the 8 features using RFE(recursive feature elimination).
# With this method I select the 4 variables that have best perfomances with this model.
# Before I build an RFE object , selector, and then I fit it on features and the selected
# regression model. With selector.support_ I get the mask of selected features and
# with selector.ranking_ I get the results of the best features.
# Using this results , I choose the 4 features for the regression model, X1 , and y1 will be
# the target variable.
selector = RFE(estimator,n_features_to_select=4,step=1)
selector = selector.fit(X,y)
print(selector.support_)
print(selector.ranking_)
X1 = xlsx.iloc[:,0:4]
y1 = y
# normalization of the X and y variables.I use 2 Standardscaler objects , one for X and one
# for y in order to keep the proportions. I fit and transform the X and y variables.
# I use to_frame method to transform the y1 serie in a 2d dataframe to use it with
# the fit and transform methods
sc_x = StandardScaler()
sc_y = StandardScaler()
scaler_x = sc_x.fit(X1)
X1_std = scaler_x.transform(X1)
y1 = y1.to_frame()
scaler_y = sc_y.fit(y1)
y1_std = scaler_y.transform(y1)
# splitting the X,y variables into X,y train values and X,y test values.I use 30% test and 70% train datas.
X_train,X_test,y_train,y_test = train_test_split(X1_std,y1_std,test_size=0.3,random_state=0) 
# create a LinearRegression object , then I fit and predict this object on Xtrain and Xtest datas.
slr = LinearRegression()
slr.fit(X_train,y_train)
y_test_pred = slr.predict(X_test)
y_train_pred = slr.predict(X_train)
# using r2_score to check the perfomance of the model on train and test datas. More the value is
# near 1, more the efficiency of the model is better.
# The R2 train = 0.832 while R2 test = 0.81 .
print("R2 train: %.3f, R2 test: %.3f" % (r2_score(y_train,y_train_pred), r2_score(y_test,y_test_pred)))
