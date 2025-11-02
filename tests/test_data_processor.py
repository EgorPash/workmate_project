import pytest
from src.data_processor import read_csv_files
import tempfile

@pytest.fixture
def sample_csv1():
    content = "name,brand,price,rating\niphone 15 pro,apple,999,4.9\ngalaxy s23 ultra,samsung,1199,4.8"
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        return f.name

@pytest.fixture
def sample_csv2():
    content = "name,brand,price,rating\nredmi note 12,xiaomi,199,4.6\npixel 7,google,599,4.7"
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(content)
        return f.name

def test_read_csv_files_valid(sample_csv1, sample_csv2):
    result = read_csv_files([sample_csv1, sample_csv2])
    assert 'apple' in result
    assert result['apple'] == [4.9]
    assert result['xiaomi'] == [4.6]

def test_read_csv_files_missing_file():
    with pytest.raises(FileNotFoundError):
        read_csv_files(['nonexistent.csv'])

def test_read_csv_files_invalid_columns(sample_csv1):
    with open(sample_csv1, 'w') as f:
        f.write("name,price,rating\niphone,999,4.9")
    with pytest.raises(ValueError):
        read_csv_files([sample_csv1])
