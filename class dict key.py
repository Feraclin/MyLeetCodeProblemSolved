class A():
    def __init__(self, name:str) -> None:
        self.name = name
        from random import randint
        self.id_ = randint(1, 1e6)

    def __hash__(self) -> int:
        return hash(self.id_)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

print(a:=A("name")) # name

dct = {'c': 7, a: 5, 'b': 6}
print(dct) # {'c': 7, name: 5, 'b': 6}

a.name = 'surname'
print(a) # surname

print(dct) # {'c': 7, surname: 5, 'b': 6}