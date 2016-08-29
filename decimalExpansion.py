def decimalExpansion(num,denom):
    loopFound = False
    seenPairs = {}
    digits = []
    wholeNum = num/denom
    remainder = num%denom
    print str(wholeNum) + '.',
    if remainder == 0:
        print "(0)"
        return
    
    position = 0
    while(1):
        num = (remainder*10)/denom
        remainder = (remainder*10)%denom
        key = str(num) + str(remainder)
        if key in seenPairs.keys():
            startDigit = seenPairs[key]
            # First print non-looping digits (if any)
            for i in range(0,startDigit):
                print str(digits[i]),

            # Now print looping digits in parenthesis
            print "(",
            for i in range(startDigit,position):
                print str(digits[i]),
            print ")"
            break
        else:                
            seenPairs[key] = position
            digits.append(num)
        position +=1

decimalExpansion(1,3)
decimalExpansion(1,4)
decimalExpansion(9,11)
decimalExpansion(2,13)
