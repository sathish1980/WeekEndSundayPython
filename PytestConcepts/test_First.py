import pytest

class Test_First():

    @pytest.mark.Sanity
    def testfirststestcase(self):
        print("first Test case")

    @pytest.mark.SIT
    def test_001(self):
        print("first Test case")