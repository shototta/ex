class Human:
    genom_count = 46
    def __init__(self,name:str,age:int,description:str) -> None:
        self.name = name
        self.age = age
        self.description = description

    def show_des(self):
        print(f'{self.name},{self.description},{self.age} years old')

    @classmethod
    def get_genom_count(cls):
        return cls.genom_count

    @classmethod
    def get_genom_count(cls,count: int):
        cls.genom_count = count

    @staticmethod
    def chose_name():
        return random.choise(('ilias','ruslan','maxim','triva'))