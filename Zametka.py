import datetime

class Zametka (object):
    def __init__(self, id:int, heading:str, body:str):
        self._id = id # Идентификатор заметки
        self._heading = heading # Заголовок
        self._body = body # Тело заметки
        self.__installtime() # Дата и время последнего изменения

    # @property
    def get_data(self):
        return self._sortDate

    def get_id(self):
        return self._id
    @property
    def get_heading(self):
        return self._heading
    @property
    def get_body(self):
        return self._body
    @property
    def get_date(self):
        return self._date
    
    # Перезапись тела
    def overwriting(self,string:str):
        self._body = string
        self._installtime()

    # Дописывание тела
    def complement(self,string:str):
        self._body = self._body + string
        self.__installtime()
    
    # Вывод заметки в консоль
    def __str__(self):
        string = str(self._id)+'. '+self._heading.upper()+'\n'
        string += self._body+'\n'
        string += self._date+'\n'
        return string

    def __installtime(self):
        self._sortDate = datetime.datetime.today()
        self._date = self._sortData.strftime("%Y.%m.%d %H:%M")
    
