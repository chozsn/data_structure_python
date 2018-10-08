class LNode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

#创建链表
def creatlist(n):
    '''int n :the number of Node'''
    if n < 0:
        return False
    elif n == 1:
        elem = input('Elem>')
        head = LNode(elem)
    else:
        elem = input('Elem>')
        head =LNode(elem)
        p = head
        while n - 1 > 0:#由于已经有头结点，所以循环的节点数会少一个
            elem = input('Elem>')
            p.next = LNode(elem)
            p = p.next
            n -= 1
    print('Done!')
    return head

'''
#插入头元素
def inserthead(head):
    elem = input('Elem>')
    q = LNode(elem)
    q.next = head.next
    head = q
    print('Done!')
    return head
''' 
#插入元素
def insert(head, n):
    if n < 0:
        return False
    elif n > lengthlist(head):
        print('n out of range')
        return False
    elif n == 0:#插入头结点
         elem = input('Elem>')
         q = LNode(elem)
         q.next = head.next
         head = q
         return head
    else:
        elem = input('Elem>')
        q = LNode(elem)
        pre = head #pre used to present the last Node in which want insert
        while pre and n - 1 > 0:
            n -= 1
            pre = pre.next
        q.next = pre.next
        pre.next = q
    print('Done!')
    return head

#删除元素
def delete(head, n):
    '''int n:the number of element want to be deleted'''
    if n < 0:
        return False
    elif n > lengthlist(head):
        print('n out of range')
        return False
    elif n == 0:
        head = head.next
    else:
        pre = head
        while pre and n - 1 > 0 :
            n -= 1
            pre = pre.next
        pre.next = pre.next.next#pre present the last element we want to deleted
        #pre.next 代表希望删除的元素，直接将前一个元素接到后一个元素上，让Python的解释器自动
        #回收节点使用的内存
    print('Done!')
    return head

#打印链表
def printlist(head):
    p = head
    while p:
        print(p.elem)
        p = p.next
    print('Done!')

#链表长度
def lengthlist(head):
    p, n = head, 0
    while p:
        n += 1
        p = p.next
    return n
