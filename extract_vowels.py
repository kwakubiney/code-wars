def disemvowel(string):
    new_string = ""
    vowel = "aeiou"
    for x in string:
        if x in vowel:
            pass
        else:
            new_string+=x

    return new_string

            
print(disemvowel("hello"))