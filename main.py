"""
Main code
"""
import pandas as pd

def mycar(data):
    mydataset = {'cars': ["BMW", "Volvo", "Ford"],'counts': [3, 7, 2]}
    mycar1 = pd.DataFrame(mydataset)
    mycar1 = mycar1.max()
    car_column = mycar1['counts']
    if data == car_column :
      return True
    else:
      return False
