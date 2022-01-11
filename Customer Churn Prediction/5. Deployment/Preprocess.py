#!/usr/bin/env python
# coding: utf-8

# # Preprocess

# In[1]:


# Import package

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler


# In[2]:


# Function for data cleaning, peprocessing, featuring enginnering

def preprocess(df): 
    
# Drop the rows with missing values.
    df = df.dropna() 

# Consolidating wording with same meaning
    df.replace('No phone service', 'No', inplace=True)
    df.replace('No internet service', 'No', inplace=True)

# Change data type from object to float
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'],errors = 'coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    
    df = df.drop(columns=['customerID'])
    
# Check columns with two classes
    columns = df.columns
    binary_columns = []
    for col in columns:
            if df[col].value_counts().shape[0] == 2:
                binary_columns.append(col)

# Check columns with multiple classes
    columns = df.columns
    multiple_class_columns = []
    for col in columns:
        if df[col].value_counts().shape[0] != 2:
            multiple_class_columns.append(col)
        
# Label Male & Female to 1 & 0
    df.gender.replace({'Male':1, 'Female':0}, inplace=True)
    
# Convert Yes & No to 1 & 0
    for column in binary_columns:
        df[column].replace({'Yes':1, 'No':0}, inplace=True)
        df[column] = pd.to_numeric(df[column],errors = 'coerce')
        
# Creating dummy columns for features with multiple classes and non continuos datapoint
    df = pd.get_dummies(data=df, columns=['InternetService', 'Contract', 'PaymentMethod'])
     
# Rename column to presentable format
    df = df.rename({'gender': 'Gender',
                   'tenure': 'Tenure',
                   'InternetService_DSL': 'IntService_DSL', 
                   'InternetService_Fiber optic': 'IntService_Fiber', 
                   'InternetService_No': 'IntService_No',
                   'Contract_Month-to-month': 'Contract_Mth', 
                   'Contract_One year': 'Contract_1Y', 
                   'Contract_Two year': 'Contract_2Y',
                   'PaymentMethod_Bank transfer (automatic)': 'PayMethod_Bank', 
                   'PaymentMethod_Credit card (automatic)': 'PayMethod_C_Card', 
                   'PaymentMethod_Electronic check': 'PayMethod_Electonic', 
                   'PaymentMethod_Mailed check': 'PayMethod_Mail'},axis=1)    

# Create updated columns
    new_columns = df.columns   

# Convert all columns to float type
    columns = df.columns
    for col in columns:
            df[columns] = df[columns].astype(float)   

# Convert the DataFrame object into NumPy array otherwise you will not be able to impute
    values = df.values
    
    
# Dfine the criteria for dealing with the missing values
    imputer = SimpleImputer(
        missing_values = np.nan,
        strategy = 'most_frequent')    
     
# Transform to impute data
    imputedData = imputer.fit_transform(values)
        
    
# Scale data betwen 0 & 1 and normalisaiton
    scaler = MinMaxScaler(feature_range = (0, 1))
    normalizedData = scaler.fit_transform(imputedData)   
    
# Move the data back to a dataframe
    df = pd.DataFrame.from_records(normalizedData, columns = new_columns)
    
    
    return df


# _____END_____
