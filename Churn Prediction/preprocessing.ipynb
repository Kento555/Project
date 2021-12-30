{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7e019fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "def preprocess(df, option):\n",
    "    \"\"\"\n",
    "    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data\n",
    "    \"\"\"\n",
    "    #Defining the map function\n",
    "    def binary_map(feature):\n",
    "        return feature.map({'Yes':1, 'No':0})\n",
    "\n",
    "    # Encode binary categorical features\n",
    "    binary_list = ['SeniorCitizen','Dependents', 'PhoneService', 'PaperlessBilling']\n",
    "    df[binary_list] = df[binary_list].apply(binary_map)\n",
    "\n",
    "    \n",
    "    #Drop values based on operational options\n",
    "    if (option == \"Online\"):\n",
    "        columns = ['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No', 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service', 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes', 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']\n",
    "        #Encoding the other categorical categoric features with more than two categories\n",
    "        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)\n",
    "    elif (option == \"Batch\"):\n",
    "        pass\n",
    "        df = df[['SeniorCitizen','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity',\n",
    "                'OnlineBackup','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod',\n",
    "                'MonthlyCharges','TotalCharges']]\n",
    "        columns = ['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No', 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service', 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes', 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']\n",
    "        #Encoding the other categorical categoric features with more than two categories\n",
    "        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)\n",
    "    else:\n",
    "        print(\"Incorrect operational options\")\n",
    "\n",
    "\n",
    "    #feature scaling\n",
    "    sc = MinMaxScaler()\n",
    "    df['tenure'] = sc.fit_transform(df[['tenure']])\n",
    "    df['MonthlyCharges'] = sc.fit_transform(df[['MonthlyCharges']])\n",
    "    df['TotalCharges'] = sc.fit_transform(df[['TotalCharges']])\n",
    "    return df\n",
    "        \n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
