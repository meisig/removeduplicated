#1
def remove_duplicates_wrong(l: list[int]) -> list[int]:
    d = {}
    i = 0
    while i < len(l):
        if l[i] in d:
            l.pop(i)
        else:
            d[l[i]] = 1
            i += 1
    return l


def remove_duplicates(l: list[int]) -> list[int]:
    s = list(set(l))
    s.sort()  # sorted(s)
    return s


if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))
#2
def remove_duplicates(lst):
    count = {}
    result = []

    for num in lst:
        if num not in count:
            count[num] = 1
            result.append(num)
        else:
            if count[num] < 2:
                count[num] += 1
                result.append(num)

    return result
if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 3, 3, 3, 5, 5, 6]))
