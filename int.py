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

# stack = Stack()
# bindDic = {}
error = ":error:"
tru = ":true:"
fal = ":false:"
unit = ":unit:"
let = "let"
end = "end"
operationBool = False
def isboolean(val):
    if(val == ':true:' or val == ':false:'):
        return True
    else: False
def isUnit(val):
    if val == ':unit:':
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
def isInbinDic(bindDic, value):
    for key in bindDic.keys():
        if key == value:
            return True
    else:
        return False
def isAscii(s):
    return all(ord(char) < 128 for char in s)
def isValue(val):
    if type(val) == str:
        return  True
    if isInteger(val):
        return True
    elif isboolean(val):
        return True
    elif isUnit(val):
        return True
    else:
        return False
def isName(val):
    try:
        val[0].isalpha()
        return True
    except(RuntimeError, TypeError, NameError, ValueError):
        return False



def computeLet(input,dic,output,s, i, inputArray):
    # print input
    letCount = 0
    ans = [[]]
    dicStr = {}
    dicList = [dic]
    # i = index of fisr occurence of let in input
    while i < len(input):
        line = input[i]
        # print "line", line, letCount
        # print "lenght", len(line)
        operation = line[0]
        if len(line) == 1:
            if operation == "let":
                # print("IN LET:" , letCount, "ans",ans, "dicList", dicList)
                list = []
                ans.append(list)
                # print "dic:::", dic
                if letCount == 0:
                    # "Let count = 0 created copy of global dic"
                    tempDic = dic.copy()
                    dicList.append(tempDic)
                elif letCount >= 1:
                    # "Let count > 0"
                    # print "newDic", dicList[letCount-1]
                    # print "dicList b4 tempDic", dicList
                    tempDic = dicList[letCount].copy()
                    # print "tempdic", tempDic
                    dicList.append(tempDic)

                letCount += 1
            elif operation == "end":
                # print("END letcount", letCount, "ans:", ans, "dicList", dicList)

                if len(ans[letCount])>=1:
                    # print("remove:" ,ans[letCount])
                    result = ans[letCount].pop()
                    # print("result", result)
                    # print("Append to:", ans[letCount-1])
                    ans[letCount-1].append(result)
                    # print("remove:" ,ans[letCount])
                    # ans.remove(ans[letCount])
                    ans.pop()
                    dicList.pop(letCount)
                    # letCount -= 1
                    # print "Append to:", ans[letCount-1]
                    # ans[letCount-1].append(result)
                    letCount -= 1
                    # ans.remove(ans[letCount])
                    # ans = ans[0:letCount-1]
                    # print "end finished letCount", letCount
                    # dicList.pop(letCount)
                    # print "dic at end", dicList
                    # letCount -= 1
                    # print("end decremented letcount and dicList:", letCount, "ans:", ans, "dicList", dicList, "ans len", len(ans))

                if letCount == 0:
                    # "print letCount = 0"
                    fileOut = output
                    fo = open(fileOut, 'w')

                    # while not s.isEmpty():
                    #     # "printing b4 let"
                    #     temp = s.pop()
                    #     fo.write(str(temp) + "\n")

                    # print "ans", len(ans)
                    # if len(ans) == 2:
                    #     "printing result of let"
                    #     temp = str(ans[0].pop())
                    #     fo.write(str(temp) + "\n")

                    temp = str(ans[0].pop())
                    list = input[i+1: len(input)]
                    # print "list---", list
                    # stk = Stack()
                    s.push(temp)
                    stack = interpreter2(list,output,dic, s)
                    # print("Stack returned from inter2:", stack.printStack())
                    while not s.isEmpty():
                        temp = s.pop()
                        fo.write(str(temp) + "\n")
                    #
                    # if operationBool == True:
                    #     while not stack.size() == 1:
                    #         # "printing after let"
                    #         temp = stack.pop()
                    #         fo.write(str(temp) + "\n")
                    # else:
                    #     while not stack.size() == 0:
                    #         # "printing after let"
                    #         temp = stack.pop()
                    #         fo.write(str(temp) + "\n")


                    break






            elif operation == "bind":
                # print "bind called"
                # print "newDic---", dicList
                stack = Stack()
                newDic = dicList[letCount]


                if len(ans[letCount])>1:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)

                    # # ans[letCount].remove(top1)
                    # top1 = ans[letCount][len(ans[letCount])-1]
                    # top2 = ans[letCount][len(ans[letCount])-2]
                    # print "top1:", top1, "top2:", top2
                    if isInbinDic(newDic,top1) and isInbinDic(newDic,top2):
                        # print "both in dic"
                        if newDic[top1] == None:
                            ans[letCount].append(error)
                            # stack.push(error)
                        else:
                            newDic[top2] = newDic[top1]
                            ans[letCount].append(unit)
                    elif not top1 == error and isValue(top1) and isName(top2) and not isInteger(top2) and not isInbinDic(dicStr, top2):
                        # print "top1:", top1, type(top1)
                        #
                        # print "top2:", top2
                        newDic[top2] = top1
                        ans[letCount].append(unit)
                        # stack.push(unit)
                        # print "top1 not in dic and is value"
                    else:
                        # print "top 2 not name"
                        # stack.push(top2)
                        # stack.push(top1)
                        # stack.push(error)
                        ans[letCount].append(error)
                else:
                    ans[letCount].append(error)
                    # stack.push(error)

            elif operation == "quit":
                ans = ans
                # print "quit called"
                # fileOut = output
                # fo = open(fileOut, 'w')
                # while not s.isEmpty():
                #     temp = s.pop()
                #     fo.write(str(temp) + "\n")
                #
                # if letCount == 0:
                #     temp = str(ans[0])
                #     if "\'" in temp:
                #         temp = temp[2:len(temp)-2]
                #     else:
                #         temp = temp[1:len(temp)-1]
                #     fo.write(str(temp) + "\n")
                # else:
                #     fo.write(str(error) + "\n")






            elif operation == "pop":
                if len(ans[letCount])>= 1:
                    # print "ans", ans[letCount]
                    ans[letCount].pop(len(ans[letCount])-1)
                else:
                    ans[letCount].append(error)

            elif operation == "neg":
                if len(ans[letCount])== 0:
                    ans[letCount].append(error)
                elif len(ans[letCount]) > 0:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))

                    if isInteger(top1):
                        # print "IN NEG"
                        result = int(top1)*-1
                        ans[letCount].append(result)
                else:
                    ans[letCount].append(result)
                    ans[letCount].append(error)

            elif operation == "swap":
                # print "output stack b4 div:"
                # print stack.printStack()
                if len(ans[letCount])<= 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                else:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    if isInbinDic(dicList[letCount],top2):
                        top2 = str(dicList[letCount].get(top2))

                    ans[letCount].append(top1)
                    ans[letCount].append(top2)

            elif operation == "cat":
                if len(ans[letCount])<= 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                else:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    if isInbinDic(dicList[letCount],top2):
                        top2 = str(dicList[letCount].get(top2))
                    if type(top1) == int:
                        top1 = str(top1)
                    if type(top2) == int:
                        top2 = str(top2)
                        # print type(top1)
                        # print type(top2)
                    # print "top1:", top1, "top2:", top2
                    if type(top1) == str and type(top2) == str:
                        if (isInbinDic(dicStr,top1) and isInbinDic(dicStr, top2)):
                            if "\n" and "\t" not in top1:
                                    if "\n" and "\t" not in top2:
                                        if isAscii(top1) and isAscii(top2):
                                            if top1.isdigit() or top1.isalpha():
                                                catString = top2 + "" + top1
                                            else:
                                                catString = top2 + " " + top1
                                                dicStr[catString] = catString
                                            ans[letCount].append(catString)
                        elif (isInbinDic(dicStr,top1) and isInbinDic(dicList[letCount], top2)):
                            if "\n" and "\t" not in top1:
                                    if "\n" and "\t" not in top2:
                                        if isAscii(top1) and isAscii(top2):
                                            if top1.isdigit() or top1.isalpha():
                                                catString = top2 + "" + top1
                                            else:
                                                catString = top2 + " " + top1
                                                dicStr[catString] = catString
                                            ans[letCount].append(catString)

                        elif (isInbinDic(dicStr,top2) and isInbinDic(dicList[letCount], top1)):
                            if "\n" and "\t" not in top1:
                                    if "\n" and "\t" not in top2:
                                        if isAscii(top1) and isAscii(top2):
                                            if top1.isdigit() or top1.isalpha():
                                                catString = top2 + "" + top1
                                            else:
                                                catString = top2 + " " + top1
                                                dicStr[catString] = catString
                                            ans[letCount].append(catString)

                        elif (isName(top1) and isName(top2)):
                            ans[letCount].append(error)

                        elif "\n" and "\t" not in top1:
                                if "\n" and "\t" not in top2:
                                    if isAscii(top1) and isAscii(top2):
                                        if top1.isdigit() or top1.isalpha():
                                            catString = top2 + "" + top1
                                        else:
                                            catString = top2 + " " + top1
                                        ans[letCount].append(catString)

                    else:
                        ans[letCount].append(error)

            elif operation == "and" or operation == "or":
                if len(ans[letCount])<= 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                elif len(ans[letCount]) >= 2:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    if isInbinDic(dicList[letCount],top2):
                        top2 = str(dicList[letCount].get(top2))
                    if isboolean(top1) and isboolean(top2):
                        if operation == "and":
                            if top1 == tru and  top2 == tru:
                                ans[letCount].append(tru)
                            else:
                                ans[letCount].append(fal)
                        if operation == "or":
                            if top1 == fal and top2 == fal:
                                ans[letCount].append(fal)
                            else:
                                ans[letCount].append(tru)
                    else:
                        ans[letCount].append(top2)
                        ans[letCount].append(top1)
                        ans[letCount].append(error)
            elif operation == "if":
                if len(ans[letCount])<= 2:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                elif len(ans[letCount]) >= 3:
                    # top1 = ans[letCount].pop(len(ans[letCount])-1)
                    # top2 = ans[letCount].pop(len(ans[letCount])-1)
                    top3 = ans[letCount].pop(len(ans[letCount])-1)
                    # if isInbinDic(dicList[letCount],top1):
                    #     top1 = str(dicList[letCount].get(top1))
                    # if isInbinDic(dicList[letCount],top2):
                    #     top2 = str(dicList[letCount].get(top2))
                    if isInbinDic(dicList[letCount],top3):
                        top3 = str(dicList[letCount].get(top3))
                    if isboolean(top3):
                        if top3 == tru:
                            ans[letCount].append(top2)
                        elif top3 == fal:
                            ans[letCount].append(top1)
                    else:
                        ans[letCount].append(top3)
                        ans[letCount].append(top2)
                        ans[letCount].append(top1)
                        ans[letCount].append(error)

            elif operation == "not":
                # print "not called"
                if len(ans[letCount])< 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                elif len(ans[letCount]) >= 1:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    # print "top1", top1
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    # print "top1:" + " "
                    # print type(top1)
                    if isboolean(top1):
                        if top1 == tru:
                            top1 = fal
                            ans[letCount].append(top1)
                        elif top1 == fal:
                            top1 = tru
                            ans[letCount].append(top1)
                    else:
                        ans[letCount].append(top1)
                        ans[letCount].append(error)

            elif operation == "equal":
                # print "equal called"
                if len(ans[letCount])<= 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                elif len(ans[letCount]) >= 2:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    if isInbinDic(dicList[letCount],top2):
                        top2 = str(dicList[letCount].get(top2))

                    if type(top1) == int and type(top2) == int:
                        if top1 == top2:
                            ans[letCount].append(tru)
                        else:
                            ans[letCount].append(fal)
                    else:
                        ans[letCount].append(top2)
                        ans[letCount].append(top1)
                        ans[letCount].append(error)

            elif operation == "lessThan":
                if len(ans[letCount])<= 1:
                    # print "stack empty 1"
                    ans[letCount].append(error)
                elif len(ans[letCount]) >= 2:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)
                    if isInbinDic(dicList[letCount],top1):
                        top1 = str(dicList[letCount].get(top1))
                    if isInbinDic(dicList[letCount],top2):
                        top2 = str(dicList[letCount].get(top2))
                    if type(top1) == int and type(top2) == int:
                        if top2 < top1:
                            ans[letCount].append(tru)
                        else:
                            ans[letCount].append(fal)
                    else:
                        ans[letCount].append(top2)
                        ans[letCount].append(top1)
                        ans[letCount].append(error)

            elif operation == "add" or operation == "sub" or operation == "mul" or operation == "div"or operation == "rem":
                top1bool = False
                top2bool = False
                # print "multiple opp called"
                # print "ans", ans[letCount]
                if len(ans[letCount])< 2:
                    ans[letCount].append(error)
                elif len(ans[letCount])>= 2:
                    top1 = ans[letCount].pop(len(ans[letCount])-1)
                    top2 = ans[letCount].pop(len(ans[letCount])-1)

                    # print "in else"
                    if isInbinDic(dicList[letCount],top1):
                        # print "top 1IN DIC"
                        top1Dic = str(dicList[letCount].get(top1))
                        top1bool = True

                    if isInbinDic(dicList[letCount],top2):
                        # print " top 2 IN DIC:", top2
                        top2Dic = str(dicList[letCount].get(top2))
                        top2bool = True


                    if top1bool == True:
                        a = int(top1Dic)
                    else:
                        a = (top1)
                    if top2bool == True:
                        # print "hi"
                        b = int(top2Dic)
                    else:
                        b = (top2)
                    #
                    # print "a:", a,  type(a), isInteger(a)
                     # type(a), a, isInteger(a)
                    # print "b:", b, type(b),  isInteger(b)
                    # # print dicList
                    # type(b), b, isInteger(b)

                    if isInteger(a) and isInteger(b) and type(a) == type(b):
                        if operation == "add":
                            result = int(a) + int(b)
                            ans[letCount].append(result)
                        elif operation == "sub":
                            result = int(b) - int(a)
                            ans[letCount].append(result)
                        elif operation == "mul":
                            result = int(a) * int(b)
                            ans[letCount].append(result)
                        elif operation == "div":
                            if a == 0:
                                ans[letCount].append(b)
                                ans[letCount].append(a)
                                ans[letCount].append(error)

                            else:
                                result = int(b) / int(a)
                                ans[letCount].append(int(result))
                        elif operation == "rem":
                            result = int(b)% int(a)
                            ans[letCount].append(result)
                    else:
                        # print "add called"
                        ans[letCount].append(top2)
                        ans[letCount].append(top1)
                        ans[letCount].append(error)


        elif len(line) >= 2:
            # print "ans at push", ans[letCount]
            # val = inputArray[lineCount]
            if len(line)>2:
                index = inputArray[i].index("\"")
                val = inputArray[i]
                val = val[index:len(val)]
            else:
                val = line[1]
            if operation == "push":
                # ans[letCount].append(val)
                val = str(val)

                if val == "-0":
                    val = "0"
                    ans[letCount].append(val)
                elif '-' in val:
                    if val[1].isalpha():    #check for "-x"
                        stack.push(error)
                    if isInteger(val):
                        ans[letCount].append(val)

                elif val.isdigit():  #checks if num
                    val = int(val)
                    if isInteger(val):
                        ans[letCount].append(val)

                elif "\"" in val:   #checks if string
                    # print "found string"
                    # print "val", type(val), val


                    if val.isdigit():
                        # print "found int string"
                        ans[letCount].append(val)


                    elif val[0] == '"' and val[len(val)-1] == '"':
                        temp = val
                        val = val[1:len(val)-1]
                        ans[letCount].append(val)
                        dicStr[val] = temp

                    elif val[1] and val[len(val)-1]:
                        ans[letCount].append(val[2:len(val)-1])


                elif val.isalnum():   #check if string has only nums and letters then name
                    ans[letCount].append(val)

                elif isboolean(val):
                    ans[letCount].append(val)
                elif isError(val):
                    ans[letCount].append(val)
                else:
                    ans[letCount].append(error)



        i+=1
    # print "letCount ", letCount



def interpreter(input, output):
    stack = Stack()
    dicStr = {}
    bindDic = {}
    inputArray = []
    inputArraySplit = []
    letCount = 0
    lineCount = 0
    fileOut = output
    f = open(input, 'r').readlines()
    for line in f:
        line = line.strip() #strip removes leading and trailing space from string
        inputArray.append(line)
    for item in inputArray:
        item = item.split()
        inputArraySplit.append(item)
    for line in inputArraySplit:
        # print("line", line)
        length = len(line)
        # print "length:", length

        if length == 1:
            operation = line[0]
            # print "opp:", operation

        elif length == 2 and line[0].isalpha:
            operation = line[0]
            # print 'operation:' + ' '+ operation
            val = line[1]
            # print 'val:' + ' ' + val
        elif length > 2:
            # print "lineCount", lineCount
            # print("inputArray", inputArray[lineCount])
            index = inputArray[lineCount].index("\"")
            # print "index", index
            val = inputArray[lineCount]
            val = val[index:len(val)]
            # print "val:", val
            operation = line[0]
            # val = line[1:len(line)]
            # string = ""
            # for line in val:
            #     string = string + " " + line
            #     print "line:", line, "String:", string
            # # print "line", string
            # val = string

        if operation == "push":
            # print "val:", val
            # print len(val)
            # if isInbinDic(val):
            #     # print "val in bindDic"
            #     val = (bindDic.get(val))
            val = str(val)

            if val == "-0":
                val = "0"
                stack.push(val)
            elif '-' in val:
                if val[1].isalpha():    #check for "-x"
                    stack.push(error)
                if isInteger(val):
                    stack.push(val)

            elif val.isdigit():  #checks if num
                val = int(val)
                if isInteger(val):
                    stack.push(val)

            elif "\"" in val:   #checks if string
                # print "found string"
                # print "val", type(val), val



                if val.isdigit():
                    # print "found int string"
                    stack.push(val)



                elif val[0] == '"' and val[len(val)-1] == '"':
                    temp = val
                    val = val[1:len(val)-1]
                    stack.push(val)
                    dicStr[val] = temp
                    # print dicStr

                elif val[1] and val[len(val)-1]:
                    stack.push(val[2:len(val)-1])


            elif val.isalnum():   #check if string has only nums and letters then name
                # if val[0].isdigit:
                #     return stack.push(error)
                # else:
                stack.push(val)

            elif isboolean(val):
                stack.push(val)
            elif isError(val):
                stack.push(val)
            else:
                stack.push(error)
        elif operation == "pop":
            if stack.size()>= 1:
                stack.pop()
            else:
                stack.push(error)

        elif operation == "add" or operation == "sub" or operation == "mul" or operation == "div"or operation == "rem":
            top1bool = False
            top2bool = False
            # if stack.isEmpty() or stack.size() == 1:
            if stack.size()<2:
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                # print "1", top1
                # print "2", top2
                # print "in else"
                if isInbinDic(bindDic,top1):
                    # print "top 1IN DIC"
                    top1Dic = (bindDic.get(top1))
                    top1bool = True

                if isInbinDic(bindDic,top2):
                    # print " top 2 IN DIC"
                    top2Dic = (bindDic.get(top2))
                    top2bool = True

                if top1bool == True:
                    a = top1Dic
                else:
                    a = top1
                if top2bool == True:
                    # print "hi"
                    b = top2Dic
                else:
                    b = top2

                # print "a:", type(a), a, isInteger(a)
                # print "b:", type(b), b, isInteger(b)

                if isInteger(a) and isInteger(b) and type(a) == type(b):
                    if operation == "add":
                        result = int(a) + int(b)
                        stack.push(int(result))
                    elif operation == "sub":
                        result = int(b) - int(a)
                        stack.push(int(result))
                    elif operation == "mul":
                        result = int(a) * int(b)
                        stack.push(int(result))
                    elif operation == "div":
                        if a == 0:
                            stack.push(b)
                            stack.push(a)
                            stack.push(error)
                        else:
                            result = int(b) / int(a)
                        stack.push(int(result))
                    elif operation == "rem":
                        result = int(b)% int(a)
                        stack.push(int(result))
                else:
                    # print "add called"
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)

        elif operation == "neg":
            if stack.size()== 0:
                # print "stack empty 1"
                stack.push(error)
            elif stack.size() > 0:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))

                if isInteger(top1):
                    # print "IN NEG"
                    result = int(top1)*-1
                    stack.push(int(result))
            else:
                stack.push(top1)
                stack.push(error)

        elif operation == "swap":
            # print "output stack b4 div:"
            # print stack.printStack()
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if stack.isEmpty():
                    # print "stack only one elem"
                    stack.push(top1)
                    stack.push(error)
                else:
                    top2 = stack.pop()
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
                stack.push(top1)
                stack.push(top2)
                # print "top1:" + " "
                # print type(top1)
                # print top1
                # print "top2:" + " "
                # print top2
                # print "add num not ints"
        elif operation == "quit":
            fo = open(fileOut, 'w')
            while not stack.isEmpty():
                temp = stack.pop()
                # print "temp:"
                # print temp
                fo.write(str(temp) + "\n")

        elif operation == "cat":
            if stack.size()<=1:
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
            if type(top1) == int:
                top1 = str(top1)
            if type(top2) == int:
                top2 = str(top2)
                # print type(top1)
                # print type(top2)
            if type(top1) == str and type(top2) == str:
                # print "top1:", top1, "top2:", top2
                # print dicStr
                if (isInbinDic(dicStr,top1) and isInbinDic(dicStr, top2)):
                    if "\n" and "\t" not in top1:
                        if "\n" and "\t" not in top2:
                            if isAscii(top1) and isAscii(top2):
                                if top1.isdigit() or top1.isalpha():
                                    catString = top2 + " " + top1
                                else:
                                    catString = top2 + "" + top1
                                dicStr[catString] = catString
                                stack.push(catString)

                elif (isInbinDic(dicStr,top1) and not isInbinDic(dicStr, top2)):
                    if isInbinDic(bindDic,top2):
                        top2 = str(bindDic.get(top2))
                        if "\n" and "\t" not in top1:
                            if "\n" and "\t" not in top2:
                                if isAscii(top1) and isAscii(top2):
                                    if top1.isdigit() or top1.isalpha():
                                        catString = top2 + "" + top1
                                    else:
                                        catString = top2 + " " + top1
                                    dicStr[catString] = catString
                                    stack.push(catString)
                    else:
                        stack.push(error)
                elif (isInbinDic(dicStr,top2) and not isInbinDic(dicStr, top1)):
                    if isInbinDic(bindDic,top1):
                        top1 = str(bindDic.get(top1))
                        if "\n" and "\t" not in top1:
                            if "\n" and "\t" not in top2:
                                if isAscii(top1) and isAscii(top2):
                                    if top1.isdigit() or top1.isalpha():
                                        catString = top2 + "" + top1
                                    else:
                                        catString = top2 + " " + top1
                                    dicStr[catString] = catString
                                    stack.push(catString)
                    else:
                        stack.push(error)
                elif (isName(top1) and isName(top2)):
                    stack.push(error)

                elif "\n" and "\t" not in top1:
                    if "\n" and "\t" not in top2:
                        if isAscii(top1) and isAscii(top2):
                            if top1.isdigit() or top1.isalpha():
                                catString = top2 + "" + top1
                            else:
                                catString = top2 + " " + top1
                            dicStr[catString] = catString
                            stack.push(catString)
            else:
                stack.push(error)

        elif operation == "and" or operation == "or":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            elif stack.size() == 1:
                stack.push(error)
            elif stack.size() >= 2:
                top1 = stack.pop()
                top2 = stack.pop()
                # print "top1:", top1
                # print "top2:", top2
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
                if isboolean(top1) and isboolean(top2):
                    if operation == "and":
                        if top1 == tru and  top2 == tru:
                            stack.push(tru)
                        else:
                            stack.push(fal)
                    if operation == "or":
                        if top1 == fal and top2 == fal:
                            stack.push(fal)
                        else:
                            stack.push(tru)
                else:
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)

        elif operation == "not":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            elif stack.size()>= 1:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                # print "top1:" + " "
                # print type(top1)
                if isboolean(top1):
                    if top1 == tru:
                        top1 = fal
                        stack.push(top1)
                    else:
                        top1 = tru
                        stack.push(top1)
                else:
                    # print "add num not ints"
                    stack.push(top1)
                    stack.push(error)

        elif operation == "equal":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if stack.isEmpty():
                    stack.push(top1)
                    stack.push(error)
                else:
                    top2 = stack.pop()
                    if isInbinDic(bindDic,top2):
                        top2 = str(bindDic.get(top2))

            if type(top1) == int and type(top2) == int:
                if top1 == top2:
                    stack.push(tru)
                else:
                    stack.push(fal)
            else:
                stack.push(top2)
                stack.push(top1)
                stack.push(error)

        elif operation == "lessThan":
            if stack.size()<2:
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                # print("top1:", top1, "top2:", top2)
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                    if isInteger(top1):
                        top1 = int(top1)
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
                    if isInteger(top2):
                        top2 = int(top2)

                # print("top1:", top1, "top2:", top2)

                if type(top1) == int and type(top2) == int:
                    if int(top2) < int(top1):
                        stack.push(tru)
                    else:
                        stack.push(fal)
                else:
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)

        elif operation == "bind":
            # print "bind called"
            if stack.size()>1:
                top1 = stack.pop()
                top2 = stack.pop()
                if isInbinDic(bindDic,top1) and isInbinDic(bindDic,top2):
                    # print "both in dic"
                    if bindDic[top1] == None:
                        stack.push(error)
                    else:
                        bindDic[top2] = bindDic[top1]
                        stack.push(unit)
                elif not top1 == error and isValue(top1) and isName(top2) and not isInteger(top2) and not isInbinDic(dicStr, top2):
                    # print "top1:--", top1, type(top1)
                    #
                    # print "top2:", top2, type(top2)
                    bindDic[top2] = top1
                    stack.push(unit)
                    # print "top1 not in dic and is value"
                else:
                    # print "top 2 not name"
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)
            else:
                stack.push(error)

        elif operation == "if":
                if stack.size()<3:
                    stack.push(error)
                elif stack.size()>=3:
                    top1 = stack.pop()
                    top2 = stack.pop()
                    top3 = stack.pop()

                    # if isInbinDic(bindDic,top1):
                    #     top1 = str(bindDic.get(top1))
                    # if isInbinDic(bindDic,top2):
                    #     top2 = str(bindDic.get(top2))
                    if isInbinDic(bindDic,top3):
                        top3 = str(bindDic.get(top3))
                    # print("top1:",top1, "top2", top2, "top3", top3)
                    # print "top3 is boolean"
                    if not isboolean(top3):
                        stack.push(top3)
                        stack.push(top2)
                        stack.push(top1)
                        stack.push(error)
                    elif top3 == tru:
                        # print("top3 is tru push top2")

                        stack.push(top2)
                    elif top3 == fal:
                        # print ("top3 is fal push top1")

                        stack.push(top1)

        elif operation == "let":
            # print "lineCount", lineCount
            # "print opp == let"
            # letFrame = getlet(inputArray)
            # print "letFrame", letFrame
            newDic = bindDic.copy()
            # print "int stack", stack.printStack()
            computeLet(inputArraySplit, newDic, output, stack, lineCount, inputArray)
            break


        elif operation == "end":
            stack = stack
        lineCount+= 1
    # print "STACK:", stack.printStack()



#
def interpreter2(input, output, bindDic, stack):
    # print "interpreter2 called input:", input
    # print("stk at starting inter2:", stack.printStack())
    # stack = Stack()
    # bindDic = {}
    # print "bindDic:", bindDic
    dicStr = {}
    letCount = 0
    lineCount = 0
    fileOut = output
    for line in input:
        # print "line", line
        length = len(line)
        # print "length:", length

        if length == 1:
            operation = line[0]
            operationBool = True
            # print "opp:", operation

        elif length == 2 and line[0].isalpha:
            operation = line[0]
            # print 'operation:' + ' '+ operation
            val = line[1]
            # print 'val:' + ' ' + val
        elif length > 2:
            # print "lineCount", lineCount
            # print "inputArray", inputArray[lineCount]
            index = inputArray[lineCount].index("\"")
            # print "index", index
            val = inputArray[lineCount]
            val = val[index:len(val)]
            # print "val:", val
            operation = line[0]
            # val = line[1:len(line)]
            # string = ""
            # for line in val:
            #     string = string + " " + line
            #     print "line:", line, "String:", string
            # # print "line", string
            # val = string

        if operation == "push":
            # print "val:", val
            # print len(val)
            # if isInbinDic(val):
            #     # print "val in bindDic"
            #     val = (bindDic.get(val))
            val = str(val)

            if val == "-0":
                val = "0"
                stack.push(val)
            elif '-' in val:
                if val[1].isalpha():    #check for "-x"
                    stack.push(error)
                if isInteger(val):
                    stack.push(val)

            elif val.isdigit():  #checks if num
                val = int(val)
                if isInteger(val):
                    stack.push(val)

            elif "\"" in val:   #checks if string
                # print "found string"
                # print "val", type(val), val


                if val.isdigit():
                    # print "found int string"
                    stack.push(val)


                elif val[0] == '"' and val[len(val)-1] == '"':
                    temp = val
                    val = val[1:len(val)-1]
                    stack.push(val)
                    dicStr[val] = temp


                elif val[1] and val[len(val)-1]:
                    stack.push(val[2:len(val)-1])


            elif val.isalnum():   #check if string has only nums and letters then name
                # if val[0].isdigit:
                #     return stack.push(error)
                # else:
                stack.push(val)

            elif isboolean(val):
                stack.push(val)
            elif isError(val):
                stack.push(val)
            else:
                stack.push(error)
        elif operation == "pop":
            if stack.size()>= 1:
                stack.pop()
            else:
                stack.push(error)

        elif operation == "add" or operation == "sub" or operation == "mul" or operation == "div"or operation == "rem":
            top1bool = False
            top2bool = False
            if stack.size() < 2:
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                # print "1", top1
                # print "2", top2
                # print "in else"
                if isInbinDic(bindDic,top1):
                    # print "top 1IN DIC"
                    top1Dic = (bindDic.get(top1))
                    top1bool = True

                if isInbinDic(bindDic,top2):
                    # print " top 2 IN DIC"
                    top2Dic = (bindDic.get(top2))
                    top2bool = True

                if top1bool == True:
                    a = int(top1Dic)
                else:
                    a = top1
                if top2bool == True:
                    # print "hi"
                    b = int(top2Dic)
                else:
                    b = top2

                # print "a:", type(a), a, isInteger(a)
                # print "b:", type(b), b, isInteger(b)

                # if type(b) == str:
                #     try:
                #         # int(top1)
                #         b = int(b)
                #     except(RuntimeError, TypeError, NameError, ValueError):
                #         stack.push(top2)
                #         stack.push(top1)
                #         stack.push(error)

                if isInteger(a) and isInteger(b) and type(a) == type(b):
                    if operation == "add":
                        result = int(a) + int(b)
                        stack.push(int(result))
                    elif operation == "sub":
                        result = int(b) - int(a)
                        stack.push(int(result))
                    elif operation == "mul":
                        result = int(a) * int(b)
                        stack.push(int(result))
                    elif operation == "div":
                        if a == 0:
                            stack.push(b)
                            stack.push(a)
                            stack.push(error)
                        else:
                            result = int(b) / int(a)
                        stack.push(result)
                    elif operation == "rem":
                        result = int(b)% int(a)
                        stack.push(int(result))
                else:
                    # print "add called"
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)

        elif operation == "neg":
            if stack.size()== 0:
                # print "stack empty 1"
                stack.push(error)
            elif stack.size() > 0:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))

                if isInteger(top1):
                    # print "IN NEG"
                    result = int(top1)*-1
                    stack.push(result)
            else:
                stack.push(top1)
                stack.push(error)

        elif operation == "swap":
            # print "output stack b4 div:"
            # print stack.printStack()
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if stack.isEmpty():
                    # print "stack only one elem"
                    stack.push(top1)
                    stack.push(error)
                else:
                    top2 = stack.pop()
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
                stack.push(top1)
                stack.push(top2)
                # print "top1:" + " "
                # print type(top1)
                # print top1
                # print "top2:" + " "
                # print top2
                # print "add num not ints"
        elif operation == "quit":
            # print ("STACK:", stack.printStack())
            # # fo = open(fileOut, 'w')
            # while not stack.isEmpty():
            #     temp = stack.pop()
            #     print "temp:",temp
            #     fo.write(str(temp) + "\n")

            return stack

        elif operation == "cat":
            if stack.size()<=1:
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
            if type(top1) == int:
                top1 = str(top1)
            if type(top2) == int:
                top2 = str(top2)
                # print type(top1)
                # print type(top2)
            if type(top1) == str and type(top2) == str:
                # print "top1:", top1, "top2:", top2
                # print dicStr
                if (isInbinDic(dicStr,top1) and isInbinDic(dicStr, top2)):
                    if "\n" and "\t" not in top1:
                        if "\n" and "\t" not in top2:
                            if isAscii(top1) and isAscii(top2):
                                if top1.isdigit() or top1.isalpha():
                                    catString = top2 + "" + top1
                                else:
                                    catString = top2 + " " + top1
                                dicStr[catString] = catString
                                stack.push(catString)

                elif (isInbinDic(dicStr,top1) and not isInbinDic(dicStr, top2)):
                    if isInbinDic(bindDic,top2):
                        top2 = str(bindDic.get(top2))
                        if "\n" and "\t" not in top1:
                            if "\n" and "\t" not in top2:
                                if isAscii(top1) and isAscii(top2):
                                    if top1.isdigit() or top1.isalpha():
                                        catString = top2 + "" + top1
                                    else:
                                        catString = top2 + " " + top1
                                    dicStr[catString] = catString
                                    stack.push(catString)
                    else:
                        stack.push(error)
                elif (isInbinDic(dicStr,top2) and not isInbinDic(dicStr, top1)):
                    if isInbinDic(bindDic,top1):
                        top1 = str(bindDic.get(top1))
                        if "\n" and "\t" not in top1:
                            if "\n" and "\t" not in top2:
                                if isAscii(top1) and isAscii(top2):
                                    if top1.isdigit() or top1.isalpha():
                                        catString = top2 + "" + top1
                                    else:
                                        catString = top2 + " " + top1
                                    dicStr[catString] = catString
                                    stack.push(catString)
                    else:
                        stack.push(error)
                elif (isName(top1) and isName(top2)):
                    stack.push(error)

                elif "\n" and "\t" not in top1:
                    if "\n" and "\t" not in top2:
                        if isAscii(top1) and isAscii(top2):
                            if top1.isdigit() or top1.isalpha():
                                catString = top2 + "" + top1
                            else:
                                catString = top2 + " " + top1
                            dicStr[catString] = catString
                            stack.push(catString)
            # else:
            #     stack.push(error)

        elif operation == "and" or operation == "or":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            elif stack.size() == 1:
                stack.push(error)
            elif stack.size() >= 2:
                top1 = stack.pop()
                top2 = stack.pop()
                # print "top1:", top1
                # print "top2:", top2
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))
                if isboolean(top1) and isboolean(top2):
                    if operation == "and":
                        if top1 == tru and  top2 == tru:
                            stack.push(tru)
                        else:
                            stack.push(fal)
                    if operation == "or":
                        if top1 == fal and top2 == fal:
                            stack.push(fal)
                        else:
                            stack.push(tru)
                else:
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)

        elif operation == "not":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            elif stack.size()>= 1:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                # print "top1:" + " "
                # print type(top1)
                if isboolean(top1):
                    if top1 == tru:
                        top1 = fal
                        stack.push(top1)
                    else:
                        top1 = tru
                        stack.push(top1)
                else:
                    # print "add num not ints"
                    stack.push(top1)
                    stack.push(error)

        elif operation == "equal":
            if stack.size()<=1:
                # print "stack empty 1"
                stack.push(error)
            elif stack.size()>=2:
                top1 = stack.pop()
                top2 = stack.pop()
                # print "stk at =:", stack.printStack()
                if isInbinDic(bindDic,top1):
                    top1 = str(bindDic.get(top1))
                if isInbinDic(bindDic,top2):
                    top2 = str(bindDic.get(top2))

                # print "top1:", top1, type(top1),"top2", top2, type(top2)

                if type(top2) == str:
                    try:
                        # int(top1)
                        top2 = int(top2)
                    except(RuntimeError, TypeError, NameError, ValueError):
                        stack.push(top2)
                        stack.push(top1)
                        stack.push(error)

                if type(top1) == int and type(top2) == int:
                    if top1 == top2:
                        stack.push(tru)
                    else:
                        stack.push(fal)
                # else:
                #     stack.push(top2)
                #     stack.push(top1)
                #     stack.push(error)

        elif operation == "lessThan":
            if stack.isEmpty():
                # print "stack empty 1"
                stack.push(error)
            else:
                top1 = stack.pop()
                if isInbinDic(bindDic,top1):
                    top1 = int(bindDic.get(top1))
                if stack.isEmpty():
                    stack.push(top1)
                    stack.push(error)
                else:
                    top2 = stack.pop()
                    if isInbinDic(bindDic,top2):
                        top2 = int(bindDic.get(top2))

            if type(top1) == int and type(top2) == int:
                if top2 < top1:
                    stack.push(tru)
                else:
                    stack.push(fal)
            else:
                stack.push(top2)
                stack.push(top1)
                stack.push(error)

        elif operation == "bind":
            # print "bind called"
            # print ("STACK at bind:", stack.printStack())
            if stack.size()>1:
                top1 = stack.pop()
                top2 = stack.pop()
                if isInbinDic(bindDic,top1) and isInbinDic(bindDic,top2):
                    # print "both in dic"
                    if bindDic[top1] == None:
                        stack.push(error)
                    else:
                        bindDic[top2] = bindDic[top1]
                        stack.push(unit)
                elif not top1 == error and isValue(top1) and isName(top2) and not isInteger(top2) and not isInbinDic(dicStr, top2):
                    # print "top1:", top1, type(top1)
                    #
                    # print "top2:", top2
                    bindDic[top2] = top1
                    stack.push(unit)
                    # print stack.printStack()
                    # print "top1 not in dic and is value"
                else:
                    # print "top 2 not name"
                    stack.push(top2)
                    stack.push(top1)
                    stack.push(error)
            else:
                stack.push(error)

        elif operation == "if":
                if stack.size()<3:
                    stack.push(error)
                elif stack.size()>=3:
                    top1 = stack.pop()
                    top2 = stack.pop()
                    top3 = stack.pop()

                    # if isInbinDic(bindDic,top1):
                    #     top1 = str(bindDic.get(top1))
                    # if isInbinDic(bindDic,top2):
                    #     top2 = str(bindDic.get(top2))
                    if isInbinDic(bindDic,top3):
                        top3 = str(bindDic.get(top3))
                    # print("top1:",top1, "top2", top2, "top3", top3)
                    # print "top3 is boolean"
                    if not isboolean(top3):
                        stack.push(top3)
                        stack.push(top2)
                        stack.push(top1)
                        stack.push(error)
                    elif top3 == tru:
                        # print("top3 is tru push top2")
                        if isInbinDic(bindDic,top2):
                            top2 = str(bindDic.get(top2))
                        stack.push(top2)
                    elif top3 == fal:
                        # print ("top3 is fal push top1")
                        if isInbinDic(bindDic,top1):
                            top1 = str(bindDic.get(top1))
                        stack.push(top1)

        # elif operation == "end":
        #     stack = stack
        # lineCount+= 1







# # #
# if __name__== "__main__":
#     interpreter('test-Input.txt', 'test-Output.txt')
    # # string = "!"
    # # print string.isalpha()

    # s = Stack()
    # s.push(s)
    # print x
    # # if x.find('\"'):
    # #     print "hi"
    # y = s.pop()


    # print x.isalpha()
