def unHash(num):
    res=""
    letters= "acdegilmnoprstuw"
    num = int(num)
    while num >7:
        res = letters[int(num%37)] + res
        num = num/37
    return res[1:]
