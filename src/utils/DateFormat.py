import datetime


class DateFormat():

    @classmethod
    def ConvertDate(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
    
    @classmethod
    def ConvertDateTime(self, datetime):
        return datetime.datetime.strftime(datetime, '%d/%m/%Y %H:%M')
