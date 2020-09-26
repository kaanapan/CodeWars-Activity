def encode_rail_fence_cipher(string, n):
    dct,s = {x:"" for x in range(n)}, gen(n)
    for i in range(len(string)):
        rail = next(s)
        dct[rail] += string[i]
    return "".join([dct[x] for x in range(n)])
def decode_rail_fence_cipher(string, n):
    len_s, dct, s = len(string), {x:0 for x in range(n)}, gen(n)
    for i in range(len_s):
        rail = next(s)
        dct[rail] += 1
    for i in range(n):
        take_len = dct[i]
        dct[i],string = string[:take_len], string[take_len:]
    res,s = "", gen(n)
    for i in range(len_s):
        rail = next(s)
        res,dct[rail] = res + dct[rail][0], dct[rail][1:]
    return res
def gen(n):
    while True:
        for i in range(n): yield i
        for i in range(n-2,0,-1): yield i