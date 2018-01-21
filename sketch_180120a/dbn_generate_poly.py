"""
s18020a - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

This script generates code on console for dbn_letters.py

Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""
    

def convert_dbn_source(file_path):
    with open("dbn_polys.py", 'w') as out:
        out.write('"""\n')
        out.write("s18019 - Alexandre B A Villares\n")
        out.write("https://abav.lugaralgum.com/sketch-a-day\n")
        out.write("This code was generated by dbn_generata_poly.py\n")
        out.write("Converting some of Maeda's Design by Number\n")
        out.write('dbnletters.dbn code -> Processing\n"""\n')
        out.write("dbn_letter = {}  # Dict of functions\n")
        out.write("\n")
    with open(file_path, "r") as f:
        dbn_source = f.readlines()
    inside_block = False
    command_name = ""
    command_block = []
    for ln in dbn_source:
        if ln.count("command"):
            command_name = ln[14:15]
        elif ln.count("{"):
            inside_block = True
        elif ln.count("}"):
            if command_name in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                def_dbn_letter(command_block, command_name)
            command_block = []  # empty block
            inside_block = False
        elif inside_block:
            command_block.append(ln.lstrip())


def def_dbn_letter(dbn_block, key_):
    p_block = []

    for dbn_line in dbn_block:
        if dbn_line:
            p_lines =("    " + dbn_line       # all this to convert lines() to shapes
                           .replace("(", "") 
                           .replace(")", "")
                           .replace("line ", "vertex(")
                           .replace(" ", ",", 1)
                           .replace(" ", "$", 1)  # token to split line into 2 vertices
                           .replace(" ", ",")
                           .replace("$", ")\n    vertex(", 1)
                           .replace("//", "#")
                           .strip()
                           + ")")
            p_block.append(p_lines.split("\n")[0]) 
            p_block.append(p_lines.split("\n")[1])
    # for ln in p_block:
    #     print ln.replace(" ","-")
            
    with open("dbn_polys.py", 'a') as out:
        out.write("# " + key_ + "\n")
        out.write("def dbn_letter" + key_ + "(h, v, debug_poly=False):\n")
        out.write("    pushMatrix()\n")
        out.write("    scale(1, -1)\n")
        out.write("    if debug_poly: stroke(random(256),200, 200)\n") # for debug
        out.write("    beginShape()\n")
        v_count = 0
        for i, line_ in enumerate(p_block):
            if line_ != p_block[i-1]: # and line_ != p_block[i-2]: # if repeated
                out.write(line_ + "\n")
                v_count += 1
            else: out.write("    # " + line_.lstrip() + "\n")
            if i % 2 and i < len(p_block)-2:  # if on odd lines, next doesn't repeat
                if line_ != p_block[i+1]:
                    #out.write("    #---\n")
                    out.write("    endShape()\n")
                    out.write("    if debug_poly: stroke(random(256),200, 200)\n") # for debug
                    out.write("    beginShape()\n")                        
        out.write("    endShape()\n")
        out.write("    popMatrix()\n")
        out.write("dbn_letter['" + key_ + "'] = dbn_letter" + key_ + "\n")
        out.write("dbn_letter[" + str(ord(key_) - 64)
                  + "] = dbn_letter" + key_ + "\n")
