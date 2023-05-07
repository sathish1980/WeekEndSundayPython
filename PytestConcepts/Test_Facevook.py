import pytest


class Test_facebook():

    @pytest.mark.usefixtures("dataload")
    def test_facebookLogin(self,dataload):
        print(dataload[0])
        print(dataload[1])
        print(dataload[2])
        for eachdata in dataload:
            print(eachdata)
    @pytest.mark.usefixtures("mutidata")
    def test_browsernames(self,mutidata):
        print(mutidata[1])
