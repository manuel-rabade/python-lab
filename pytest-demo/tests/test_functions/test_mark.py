import pytest
import sys

@pytest.mark.slow
def test_heavy():
    i = 0
    for x in range(100):
        for y in range(1000):
            x**y
            i += 1
    assert i == 100000

@pytest.mark.parametrize('test_input', [82, 78, 66])
def test_params(test_input):
    assert test_input > 50

@pytest.mark.skip(reason="Skipping unconditional")
def test_skip_01():
    assert 5 + 5 == 10

@pytest.mark.skipif(sys.platform == 'win32', reason="Skipping because OS is Windows")
def test_skip_02():
    assert 5 + 6 == 11

@pytest.mark.xfail(reason="known bug")
def test_xfail_01():
    assert 5 + 6 == 10

@pytest.mark.xfail(raises=AssertionError, reason="known issue")
def test_xfail_02():
    assert 5 + 6 == 15
