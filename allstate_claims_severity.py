# # kaggel_allstate

import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# train.shape #(188318, 132)
# pd.isnull(train).values.any() # False
# train.info()

# train_cat = list(train.select_dtypes(include = ['object']).columns)
# train_cont = [cont for cont in list(train.select_dtypes(include = ['float64', 'int64']).columns) if cont not in ['loss', 'id']]
# train_id = list(trian.select_dtypes(include = ['int64']).columns)

# train_cat = [var for var in train.columns if 'cat' in var]

train_cat = train[train.dtypes[train.dtypes == 'object'].index]
test_cat = test[test.dtypes[test.dtypes == 'object'].index]

train_con = train[train.dtypes[train.dtypes != 'object'].index]
test_con = test[test.dtypes[test.dtypes != 'object'].index]


# train_corr = train_con.corr(method = 'pearson')

# # for x in range(len(train_corr)):
# # 	for y in range(len(train_corr)):
# # 		if (x > y) and (train_corr.iloc[x, y] > 0.6):
# # 			print(" %s and %s = %.2f" % (train.columns[x], train.columns[y], train_corr.iloc[x, y]))


#  # cat6 and cat1 = 0.76
#  # cat7 and cat6 = 0.66
#  # cat9 and cat1 = 0.93
#  # cat9 and cat6 = 0.80
#  # cat10 and cat1 = 0.81
#  # cat10 and cat6 = 0.88
#  # cat10 and cat9 = 0.79
#  # cat11 and cat6 = 0.77
#  # cat11 and cat7 = 0.75
#  # cat11 and cat9 = 0.61
#  # cat11 and cat10 = 0.70
#  # cat12 and cat1 = 0.61
#  # cat12 and cat6 = 0.79
#  # cat12 and cat7 = 0.74
#  # cat12 and cat9 = 0.63
#  # cat12 and cat10 = 0.71
#  # cat12 and cat11 = 0.99
#  # cat13 and cat6 = 0.82
#  # cat13 and cat9 = 0.64
#  # cat13 and cat10 = 0.71

# # for feature in train_cat:
# # 	print(feature, 'has', len(train_cat[feature].unique()), 'values. Uniques are::', train[feature].unique())


# # for feature in train_cat:
# # 	sns.countplot(x = train[feature], data = train)
# 	# plt.show()

# train.drop('id', axis = 1, inplace = True)
# test.drop('id', axis = 1, inplace = True)
# loss = train.drop('loss', axis = 1, inplace = True)

# # print(train.shape[1])
# # print(test.shape[1])

# train_test = pd.concat([train, test], axis = 0).reset_index(drop = True)
# cat = train_test.dtypes[train_test.dtypes == 'object'].index

# # print(train_test)
# # train_test.shape[1] # 130
# # len(train_test) #313864

# # for feature in cat:
# # 	print feature, 'has', len(cat[feature].unique()), 'values. Uniques are: ', cat[feature].unique()
# # ------------------------------------------------------------------------
for feature in train_test.columns:
	train_test[feature] = pd.factorize(train_test[feature])[0]

# train_feature = train_test.iloc[: train.shape[0], :]
# test_feature = train_test.iloc[train.shape[0]: ]
# print(train_feature)


# # print(train_test[feature])
# # train_feature = train_test.iloc[: train.shape[0], :]





# # len_cat = len(data.columns[data.columns.str.contains('cat')]) # 116
# # cat = data.ix[:, 1: 116]
# # cont = data.ix[:, 117: 131]
# # loss = data['loss']


# # rf = RandomForestClassifier(n_estimators = 1000)
# # rf.fit(train[: 131], train[132] )

# # cont_describe = cont.describe()



# # cat = pd.Series(data, dtype = 'category')



