from unittest.mock import patch

import pandas

from src.file_readers import read_csv_file, read_excel_file


def test_read_csv_file(df_transaction_from_file, result_transaction_from_file):
    with patch("pandas.read_csv", return_value=df_transaction_from_file):
        result = read_csv_file("path")
        assert result == result_transaction_from_file


def test_read_excel_file(df_transaction_from_file, result_transaction_from_file):
    with patch("pandas.read_excel", return_value=df_transaction_from_file):
        result = read_excel_file("path")
        assert result == result_transaction_from_file
