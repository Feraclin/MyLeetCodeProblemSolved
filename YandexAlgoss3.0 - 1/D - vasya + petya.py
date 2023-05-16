def vasya_seat(child: int, var: int, row: int, col: int) -> tuple[int, int]|tuple[int]:
    petya_num = (row - 1) * 2 + col
    petya_var = petya_num % var
    if not petya_var:
        petya_var = var

    if child // petya_var < 2 or child  == var:

        return (-1,)

    if (child - petya_num) - var >= 0:
        tmp = 0
        if var % 2 == 1:
            if col == 2:
                tmp = 1
                col = 1
            else:
                col += 1

        return row + var // 2 + tmp, col

    else:
        tmp = 0
        if var % 2 == 1:
            if col == 1:
                tmp = 1
                col = 2
            else:
                col -= 1

        return row - var // 2 - tmp, col


#print(*vasya_seat(*[int(input()) for _ in range(4)]))
print(vasya_seat(11,5,3,2))
assert(vasya_seat(25, 2, 1,2) == (2, 2))
assert(vasya_seat(25, 2, 7,2) == (8, 2))
assert(vasya_seat(25, 3, 7,2) == (9, 1))
assert(vasya_seat(25, 3, 1,2) == (3, 1))
assert(vasya_seat(25, 4, 1,2) == (3, 2))
assert(vasya_seat(25, 10, 1,2) == (6, 2))
assert(vasya_seat(25, 11, 1,2) == (7, 1))
assert(vasya_seat(25, 2, 13,1) == (12, 1))
assert(vasya_seat(25, 13, 7,1) == (-1,))
assert(vasya_seat(2, 2, 1,1) == (-1,))
assert(vasya_seat(5, 2, 2,2) == (1, 2))
assert(vasya_seat(5, 3, 2,2) == (1, 1))
assert(vasya_seat(5, 3, 2,1) == (-1,))
assert(vasya_seat(6, 2, 2,2) == (3, 2))