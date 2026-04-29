import sys


def first(lhs):
    result = set()

    for p in productions[lhs]:
        if p == "E":
            result.add(p)
        else:
            ctr = 0
            for x in p:
                if x not in LHS_list:
                    result.add(x)
                    break
                else:
                    fx = first(x)
                    result.update(x for x in fx if x != "E")

                    if "E" not in fx:
                        break
                    else:
                        ctr += 1

            if ctr == len(p):
                result.add("E")

    return result


print("Enter PRoduction RUles: e.g., S -> iEtS | iEtSeS | a). Hit Enter twice to terminate:")
productions = {}
LHS_list = []
rules = []
while True:
    line = input()
    if line == '':
        break
    rules.append(line)

for rule in rules:

    lhs, rhs = [x.strip() for x in rule.split('->')]
    # Split productions and clean up leading/trailing whitespace from each
    productions[lhs] = [p.strip() for p in rhs.split('|')]
    LHS_list.append(lhs)

LHS_ordered = LHS_list[::-1]

print("FIRST SETS")
first_of = {}

for l in LHS_ordered:
    first_of[l] = first(l)
    print(f"First{l} : {first_of[l]}")