"""
Main code
"""

import pandas as pd

def mycar(data):
  mydataset = {'cars': ["BMW", "Volvo", "Ford"],'counts': [3, 7, 2]}
  mycar = pd.DataFrame(mydataset)
  mycar = mycar.max()
  car_column = mycar['counts']
  if a == car_column :
      return True
  else:
      pass
