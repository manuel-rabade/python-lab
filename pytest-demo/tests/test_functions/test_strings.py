from pytest_demo import strings
import pytest

@pytest.mark.strings
class TestFrameworkSuite:
    def test_fixture_values(self, setup_list):
        assert setup_list[0] == "NYC"

    def test_reversed_text(self):
        assert strings.reversed_text("hello") == "olleh"

    def test_lower_text(self):
        assert strings.lower_text("HELLO") == "hello"

def test_example():
    assert 1 == 1
