
def clean_line(line):
    return line.replace(" ", "")
def split_production(rhs):
    return rhs.split("|")

def follow_compute(start_symbol, grammar, first_set):
    # Initialize FOLLOW sets as empty sets for all Non-Terminals
    follow_set = {nt: set() for nt in grammar}

    # RULE 1: The start symbol always contains '$' (End of Input marker)
    follow_set[start_symbol].add("$")

    changed = True #Flag that sets whenever a symbol is added to FOLLOW SET
    while changed:
        changed = False
        for lhs in grammar:
            for production in grammar[lhs]:
                for i in range(len(production)):
                    symbol = production[i]

                    # We only calculate FOLLOW sets for Non-Terminals
                    if not symbol.isupper():
                        continue

                    j = i + 1 #Iterator for next symbol in the same production
                    add_follow = True  # Flag to trigger Rule 3 if needed

                    while j < len(production):
                        next_symbol = production[j]

                        # RULE 2 (Part A): If the neighbor is a terminal
                        if not next_symbol.isupper():
                            if next_symbol not in follow_set[symbol]:
                                follow_set[symbol].add(next_symbol)
                                changed = True
                            add_follow = False  # Terminal blocks further symbols
                            break

                        # RULE 2 (Part B): If neighbor is a Non-Terminal
                        # Add FIRST(neighbor) - {epsilon} to current symbol's FOLLOW set
                        before = len(follow_set[symbol])
                        follow_set[symbol].update(first_set[next_symbol] - {"eps", "Epsilon", "ε"})

                        if len(follow_set[symbol]) > before:
                            changed = True

                        # Check if the neighbor can derive Epsilon
                        if any(e in first_set[next_symbol] for e in ["eps", "Epsilon", "ε"]):
                            j += 1  # Nullable neighbor: move to the next symbol
                        else:
                            add_follow = False  # Neighbor is NOT nullable; blocks Rule 3
                            break

                    # RULE 3: If symbol is at the end or all neighbors were nullable
                    if add_follow:
                        before = len(follow_set[symbol])
                        # Inherit everything from the parent (LHS) FOLLOW set
                        follow_set[symbol].update(follow_set[lhs])
                        if len(follow_set[symbol]) > before:
                            changed = True

    return follow_set


# --- Main Execution Block ---

n = int(input("Enter the number of non terminals: "))
print("Enter the production rules (e.g., S -> AB | c):")

grammar = {}
for _ in range(n):
    line = input()
    line = clean_line(line)
    lhs, rhs = line.split("->")
    grammar[lhs] = split_production(rhs)

# Collect pre-calculated FIRST sets
first_set = {}
print("\nEnter FIRST sets (space-separated, e.g., a b eps):")
for nt in grammar:
    vals = input(f"First({nt}) : ").split()
    first_set[nt] = set(vals)

# Identify the first Non-Terminal entered as the Start Symbol
start_symbol = list(grammar.keys())[0]

# Compute and Display Results
result = follow_compute(start_symbol, grammar, first_set)

print("\n--- FINAL FOLLOW SETS ---")
for nt, s in result.items():
    print(f"FOLLOW({nt}) = {s if s else '{}'}")