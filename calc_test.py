import pytest
from commandManager import CommandManager

def test_add():
    assert CommandManager.add(2, 3) == 5

def test_subtract():
    assert CommandManager.subtract(5, 2) == 3

def test_multiply():
    assert CommandManager.multiply(4, 3) == 12

def test_divide():
    assert CommandManager.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        CommandManager.divide(10, 0)

def test_custom_action():
    assert CommandManager.custom_action(2, 3, '^') == 8

def test_invalid_operand():
    with pytest.raises(ValueError):
        CommandManager.custom_action(2, 3, '+')

def test_perform_operation_add():
    assert CommandManager.perform_operation('add', 2, 3) == 5

def test_perform_operation_subtract():
    assert CommandManager.perform_operation('subtract', 5, 2) == 3

def test_perform_operation_multiply():
    assert CommandManager.perform_operation('multiply', 4, 3) == 12

def test_perform_operation_divide():
    assert CommandManager.perform_operation('divide', 10, 2) == 5

def test_perform_operation_custom():
    assert CommandManager.perform_operation('custom', 2, 3, '^') == 8

def test_invalid_operation():
    with pytest.raises(ValueError):
        CommandManager.perform_operation('invalid', 2, 3)
