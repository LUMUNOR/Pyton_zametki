import Zametka
import SaveLoad

class Book(object):
    def __init__(self) -> None:
        self._list = list()
        self._saveLoad = SaveLoad.SeveLoad()
    
    #Добавление новой заметки в книгу
    def addNewZametka(self):
        print('Введите заголовок:')
        heading = input()
        print('Введите тело заметки:')
        body = input()
        newZam = Zametka.Zametka(self.__maxID(),heading,body)
        self._list.append(newZam)

    # Вывод на экран всех заметок
    def printBook(self):
        print('Список заметок:\n')
        for zam in self._list:
            print(zam)
    
    # Определитель нового ID
    def __maxID(self):
        maxID = 0
        if len(self._list) == 0: return maxID
        else:
            for zam in self._list:
                if (zam.get_id() > maxID): maxID = zam.get_id()
        return maxID+1
    
    # Возврат заметки по ID
    def __zamById(self,id):
        for zam in self._list:
            if zam.get_id == id: return zam
    
    # Вывод конкретной заметки по ID
    def printZam(self):
        print('Введлте ID заметки которую хотите вывести на экран:')
        id = int(input)
        print(self.__zamById(id))
    
    # Редактирование заметки по ID
    def editingZam(self):
        print('Введите ID заметки:')
        id = int(input)
        print('1.Дополнить заметку;')
        print('2.Переписать заметку.')
        index = int(input)
        match index:
            case 1:
                self._complementZam(id)
            case 2:
                self._overwritingZam(id)


    def _complementZam(self,id):
        print("Введите текст которым хотите дополнить заметку #"+id+":")
        string = input()
        zam = self.__zamById(id)
        zam.complement(string)

    def _overwritingZam(self,id):
        print("Введите новое содержание заметки #"+id+":")
        string = input()
        zam = self.__zamById(id)
        zam.overwriting(string)

    # Удаление заметки по ID
    def deleteZam(self):
        print('Введите ID заметки которую хотите удалить:')
        id = int(input())
        self._list.remove(self.__zamById(id))

    # Сортировка списка заметок по дате
    def sortByDate(self):
        self._list.sort(key = self.getDate)
   
    def getDate(zam):
        return zam.getDate()
    
    # Сохранение заметки в файл
    def save(self):
        print('Введите ID заметки которую хотите сохранить в файл:')
        id = int(input())
        self._saveLoad.seveZametka(self.__zamById(id))

    # Загрузка заметки из файла
    def load(self):
        print('Введите имя файла с заметкой:')
        nameFile = input()
        newZam:Zametka.Zametka = self._saveLoad.loadZametka(nameFile)
        newId = newZam.get_id()
        for zam in self._list:
            if (zam.get_id() == newId):
                newZam.set_id(self.__maxID())
                break
        self._list.append(newZam)