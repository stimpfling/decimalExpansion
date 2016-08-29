import sys

def decimalExpansion(num,denom):
    if denom == 0:
        print "Denominator cannot be 0"
        return

    seenPairs = {}
    digits = []
    position = 0

    wholeNum = num/denom
    remainder = num%denom
    sys.stdout.write(str(wholeNum) + '.')
    
    while(position < 5000):
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
            return
        else:                
            seenPairs[key] = position
            digits.append(num)
        position +=1
    
    print "No loop found after 5000 decimal places!"

decimalExpansion(1,3)
decimalExpansion(1,4)
decimalExpansion(9,11)
decimalExpansion(2,13)
decimalExpansion(1,17)
decimalExpansion(1,28)
