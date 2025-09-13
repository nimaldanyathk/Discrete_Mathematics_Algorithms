def biconditional(p, q):
    return ((not p) or q)and((not q)or p)  # Correct formula for p --> q

print("p       q       p<-->q")  
print("----------------------")

for p in [True, False]:
    for q in [True, False]:
        a = biconditional(p, q)
        print(f"{p:<7} {q:<7} {a}")