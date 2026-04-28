print("Enter Expression: ")
lines = []

while True:
    temp = input()
    if temp == "":
        break
    lines.append(temp.replace(" ", ""))

replaces = {}
exps = {}

optimized = []

for line in lines:
    lhs,rhs = line.split("=")

    for replicate, original in replaces.items(): #.items(COPY PROPOGATION
        rhs = rhs.replace(replicate, original)

    if rhs in exps:
        optimized.append(f"{lhs} = {exps[rhs]}")
        replaces[lhs] = exps[rhs]
    else:
        exps[rhs] = lhs
        optimized.append(f"{lhs} = {rhs}")

print("Optimzed Expressions: ")
for line in optimized:
    print(line)
