import datetime

class Zametka (object):
    def __init__(self, id:int, heading:str, body:str):
        self._id = id # Идентификатор заметки
        self._heading = heading # Заголовок
        self._body = body # Тело заметки
        self.__installtime() # Дата и время последнего изменения
    
    # def __init__(self, id:str, heading:str, body:str,date:str):
    #     self._id = int(id) # Идентификатор заметки
    #     self._heading = heading # Заголовок
    #     self._body = body # Тело заметки
    #     self._date = date # Дата и время последнего изменения
    #     self._sortDate = datetime.datetime.strptime(date, '%Y.%m.%d %H:%M')

    def get_data(self):
        return self._sortDate

    def get_id(self):
        return self._id
    
    def get_heading(self):
        return self._heading
    
    def get_body(self):
        return self._body
    
    def get_date(self):
        return self._date
    
    def set_id(self,id:int):
        self._id = id
    
    # Перезапись тела
    def overwriting(self,string:str):
        self._body = string
        self.__installtime()

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
        self._date = self._sortDate.strftime("%Y.%m.%d %H:%M")

class Zametkaload(Zametka):
    
    def __init__(self, id:str, heading:str, body:str,date:str):
        self._id = int(id) # Идентификатор заметки
        self._heading = heading # Заголовок
        self._body = body # Тело заметки
        self._date = date # Дата и время последнего изменения
        self._sortDate = datetime.datetime.strptime(date, '%Y.%m.%d %H:%M')
    
