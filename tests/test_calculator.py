
import pytest
from src.calculator import add


@pytest.mark.unit
def test_add():

    assert add(2, 3) == 5
