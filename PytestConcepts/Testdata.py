from Utils import ExcelRead


class Testdata():

    credentials = [("kumar.sathish189@gmail.com", "Admin@123"), ("kumar.sathish189@gmail.com", "Admin@123")]
    credentials_dic = [{"username": "kumar.sathish189@gmail.com", "password": "Admin@123"},
                       {"username": "kumar.sathish189@gmail.com", "password": "Admin@123"}]
    credential_excel_dic = [ExcelRead.Excel_Read.retrundicvalue()]