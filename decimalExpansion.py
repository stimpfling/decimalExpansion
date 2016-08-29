import sys

def decimalExpansion(num,denom):
    loopFound = False
    seenPairs = {}
    digits = []
    position = 0

    wholeNum = num/denom
    remainder = num%denom

    sys.stdout.write(str(wholeNum) + '.')
    if remainder == 0:
        sys.stdout.write('(0)')
        return
    
    while(1):
        num = (remainder*10)/denom
        remainder = (remainder*10)%denom
        key = str(num) + str(remainder)

        if key in seenPairs.keys():
            startDigit = seenPairs[key]
            # First print non-looping digits (if any)
            for i in range(0,startDigit):
                sys.stdout.write(str(digits[i]))
            # Now print looping digits in parenthesis
            sys.stdout.write('(')
            for i in range(startDigit,position):
                sys.stdout.write(str(digits[i]))
            sys.stdout.write(')\n')
            break
        else:                
            seenPairs[key] = position
            digits.append(num)
        position +=1

decimalExpansion(1,3)
decimalExpansion(1,4)
decimalExpansion(9,11)
decimalExpansion(2,13)
