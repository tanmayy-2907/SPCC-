lines = []
while True:
    temp = input()
    if temp == '':
        break
    lines.append(temp)

symtab = []
data_type = {'int':4, 'float':4, 'double':8, 'char':1}

for line in lines:
    line = line.replace('=',' ')
    line = line.replace(';',' ')
    line = line.replace(',',' ')
    words = line.split()

    if words[0] not in data_type:
        continue
    else:
        for variable in words[1:]:
            if variable[0].isalpha():
                symtab.append(f'{words[0]} \t {data_type[words[0]]} \t\t {variable}')

print("Symbol table is:")
print("Type \t Size \t Symbol")
for line in symtab:
    print(line)