import re

def generate_tac(expression):
    lhs, rhs = [x.strip() for x in expression.split('=')]

    tokens = re.findall(r'[a-zA-Z0-9]+|[\+\-\*/]', rhs)

    precedence = [['*', '/'], ['+', '-']]
    temp_count = 1

    print("\nGenerated TAC:")
    for ops in precedence:
        i = 0
        while i < len(tokens):
            if tokens[i] in ops:
                # Identify the "triplet": operand1 operator operand2
                operator = tokens[i]
                left_operand = tokens[i - 1]
                right_operand = tokens[i + 1]

                temp_name = f"t{temp_count}"

                print(f"{temp_name} = {left_operand} {operator} {right_operand}")

                # Replace the three tokens with the new temporary variable
                tokens[i - 1: i + 2] = [temp_name]

                temp_count += 1
                # Adjust index to account for the shortened list
                i -= 1
            i += 1

    # 4. Final Assignment
    # The last remaining token is the final result of the RHS
    print(f"{lhs} = {tokens[0]}")


# --- Main Block ---
expr = input("Enter an assignment expression (e.g., x = a + b * c / d): ")
generate_tac(expr)