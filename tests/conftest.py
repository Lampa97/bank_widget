import pytest

@pytest.fixture
def invalid_card_number():
    return 'Visa 45679345205'

