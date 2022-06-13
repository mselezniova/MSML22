import numpy as np

class LinearBinaryClassification:

    def __init__(self, w, b):
        self._w = np.array(w, dtype=float)
        self._b = np.array(b, dtype=float)
        self.history = [{'w': self._w.copy(),
                         'b': self._b.copy(),
                         'loss': None,
                         'accuracy': None}]
        
    def h(self, x):
        return np.where(x @ self._w + self._b >= 0.0, 1, -1)
    
    def accuracy(self, X, Y):
        return 1. - np.sum(self.h(X) != Y)/Y.size
    
    def loss(self, X, Y):
        lin_term = X@self._w + self._b*np.ones(X.shape[0]) - Y
        return 0.5/X.shape[0]*np.dot(lin_term,lin_term)
    
    def loss_grad(self, X,Y):
        lin_term = X@self._w + self._b*np.ones(X.shape[0]) - Y
        return X.T@(lin_term)/X.shape[0], np.mean(lin_term, axis=0)
    
    def train(self, X, Y, lr = 1e-3, num_iter = 100):

        self.history[0]['loss'] = self.loss(X,Y)
        self.history[0]['accuracy'] = self.accuracy(X,Y)
        
        for e in range(num_iter):
            
            grad_w, grad_b = self.loss_grad(X,Y)
            self._w -= lr*grad_w
            self._b -= lr*grad_b
            
            self.history.append({'w': self._w.copy(),
                                 'b': self._b.copy(),
                                 'loss': self.loss(X,Y),
                                 'accuracy': self.accuracy(X,Y)})
            
        return self._w, self._b
    

class LogisticRegression(LinearBinaryClassification):
    
    def __init__(self, w, b):
        super().__init__(w,b)
        
        self.activation = lambda x: 1./(1.+np.exp(-x))
        
    def h(self,x):
        return self.activation(x @ self._w + self._b)
    
    def accuracy(self,X,Y):
        pred = np.where(self.h(X) >= 0.5, 1, 0)
        return 1. - np.sum(pred != Y)/Y.size
    
    def loss(self,X,Y):
        lin_term = X @ self._w + self._b
        return -np.mean(Y*np.log(self.activation(lin_term))+
                       (1.-Y)*np.log(1.-self.activation(lin_term)) )
    
    def loss_grad(self,X,Y):
        lin_term = self.activation(X@self._w+self._b) - Y
        return  X.T@lin_term/X.shape[0], np.mean(lin_term, axis=0)

class RidgeClassification(LinearBinaryClassification):
    
    def __init__(self, w, b, l):
        super().__init__(w,b)
        self.l = np.array(l, dtype=float)

        
    def MSE(self, X, Y):
        ones_vec = np.ones(X.shape[0])
        return 0.5/X.shape[0]*np.dot(X@self._w + self._b*ones_vec - Y,
                          X@self._w + self._b*ones_vec - Y)
    
    def loss(self, X, Y):
        ones_vec = np.ones(X.shape[0])
        return 0.5/X.shape[0]*np.dot(X@self._w + self._b*ones_vec - Y,
                          X@self._w + self._b*ones_vec - Y) + self.l*np.dot(self._w,self._w)
    
    def loss_grad(self, X,Y):
        ones_vec = np.ones(X.shape[0])
        return X.T@(X@self._w + self._b*ones_vec - Y)/X.shape[0]+2*self.l*self._w, ones_vec.T@(X@self._w 
                                                                    + self._b*ones_vec - Y)/X.shape[0]

class LinearMulticlassClassification:

    def __init__(self, w, b):
        
        self._params = np.vstack((np.array(w, dtype=float),  # stack the parameters into a single matrix [W,B]                                
                                  np.array(b, dtype=float))) # of shape (d+1,K)
        
        self._w = self._params[:-1,:] # save views of the parameters array as _w and _b
        self._b = self._params[-1,:]  # it's not a copy! when _params changes, _w and _b change
                                      # and vise versa
         
        self.labels = None            # class labels (can be different from [0,1,2])
                                      # labels are saved when the classifier sees Y during training
        
        self.history = [{'w': self._w.copy(),
                         'b': self._b.copy(),
                         'loss': None,
                         'accuracy': None}]
        
        
        
    def h(self, X):
        # the code accounts for any shape of X of the form (n1,n2,...np,d)
        # where d - the number of features
        
        ones_vec = np.ones(X.shape[:-1]+(1,)) # array of ones with shape (n1,n2,...np,1),
        
        _X = np.concatenate((X,ones_vec), axis=-1) # adds new dimension with value one to each point in X
                                                   # (x1,x2,...xd) is transformed to (x1,x2,...xd,1)
                                                   # the shape of X changes from (n1,n2,...np,d) 
                                                   # to (n1,n2,...np,d+1)  
        
        return np.argmax(_X@self._params, axis=-1)
    
    def accuracy(self, X, Y):
        return 1. - np.mean(self.labels[self.h(X)] != Y)
    
    def _accuracy(self, X, Y):
        return 1. - np.mean(np.argmax(X@self._params, axis=-1) != np.argmax(Y, axis=-1))
    
    def _loss(self, X, Y):
        lin_term = X@self._params - Y
        return 0.5/X.shape[0]*np.linalg.norm(lin_term)
    
    def _loss_grad(self, X,Y):
        
        lin_term = X@self._params - Y
        grad = X.T@lin_term/X.shape[0]
        return grad[:-1,:], grad[-1,:]
    
    def _labels_encoding(self, Y):
        self.labels = np.unique(Y)
        K = self.labels.size
        y_t = -np.ones(Y.shape+(K,))
    
        for k in range(K):
            ind = np.argwhere(Y==self.labels[k]).T.tolist()
            ind.append([k]*len(ind[0]))
            y_t[tuple(ind)] = 1

        return y_t

    def train(self, X, Y, lr = 1e-3, num_iter = 100, verbose=False):
        
        ones_vec = np.ones(X.shape[:-1]+(1,))
        _X = np.concatenate((X,ones_vec), axis=-1) # same shape transformation as in h()
        _X = _X.reshape((-1,_X.shape[-1]))         # make X two dimensional
                                                   # of shape (n1*n2*...*np,d+1)
        _Y = self._labels_encoding(Y) 
            
        self.history[0]['loss'] = self._loss(_X,_Y)
        self.history[0]['accuracy'] = self._accuracy(_X,_Y)
        
        for e in range(num_iter):
            
            grad_w, grad_b = self._loss_grad(_X,_Y)
            self._w -= lr*grad_w
            self._b -= lr*grad_b
            
            loss = self._loss(_X,_Y)
            acc = self._accuracy(_X,_Y)
           
            self.history.append({'w': self._w.copy(),
                                 'b': self._b.copy(),
                                 'loss': loss,
                                 'accuracy': acc})
            
            if verbose==True:
                if e%100==0:
                    print(f'Epoch {e}/{num_iter}. Loss value: {loss}, accuracy: {acc}')     
            
        return self._w, self._b

class MulticlassLogisticRegression(LinearMulticlassClassification):

    def __init__(self, w, b):
        
        super().__init__(w,b)
        self.activation = lambda x: 1./(1.+np.exp(-x))
        
        
        
    def h(self, X):
        # the code accounts for any shape of X of the form (n1,n2,...np,d)
        # where d - the number of features
        
        ones_vec = np.ones(X.shape[:-1]+(1,)) # array of ones with shape (n1,n2,...np,1),
        
        _X = np.concatenate((X,ones_vec), axis=-1) # adds new dimension with value one to each point in X
                                                   # (x1,x2,...xd) is transformed to (x1,x2,...xd,1)
                                                   # the shape of X changes from (n1,n2,...np,d) 
                                                   # to (n1,n2,...np,d+1)  
        
        return np.argmax(self.activation(_X@self._params), axis=-1)
    
    def _accuracy(self, X, Y):
        pred = self.activation(X@self._params)
        return 1. - np.mean(np.argmax(pred, axis=-1) != np.argmax(Y, axis=-1))
    
    def _loss(self, X, Y):
        lin_term = self.activation(X@self._params)
        return -np.mean(Y*np.log(lin_term) + (1.-Y)*(np.log(1.-lin_term)))
    
    def _loss_grad(self, X,Y):
        
        lin_term = self.activation(X@self._params) - Y
        grad = X.T@lin_term/X.shape[0]
        return grad[:-1,:], grad[-1,:]
    
    def _labels_encoding(self, Y):
        self.labels = np.unique(Y)
        K = self.labels.size
        y_t = np.zeros(Y.shape+(K,))
    
        for k in range(K):
            ind = np.argwhere(Y==self.labels[k]).T.tolist()
            ind.append([k]*len(ind[0]))
            y_t[tuple(ind)] = 1

        return y_t
