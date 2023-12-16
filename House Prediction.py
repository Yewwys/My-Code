import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\WIN10\\Desktop\\Dataset\\housing.csv')
df.dropna(inplace=True)
from sklearn.model_selection import train_test_split

X = df.drop(['median_house_value'],axis=1)
y = df['median_house_value']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
train_data  = X_train.join(y_train)

train_data['total_rooms'] = np.log(train_data['total_rooms']+1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms']+1)
train_data['population'] = np.log(train_data['population']+1)
train_data['households'] = np.log(train_data['households']+1)

#plot histogram
# histo = train_data.hist(figsize=(15,8))
# # print(histo)

# dum = train_data.join(pd.get_dummies(train_data.ocean_proximity)).drop(['ocean_proximity'],axis=1)

# train_data['bedroom_ratio'] = train_data['total_bedrooms'] / train_data['total_rooms']
# train_data['household_rooms'] = train_data['total_rooms'] / train_data['household_rooms']


from sklearn.linear_model import LinearRegression

x_train,y_train = train_data.drop(['median_house_value'],axis=1) , train_data['median_house_value']
reg = LinearRegression()

# reg.fit(x_train,y_train)


from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor()

forest.fit(x_train,y_train)

forst.score(X_test,y_test)


from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators":[3,10,30],
    "max_features":[2,4,6,8]
}

grid_search = GridSearchCV(forst,param_grid,cv=5,
scoring='neg_mean_squred_error',return_train_score=True)

grid_search,fit(X_train,y_train)

best_forest = grid_search.best_estimator_
best_forest.score(X_test,y_test)
