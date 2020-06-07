import re
fo = open("struct.txt", "r+")                                                                                            #opens a file
str = fo.read()                                                                             			       #reads the file
fo.close()
str=str.strip()
#print(str)
global alpha
global digit
alpha =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digit = ['0','1','2','3','4','5','6','7','8','9']
while " \n" in str :
    str=str.replace(" \n","\n")
while "\n\n" in str :
    str=str.replace("\n\n","\n")
while "  " in str :
    str=str.replace("  "," ")
#print(str)
def var_check(str):
    str=str.strip()
    #print(str[0])
    if str[0] in digit :
        print('Error!: Invalid variable name for',str)
        return 0
    else:
        for letter in str :
            if(letter not in digit and letter not in alpha) :
                print('Error! Invalid variable name for',str)
                return 0
                break
    return 1

def setf(str,var):
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
        print('Error! Syntax error')
    else :
        if str[0]!=":":
            print('Error!Syntax error')
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
                    if item not in var:
                        print("Error! First use in program ",item)
                    else:
                        print(var[item],end='')
    print("")

list1 = str.split("\n")
#print(list1)
list=[]
for l in list1 :
    if '}' not in l :
        list+=[l]
        list1=list1[1:]
    else :
        list+=[l]
        list1=list1[1:]
        break
#print(list,list1)
if ' ' in list[0]:
    lim=list[0].split(" ")
    if len(lim)>2:
        list[0]=lim[0] + lim[len(lim)-1]
        var_check(lim[1])
    else :
        list[0]=lim[0]
        var=lim[len(lim)-1]
        if var[len(var)-1]=="{":
            var=var[:len(var)-1]
            list[0]+="{"
            var_check(var)
if list[0] == 'struct' :
    list[1]=list[1].strip()
    if list[1] != '{' :
        it=list[1]
        if it[0] != "{" :
            print("Error ! Opening parenthesis missing")
        else :
            it=it[1:]
            list[1]=it
            list =list[1:]
    else :
        list=list[2:]
elif list[0] == 'struct{' :
    list=list[1: ]
else :
    print("Error! data-type not defined")
list[len(list)-1]=list[len(list)-1].strip()
if list[len(list)-1] != '};' :
    it=list[len(list)-1]
    if it[len(it)-1] != '}' :
        if it[0] != '}' :
            print("Error ! closing parenthesis missing")
        else :
            it=it[1:]
            if it[len(it)-1] != ';' :
                print("Error! The structure declaration must terminates with a semicolon")
            else :
                it=it[:len(it)-1]
                if ',' in it :
                    decl=it.split(',')
                    for items in decl :
                        var_check(items)
                elif it!='' and it!=' ' :
                    var_check(it)
            list=list[:len(list)-1]
    else :
        it=it[:len(it)-1]
        list[len(list)-1]=it
else :
    list=list[:len(list)-1]
#print(list)
lit=[]
dict={}
var_list=[]
for item in list :
    if item[len(item)-1] != ";" :
        print("Error ! Statement must terminates with a semi-colon")
    else :
        li=item.split(';')
        li=li[:len(li)-1]
        for it in li :
            var=''
            for letter in it:
                if letter != ' ' :
                    var+=letter
                    it=it[1:]
                else :
                    break
            if var != 'int' and var != 'char' and var!= 'float' :
                print("Error ! Primary data-type not defined")
            else :
                if ',' in it :
                    lit+=it.split(',')
                    for mem in lit :
                        mem= mem.strip()
                        var_check(mem)
                else :
                    var_check(it)
                    it=it.strip()
                    lit+=[it]
print("Thank you !")
#print(decl)
#print(lit)
for mem in decl :
    for itm in lit :
        var_list+=[mem+'.'+itm]
#print(var_list)
for item in list1:
    if 'set'in item:
        setf(item,dict)
    else:
        if item[len(item)-1]!=';':
            print("Error ! Statement must terminates with a semi-colon")
        else :
            item=item[:len(item)-1]
            if '=' in item :
                list2=item.split('=')
                if list2[0] not in var_list :
                    print("Error! Undeclared variable used")
                else:
                    dict[list2[0]] = list2[1]
#print(dict)        
