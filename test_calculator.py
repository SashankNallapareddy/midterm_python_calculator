# test_calculator.py
from calculator import process_command, save_calculation, get_valid_float_input
from unittest.mock import patch
import pytest

@pytest.mark.parametrize("input_str, expected_result", [("1 2 add", 3), ("10 5 subtract", 5), ("2 3 multiply", 6), ("10 2 divide", 5), ("2 3 custom ^", 8)])
def test_process_command_valid(input_str, expected_result):
    with patch('builtins.input', side_effect=input_str.split()):
        assert process_command(input_str) == expected_result

def test_save_calculation():
    with patch('builtins.print') as mocked_print:
        save_calculation(2, 'add', 3, 5, 'null')
        mocked_print.assert_called_once_with("Calculation saved successfully.")

def test_get_valid_float_input():
    with patch('builtins.input', return_value='3.5'):
        assert get_valid_float_input("") == 3.5
    with patch('builtins.input', return_value='invalid'):
        with pytest.raises(ValueError):
            get_valid_float_input("")