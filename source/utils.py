from sklearn.model_selection import train_test_split

def mean_df (pd):
    return pd.mean()
def sum_df (pd):
    return pd.sum()
def skew_df (pd):
    return pd.skew()
def kurt_df (pd):
    return pd.kurt()

def creat_rollingData (df, window_arr = [10, 20, 30, 40, 50, 100], method = sum_df, ax = 1):
    df_arr = []
    for w in window_arr:
        df_tmp = df.copy()
        
        df_tmp =  method(df_tmp.rolling(w, axis = ax ))
        # df_tmp =  df_tmp.rolling(w, axis = ax ).mean()
        
        df_tmp = df_tmp.iloc[:, w-1::w]
        df_arr.append(df_tmp)
    return df_arr

def split (x, y ):
    Xtrain, Xtest, Ytrain, Ytest  = train_test_split( x, y, test_size = 0.3, random_state=3, stratify=y) # splitting the data
    return Xtrain, Xtest, Ytrain, Ytest
