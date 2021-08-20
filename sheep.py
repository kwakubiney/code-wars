sheep=[True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True]




def count_sheep(sheep):
    y = 0
    for x in range(len(sheep)):
        if sheep[x] == True: ##This was my solution but terrible code because sheep is already a boolean
            y += 1
    return y