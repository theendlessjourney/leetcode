import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        len_s = len( s )
        diagnalNumRows = max(0,numRows - 2)
        expandedMatrixNumRows = numRows + diagnalNumRows
        expandedMatrixNumCols = int( math.ceil( float( len_s ) / float( expandedMatrixNumRows ) ) )
        expandedMatrixNumCols += 1

        result = ""

        for row in range( numRows ):
            for col in range( expandedMatrixNumCols ):
                columnFirstIndex = col * expandedMatrixNumRows

                if ( 0 < col ) and ( 0 < row ) and ( row < ( numRows - 1) ):
                    diagLetterIndex = columnFirstIndex - row
                    if diagLetterIndex < len_s:
                        result += s[ diagLetterIndex ]

                letterIndex = columnFirstIndex + row
                if letterIndex < len_s:
                    result += s[ letterIndex ]

        return result

def test( s, numRows ):
    sol = Solution()
    r = sol.convert( s, numRows )
    print ( '{}, {} : {}'.format( s, numRows, r ) )

test( "PAYPALISHIRING", 3 )
test( "PAYPALISHIRING", 4 )
test( "A", 1 )
test( "ABCD", 3 )
