import itertools

#Define the logical expression (p-->q)and(q-->r)-->(p-->r)

def implies(a,b):
    return not a or b
#a-->b i s equivalent to not a or b 

def check_expression(p,q,r):
    return implies(implies(p,q) and implies(q,r), implies(p,r))

#Generate all combinations of truth values for p,q,r
truth_values=list(itertools.product([False,True], repeat=3))

#Check the expression for each combination of p,q,r
results=[]
print(f"{'p':<5} {'q':<5} {'r':<5} {'result':<7}")


for p,q,r in truth_values:
    result=check_expression(p,q,r)
    print(f"{p:<5} {q:<5} {r:<5} {result:<7}")
    results.append(result)

print(results)


#check if the result is a tautology, contadiction or contigency
if all(results):
    print("The expression is a tautology")
elif not any(results):
    print("The expression is a contradiction")
else:
    print("The expression is a contigency")