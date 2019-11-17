# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Waste_estimator : returns the estimate the waste.
p : product ID
answer: 0 if the answer to "Have you consumed all the quantity you bought last time?" is No
        1 otherwise.
consump_period : the estimated consumption per period of the product.
quantity : the quantity of the product bought the last time the customer purchased the product.
current_date : current date.
last_purchase_date : the date of the last time the customer purchased the product.
"""
def waste_estimator(p, answer,consump_period, quantity, current_date,last_purchase_date):
    if (answer == 0):
        return 0
    else:
        d=(current_date-last_purchase_day).days
        return quantity-consump*d
    