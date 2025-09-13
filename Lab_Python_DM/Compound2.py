
def implication(p, q):
    return (not p) or q  # Correct formula for p --> q
def implication1(q, r):
    return (not q)or r

print("p       q       r       (p-->q)^(q-->r)")  
print("----------------------------------------")

for p in [True, False]:
    for q in [True, False]:
        for r in[True, False]:
            a = implication(p, q)
            b =implication1(q,r)
            c=a and b
            print(f"{p:<7} {q:<7} {r:<7} {c}")