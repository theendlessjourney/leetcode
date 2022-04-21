class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len( self.longestSubstring(s) )

    def hasRepeatCharacters(self, s):
        letterDict = {}
        for letter in s:
            if letterDict.get( letter ) != None:
                return True
            letterDict[letter] = 1
        return False


    def longestSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        finalStr = ""
        finalStrLen = 0
        for i in range(len(s)):
            subStringMaxLen = len(s) - i
            if subStringMaxLen < finalStrLen:
                # if the max substring we can form is shorter than what we have, then quit
                return finalStr
            for subStringLen in range( subStringMaxLen, 0, -1 ):
                if subStringLen < finalStrLen:
                    break
                subStr = s[ i : i + subStringLen ]
                if self.hasRepeatCharacters( subStr ):
                    continue
                if len(subStr) > finalStrLen:
                    finalStr = subStr
                    finalStrLen = len(subStr)
        return finalStr


class Solution2(object):

    def ClearLetterSeen( self, letterSeen, s, processingFirst, lastSeenIndex ):
        for i in range( processingFirst, lastSeenIndex ):
            letter = s[i]
            letterSeen[ ord(letter) ] = -1

    def RecordLongest( self, longestFirst, longestLen, first, len ):
        if len > longestLen:
            return first, len
        else:
            return longestFirst, longestLen

    def lengthOfLongestSubstring(self, s):
        first, len = self.longestSubstring_FirstAndLen(s)
        return len

    def longestSubstring_FirstAndLen(self, s):
        """
        :type s: str
        :rtype: int, int
        """
        letterSeen = [-1] * 256
        processingFirst = 0
        processingLen = 0
        longestFirst = 0
        longestLen = 0
        for i in range(len(s)):
            # print( "for loop, ", i, ": ", s[i] )
            letterOrd = ord( s[i] )
            lastSeenIndex = letterSeen[letterOrd]
            if lastSeenIndex >= 0:
                # print( "seen ", s[i], " at index ", lastSeenIndex )
                self.ClearLetterSeen( letterSeen, s, processingFirst, lastSeenIndex )
                longestFirst, longestLen = self.RecordLongest( longestFirst, longestLen, processingFirst, i - processingFirst )
                processingFirst = lastSeenIndex + 1
                processingLen = i - lastSeenIndex
            else:
                # print( "new letter ", s[i], " at index ", i )
                processingLen += 1
            # print( "processing {} {}".format( processingFirst, processingLen ) )
            # print( "longest {} {}".format( longestFirst, longestLen ) )
            letterSeen[letterOrd] = i

        longestFirst, longestLen = self.RecordLongest( longestFirst, longestLen, processingFirst, processingLen )
        return longestFirst, longestLen


    def longestSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        first, len = self.longestSubstring_FirstAndLen(s)
        return s[first : first+len]


class Solution_leetcode:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans


def test( s ):
    # sol = Solution_leetcode()
    sol = Solution2()
    # result = sol.longestSubstring( s )
    result = ""
    resultLen = sol.lengthOfLongestSubstring( s )
    print( "{} : {} {}".format( s, result, resultLen ) )

test( "abcabcbb" )
test( "bbbbb" )
test( "pwwkew" )
test( "abcd12dabc" )
test( "" )

