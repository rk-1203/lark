import re
fo = open("prog.txt", "r+")                                                                                            #opens a file
str = fo.read()                                                                             			       #reads the file
fo.close()
while '$' in str:
    i=0;
    while i<len(str):
        if str[i] == '$':
            str=str[0:i]+str[i+1:]
            break
        else:
            i+=1
    while str[i]!='$':
        if i!=len(str)-1:
            str=str[0:i]+str[i+1:]
        else:
            print("ErroR")
            break
    str=str[0:i]+str[i+1:]
#print(str)
flag = 0
digit = ['0','1','2','3','4','5','6','7','8','9']
op1 = ['+', '-']
op2 = [ '*', '/', '%']
op3= ['|','&','!']
global op
op = op1 + op2 + op3
sp=op+[';']
alpha =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
key = ['int', 'float', 'string']
global keywords
keywords=['kick_start','get','set']+key
return_type = ['int', 'void']
count=0
global var_final
var_final={}

def int_float(s):
    try:
        int(s)
        return 1    
    except ValueError:
        try:
            float(s)
            return 1
        except ValueError :
            return 0
def var_check(str5,x):
    if(str5[0] in digit) :
        print('Error! line',x,": Invalid variable name for",str5)
        return 0
    else:
        for letter in str5 :
            if(letter not in digit and letter not in alpha and letter!='_') :
                print('Error! line',x,": Invalid variable name for",str5)
                return 0
                break
    return 1

def setf(str,x,var):
    inp=''
    li=[]
    str=str.strip()
    if str[len(str)-1]!=';':
        print('Error! line',x,": Statement must terminates with a semi-colon")
    else :
        str=str[:len(str)-1]
    for letter in str :
        if letter ==':' :
            break
        else :
            inp+=letter
            str=str[1:]
    inp=inp.strip()
    if inp != "set":
        print('Error! line',x, "Syntax error")
    else :
        if str[0]!=":":
            print('Error! line',x, "Syntax error")
        else :
            str=str[1:]
            str=str.strip()
            list=str.split(',')
            #print(list)
            for item in list:
                item=item.strip()
                if item[0] == '\'':
                    if item[len(item)-1]!='\'':
                        print('Error! line',x,": Closing quote missing")
                if item[len(item)-1]=='\'':
                    if item[0] != '\'':
                        print('Error! line',x,": Opening quote missing")
                if item[0]==item[len(item)-1]=='\'':
                    print(item[1:len(item)-1],end=''),
                else:
                    item=item.strip()
                    if var_check(item,x):
                        if item not in var:
                            print("Error! line",x,"First use in program \'",item,'\'')
                        else:
                            print(var[item],end='')
    print("")


def getf(str,x,var):
    inp=''
    str=str.strip()
    #global keywords
    if str[len(str)-1]!=';':
        print('Error! line',x,": Statement must terminates with a semi-colon")
    else :
        str=str[:len(str)-1]
    for letter in str :
        if letter ==':' :
            break
        else :
            inp+=letter
            str=str[1:]
    inp=inp.strip()
    if inp != "get":
        print('Error! line',x, "Syntax error")
    else :
        if str[0]!=":":
            print('Error! line',x, "Syntax error")
        else :
            str=str[1:]
            str=str.strip()
            li=str.split(",")
            for item in li:
                item=item.strip()
                if var_check(item,x):
                    if item not in keywords:
                        var[item]=input()
                    else:
                        print("Error! line:",x,'\'',item,'\'',"can't be used as a variable")


def split(str):
    var=''
    list=[]
    for letter in str :
        if(letter not in sp):
            var+=letter
            str=str[1:]
        else:
            var=var.strip(' \t\r')
            if not int_float(var) :
                list+=[var]
            var=''
            str=str[1:]
    if var!='':
        var=var.strip(' \t\r')
        if not int_float(var) :
            list+=[var]
    return list



def number(str):
    try:
        val = int(str) or float(str)
        return 1
    except ValueError:
        return 0

def evaluate(str,x,var):
    str=str.strip()
    #print(str,var)
    temp=''
    exp=''
    for letter in str:
        if letter not in op and letter!='(' and letter!=')' and letter!=';' and letter!=' ':
           temp+=letter
        elif letter!=' ':
            if temp=='':
                exp+=letter
            else:
                temp=temp.strip()
                if(int_float(temp)):
                    exp=exp+temp+letter
                    temp=''
                elif temp in var_final:
                    exp=exp+var_final[temp]+letter
                    temp=''
    exp=exp[:len(exp)-1]
    #print(exp)
    exp=exp.replace('&',' and ')
    exp=exp.replace('|',' or ')
    exp=exp.replace('!',' not ')
    #print(exp)
    var_final[var]=eval(exp).__str__()
    #print(var_final)



def initial_check(str,x,var_final):
    str=str.strip()
    if(str[len(str)-1] != ';'):
        print('Error! line',x,": Statement must terminates with a semi-colon\n")
    else:
        str=str[:len(str)-1]
    li=[]
    li1=[]
    li1=str.split(",")
    for items in li1:
        li=items.split("=")
        #print (li)
        matchObj = re.match( r'["]*(.|\n)*["]*', li[len(li)-1], re.M)
        if(matchObj and not int_float(li[len(li)-1])):
            value=li[len(li)-1]
            value=value[1:len(value)-1]
            li[len(li)-1]=value
        if not int_float(li[len(li)-1])and not matchObj:
            print('Syntax Error! line',x,": Variables not initialized ")
            return []
        else:
            value = li[len(li)-1]
            li=li[0:len(li)-1]
            for item in li:
                item=item.strip()
                if var_check(item,x):
                    if item not in keywords:
                        var_final[item]=value
                    else:
                        print("Error! line:",x,'\'',item,'\'',"can't be used as a variable")
                #print (item)
    return var_final


def expr_check(strc,x,var_final):
    #print (strc)
    ob=cb=0
    strc=strc.strip()
    if(strc[len(strc)-1] != ';'):
        print('Error! line',x,": Statement must terminates with a semi-colon")
    var=''
    for letter in strc :
        if(letter != '='):
            var+=letter
            strc=strc[1: ]
        else:
            strc=strc[1: ]
            break
    var=var.strip()
    if var_check(var,x):
        if var not in keywords:
            strk=strc
            for letter in strc :
                if letter == '(' :
                    ob+=1
                elif letter == ")" :
                    cb+=1
            if ob!=cb :
                print("Error! line :",x,'Improper pair of parenthesis')
            else :
                strc=strc.replace('(','')
                strc=strc.replace(")",'')
                var_list=split(strc)
                for items in var_list :
                    if items not in var_final:
                        print('Syntax Error! line',x,": Undeclared variable\'",items,'\'')
                    else:
                        var_check(items,x)
                var_list+=[var]
                evaluate(strk,x,var)
        else:
             print("Error! line:",x,'\'',item,'\'',"can't be used as a variable")


str1=""
start = ['intkick_start()','voidkick_start()']                                                                         #start check
for letter in str :                                                                                                        
    if(letter == ' '):
        str=str[1: ]
    elif(letter == "\n" and str1 != '') :
        str=str[1: ]
        count+=1
        break
    elif(letter == "\n" and str1 == '') :
        count+=1
        str=str[1: ]
    else :
        str1+=letter
        str=str[1: ]
if(str1 not in start) :
    print('Error! line',count,': Code start')
str2=''                                                                                                                 #opening check
for letter in str :                                                                                                        
    if(letter == ' ' and str2==''):
        str=str[1: ]
    elif(letter == " " and str2 != '') :
        str=str[1: ]
        break
    elif(letter == "\n" and str2 != '') :
        str=str[1: ]
        count+=1
        break
    elif(letter == "\n" and str2 == '') :
        count+=1
        str=str[1: ]
    else :
        str2+=letter
        str=str[1: ]
if(str2[0]!='{') :
    print('Error! line',count,": Opening brace missing")
l=len(str)                                                                                                              #closing check
for i in range(l-1,0,-1) :
    if(str[i] == '}') :
        flag=1
        break
if(flag==0) : print("Error! The program must terminates with a closing brace")
#print (str)
new=0
for letter in str :
    if(letter=='\n') :
        new+=1
#print(new)
i=1
while(i<=new):                                                                                                           #program body
    str2=''
    for letter in str :
        #print (letter)
        if(letter != '\n') :
            str2+=letter
            str=str[1: ]
        else :
            count+=1
            str2+=letter
            str=str[1:]
            break
    #print(str2)
    str2=str2.strip(' \t\r')
    #print(str2)
    if str2 == '\n':
        i+=1
    else :
        k=1
        if "get" in str2:
            k=0
            getf(str2,count,var_final)
        elif "set" in str2 :
            k=0
            setf(str2,count,var_final)
        elif any(ext in str2 for ext in op):
            expr_check(str2,count,var_final)
        else:
            var_final=initial_check(str2,count,var_final)
        i+=1
    #print(i)
#print (var_final)
print(eval("3^1"))
