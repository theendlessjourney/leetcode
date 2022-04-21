# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def accumulateValue( node, value ):
        assert node is not None 
        newVal = node.val + value
        if newVal <= 9:
            node.val = newVal
        else:
            node.val = newVal - 10;
            if node.next is None:
                node.next = ListNode()
            Solution.accumulateValue( node.next, int( newVal / 10 ) )

    @staticmethod
    def processList( curOutNode, n1 ):
        while n1 is not None:
            Solution.accumulateValue( curOutNode, n1.val )
            n1 = n1.next
            if ( n1 is not None ) and (curOutNode.next is None):
                curOutNode.next = ListNode();
            curOutNode = curOutNode.next;


    def addTwoNumbers_impl1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out = ListNode()
        self.processList( out, l1 )
        self.processList( out, l2 )
        return out

    def addTwoNumbers_impl2(self, l1, l2):
        a = l1
        b = l2
        out = ListNode(0)
        pre = None
        carry = 0
        while not ( ( a is None ) and ( b is None ) and ( carry == 0 ) ):
            vala = 0 if a is None else a.val
            valb = 0 if b is None else b.val
            cur = None
            if pre is None:
                cur = out
            else:
                cur = ListNode()
                pre.next = cur
            summ = carry + vala + valb
            cur.val = summ % 10
            carry = int( summ / 10 )
            pre = cur
            a = None if a is None else a.next
            b = None if b is None else b.next
        return out

    def addTwoNumbers(self, l1, l2):
        return self.addTwoNumbers_impl2( l1, l2 )

def printList( l ):
    output = ""
    curNode = l
    while curNode != None:
        output += str(curNode.val) + " "
        curNode = curNode.next
    print( output )

def makeList( pythonList ):
    out = None
    pre = None
    for i in pythonList:
        if pre is None:
            out = ListNode(i)
            pre = out
        else:
            pre.next = ListNode(i)
            pre = pre.next
    return out

def test1():
    l1 = makeList( [ 2, 4, 3 ] )
    l2 = makeList( [ 5, 6, 4 ] )
    sol = Solution()
    sumList = sol.addTwoNumbers( l1, l2 )
    printList( sumList )

def test2():
    l1 = ListNode() 
    l2 = ListNode() 
    sol = Solution()
    sumList = sol.addTwoNumbers( l1, l2 )
    printList( sumList )

def test3():
    l1 = makeList( [9,9,9,9,9,9,9] )
    l2 = makeList( [ 9,9,9,9 ] )
    sol = Solution()
    sumList = sol.addTwoNumbers( l1, l2 )
    printList( sumList )

test1()
test2()
printList( makeList( [5,22,11,99] ) )
test3()
