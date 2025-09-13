import itertools

#Define the logical expression (p<-->q)=(p^q)or(¬p^¬q)

def implies(a,b):
    return not a or b
#a-->b i s equivalent to not a or b

def check_expression(p,q):
    return implies(implies(p,q) and implies(q,p), (p and q)or(not p and not q))

#Generate all combinations of truth values for p,q,r
truth_values=list(itertools.product([False,True], repeat=2))

#Check the expression for each combination of p,q,r
results=[]

for p,q in truth_values:
    result=check_expression(p,q)
    results.append(result)

print(results)


#check if the result is a tautology, contradiction or contingency
if all(results):
    print("The expression is a tautology")
elif not any(results):
    print("The expression is a contradiction")
else:
    print("The expression is a contigency")

  
#Try all the qns !
           