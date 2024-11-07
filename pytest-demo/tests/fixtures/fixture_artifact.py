import pytest

@pytest.fixture(scope="module")
def setup_list():
    city = ["NYC", "Chicago", "London", "Mumbai"]
    yield city
