def frequencies(s):
    dct = {x:s.count(x) for x in s}
    return [(x,dct[x])for x in dct]

def encode(freqs, s):
    my_freq = list(freqs)
    if len(my_freq)<=1: return None
    tree_sim, res = get_tree(my_freq), ""
    for i in s: res += tree_sim[i]
    return res

def decode(freqs,bits):
    my_freq = list(freqs)
    if len(my_freq)<=1: return None
    tree_sim = get_tree(my_freq)
    tree_sim= {tree_sim[x]:x for x in tree_sim}
    i,res = 0, ""
    while i < len(bits):
        char = ""
        while i < len(bits) and char not in tree_sim: char, i= char + bits[i], i+1
        res += tree_sim[char]
    return res


def get_tree(my_freq):
    tree_sim = {}
    while len(my_freq) >1:
        my_freq.sort(key=lambda x:x[1],reverse=True)
        a,b = my_freq.pop(), my_freq.pop()
        s_a,s_b = a[0], b[0]
        my_freq.append((s_a+s_b, a[1] + b[1]))
        for i in s_a: tree_sim[i] = "0" + tree_sim.get(i,"")
        for j in s_b: tree_sim[j] = "1" + tree_sim.get(j,"")
    return tree_sim