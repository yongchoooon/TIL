## Lab_Gradient_Descent 진행 이후 LR_5에서 Mini-Batch SGD Implementation을 위해 코드에 batch_size와 shuffle을 추가함

import numpy as np

class LinearRegressionGD(object):
    def __init__(self, fit_intercept=True, copy_X=True,
                 eta0=0.001, epochs=1000, eta0_decay=1,
                 batch_size=None, shuffle=False):
        self.fit_intercept = fit_intercept
        self.copy_X = copy_X
        self._eta0 = eta0
        self._epochs = epochs
        self._eta0_decay = eta0_decay
        self._batch_size = batch_size
        self._shuffle = shuffle

        self._cost_history = []
        self._w_history = []

        self._batch = None
        self._coef = None
        self._intercept = None
        self._new_X = None
        self._theta_hat = None


    def cost(self, h, y):
        return (1 / (2 * len(y))) * np.sum((h-y)**2)

    def hypothesis_function(self, X, theta):
        return X.dot(theta)

    def gradient(self, X, y, theta):
        return (1 / len(y)) * ((X.dot(theta) - y).dot(X))

    def fit(self, X, y):
        self._new_X = X
        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            self._new_X = np.concatenate([array_ones, X], axis = 1)

        theta = np.random.normal(0, 1, self._new_X.shape[1])
    
        self._batch = len(self._new_X) // self._batch_size

        for epoch in range(self._epochs):
            X_copy = np.copy(self._new_X)
            if self._shuffle:
                X_index = np.array(range(len(X_copy)))
                np.random.shuffle(X_index)
                X_copy = X_copy[X_index]
                y = y[X_index]

            for batch_count in range(self._batch):
                X_batch = np.copy(X_copy[batch_count * self._batch_size : (batch_count + 1) * self._batch_size])
                y_batch = np.copy(y[batch_count * self._batch_size : (batch_count + 1) * self._batch_size])
               
                gradient = self.gradient(X_batch, y_batch, theta).flatten()
                # print(gradient)
                theta = theta - self._eta0 * gradient 

            if epoch % 10 == 0:
                self._w_history.append(theta)
                cost = self.cost(
                    self.hypothesis_function(X_copy, theta), y)
                self._cost_history.append(cost)
            self._eta0 = self._eta0 * self._eta0_decay

        self._theta_hat = theta
        self._coef = self._theta_hat[1:]
        self._intercept = self._theta_hat[0]
        return self

    def predict(self, X):
        if self.fit_intercept == True:
            array_ones = np.ones((len(X),1))
            X = np.concatenate([array_ones, X], axis = 1)

        return X.dot(self._theta_hat)

    @property
    def coef(self):
        return self._coef

    @property
    def intercept(self):
        return self._intercept

    @property
    def weights_history(self):
        return np.array(self._w_history)

    @property
    def cost_history(self):
        return self._cost_history
