def disjunction(p, q):
    return p or q

print("p       q       p|q")  
print("--------------------")

for p in [True, False]:
    for q in [True, False]:
        a = disjunction(p, q)
        print(f"{p:<7} {q:<7} {a}")  