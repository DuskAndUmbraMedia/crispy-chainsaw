from allWords_final import allWords # Original
# from allWords_finalWM import allWords
# allWords = ['seven', 'world', 'about', 'again', 'heart', 'pizza', 'water', 'happy', 'hpppp', 'hpppy', 'sixty', 'board', 'month', 'angel', 'death', 'green', 'music', 'fifty', 'three', 'party', 'piano', 'mouth', 'woman', 'ruple', 'sugar']
# allWords = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy']
# allWords = ['smirk']

word_list = allWords.copy() ## Makes a copy of all words and puts it into loop.

INPUTWORD = ''

output_list = []
output_list_a = []

INSTRUCTIONS = ('\n1. The word you enter must be 5 characters long. \n2. For CORRECT letters in the INCORRECT position; enter the letter in it\'s lower case form: "a". \n3. For CORRECT letters in the CORRECT position; enter the letter in it\'s upper case form: "A". \n4. For letters that are COMPLETELY INCORRECT enter a "*" in the position as a wildcard. \n5. Remember to type in unused or dead letters into the secondary "Not these letters :" field.\nEXAMPLE: *aB*c \n \nGood Luck!\n')

# ---------------------------------- START OF LOOP

while INPUTWORD != 'exit':
    # print('\nCharacters must be uppercase, lowercase or * for wildcards. \nEnter "help" for more information.\nEnter "exit" to close program.\n')
    INPUTWORD = input('\nEnter help/exit or - Enter Word: ')
    if INPUTWORD == 'exit': #Forces immediate EXIT without going to second input.
        break
    elif INPUTWORD == 'help':
        print(INSTRUCTIONS)
        continue
    
    noLetter = input('Not these letters : ')
     
    ICOUNTER = 0 # I COUNTER

    for word in word_list: # x_list, x_list equals survivors(iteration)
        for letter in word:
            
            XCOUNTER = 0 # X COUNTER
            XLOWER = 0 # counts LOWER only
            XDOUBLE = 0
            NOLETCOUNT = 0
# ---------------------------------- START NOLETTER QUALIFIER  # Needs to be condensed.
            
        for letter in noLetter: #Qualifies noLetter and Changes to noLetAddStar
            if len(noLetter) <= 5: 
                if len(noLetter) == 5:
                    noLetAddStar = (noLetter + '')
                if len(noLetter) == 4:
                    noLetAddStar = (noLetter + '*')
                if len(noLetter) == 3:
                    noLetAddStar = (noLetter + '**')
                if len(noLetter) == 2:
                    noLetAddStar = (noLetter + '***')
                if len(noLetter) == 1:
                    noLetAddStar = (noLetter + '****')
            else: pass
                
            if (noLetAddStar[0]) in word: #CHECKS WORD FOR NOLETTERS
                NOLETCOUNT += 1
            elif (noLetAddStar[1]) in word:
                NOLETCOUNT += 1
            elif (noLetAddStar[2]) in word:
                NOLETCOUNT += 1
            elif (noLetAddStar[3]) in word:
                NOLETCOUNT += 1
            elif (noLetAddStar[4]) in word:
                NOLETCOUNT += 1
            else: pass

    # ---------------------------------- END NOLETTER QUALIFIER                                
                        
        for letter in INPUTWORD:    
                        
            if letter != '*': # CHECKS INPUT AND WORD FOR DOUBLE LETTERS
                h = INPUTWORD.lower() #MAKE EVERTHING LOWER FOR DOUBLE COMPARISON
                j = h.count(letter) #H INSTEAD OF INPUTWORD (NOW LOWER)
                k = word.count(letter)
                # print(i)

            if letter.islower() and (INPUTWORD[XCOUNTER]) == word[XCOUNTER] and j == 2: #IS LOWER, ACCOUNTS FOR DOUBLES         
                XDOUBLE += 1 
            elif letter.islower() and (INPUTWORD[XCOUNTER]) == word[XCOUNTER] and j == 3: #IS LOWER, ACCOUNTS FOR TRIPLES         
                XDOUBLE += 2 
            elif letter.islower() and (INPUTWORD[XCOUNTER]) == word[XCOUNTER] and j == 4: #IS LOWER, ACCOUNTS FOR QUADRUPLES         
                XDOUBLE += 3                 
            else: pass
            
            if letter.islower() and (INPUTWORD[XCOUNTER]) == word[XCOUNTER]: #IS LOWER AND KILLS DIRECT MATCHES         
                XLOWER += 1 #IF THIS IS ANYTHING BUT 0 WORD IS NOT APPENDED TO NEW LIST
            else: pass
            
            if letter.islower() and (INPUTWORD[XCOUNTER]) in word: #IS LOWER FORCES INCLUSION
                XCOUNTER += 1
            else: pass
            
            if letter == '*': #IS STAR
                XCOUNTER += 1
            else: pass
            
            if letter.isupper() and (INPUTWORD[XCOUNTER].lower()) == word[XCOUNTER]: #CHECKS UPPERCASE LETTERS FOR MATCHING POSITION
                XCOUNTER += 1
            else: pass
            
            if XCOUNTER == 5 and XLOWER == 0 and j == k and NOLETCOUNT == 0: #COUNTS THE COUNTERS
                
                

                output_list_a.append(word) #MAKES THE NEW LIST
                for i in output_list_a: 
                    if i not in output_list: 
                        output_list.append(i)
                            
            ICOUNTER = ICOUNTER + 1 #COUNTS LETTERS TO GET WORD COUNT (LETTERS/5)

        #TEST
        # print('REPORT OUT --- word#:', round(ICOUNTER), '    j:', j, '   k:', k, '   Double?:', XDOUBLE, '   XCOUNTER=5:', XCOUNTER, '   XLOWER=0:', XLOWER, '   NOLETCOUNT:', NOLETCOUNT)

    # print('S1:', output_list)
    
    word_list = output_list.copy()
    
    output_list = []
    output_list_a = []
    
    print('\nPossible words are:\n')
    
    for word in range(len(word_list)):
        print(word_list[word], end = ' ')
    
    if len(word_list) == 0:
        # print('EXIT')
        break
  