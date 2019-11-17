"""
Prepare a dataset with Customer ID and Food wast information for testing recommendation
"""

import pandas as pd
import random
from sklearn import linear_model


def readCSVFile(csv_file, nrows):
    """
    reads a CSV file in a pandas dataframe and adds ClientID/LostQuantity
    :param csv_file: input data
    :param nrows: the max rows to read
    :return: a pandas dataframe
    """
    data = pd.read_csv(csv_file, sep=";", nrows=nrows)
    output_data = {"AreaId": [],  "Receipt": [], "TransactionDate": [], "EAN" : [] , "Quantity" : [] }
    #convert str to integers
    for index, row in data.iterrows():
        for key in output_data:
            if key != "Quantity":
                output_data[key].append(row[key])
            else :
                output_data[key].append(int(row["Quantity"].split(',')[0]))
    customers = [random.randrange(10, 20, 1) for i in range(nrows) ]
    output_data["ClientID"] = customers
    return pd.DataFrame(output_data)



def generateDataSet(csv_file, nLines):
    """
    Generate a wast Food dataset
    :param csv_file: data set from K Group
    :param nLines: maximum lines to read from the csv file
    :return: a pandas dataframe that addes randomly a customer ID and a lost quantity
    """
    input_data = readCSVFile(csv_file, nLines)
    data = []
    for index, row in input_data.iterrows():
        lostFood = int(row["Quantity"])- random.randrange(0,2,1)
        if lostFood < 0:
            lostFood = 0
        data.append(lostFood)
    input_data["LostQuantity"] = data
    return input_data

def recommendationModel(dataframe):
    """
    A Multi-Creteria regression model
    :param dataframe:  the input training data
    :return: a multicretaria regression model [clientID, Product , quantity ] vs lost quantit
    """
    x = dataframe[['ClientID', 'EAN', 'Quantity']]
    y = dataframe['LostQuantity']
    regr = linear_model.LinearRegression()
    regr.fit(x, y)
    return regr

def recommendationPrediction(csv_file, model, nrows):
    """
    Predict the lost quantity for a given Client, Product
    :param csv_file: input data
    :param model: the regression model
    :param nrows: max lines to read from file
    :return: a recommendation
    """
    df = readCSVFile(csv_file, nrows)
    return model.predict(df[['ClientID', 'EAN', 'Quantity']])




csv_model = "Data/Junction_data_sample.csv"
csv_pred = "Data/Junction_data_sample.csv"
df = generateDataSet(csv_model, 50)
print("dataset generated")
reg = recommendationModel(df)
print("model generated")
pred = recommendationPrediction(csv_pred, reg, 10)
print("prediction done")
print(pred)






