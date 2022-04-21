def compareEqual( s, index1, index2 ):
    return s[index1].lower() == s[index2].lower()

class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        prevPalLengths = []
        finalPalIndex = 0
        finalPalLen = 1
        for letterIndex in range(1,len(s)):
            letter = s[letterIndex]
            # print( "letterIndex {} letter {}".format( letterIndex, letter ) )
            newRecord = [] 

            # 0 length used to check two consecutive letters, like "aa", it's like there's a
            # 0-length palindrome in the previous letter
            # and of course, the previous letter by itself is a palindrome, so it's a 1-length palindrome
            # palLengths = [0,1]
            # palLengths.extend( prevRecord.palLengths )
            if compareEqual( s, letterIndex, letterIndex - 1 ):
                newRecord.append( 2 )
            if (letterIndex >= 2) and compareEqual( s, letterIndex, letterIndex - 2 ):
                newRecord.append( 3 )
            for palLen in prevPalLengths:
                indexToCheck = letterIndex - palLen - 1
                if ( indexToCheck >= 0 ) and compareEqual( s, letterIndex, indexToCheck ): 
                    # if this letter matches the letter proceeding the previous palindrome, then we have a new palindrom
                    newRecord.append( palLen + 2 )

            if len( newRecord ) > 0:
                maxLen = max( newRecord )
                if maxLen > finalPalLen:
                    finalPalIndex = letterIndex
                    finalPalLen = maxLen
            # print( "letterIndex {} letter {} newRecord {} pal {} {}".format( letterIndex, letter, newRecord, finalPalIndex, finalPalLen ) )
            prevPalLengths = newRecord

        palStart = finalPalIndex - finalPalLen + 1
        palEnd = finalPalIndex + 1
        return s[palStart:palEnd:1]


class Solution2(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""

        prevPalLengths = []
        finalPalIndex = 0
        finalPalLen = 1
        for letterIndex in range(1,len(s)):
            letter = s[letterIndex]
            # print( "letterIndex {} letter {}".format( letterIndex, letter ) )
            newRecord = [] 

            # 0 length used to check two consecutive letters, like "aa", it's like there's a
            # 0-length palindrome in the previous letter
            # and of course, the previous letter by itself is a palindrome, so it's a 1-length palindrome
            # palLengths = [0,1]
            # palLengths.extend( prevRecord.palLengths )
            if compareEqual( s, letterIndex, letterIndex - 1 ):
                newRecord.append( 2 )
            if (letterIndex >= 2) and compareEqual( s, letterIndex, letterIndex - 2 ):
                newRecord.append( 3 )
            for palLen in prevPalLengths:
                indexToCheck = letterIndex - palLen - 1
                if ( indexToCheck >= 0 ) and compareEqual( s, letterIndex, indexToCheck ): 
                    # if this letter matches the letter proceeding the previous palindrome, then we have a new palindrom
                    newRecord.append( palLen + 2 )

            if len( newRecord ) > 0:
                maxLen = max( newRecord )
                if maxLen > finalPalLen:
                    finalPalIndex = letterIndex
                    finalPalLen = maxLen
            # print( "letterIndex {} letter {} newRecord {} pal {} {}".format( letterIndex, letter, newRecord, finalPalIndex, finalPalLen ) )
            prevPalLengths = newRecord

        palStart = finalPalIndex - finalPalLen + 1
        palEnd = finalPalIndex + 1
        return s[palStart:palEnd:1]

# a single letter is a palindrome 
# a letter following a palindrome makes a new palindrome,
#   if the letter matches the letter before the palindrome

class PalRecord:
    def __init__(self, inLetter):
        self.letter = inLetter
        self.palLengths = []

    def appendPalLength( self, inLen ):
        self.palLengths.append( inLen )
        

def findPalindromes( s ):
    records = []
    for letterIndex in range(len(s)):
        letter = s[letterIndex]
        newRecord = PalRecord( letter ) 
        records.append( newRecord )

        # print( "letterIndex {} records {}".format( letterIndex, len(records) ) )
        if letterIndex == 0:
            continue

        prevRecord = records[ letterIndex - 1 ]
        # 0 length used to check two consecutive letters, like "aa", it's like there's a
        # 0-length palindrome in the previous letter
        # and of course, the previous letter by itself is a palindrome, so it's a 1-length palindrome
        # palLengths = [0,1]
        # palLengths.extend( prevRecord.palLengths )
        if compareEqual( s, letterIndex, letterIndex - 1 ):
            newRecord.appendPalLength( 2 )
        if (letterIndex >= 2) and compareEqual( s, letterIndex, letterIndex - 2 ):
            newRecord.appendPalLength( 3 )
        for palLen in prevRecord.palLengths:
            indexToCheck = letterIndex - palLen - 1
            if ( indexToCheck >= 0 ) and compareEqual( s, letterIndex, indexToCheck ): 
                # if this letter matches the letter proceeding the previous palindrome, then we have a new palindrom
                newRecord.appendPalLength( palLen + 2 )

    return records

def printRecords( records ):
    index = 0
    for i in range( len(records) - 1, -1, -1 ):
        rec = records[i]
        buf = str(i) + "," + rec.letter + " "
        index += 1
        for palLen in rec.palLengths:
            buf += str(palLen) + " "

        print( buf )

printRecords( findPalindromes( "saas" ) )
print("\n")
printRecords( findPalindromes( "saacas" ) )
print("\n")
printRecords( findPalindromes( "sacas" ) )
print("\n")
printRecords( findPalindromes( "babad" ) )
print("\n")
printRecords( findPalindromes( "step on no pets" ) )
print("\n")
printRecords( findPalindromes( "Able was I ere I saw Elba") )
print("\n")
printRecords( findPalindromes( "babaderredabab" ) )
print("\n")

def test( s ):
    sol = Solution()
    pal = sol.longestPalindrome( s )
    print( s, ": ", pal )

test( "saas" )
test( "saacas" ) 
test( "sacas" ) 
test( "babad" )
test( "step on no pets" )
test( "Able was I ere I saw Elba")
test( "babaderredabab" )
test( "" )
test( "a" )
test( "banana" )
