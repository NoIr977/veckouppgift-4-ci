
import pytest
from src.price_service import calculate_total


@pytest.mark.integration
def test_total():

    assert calculate_total(100, 200) == 300
