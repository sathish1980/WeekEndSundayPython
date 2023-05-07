import pytest
@pytest.mark.usefixtures("add")
class Test_Second():

    @pytest.mark.run(order=1)
    #@pytest.mark.usefixtures("add")
    def test_second_001(self):
        print("secondlass")

   # @pytest.mark.dependency()
    @pytest.mark.run(order=2)
    #@pytest.mark.usefixtures("add")
    def test_firstssecondclass(self,add):
        print("test_firstsecondclass")
        print(add)



    @pytest.mark.run(order=3)
    #pytest.mark.usefixtures("add")
    def test_additionof2number(self,add):
        print(add)