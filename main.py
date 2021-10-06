# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

if __name__ == '__main__':

    f = open(sys.argv[1],'r')
    keyword = {'if':'If', 'else':'Else', 'while':'While', 'break':'Break', 'continue':'Continue',
                'return':'Return', '=':'Assign', ';':'Semicolon', '(':'LPar', ')':'RPar', '{':'LBrace',
                '}':'RBrace', '+':'Plus', '*':'Mult', '/':'Div', '<':'Lt', '>':'Gt', '==':'Eq'}
    semiFlag = 0
    rParFlag = 0
    for line in f:
        temp = line.split(' ')
        # print(temp)
        for temp2 in temp:
            if(';' in temp2):
                temp2 = temp2[:temp2.find(';')] # semicolon delete
                semiFlag = 1 # semicolon flag on
            elif('\n' in temp2):
                temp2 = temp2[:temp2.find('\n')]
                #print("테스트입니다:"+temp2)
            elif('(' in temp2):
                temp2 = temp2[temp2.find('(')+1:]
                # print("테스트용1:"+temp2)
                # print("LPar")
            elif(')' in temp2):
                temp2 = temp2[:temp2.find(')')]
                # print("테스트용2:" + temp2)

                rParFlag = 1

            if (temp2 in keyword.keys()):
                print(keyword[temp2])
            elif(temp2.isalpha()):
                print("Ident("+temp2+")")
            elif(temp2.isdigit()):
                print("Number("+temp2+")")
            elif(temp2==""):
                continue # space
            else:
                print("Err")
                print(temp2)
                exit(0)
            if semiFlag:
                print("Semicolon")
                semiFlag=0
            elif rParFlag:
                print("RPar")
                rParFlag = 0




