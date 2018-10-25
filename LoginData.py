from FileReader import FileReader

class LoginData():
    def __init__(self):
        self.SetLoginData()

    def SetLoginData(self):
        fileReader = FileReader()
        loginData = fileReader.ReadLines("loginData.txt")
        self.login = loginData[0]
        self.password = loginData[1]
    
    def GetLogin(self):
        return self.login

    def GetPassword(self):
        return self.password