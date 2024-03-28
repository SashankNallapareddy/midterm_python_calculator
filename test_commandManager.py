from commandManager import CommandManager
import pytest

@pytest.mark.parametrize("x, y, expected_result", [(3, 2, 5), (10, 5, 5), (2, 3, 6), (10, 2, 5), (2, 3, 8)])
def test_add(x, y, expected_result):
    assert CommandManager.add(x, y) == expected_result

# Add similar tests for other operations in CommandManager