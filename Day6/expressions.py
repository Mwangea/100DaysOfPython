#((P ∨ Q) ∧ R) v ((P ∧ R) ∨ (Q ∧ R))

P = True
Q = False
R = True

var_1 = (P or Q) and R     #(P ∨ Q) ∧ R
var_2 = (P and R) or (Q and R)  #(P ∧ R) ∨ (Q ∧ R)

result = var_1 or var_2

print("Result of Expression :", result)


#(-P ^ - Q) v (Q ^ -R)

P = True
Q = False
R = True

var_1 = (not P) and (not Q)  #(-P ^ -Q)
var_2 = Q and (not R) # (Q ^ -R)

result = var_1 or var_2

print("Result of Expression:", result)