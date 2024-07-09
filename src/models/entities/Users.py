from utils.DateFormat import DateFormat


class Users():

    def __init__(self, name=None,second_name=None, cellphone=None, password=None) -> None:
        self.id = id
        self.name = name
        self.second_name = second_name
        self.cellphone = cellphone
        self.password = password

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'cellphone': self.cellphone,
            'password': str(self.password)
        }
