print("Enter Production Rules (e.g., E -> E+T | T). Hit Enter twice to terminate:")

rules = []
while True:
    line = input()
    if line == '':
        break
    rules.append(line)

print("\nGrammar after Eliminating Left Recursion:")

for rule in rules:

    lhs, rhs = [x.strip() for x in rule.split('->')]
    # Split productions and clean up leading/trailing whitespace from each
    productions = [p.strip() for p in rhs.split('|')]

    alphas = []
    betas = []

    for p in productions:
        if p.startswith(lhs):
            alphas.append(p[len(lhs):].strip())
        else:
            betas.append(p)

    if alphas:
        new_lhs = lhs + "'"

        # A -> beta A'
        if not betas:
            res1 = f"{lhs} -> {new_lhs}"
        else:
            res1 = f"{lhs} -> {' | '.join([b + new_lhs for b in betas])}"

        # A' -> alpha A' | ε
        res2 = f"{new_lhs} -> {' | '.join([a + new_lhs for a in alphas])} | ε"

        print(res1)
        print(res2)
    else:
        # If no left recursion was found, print the original rule
        print(rule)