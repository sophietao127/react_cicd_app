import pytest

# Function to write to a file
def write_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)

# Function to read from a file
def read_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Test functions using pytest
def test_file_processing(tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "test_file.txt"

    # Data to be written
    test_data = "Hello, this is a test."

    # Write data to file
    write_to_file(temp_file, test_data)

    # Read data from file
    result = read_from_file(temp_file)
    # result1 = 'test'

    # Assertions
    assert result == test_data, "File content does not match expected data"
    assert temp_file.exists(), "File should exist after writing"