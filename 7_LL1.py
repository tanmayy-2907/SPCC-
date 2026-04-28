#PROVIDED THAT FIRST & FOLLOW SET IS GIVEN FOR THE GRAMMAR
def clean_line(line):
    return line.replace(" ","")

def split_production(rhs):
    return rhs.split("|")

def compute(production, first_set):
    """
        Calculates the FIRST set of a production string (e.g., FIRST(alpha)).
        Used to determine which terminals trigger a specific production.
    """
    result = set()

    if production == "eps":
        result.add("eps")
        return result

    all_nullable = True
    for p in production:
        # Case 1: Symbol is a terminal - It is the FIRST and terminates scan
        if p.islower():
            result.add(p)
            all_nullable = False
            return result

        #Case 2: Non-Terminal - Inherit FIRST symbols excluding epsilon
        result.update(first_set[p] - {"eps"})

        # Case 3: Blocking - If neighbor isn't nullable, stop scanning RHS
        if "eps" not in first_set[p]:
            all_nullable = False
            break

    # Case 4: Complete Nullability - If all symbols derive eps, the whole rule derives eps
    if all_nullable:
        result.add("eps")

    return result


def ll1parser(first_set, follow_set, grammar):
    """
        Constructs the 2D Parsing Table M[Non-Terminal, Terminal].
        Logic: Map productions to input symbols that can start them.
    """
    table = {}

    for lhs in grammar:
        table[lhs] = {} #ROWS

        for production in grammar[lhs]:
            # Find the FIRST set of the right-hand side string
            test = compute(production, first_set)

            # TABLE RULE 1: For each terminal 'a' in FIRST(alpha),
            # place A -> alpha in M[A, a]
            for t in test - {"eps"}:
                table[lhs][t] = production

            # TABLE RULE 2: If epsilon is in FIRST(alpha),
            # for each terminal 'b' in FOLLOW(A), place A -> alpha in M[A, b]
            if "eps" in test:
                for t in follow_set[lhs]:
                    table[lhs][t] = production

    return table

#INPUT
n = int(input("Enter the number of non terminals present in the grammar = "))
print("enter the the production (Eg: S -> AB | c): ")

grammar={}
for _ in range(n):
    line = input()
    line = clean_line(line)
    lhs, rhs = line.split("->")
    grammar[lhs] = split_production(rhs)

# Manual data entry for FIRST sets (calculated in Exp 5)
first_set = {}
for nt in grammar:
    vals = input(f"First({nt}) : ").split()
    first_set[nt] = set(vals)

# Manual data entry for FOLLOW sets (calculated in Exp 6)
follow_set = {}
for nt in grammar:
    vals = input(f"Follow_{nt} = ").split()
    follow_set[nt] = set(vals)

table = ll1parser(first_set, follow_set, grammar)
print("\nLL(1) Parsing Table Structure:")
for nt, rules in table.items():
    print(f"{nt} : {rules}")