#coding=utf-8

class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

#node = Node(100)
class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = None
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        #cur游标，用来移动遍历节点
        cur = self.__head
        #  count记录数量
        count = 1
        while cur.next != self.__head:
                count += 1
                cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
            #退出循环，cur指向尾节点，但尾节点的元素未打印
        print('')

    def add(self, item):
        """链表头部添加元素,头插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
                #退出循环，cur指向尾节点
            node.next = self.__head
            self.__head = node
            #cur.next = self.__head
            cur.next = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
                # 退出循环，cur指向尾节点
            #node.next = cur.next
            #cur.next = node
            cur.next = node
            node.next = self.__head

    def insert(self, pos, item):
        """链表指定位置添加元素
        :param pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            #当退出循环后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头节点
                #头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找结点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
                # 退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False

if __name__ == "__main__":
    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())

    li.append(1)
    print(li.is_empty())
    print(li.length())

    li.append(2)
    li.add(8)
    li.append(3)
    li.append(4)
    li.append(5)
    li.append(6)
    li.insert(-1, 9)
    li.insert(2, 100)
    li.insert(10, 200)
    li.travel()
    li.remove(9)
    li.travel()
    li.remove(100)
