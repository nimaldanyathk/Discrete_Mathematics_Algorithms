def is_reflexive(relation, set_A):
    for a in set_A:
        if (a, a) not in relation:
            print("The relation is NOT reflexive.")
            return False  
    print("The relation is reflexive.")
    return True  

def is_symmetric(relation):
    for (a, b) in relation:
        if (b, a) not in relation:  
            print("The relation is NOT symmetric.")
            return False
    print("The relation is symmetric.")
    return True  

def is_transitive(relation):
    for (a, b) in relation:
        for (x, y) in relation:
            if b == x and (a, y) not in relation:
                print("The relation is NOT transitive.")
                return False
    print("The relation is transitive.")
    return True
            
def verify_equivalence_relation(relation, set_A):
    reflexive = is_reflexive(relation, set_A)
    symmetric = is_symmetric(relation)
    transitive = is_transitive(relation)
    
    return reflexive and symmetric and transitive

set_A = {1, 2, 3, 4}
relation1 = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 1), (3, 4), (4, 3)}

if verify_equivalence_relation(relation1, set_A):
    print("The relation is an equivalence relation.")
else:
    print("The relation is NOT an equivalence relation.")