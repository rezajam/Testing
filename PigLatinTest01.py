inputRaw= raw_input('Enter a word:')
inputLower = inputRaw.lower()

inputList = inputLower.split()

jav = ' '
c = ''
for inp in inputList:
            for j in inp:
                        if (inp.startswith('a') or inp.startswith('e') or inp.startswith('i') or inp.startswith('o') or inp.startswith('u') or inp.startswith('y')):
                                                c = inp + 'way'
                                                if len(c) == (len(inp) + 3):
                                                            print c
                                                            break            
                        elif j in 'ieouay':
                                    b = inp[inp.find(j):] + inp[:inp.find(j)] +'ay'
                                    print b
                                    if len(b) == (len(inp) + 2):
                                                break
