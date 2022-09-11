def Recursive(num,carry = None):
    def printA(array,tempA = None):
        if(tempA == None):
            tempA = ''
        tempA += str(array.pop(0))
        if(len(array)==0):
            print(tempA)
        else:
            printA(array,tempA)
    temp = []
    def bitCalculate(array,bit):
        bit -= 1
        array[bit] += 1
        if(array[bit] >= 2):
            array[bit] = 0
            return bitCalculate(array,bit)
        else:
            return array
    def bitCheck(array,bit):
        bit -= 1
        if(array[bit] == 1 and bit == 0):
            return True
        else:
            if(array[bit] == 1):
                return bitCheck(array,bit)
            else:
                return False
    def creatTemp(array,num1):
        num1 -= 1
        if(num1 == -1):
            return array
        else:
            array.append(0)
            return creatTemp(array,num1)
    if(num == 0):
        print("0")
        return
    if(num < 0):
        print("Only Positive & Zero Number ! ! !")
        return
    if(carry == None):
        temp = creatTemp(temp.copy(),num)
        printA(temp.copy())
        carry = temp.copy()
        return Recursive(num,carry)
    else:
        carry = bitCalculate(carry,num)
        printA(carry.copy())
        if(bitCheck(carry,num)):
            return
        else:
            return Recursive(num,carry)

x = int(input("Enter Number : "))
Recursive(x)
