import pandas as pd
import random
import numpy as np
from sklearn import linear_model

class recommendationSystem:

    def __init__(self, data_input, nrows):
        self.dataSet = self.generateDataSet(data_input, nrows)
        self.model = self.recommendationModel()

    def readCSVFile(self, csv_file, nrows):
        """
        reads a CSV file in a pandas dataframe and adds ClientID
        :param csv_file: input data
        :param nrows: the max rows to read
        :return: a pandas dataframe
        """
        data = pd.read_csv(csv_file, sep=";", nrows=nrows)
        output_data = {"AreaId": [], "Receipt": [], "TransactionDate": [], "EAN": [], "Quantity": []}
        # convert str to integers
        for index, row in data.iterrows():
            for key in output_data:
                if key != "Quantity":
                    output_data[key].append(row[key])
                else:
                    output_data[key].append(int(row["Quantity"].split(',')[0]))
        customers = [random.randrange(10, 20, 1) for i in range(nrows)]
        output_data["ClientID"] = customers
        return pd.DataFrame(output_data)

    def generateDataSet(self, csv_file, nLines):
        """
        Generate a wast Food dataset
        :param csv_file: data set from K Group
        :param nLines: maximum lines to read from the csv file
        :return: a pandas dataframe that addes randomly a customer ID and a lost quantity
        """
        input_data = self.readCSVFile(csv_file, nLines)
        data = []
        for index, row in input_data.iterrows():
            lostFood = int(row["Quantity"]) - random.randrange(0, 2, 1)
            if lostFood < 0:
                lostFood = 0
            data.append(lostFood)
        input_data["LostQuantity"] = data
        return input_data

    def recommendationModel(self):
        """
        A Multi-Creteria regression model
        :return: a multicretaria regression model [clientID, Product , quantity ] vs lost quantit
        """
        dataframe = self.dataSet
        x = dataframe[['ClientID', 'EAN', 'Quantity']]
        y = dataframe['LostQuantity']
        regr = linear_model.LinearRegression()
        regr.fit(x, y)
        return regr


    def recommendationPredictionBySet(self, csv_file, nrows):
        """
        Predict the lost quantity for a given Client, Product
        :param csv_file: input data
        :param nrows: max lines to read from file
        :return: a recommendation
        """
        model = self.model
        df = self.readCSVFile(csv_file, nrows)
        return model.predict(df[['ClientID', 'EAN', 'Quantity']])

    def recommendationPredictionByVector(self, ClientID, EAN, quantity, model):
        """
        Predict the lost quantity for a given Client, Product
        :param csv_file: input data
        :param model: the regression model
        :return: a recommendation
        """
        vector = [[ClientID, EAN, quantity]]
        waste = model.predict(vector)
        effectve_use = int(quantity - waste[0])
        if effectve_use > 0:
            meg = "It's better to take " + str(effectve_use) + " of " + str(EAN) + "so you waste less"
        else :
            meg = "it's better to not purshase this product"
        return meg


print("Test 1")
csv_model = "Data/Junction_data_sample.csv"
csv_pred = "Data/Junction_data_sample.csv"
recom = recommendationSystem(csv_model, 50)
print("dataset generated")
reg = recom.recommendationModel()
print("model generated")
pred = recom.recommendationPredictionBySet(csv_pred, 10)
print("prediction :")
print(pred)
print("Test 2")
pred = recom.recommendationPredictionByVector(19,6413600017523, 4,reg)
print(pred)



















