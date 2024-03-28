from history import History
import os
import pandas as pd
import pytest

@pytest.fixture
def history_instance(tmpdir):
    os.environ["HISTORY_CSV_FILE"] = str(tmpdir.join("history.csv"))
    return History()

def test_save_to_csv(history_instance):
    history_instance.save_to_csv(2, 'add', 3, 5, 'null')
    df = pd.read_csv(os.getenv("HISTORY_CSV_FILE"))
    assert len(df) == 1

# Add more tests for other functionalities in History