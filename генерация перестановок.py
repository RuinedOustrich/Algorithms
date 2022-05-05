def gen_numbers(N: int, M: int, prefix=[]):

    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_numbers(N, M - 1, prefix)
        prefix.pop()

def gen_bin(M, prefix = ""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M - 1, prefix + digit)

def generate_permutations(N: int, M: int=-1, prefix=[]):
    """ Генерация всех перестановок N числе в M позициях,
        с префиксом
    """
    M = N if M == -1 else M # По умолчанию M числе в N позициях
    if M == 0:
        print(*prefix)
        return
    for number in range(N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

def find(number, A):
    "Ищет number в А и возвращает True если такой есть и False, если нет"
    for x in A:
        if number == x:
            return True
    return False

# Для N ричной CC
#gen_numbers(4, 5)

# Только для двоичной СС
#gen_bin(10)

generate_permutations(5)