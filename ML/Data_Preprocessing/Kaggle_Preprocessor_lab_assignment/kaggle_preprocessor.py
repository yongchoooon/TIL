import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import skew
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

def get_train_test_split_dataset(train_dataset_filename  = None, test_dataset_filename = None):
    '''
    - 함수목적
      - Kaggle의 dataset중 "House Price" 문제의 train dataset과 test dataset의 파일을 입력하면 해당 데이터셋을
        학습가능한 형태로 X_train, y_train, X_test 로 전처리 하여 반환해준다.
      - 반환된 X_train과 y_train 데이터셋을 자동채점 시스템이 Linear Regression으로 모델을 만들어
        Root-Mean-Squared-Error (RMSE) value를 측정하여 threshold 이상의 결과를 내야만 test를 합격할 수 있다.
      - https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data
    - Args
        - train_dataset_filename: house price 문제의 "train.csv" 파일 이름 (str 타입)
        - test_dataset_filename: house price 문제의 "test.csv" 파일 이름 (str 타입)
    - Returns
        - X_train: "train.csv"파일의 feature들을 전처리한 결과값으로 two-dimensional ndarrray type
        - y_train = "train.csv"파일의 feature들 중 `SalePrice` 값이 one-dimensional ndarrray type
        - X_test: "test.csv"파일의 feature들을 전처리한 결과값으로 two-dimensional ndarrray type
        - test_id_idx: "test.csv"파일의 index 값들을 one-dimensional ndarrray type으로 반환함
    - Constraints for return value
        - X_train 에서 사용되는 feature 개수는 30개 이상이어야 한다.
        - X_train과 y_train의 row의 개수는 같아야 한다.
        - X_train과 X_test의 feature의 개수는 같아야 한다.
        - X_train, y_train을 가지고  Root-Mean-Squared-Error (RMSE) value를 취했을 때, 9 이하이어야 한다(CV 5 times)
        - test_id_idx의 값의 개수는 X_test의 row의 개수와 같아야 한다.



    '''
    # data loading
    train_df = pd.read_csv(train_dataset_filename)
    test_df = pd.read_csv(test_dataset_filename)
    
    # set index 'Id"
    train_df.set_index("Id", inplace=True)
    test_df.set_index("Id", inplace=True)

    # save index
    train_index = train_df.index
    test_index = test_df.index
    
    # y_train_df 따로 저장
    y_train_df = train_df.pop("SalePrice")
    
    # y_train Log Transformation
    log_y_train_df = np.log10(y_train_df)
    
    # 데이터 모판
    all_df = pd.concat([train_df, test_df], axis = 0)
    
    # 결측치가 너무 많아서 삭제
    del all_df["Alley"]
    del all_df["PoolQC"]
    del all_df["Fence"]
    del all_df["MiscFeature"]
    
    # 하나의 value가 전체 데이터의 80% 이상을 차지하는 column 삭제
    for col_name in all_df.columns:
        most_freq_value_ratio = (Counter(all_df[col_name]).most_common(1)[0][1] / len(all_df)) * 100
        if most_freq_value_ratio > 80:
            del all_df[col_name]
            
    # numeric column을 category type column으로 변경
    all_df["MSSubClass"] = all_df["MSSubClass"].astype(str)
    all_df["MoSold"] = all_df["MoSold"].astype(str)
    all_df["YrSold"] = all_df["YrSold"].astype(str)
    
    # numeric, object type column 따로 저장
    numeric_columns = all_df.select_dtypes(["int", "float"]).columns
    object_columns = all_df.select_dtypes("object").columns
    
    # 결측치 채우기
    all_df["MSZoning"] = all_df["MSZoning"].fillna("RL")
    all_df["Exterior1st"] = all_df["Exterior1st"].fillna("VinylSd")
    all_df["Exterior2nd"] = all_df["Exterior2nd"].fillna("VinylSd")
    all_df["KitchenQual"] = all_df["KitchenQual"].fillna("TA")
    all_df["MasVnrType"] = all_df["MasVnrType"].fillna("None")
    all_df["MasVnrArea"] = all_df["MasVnrArea"].fillna(0)
    all_df["LotFrontage"] = all_df["LotFrontage"].fillna(all_df["LotFrontage"].mean())
    # all_df["LotFrontage"] = all_df["LotFrontage"].fillna(all_df.groupby(["TotalBsmtSF"])["LotFrontage"].transform("mean"))
    all_df["GarageYrBlt"] = all_df["GarageYrBlt"].fillna(all_df["YearBuilt"])
    all_df["FireplaceQu"] = all_df["FireplaceQu"].fillna("None")
    for data in ['BsmtQual', 'BsmtExposure', 'BsmtFinType1', 'GarageType', 'GarageFinish']:
        all_df[data] = all_df[data].fillna("None")
    for data in ['BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'GarageCars', 'GarageArea']:
        all_df[data] = all_df[data].fillna(0)

    # 순위형 변수 Label Encoding
    label_obj_list = ['ExterQual', 'BsmtQual', 'HeatingQC', 'KitchenQual', 'FireplaceQu']
    all_df[label_obj_list] = all_df[label_obj_list].replace({"Ex" : 6, "Gd" : 5, "TA" : 4, "Fa" : 3, "Po" : 2, "None" : 1})
    
    # One-Hot Encoding
    onehot_all_df = pd.get_dummies(all_df)
    
    # Feature Log Transformation
    skewness = all_df[numeric_columns].apply(lambda x: skew(x.dropna())).sort_values(ascending = False)
    high_skewness = skewness[abs(skewness) > 1] # 왜도 값이 1 이상인 column만 채택
    skew_columns = high_skewness.index
    
    onehot_all_df[skew_columns] = np.log10(onehot_all_df[skew_columns]+0.5)
    log_onehot_all_df = onehot_all_df.copy()
    
    # 159개의 feature 중 y와의 상관계수 절댓값이 0.2 이상인 feature만 추출하여 학습에 사용
    temp_df = pd.merge(log_onehot_all_df, log_y_train_df, left_index = True, right_index = True)
    temp_df = temp_df.corr()
    temp_columns = temp_df[(temp_df["SalePrice"] >= 0.2) | (temp_df["SalePrice"] <= -0.2)].T.columns
    temp_columns = temp_columns.tolist()[:-1]
    
    log_onehot_all_df = log_onehot_all_df[temp_columns]
    
    # 데이터 모판에서 train data와 test data를 분리
    train_df = log_onehot_all_df[all_df.index.isin(train_index)]
    test_df = log_onehot_all_df[all_df.index.isin(test_index)]
    
    # train data를 Cross Validation 하기 위해 X와 y로 지정
    X = np.array(train_df)
    y = np.array(log_y_train_df)

    # Cross Validation
    kfold = KFold(n_splits = 5, shuffle = True)
    
    mse = []
    reg_list = []
    X_y_train_list = []
    for train_idx, test_idx in kfold.split(X):
        X_train = X[train_idx]
        y_train = y[train_idx]
    
        X_test = X[test_idx]
        y_test = y[test_idx]
    
        reg = LinearRegression()
        reg.fit(X_train, y_train)
        reg_list.append(reg)
    
        y_pred = reg.predict(X_test)
        
        mse.append(mean_squared_error(y_test, y_pred))
        X_y_train_list.append([X_train, y_train])
    
    best_reg_idx = np.array(mse).argmin()
    print(f"Best Regression Model's MSE : {mse[best_reg_idx]}")
    
    
    # return value
    X_train, y_train = X_y_train_list[best_reg_idx]
    X_test = np.array(test_df)
    test_id_idx = np.array(test_index)


    return X_train, X_test, y_train, test_id_idx

if __name__ == "__main__":
    train_dataset_filename = "./data/house_train.csv"
    test_dataset_filename = "./data/house_test.csv"
    X_train, X_test, y_train, test_id_idx = get_train_test_split_dataset(train_dataset_filename  = train_dataset_filename, 
                                                                         test_dataset_filename = test_dataset_filename)
    
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    test_result = 10**lr.predict(X_test)
    result_dict = {
        "id" : test_id_idx, "SalePrice": test_result
    }
    result_df = pd.DataFrame(result_dict)
    result_df.to_csv("submission.csv", index=False) 