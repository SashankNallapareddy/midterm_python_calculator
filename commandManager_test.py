import logging
import pytest
from commandManager import CommandManager

class TestCommandManager:
    def test_add(self):
        assert CommandManager.add(2, 3) == 5

    def test_subtract(self):
        assert CommandManager.subtract(5, 3) == 2

    def test_multiply(self):
        assert CommandManager.multiply(2, 3) == 6

    def test_divide(self):
        assert CommandManager.divide(6, 3) == 2

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            CommandManager.divide(6, 0)

    def test_custom_action_power(self):
        assert CommandManager.custom_action(2, 3, '^') == 8

    def test_custom_action_divide(self):
        assert CommandManager.custom_action(6, 3, '/') == 2.0

    def test_custom_action_floor_divide(self):
        assert CommandManager.custom_action(6, 4, '//') == 1

    def test_custom_action_modulo(self):
        assert CommandManager.custom_action(6, 4, '%') == 2

    def test_custom_action_invalid_operand(self):
        with pytest.raises(ValueError):
            CommandManager.custom_action(2, 3, '+')

    def test_perform_operation_add(self):
        assert CommandManager.perform_operation('add', 2, 3) == 5

    def test_perform_operation_subtract(self):
        assert CommandManager.perform_operation('subtract', 5, 3) == 2

    def test_perform_operation_multiply(self):
        assert CommandManager.perform_operation('multiply', 2, 3) == 6

    def test_perform_operation_divide(self):
        assert CommandManager.perform_operation('divide', 6, 3) == 2

    def test_perform_operation_custom(self):
        assert CommandManager.perform_operation('custom', 2, 3, '^') == 8

    def test_perform_operation_invalid_operation(self):
        with pytest.raises(ValueError):
            CommandManager.perform_operation('invalid', 2, 3)

if __name__ == '__main__':
    pytest.main()