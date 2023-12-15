inp = [int(i) for i in input("Enter Input : ").split()]

def sort(L: list) -> list:
    T = [None] * (len(L))
    temp = []
    for i, data in enumerate(L):
        if data < 0:
            T[i] = data
        else:
            temp.append(data)

    temp = mergesort(temp)

    for i, data in enumerate(T):
        if data is None:
            T[i] = temp.pop(0)

    return T

def mergesort(L : list):
    if len(L) > 1: # not base case
        mid = len(L) // 2
        
        LL = L[:mid]
        RL = L[mid:]

        mergesort(LL)
        mergesort(RL)


        i = 0
        j = 0
        k = 0

        while i < len(LL) and j < len(RL):
            if LL[i] < RL[j]:
                L[k] = LL[i]
                i += 1
            else:
                L[k] = RL[j]
                j += 1

            k += 1

        while i < len(LL):
            L[k] = LL[i]
            i += 1
            k += 1

        while j < len(RL):
            L[k] = RL[j]
            j += 1
            k += 1

    return L


print(*sort(inp))