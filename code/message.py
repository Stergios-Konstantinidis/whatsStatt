from datetime import datetime
class message:
    def __init__(self, date: datetime,  user: str, nombreCaractères = int):
        self.date = date
        self.user = user
        self.nombreChars = nombreCaractères
    def getUser(self):
        return self.user
    
    def __str__(self):
        return self.user
    def __repr__(self) -> str:
        return str(self)