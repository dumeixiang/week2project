"""
Test goes here

"""
from main import myvar

import pandas as pd

def test_dataset():
    # Test with dataset
    mydataset = {'cars': ["BMW", "Volvo", "Ford"], 'passings': [3, 7, 2]}
    myvar = pd.DataFrame(mydataset)
    result = myvar
    assert result, "Test failed to meet the dataset"


if __name__ == "__main__":
    test_dataset()
