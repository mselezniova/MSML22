import numpy as np
import pandas as pd

def  train_test_split(df, training_data_fraction, shuffle=True):

    if shuffle is True:
        df_ = df.sample(frac=1).reset_index(drop=True)
    else:
        df_= df
    
    train_df = df_.iloc[:round(training_data_fraction*len(df_)),:]
    test_df = df_.iloc[round(training_data_fraction*len(df_)):,:]
    
    return df_, train_df, test_df

def k_fold_split(X,Y,k):
    perm_ind = np.random.permutation(np.arange(X.shape[0]))
    return np.array_split(X[perm_ind],k), np.array_split(Y[perm_ind],k)

def normalize(x, method='standardization'):
	if method=='standardization':
		return (x - np.mean(x, axis=0))/np.std(x,axis=0)
	elif method=='min-max':
		return (x - np.min(x, axis=0))/(np.max(x, axis=0) - np.min(x, axis=0))
	else:
		raise Exception('Unknown method!')


