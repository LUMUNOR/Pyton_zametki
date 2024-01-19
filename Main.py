import Book

book = Book.Book()

book.addNewZametka()

def printMenu():
    print('-------------------------------')
    print('Выберите дальнейшее действие:')
    print('1.Вывести все заметки;')
    print('2.Добавить новую заметку;')
    print('3.Редактировать заметку;')
    print('4.Удалить заметку;')
    print('5.Вывести конкретную заметку;')
    print('6.Отсортировать заметки по дате;')
    print('7.Сохранить заметку в файл;')
    print('8.Загрузить заметку из файла;')
    print('9.Завершить работу.')
    print('-------------------------------')

flag = True
while flag:
    printMenu()
    index = int(input())
    match index:
        case 1:
            book.printBook()
        case 2:
            book.addNewZametka()
        case 3:
            book.editingZam()
        case 4:
            book.deleteZam()
        case 5:
            book.printZam()
        case 6:
            book.sortByDate()
        case 7:
            book.save()
        case 8:
            book.load()
        case 9:
            print('Досвидания!')
            flag = False