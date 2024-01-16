import Zametka

class SeveLoad():
    # with open('example.txt') as f:
    # # работа с файлом
        
    # f = open('example.txt','r')
    # try:
    #     # работа с файлом
    # finally:
    #     f.close()
    def __init__(self) -> None:
        pass

    def _save(self,name:str,json:str):
        nameFile = name + '.txt'
        with open(nameFile,'w') as f:
            f.write(json)
    
    def _load(self,nameFile:str):
        with open(nameFile,'r') as f:
            json = f.read()
        return json
    
    def seveZametka(self,zametka:Zametka.Zametka):
        json = self._jsonFormat(zametka)
        name = str(zametka.get_id)+'_'+ zametka.get_heading
        self._save(name,json)

    def _jsonFormat(self,zametka:Zametka.Zametka):
        json = str(zametka.get_id)+';'
        json += zametka.get_heading+';'
        json += zametka.get_body+';'
        json += zametka.get_date
        return json
    
    def loadZametka(self,nameFile:str):
        json = self._load(nameFile)
        zametka = self._zametkaFromJson(json)
        return zametka

    def _zametkaFromJson(self,json:str):
        list = json.split(';')
        zametka = Zametka(list[0],list[1],list[2],list[3])
        return zametka