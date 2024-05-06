import pytest


class TestClass:
    def test_one(self):
        x = 'this'
        assert "t" in x


def test_always_passes():
    assert True


def test_always_fails():
    assert False
