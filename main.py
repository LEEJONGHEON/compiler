# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import re
if __name__ == '__main__':

    f = open(sys.argv[1],'r')
    keyword = {'if':'If', 'else':'Else', 'while':'While', 'break':'Break', 'continue':'Continue',
                'return':'Return', '=':'Assign', ';':'Semicolon', '(':'LPar', ')':'RPar', '{':'LBrace',
                '}':'RBrace', '+':'Plus', '*':'Mult', '/':'Div', '<':'Lt', '>':'Gt', '==':'Eq'}
    semiFlag = 0
    rParFlag = 0
    inputFlag = 0
    p = re.compile('[a-z]+')
    for line in f:
        temp = line.split(' ')
        # print(temp)
        for temp2 in temp:
            if(';' in temp2):
                temp2 = temp2[:temp2.find(';')] # semicolon delete
                semiFlag = 1 # semicolon flag on
                # print("테스트입니다 : "+temp2)
            elif('(' in temp2):
                temp2 = temp2[temp2.find('(')+1:]
                # print("테스트용1:"+temp2)
                print("LPar")
            elif(')' in temp2):
                temp2 = temp2[:temp2.find(')')]
                # print("테스트용2:" + temp2)
                rParFlag = 1
            elif "==" in temp2 and len(temp2)>=3:
                temp2 = temp2[:len(temp2)-3]
                print('Eq')
                inputFlag = 1

            if ('\n' in temp2):
                temp2 = temp2[:temp2.find('\n')]


            if (temp2 in keyword.keys()): # keword
                print(keyword[temp2])

                inputFlag = 1
            elif(temp2.isalpha()): #  aa , abc
                print("Ident("+temp2+")")
                inputFlag = 1
            elif(temp2.isdigit()): # 12
                print("Number("+temp2+")")
                inputFlag = 1
            elif (temp2.isalnum()): # a123
                if(temp2[0].isdigit()): # 123a123
                    m = p.search(temp2)
                    # print("테스트 입니다 : " +str(m.end()))
                    number = temp2[:m.end()-1]
                    string = temp2[m.end()-1:]
                    print("Number("+number+")")
                    print("Ident(" + string + ")")
                else:
                    print("Ident("+temp2+")")
                inputFlag = 1
            elif(temp2=="" and semiFlag==0 and rParFlag==0):
                continue # space
                inputFlag = 1

            if semiFlag:
                print("Semicolon")
                semiFlag = 0
                inputFlag = 1

            if rParFlag:
                print("RPar")
                rParFlag = 0
                inputFlag = 1

            if inputFlag==0:
                print("Err")
                # print(temp2)
                exit(0)
            inputFlag = 0







