def SwitchExample(number):
    switcher ={
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(number, "nothing")

number = 3
print (SwitchExample(number))

# Python dosen't have switch case. It uses Dictionary mapping for switch-cases.