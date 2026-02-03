def is_armstrong_number(number):
    strNumber = str(number)
    l = len(strNumber)
    tot = 0
    for i in range(l):
        tot += int(strNumber[i]) ** l
    return number == tot
        
    
