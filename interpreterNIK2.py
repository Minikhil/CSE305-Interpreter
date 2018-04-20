inputArray = []
inputArraySplit = []
error = ":error:"
class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)
    def printStack(self):
         x = []
         for items in reversed(self.items):
             x.append(items)
         return x
outputStack = Stack() #have to create stack after it's def


def interpreter(input, output):
    fileOut = output
    f = open(input, 'r').readlines()
    for line in f:
        line = line.strip() #strip removes leading and trailing space from string
        inputArray.append(line)
    for item in inputArray:
        item = item.split()
        inputArraySplit.append(item)
    readInputArray(inputArraySplit, fileOut);
def operationDic(operation):
    # if operation == 'quit':
    #     quit()
    if operation == 'pop':
        return pop()
    elif operation == 'add':
        return add()
    elif operation == 'sub':
        return sub()
    elif operation == 'mul':
        return mul()
    elif operation == 'div':
        return div()
    elif operation == 'rem':
        return rem()
    elif operation == 'neg':
        return neg()
    elif operation == 'swap':
        return swap()
    return
def isboolean(val):
    if(val == ':true:' or val == ':false:'):
        return True
    else: False

def isInteger(val):
    if type(val) == float:
        return False
    elif type(val) == int:
        return True
    if type(val) == str:
        try:
            int(val)
            return True
        except(RuntimeError, TypeError, NameError, ValueError):
            return False

def isError(val):
    if (val == error):
        return True
    else:
        return False

def readInputArray(arr, fileOut):
    lineCount = 0
    for line in arr:
        length = len(line)
        if length == 1:
            operation = line[0]
            # print 'operation:' + ' '+ operation
            if operation == "quit":
                quit(fileOut)
                break
            operationDic(operation)
        elif length == 2 and line[0].isalpha:
            operation = line[0]
            # print 'operation:' + ' '+ operation
            val = line[1]
            # print 'val:' + ' ' + val
            if operation == "push":
                push(val)

        elif length > 2:
            # print("lineCount", lineCount)
            operation = line[0]
            index = line[lineCount].index("\"")
            val = line[lineCount]
            val = line[index+1:len(line)]
            print("val:", val)
            temp = ""
            for line in val:
                temp = temp + str(line + ' ')

            if operation == "push":
                # print("PUSH BISHH")
                # print("val:", val, "opp", operation)
                if type(temp) == str and temp.startswith('"'):
                    temp = temp.strip('"')
                outputStack.push(temp)
                # push(str(val))


        lineCount += 1
    return

def push(val):
    # print "val:"
    # print val
    # print type(val)
    # if val == "-0":
    #     val = "0"
    #     return outputStack.push(val)
    if '-' in val:
        if val[1].isalpha():    #check for "-x"
            return outputStack.push(error)
        val = int(val)
        if isInteger(val):
            outputStack.push(val)

    elif val.isdigit():  #checks if num
        val = int(val)
        if isInteger(val):
            outputStack.push(val)

    elif "\"" in val:   #checks if string
        # print "found string"
        if val[0] == '"' and val[len(val)-1] == '"':
            val = val[1:len(val)-1]
            outputStack.push(val)
    elif val.isalnum():   #check if string has only nums and letters then name
        # if val[0].isdigit:
        #     return outputStack.push(error)
        # else:
            return outputStack.push(val)

    elif isboolean(val):
        outputStack.push(val)
    elif isError(val):
        outputStack.push(val)
    else: outputStack.push(error)
    return

def quit(output):
    # print ("quit was called")
    # print(outputStack.printStack())

    fo = open(output, 'w')
    while not outputStack.isEmpty():
        temp = outputStack.pop()
        # print "temp:"
        # print temp
        fo.write(str(temp) + "\n")



def pop():
    # print "pop was called"
    # if not outputStack.isEmpty():
    #     return outputStack.pop()
    if outputStack.size()>= 1:
        return outputStack.pop()
    else:
        return outputStack.push(error)
def add():
    # print("output stack b4 add:")
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        # print "top1:" + " "
        # print top1
        # print "top2:" + " "
        # print top2
    if isInteger(top1) and isInteger(top2):
        # print "nedd to write add method"
        result = top1 + top2
        outputStack.push(int(result))
        return
    else:
        # print "add num not ints"
        outputStack.push(top2)
        outputStack.push(top1)
        return push(error)
def sub():
    # print "output stack b4 sub:"
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        # print "top1:" + " "
        # print top1
        # print "top2:" + " "
        # print top2
    if isInteger(top1) and isInteger(top2):
        # print "nedd to write add method"
        result = top2 - top1
        outputStack.push(int(result))
        return
    else:
        # print "add num not ints"
        outputStack.push(top2)
        outputStack.push(top1)
        return push(error)
def mul():
    # print "output stack b4 sub:"
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        # print "top1:" + " "
        # print top1
        # print "top2:" + " "
        # print top2
    if isInteger(top1) and isInteger(top2):
        # print "nedd to write add method"
        result = top2 * top1
        outputStack.push(int(result))
        return
    else:
        # print "add num not ints"
        outputStack.push(top2)
        outputStack.push(top1)
        return push(error)
def div():
    # print "output stack b4 div:"
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        if top1 == 0:
            # print "top1 = 0"
            outputStack.push(top2)
            outputStack.push(top1)
            return push(error)
        # print "top1:" + " "
        # print type(top1)
        # print top1
        # print "top2:" + " "
        # print top2
    if isInteger(top1) and isInteger(top2):
        # print "nedd to write add method"
        result = int(top2) / int(top1)
        outputStack.push(int(result))
        return
    else:
        # print "add num not ints"
        outputStack.push(top2)
        outputStack.push(top1)
        return push(error)
def rem():
    # print "output stack b4 div:"
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        if top1 == 0:
            # print "top1 = 0"
            outputStack.push(top2)
            outputStack.push(top1)
            return push(error)
        # print "top1:" + " "
        # print type(top1)
        # print top1
        # print "top2:" + " "
        # print top2
    if isInteger(top1) and isInteger(top2):
        # print "nedd to write add method"
        result = int(top2)%int(top1)
        outputStack.push(int(result))
        return
    else:
        # print "add num not ints"
        outputStack.push(top2)
        outputStack.push(top1)
        return push(error)
def neg():
    # print "output stack b4 div:"
    # print outputStack.printStack()
    if outputStack.isEmpty():
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        # print "top1:" + " "
        # print type(top1)
        if isInteger(top1):
            negative = -1
            # print "nedd to write add method"
            result = top1*negative
            outputStack.push(result)
            return
        else:
            # print "add num not ints"
            outputStack.push(top1)
            return push(error)
def swap():
    # print "output stack b4 div:"
    # print outputStack.printStack()
    if outputStack.size()<2:
        # print "stack empty 1"
        return outputStack.push(error)
    else:
        top1 = outputStack.pop()
        top2 = outputStack.pop()
        outputStack.push(top1)
        outputStack.push(top2)






# #
# if __name__== "__main__":
#     interpreter('test-Input.txt', 'test-Output.txt')
#     # for i in inputArraySplit:
#     #     push(i)
    # print(outputStack.printStack())
#     # val = "20"
#     # print "val is alpha"
#     # print val.isdigit()
#     val = "-x"
#     print val[1].isalpha()
#     # print 5 % 8
