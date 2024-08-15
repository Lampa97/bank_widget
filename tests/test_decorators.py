import pytest

from src.decorators import log


@log()
def slice(string):
    return string[1:]


def test_log_success(capsys):
    slice("abc")
    captured = capsys.readouterr()
    assert captured.out == f"slice ok.\n"


def test_log_error(capsys):
    slice(5678)
    captured = capsys.readouterr()
    assert captured.out == f"slice error: 'int' object is not subscriptable. Inputs: (5678,), {{}}\n"
