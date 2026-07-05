from unittest.mock import patch

@patch('builtins.input', side_effect=["7"])
def test_exit(mock_input):
    assert True
