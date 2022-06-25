import numpy as np


class LinearRegression(object):
    def __init__(self, fit_intercept=True, copy_X=True):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X

        self._coef = None
        self._intercept = None
        self._new_X = None
        self._w_hat = None

    def fit(self, X, y):
        self._new_X = X

        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            X = np.concatenate([array_ones, X], axis = 1)
    
        XTX_inv = np.linalg.inv(X.T.dot(X))
        XTy = X.T.dot(y)
        self._w_hat = XTX_inv.dot(XTy)
        self._coef = self._w_hat[1:]
        self._intercept = self._w_hat[0]
        
        return self


    def predict(self, X):
        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            X = np.concatenate([array_ones, X], axis = 1)
        
        y_hat = X.dot(self._w_hat)
        
        return y_hat

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept
