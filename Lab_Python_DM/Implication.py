def implication(p, q):
    return (not p) or q  # Correct formula for p --> q

print("p       q       p-->q")  
print("---------------------")

for p in [True, False]:
    for q in [True, False]:
        a = implication(p, q)
        print(f"{p:<7} {q:<7} {a}")