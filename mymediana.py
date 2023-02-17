def mediana(lst):
    n = len(lst)
    i = n // 2
    if n % 2:
        return sorted(lst)[i] 
    return sum(sorted(lst)[i - 1:i + 1]) / 2