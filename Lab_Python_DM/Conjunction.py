def conjunction(p,q):
    return p and q
print("p     q     p^q")
for p in[True, False]:
    for q in[True, False]:
        a=conjunction(p,q)
        print(p,q,a)