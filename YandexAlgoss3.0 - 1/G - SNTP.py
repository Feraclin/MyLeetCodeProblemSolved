from datetime import timedelta
def time_real(lst: list[str]) -> None:
    name = ['hours', 'minutes', 'seconds']
    a = timedelta(**dict(zip(name, map(int, lst[0].split(':'))))).total_seconds()
    b = timedelta(**dict(zip(name, map(int, lst[1].split(':'))))).total_seconds()
    c = timedelta(**dict(zip(name, map(int, lst[2].split(':'))))).total_seconds()

    if a <= c:
        print(timedelta(seconds=(b + round((c - a)/2))%86400))

    else:
        print(timedelta(seconds=(b + round((c + 86400 - a)/2 + 0.5)%86400)))


a = ['15:01:00',
     '18:09:45',
     '15:01:40']

b = ['23:59:55',
     '01:00:00',
     '00:00:00']

c = ['01:00:05',
     '23:59:55',
     '01:00:15']

time_real(a)
time_real(b)
time_real(c)
