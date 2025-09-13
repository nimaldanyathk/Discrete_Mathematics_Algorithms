def exclusive_disjunction(p, q):
    return (p and not q) or (not p and q)

print("p       q       p xor q")  # Column headers with space
print(".-_-_-_-_-_-_-_-_-_-_-_-.")
for p in [True, False]:
    for q in [True, False]:
        a = exclusive_disjunction(p, q)
        print(f"{p:<7} {q:<7} {a}")  