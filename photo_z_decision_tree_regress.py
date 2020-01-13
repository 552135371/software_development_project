import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''

>>> import numpy as np
>>> data = np.load('data/sdss_photoz/sdss_photoz.npy')
>>> N = len(data)
>>> X = np.zeros((N, 4))
>>> X[:, 0] = data['u'] - data['g']
>>> X[:, 1] = data['g'] - data['r']
>>> X[:, 2] = data['r'] - data['i']
>>> X[:, 3] = data['i'] - data['z']
>>> z = data['redshift']


>>> Ntrain = 3 * N / 4
>>> Xtrain = X[:Ntrain]
>>> ztrain = z[:Ntrain]
>>> Xtest = X[Ntrain:]
>>> ztest = z[Ntrain:]


from sklearn.tree import DecisionTreeRegressor
>>> clf.fit(Xtrain, ztrain)
>>> zpred = clf.predict(Xtest)


>>> rms = np.sqrt(np.mean((ztest - zpred) ** 2))
>>> print rms
0.221409442926


>>> print len(ztest)
102798
>>> print np.sum(abs(ztest - zpred) > 1)
1538
'''
mag = ["B_MAG_APER2","H_MAG_APER2","Hw_MAG_APER2","IA484_MAG_APER2","IA527_MAG_APER2",
       "IA624_MAG_APER2","IA679_MAG_APER2","IA738_MAG_APER2","IA767_MAG_APER2","IB427_MAG_APER2",
       "IB464_MAG_APER2","IB505_MAG_APER2","IB574_MAG_APER2","IB709_MAG_APER2","IB827_MAG_APER2",
       "J_MAG_APER2","Ks_MAG_APER2","Ksw_MAG_APER2","NB711_MAG_APER2","NB816_MAG_APER2","V_MAG_APER2",
       "Y_MAG_APER2","ip_MAG_APER2","r_MAG_APER2","yHSC_MAG_APER2","zpp_MAG_APER2"]
#############################################################################################################################
data = pd.read_csv('FINAL VERSION_match_COSMOS_del_rows_99.csv')
#data = pd.read_csv('without_0_FINAL VERSION_match_COSMOS_del_rows_99.csv')
##############################################################################################################################
N = len(data)
X = np.zeros((N, len(mag)-1))
for i in range(len(mag)-1):
    X[:, i] = data[mag[i]] - data[mag[i+1]]
z = data['zspec']

Ntrain = int(3 * N / 4)
Xtrain = X[:Ntrain]
ztrain = z[:Ntrain]
Xtest = X[Ntrain:]
ztest = z[Ntrain:]

from sklearn import tree
clf = tree.DecisionTreeRegressor()
clf = clf.fit(Xtrain, ztrain)
zpred = clf.predict(Xtest)


rms = np.sqrt(np.mean((ztest - zpred) ** 2))
#RMS 均方根值=0.30337678882621766    0.25401426427958085
print (rms)
#TEST NUM=4557  4321
print (len(ztest),N/4)
#>1 NUM =72     51
print (np.sum(abs(ztest - zpred) > 1))

# Plot the results
plt.figure()
#plt.scatter(ztest,ztest,label="data")
plt.scatter(ztest,zpred,marker=".",label="RMS=0.30")
plt.xlabel("zspec")
plt.ylabel("z_predict")
plt.title("[TEST DATA] Photo-z: Decision Tree Regression")
plt.legend()
plt.show()


'''
clf.predict([[1, 1]])


# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Create a random dataset
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)

# Predict
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X, y, c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()

'''

