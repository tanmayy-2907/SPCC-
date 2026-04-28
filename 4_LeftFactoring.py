# # Helper function to find the longest common prefix between two strings
# def get_common_prefix(str1, str2):
#     min_len = min(len(str1), len(str2))
#     for i in range(min_len):
#         if str1[i] != str2[i]:
#             return str1[:i]
#     return str1[:min_len]
#
# print("Enter Production Rules (e.g., S -> iEtS | iEtSeS | a). Hit Enter twice to terminate:")
#
# rules = []
# while True:
#     line = input()
#     if line == '':
#         break
#     rules.append(line)
#
# print("\nGrammar after Left Factoring:")
#
# for rule in rules:
#     lhs, rhs = [x.strip() for x in rule.split('->')]
#     productions = [p.strip() for p in rhs.split('|')]
#
#     final_rhs = []
#     new_rules = [] # To store the new A' rules
#
#     while len(productions) > 0:
#         first = productions.pop(0)
#
#
#         matches = [first]
#
#         # Check remaining productions for a common prefix
#         to_remove = []
#         for p in productions:
#             # check if they share at least the first character to be worth factoring
#             if p[0] == first[0]:
#                 matches.append(p)
#                 to_remove.append(p)
#
#         # Remove matched items from the main list so we don't process them again
#         for item in to_remove:
#             productions.remove(item)
#
#         if len(matches) > 1:
#             # 1. Find the Longest Common Prefix (alpha) for the whole group
#             # We start by assuming the first string is the prefix, then shrink it
#             alpha = matches[0]
#             for i in range(1, len(matches)):
#                 alpha = get_common_prefix(alpha, matches[i])
#
#             # 2. Create the remainders (beta)
#             betas = []
#             for m in matches:
#                 remainder = m[len(alpha):].strip()
#                 if remainder == "":
#                     betas.append("ε")
#                 else:
#                     betas.append(remainder)
#
#
#             new_lhs = lhs + "'"
#
#
#             final_rhs.append(f"{alpha}{new_lhs}")
#
#             new_rules.append(f"{new_lhs} -> {' | '.join(betas)}")
#
#         else:
#
#             final_rhs.append(first)
#
#     print(f"{lhs} -> {' | '.join(final_rhs)}")
#
#     for nr in new_rules:
#         print(nr)


import os
print("Enter PRoduction RUles: e.g., S -> iEtS | iEtSeS | a). Hit Enter twice to terminate:")

rules = []
while True:
    line = input()
    if line == '':
        break
    rules.append(line)

print("\nGrammar after Left Factoring:")

for rule in rules:
    lhs, rhs = [x.strip() for x in rule.split('->')]
    productions = [x.strip() for x in rhs.split('|')]

    if len(productions) < 2:
        print(rule)
        continue

    common = os.path.commonprefix(productions)
    if common:
        new_lhs = lhs + "'"

        # Identify which productions share the prefix and which don't
        factored_parts = []
        other_parts = []

        for p in productions:
            if p.startswith(common):
                factored_parts.append(p[len(lhs):])
            else:
                other_parts.append(p)

        # res1: A -> alpha A'
        combinedlhsrhs = [f"{common}{new_lhs}"] + other_parts
        print(combinedlhsrhs)

        res1 = f"{lhs} -> {' | '.join(combinedlhsrhs)}"

        # res2: A' -> beta1 | beta2 |
        suffixes = [s if s != "" else "E" for s in factored_parts]
        print(suffixes)
        res2 = f"{new_lhs} -> {' | '.join(suffixes)}"

        print(res1)
        print(res2)

    else:
        print(rule)