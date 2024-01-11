class Zametka ():
    def __init__(self, id, heading, body, date) -> None:
        self._id = id # Идентификатор заметки
        self._heading = heading # Заголовок
        self._body = body # Тело заметки
        self._date = date # Дата и время последнего изменения

    @property
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
    
