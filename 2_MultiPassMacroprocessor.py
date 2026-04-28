def macro_processor_pass1(input_file, output_file):
    mdt_table = []
    mnt_table = []
    ala_data = {}
    mntc = 1
    mdtc = 1
    current_macro = None
    is_defintion = False

    #STEP 1 READ FILE INPUT
    try:
        with open(input_file, 'r') as f:
            code = f.readlines()
    except FileNotFoundError:
        print(f"File Not Found!")
        return

    for line in code:
        parts = line.strip().split()
        if not parts: continue # EMPTY LINES GET SKIPPED

        if parts[0] == "MACRO":
            is_defintion = True
            continue

        if is_defintion:
            macro_name = ""
            args = []

            for p in parts:
                if p.startswith('&'):
                    args.append(p)
                else:
                    macro_name = p

            #UPDATING MNT
            mnt_table.append(f"{mntc} | {macro_name} | {mdtc}") #MNTC , macro name, MDTC where definition begins
            mntc += 1

            #UPDATING ALA
            ala_data[macro_name] = {arg: i for i, arg in enumerate(args)}

            #UPDATING MDT
            mdt_table.append(f"{mdtc} | {line}")
            mdtc += 1
            is_defintion = False
            current_macro = macro_name

        elif parts[0] == "MEND":
            mdt_table.append(f"{mdtc} | MEND")
            mdtc += 1
            current_macro = None

        elif current_macro: #macro_name APART FROM MEND AND MACRO
            processed_line = line.strip()
            for arg, idx in ala_data[current_macro].items():
                processed_line = processed_line.replace(f"&{arg}", f"&{idx}")

            mdt_table.append(f"{mdtc} | {processed_line}")
            mdtc += 1

    #PRINTING
    with open(output_file, 'w') as out:
        out.write("--- MACRO NAME TABLE (MNT) ---\n")
        out.write("Index\tName\tMDT_Ptr\n")
        for entry in mnt_table:
            out.write(entry + "\n")

        out.write("\n--- MACRO DEFINITION TABLE (MDT) ---\n")
        out.write("Index\tInstruction\n")
        for entry in mdt_table:
            out.write(entry + "\n")

        out.write("\n--- ARGUMENT LIST ARRAY (ALA) ---\n")
        for m_name, args in ala_data.items():
            out.write(f"Macro : {m_name}")
            for i, arg in args.items():
                out.write(f"{arg} : {i}" + "\n")

macro_processor_pass1('input_file', 'output_file')