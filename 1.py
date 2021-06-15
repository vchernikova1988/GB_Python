class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data):
        day, month, year = map(int, data.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(data):
        try:
            day, month, year = map(int, data.split('-'))
            return day <= 31 and month <= 12 and year <= 2021
        except ValueError:
            raise ValueError('Строка должна быть в формате "ДД-ММ-ГГГГ"')





