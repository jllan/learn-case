import random
import time

class Node(object):
    """节点类"""
    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = None

    def add(self, value):
        """为树添加节点"""
        node = Node(value)
        if not self.root:  # 如果树是空的，则对根节点赋值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:  # 对已有的节点进行层次遍历
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)

    def pre_recursion(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.value)
        self.pre_recursion(root.lchild)
        self.pre_recursion(root.rchild)

    def mid_recursion(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.mid_recursion(root.lchild)
        print(root.value)
        self.mid_recursion(root.rchild)

    def post_recursion(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.post_recursion(root.lchild)
        self.post_recursion(root.rchild)
        print(root.value)

    def pre_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                print(node.value)
                myStack.append(node)
                node = node.lchild
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = myStack.pop()
            node = node.rchild  # 开始查看它的右子树

    def mid_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:  # 从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            print(node.value)
            node = node.rchild  # 开始查看它的右子树

    def post_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(myStack2.pop().value)

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.value)
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

    def search_value(self, root, target):
        if root == None:
            return
        # print(root.value)
        if root.value == target:
            print('找到', target)
            return
        self.search_value(root.lchild, target)
        self.search_value(root.rchild, target)


if __name__ == '__main__':
    values = range(1000)  # 生成十个数据作为树节点
    tree = Tree()  # 新建一个树对象
    for value in values:
        tree.add(value)  # 逐个添加树的节点

    start_time = time.time()
    target = random.randint(0, 1000)
    tree.search_value(tree.root, target)
    print('run time:', time.time()-start_time)

    # print('队列实现层次遍历:')
    # tree.level_queue(tree.root)
    #
    # print('\n\n递归实现先序遍历:')
    # tree.pre_recursion(tree.root)
    # print('\n递归实现中序遍历:')
    # tree.mid_recursion(tree.root)
    # print('\n递归实现后序遍历:')
    # tree.post_recursion(tree.root)

    # print('\n\n堆栈实现先序遍历:')
    # tree.pre_stack(tree.root)
    # print('\n堆栈实现中序遍历:')
    # tree.mid_stack(tree.root)
    # print('\n堆栈实现后序遍历:')
    # tree.post_stack(tree.root)