import pytest


class TestSample(object):

    @pytest.mark.smoke
    def test_equal(self):
        assert 1 == 1

    def test_not_equal(self):
        assert 1 != 0

