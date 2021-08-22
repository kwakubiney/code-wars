def printer_error(s):
    length = len(s)
    count = 0
    valid = "abcdefghijklm"
    for x in s:
        if x not in valid:
            count+=1    
    return f"{count}/{length}"

print(printer_error("adjhjdcbdjjdjs"))

"""
New thing learnt:

You can use > when comparing letters

"""