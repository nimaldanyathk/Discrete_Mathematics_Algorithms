def conjunction(p,q):
    return p and q
def disjunction(p,q):
    return p or q
print("p       q       (p^q)||¬q")  
print("----------------------")

for p in [True, False]:
    for q in [True, False]:
        a = disjunction(conjunction(p, q), not q)
        print(f"{p:<7} {q:<7} {a}")