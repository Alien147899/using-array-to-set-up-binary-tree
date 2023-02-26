# class binary_tree:
#     def __init__(self):
#         self.arrayNodes = [[0 for i in range(3)] for Y in range(20)] #创建二维数组，3是row, 20是column
#         self.rootPointer = -1
#         self.freeNode = 0      #空的节点
#
#     def addNode(self, NodeData):
#         if self.freeNode <= 19:
#             self.arrayNodes[self.freeNode][0] = -1
#             self.arrayNodes[self.freeNode][1] = NodeData
#             self.arrayNodes[self.freeNode][2] = -1
#
#             if self.rootPointer == -1:   # add to start
#                 self.rootPointer = self.freeNode
#


#考试不给用class的数据结构写Binary tree， 要用数列
import flag as flag




arrayNodes = [[0 for i in range(3)] for Y in range(20)] #创建二维数组，3是row, 20是column
rootPointer = -1
freeNode = 0

def addNode(arrayNodes, rootPointer, freeNode):

        nodeData = int(input("enter a value"))
        if freeNode <= 19:
            arrayNodes[freeNode][0] = -1
            arrayNodes[freeNode][1] = nodeData
            arrayNodes[freeNode][2] = -1
            if rootPointer == -1:
                rootPointer = 0 #插的是第一个节点
            else:# 如果rootpointer 的value 有东西，就开始找下面几个有位置的节点选择插入

                currentPointer = rootPointer
                while flag == False:
                    if nodeData < arrayNodes[currentPointer][1]:
                        if arrayNodes[currentPointer][0] == -1:
                            arrayNodes[currentPointer][0] == freeNode
                            flag == True
                        else:
                            currentPointer = arrayNodes[currentPointer][2]

                    else:
                        if arrayNodes[currentPointer][2] == -1:
                            arrayNodes[currentPointer][2] == freeNode
                            flag == True
                        else:
                            currentPointer = arrayNodes[currentPointer][0]
            freeNode = freeNode + 1

        else:
             print("it is full")
        return arrayNodes, rootPointer, freeNode

for i in range(5):
    arrayNodes, rootPointer, freeNode = addNode(arrayNodes, rootPointer, freeNode)

    print(arrayNodes)



















