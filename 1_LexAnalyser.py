import re
import os

operators = ["=", "+", "-", "*", "/", "%"]
keywords = ["int", "float", "double", "char", "boolean"]
separators = [";"]
constants = r"\d+"
identifiers = r"[a-zA-Z_]\w*"

text = input("Enter expression: ")
print("Lexical Analysis Started:\n")

# Pattern (Words/Identifiers) OR (Numbers) OR (Operators/Separators)
token_pattern = r"[a-zA-Z_]\w*|\d+|[=+\-*/%;]"

tokens = re.findall(token_pattern, text) # returns list
for token in tokens:
    if token in keywords:
        print(f"'{token}' -> Keyword")

    elif token in operators:
        print(f"'{token}' -> Operator")

    elif token in separators:
        print(f"'{token}' -> Separator")

    elif re.fullmatch(constants, token):
        print(f"'{token}' -> Constant")

    elif re.fullmatch(identifiers, token):
        print(f"'{token}' -> Identifier")
