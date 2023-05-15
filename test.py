1.
def to_camel_case(text):
    import re
    return re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[1::]) # lowerCamelCase, если нужен CamelCase, убрать первые re и срез в генераторе

2.
class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs) # лучше перевернуть и создавать только в случае если _instances не содержит экземпляр класса
        return cls._instances[cls]

3.
count_bits = lambda n: bin(n).count('1') # пропущен аргумент анонимной функции

4.
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n)))) # в выводе n было не на месте

5.
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd" # пропущен number

