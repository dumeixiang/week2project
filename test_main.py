"""
Test goes here

"""
from main import mycar

def test_data():
    # Test with dataset
    result = mycar(6)
    assert result, "Test failed to meet the dataset"


if __name__ == "__main__":
    test_data()
