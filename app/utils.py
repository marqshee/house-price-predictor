from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

class Preprocessor(BaseEstimator, TransformerMixin):
    # train our custom preprocessors
    def fit(self, X, y=None):
        # create and fit simple imputer
        self.imputer = SimpleImputer()
        # by default strategy - the mean of each category is calculated
        self.imputer.fit(X[['HouseAge', 'DistanceToStation', 'NumberOfPubs']])

        # Create and fit Standard Scaler
        self.scaler = StandardScaler()
        self.scaler.fit(X[['HouseAge', 'DistanceToStation', 'NumberOfPubs']])
        
        # create and fit one hot encoder
        self.onehot = OneHotEncoder(handle_unknown='ignore')
        self.onehot.fit(X[['PostCode']])
        return self
        
        # apply custom preprocessors
    def transform(self, X):
        # apply simple imputer
        imputed_cols = self.imputer.transform(X[['HouseAge', 'DistanceToStation', 'NumberOfPubs']])
        onehot_cols = self.onehot.transform(X[['PostCode']])
        
        # copy dataframe
        transformed_df = X.copy()
        
        # apply year and month transform
        transformed_df['Year'] = transformed_df['TransactionDate'].apply(lambda x: x[:4]).astype(int)
        transformed_df['Month'] = transformed_df['TransactionDate'].apply(lambda x: x[5:]).astype(int)
        transformed_df = transformed_df.drop('TransactionDate', axis=1)
        
        transformed_df = transformed_df.drop(['YearSold','MonthSold'], axis=1)
        
        # apply transformed columns
        transformed_df[['HouseAge', 'DistanceToStation', 'NumberOfPubs']] = imputed_cols
        transformed_df[['HouseAge', 'DistanceToStation', 'NumberOfPubs']] = self.scaler.transform(transformed_df[['HouseAge', 'DistanceToStation', 'NumberOfPubs']])
        
        # drop existing post code column and replace with one hot encoder
        transformed_df = transformed_df.drop('PostCode', axis=1)
        transformed_df[self.onehot.get_feature_names_out()] = onehot_cols.toarray().astype(int)
        
        return transformed_df