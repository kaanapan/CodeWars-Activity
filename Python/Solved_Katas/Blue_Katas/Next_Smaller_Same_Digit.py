def next_smaller(n):
    n = str(n)
    first = find_first(n)
    second = find_second(n, first)
    if first == -1 or second == -1 or (first == 0 and n[second + first + 1] == "0"):
        return -1
    n = swap(n, first, second + first + 1)
    return int(n[:first + 1] + "".join(sorted(n[first + 1:], reverse=True)))


def find_first(n):
    for i in range(len(n) - 1, -1, -1):
        for char2 in n[i + 1:]:
            if n[i] > char2:
                return i
    return -1


def find_second(n, i):
    if i == -1:
        return -1
    maxi = "-1"
    j_i = -1
    for j, char2 in enumerate(n[i + 1:]):
        if n[i] > char2 > maxi:
            maxi = char2
            j_i = j
    return j_i


def swap(n, i, j):
    return n[:i] + n[j] + n[i + 1:j] + n[i] + n[j + 1:]


next_smaller("1262347")
