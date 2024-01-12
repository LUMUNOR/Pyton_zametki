import Zametka

class Book(object):
    def __init__(self) -> None:
        self._list = list()
    
    def addNewZametka(self):
        print('Введите заголовок:')
        heading = input()
        print('Введите тело заметки:')
        body = input()
        newZam = Zametka.Zametka(self.__maxID(),heading,body)
        self._list.append(newZam)

    def printBook(self):
        print('Список заметок:\n')
        for zam in self._list:
            print(zam)
    
    def __maxID(self):
        maxID = 0
        if len(self._list) == 0: return maxID
        else:
            for zam in self._list:
                if (zam.get_id() > maxID): maxID = zam.get_id()
        return maxID+1
    
    def __zamById(self,id):
        for zam in self._list:
            if zam.get_id == id: return zam