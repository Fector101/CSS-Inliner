# Make objectToStyle add comment
    # 'body':{
    #         'color': 'red',
    #         'comment'+unique_char_4_space: '   THE COMMENT '
    #     }
    # 'comment':{+unique_char_4_space: '   THE COMMENT '}
    # 'h1':{
    #         'color': 'red',
    #         'comment'+unique_char_4_space: '   THE COMMENT '
    #     }

unique_char_4_space="defiohf;qebio;gofhwe9-fpweffopefo"
with open('input/small.css', mode='r') as data:
    file_code=data.read()
    CODE=file_code
def noOfLines():
    return CODE.count('\n')
def replaceAllFromList(input:str,list_:list,char_to_replace_with:str):
    if input == '' or input == unique_char_4_space:
        return ''
    output=unique_char_4_space
    for each in list_:
        # output = unique_char_4_space 
        if(output==unique_char_4_space):
            output=input.replace(each,char_to_replace_with)
        else:
            output=output.replace(each,char_to_replace_with)
    return output
def removeComments(code:str):
    if '/*' not in code:
        return code
    new_str=''
    found_comment_end=True
    i = 0
    if code.count('/*') != code.count('*/'):

        ...
    for char in code:
        if char == '/' and i+1 != len(code) and code[i+1] == '*':
            found_comment_end = False
        elif (char == '*' and i+1 != len(code) and code[i+1] == '/') or (char == '/' and i-1 != 0 and code[i-1] == '*'):
            found_comment_end=True
        elif found_comment_end:
            new_str+=char
        i+=1
    list_for_empty_return=['/','*','{']
    if any(i.replace(' ','') == new_str for i in list_for_empty_return):
        return ''
    else:
        return new_str
def writeInFile(str_=''):
    with open('ouput/without_whitespace/style.css',mode='w')as file:
        file.write(str_)
def myStrip(code:str):
    """Removes unnesseccary white space and empty selectors. (div{})"""
    new_str=''
    i=0
    remove_space=False
    # code=replaceAllFromList(repr(code),[r'\t',r'\v',r'\n',r'\r',r'\f'],'')#.replace('\n','')
    # code=repr(code)
    code=code.replace('\n','')
    # code=removeComments(code)
    # print(code[0:30])
    # code=re.sub(r'[^\S\t\f\v\r\n]+ ','',code)
    lenght_of_str=len(code)
    checkpoints=['{',':',';','}']
    for char in code:
        if any(i == char for i in checkpoints):
            remove_space=True
            if char=='{':
                new_str=new_str.rstrip() #removing space between h1 above open curlly braces e.g "h1 {"
                new_str+=char
            elif char == '}' and new_str[-1]=='{': 
                # Removes empty selectors
                index_of_last_closed_braces = new_str.rfind('}')
                if index_of_last_closed_braces != -1:
                    new_str=new_str[0:index_of_last_closed_braces+1]
                else:
                    new_str+=char
            else:
                new_str+=char
        elif (char == '/' and i+1 != lenght_of_str and code[i+1] == '*') or (char == '*' and i-1 != 0 and code[i-1] == '/'):#/*
            # print(char, code[i+1], code[i+2], code[i+3], code[i+4], code[i+5], code[i+6], code[i+7], code[i+8], code[i+9], code[i+10], code[i+11], code[i+12])
            new_str+=char
            remove_space=True
        # elif (char == '*' and i+1 != len(code) and code[i+1] == '/'):
        elif (char == '*' and i+1 != lenght_of_str and code[i+1] == '/') or (char == '/' and i-1 != 0 and code[i-1] == '*'):
            new_str+=char
            remove_space=True
        elif char == ' ' and remove_space:
            pass
        else:# and found_style_start:
            # if new_str and any(new_str[-1] == i for i in ['{',';']):
            #     new_str+='\t'+char
            # else:
            remove_space=False
            new_str+=char
        i+=1
    return new_str

def removeWhiteSpaces(code,return_=False,comments=False):
    no_comments=code
    if not comments:
        no_comments=removeComments(CODE)    # Doesn't make sense to have comments when no whitespaces it won't be visible
    no_whitespaces=myStrip(no_comments)
    if return_:
        return no_whitespaces
    with open('ouput/without_whitespace/style.css','w')as file:
        file.write(no_whitespaces)

def stylesToObject(code:str):
    """
        Comments go to one line and
        Code Works when semi-column added to last style when a selector has another selector within.
    """
    code_=myStrip(code)
    # code_=removeComments(code_)
    
    list_of_selectors=[]
    styles={}
    found_selector_name_end=False # found end of selector e.g "hr","h1","div", ".class-name","#id"
    found_a_style_name_start=False
    found_a_style_name_end=False # i.e ":"
    selector=''
    style_des_name='' #'background-color'
    style_des_value='' #'#FF0AAA'
    new_selector=''
    found_a_style_value_start=False
    i=0
    rin=0

    def checkIfCommentEle(char='',i=0):
        # print(char)
        if not any(char == e for e in ['/','*']):
            return False
        if (char == '/' and i+1 != len(code_) and code_[i+1] == '*')  or (char == '*' and i-1 != 0 and code_[i-1] == '/') or  (char == '*' and i+1 != len(code_) and code_[i+1] == '/')  or (char == '/' and i-1 != 0 and code_[i-1] == '*') :
            return True
        else:
            return False
    def inCommentStart(char='',i=0):
        """Check if is any of the char(s) that Starts the comment"""
        if not any(char == e for e in ['/','*']):
            return False
        if (char == '/' and i+1 != len(code_) and code_[i+1] == '*')  or (char == '*' and i-1 != 0 and code_[i-1] == '/'):
            return True
    def isCommentEnd(char='',i=''):
        """Check if is the last char that Ends the comment"""
        if char != '/':
            return False
        if  char == '/' and i-1 != 0 and code_[i-1] == '*':
            return True
    print('2222222222222')
    inComment=False
    for char in code_:
        # print(char)
        if inCommentStart(char,i):
            inComment=True
        elif isCommentEnd(char,i):
            inComment=False
        
        if inComment:
            print('IN COMMENT',char)
        elif not found_selector_name_end and char !='{':
            selector+=char
        elif not found_selector_name_end and char == '{':
            styles[selector]={}
            found_selector_name_end=True
        elif char == '{' and found_selector_name_end:    # for animations and selctor with parent selector
            # found_styles=';'.join(style_des_name.split(';')[0:-1])  #returns -->> e.g color: red; display: flex; and takes out h1
            # styles[selector][style_des_name]=found_styles
            #ADD a way to if fallback user those not close with semi-colomun before child selector
            new_selector=style_des_name
            styles[selector][new_selector]={}
            style_des_value=''
            style_des_name=''
            found_a_style_name_end=False
        elif found_selector_name_end and not found_a_style_name_end and char != ':': # added (and each != ':') to move (elif found_a_style_name_start and each == ':':) section after this elif statement:
            style_des_name+=char
            found_a_style_name_start=True   
        elif found_a_style_name_start and char == ':':
            found_a_style_name_end=True
        elif found_a_style_name_end and (char != ';' and char != '}'):
            style_des_value+=char
            found_a_style_value_start=True            
        elif found_a_style_name_end and found_a_style_value_start and (char == ';' or char == '}'):#Added '}' incase last style doesn't have ';', the other vars while be true so it'll enter here
            found_a_style_name_end=False
            if new_selector:    # for animations and selctor with parent selector
                #ADD (maybe a While loop) feature for a recuring loop of sub child selectors
                styles[selector][new_selector][style_des_name]=style_des_value
            else:
                styles[selector][style_des_name]=style_des_value
            style_des_name=''
            style_des_value=''
        if found_selector_name_end and char == '}': 
            # if statement so it can come here if last written style does not have ";" and it's captured by `(char == ';' or (char == '}'))`
            if new_selector:
                new_selector=''
            else:    
                found_selector_name_end=False
                selector=''
            style_des_name=''
            style_des_value=''
        elif (char == '/' and i-1 != 0 and code_[i-1] == '*'):
            # Leaving comment
            style_des_name=style_des_value=''
            found_a_style_name_start=found_a_style_name_end=False                                
        else:
            print('--------------NOT------------')
        i+=1
    print(styles)
    return styles
# stylesToObject(CODE)
# def test():
#     i=0
#     s=1
#     d=0
#     f=1
#     def add():
#         nonlocal i,s,d,f
#         i+=1
#         f+=1
#         d+=1
#         s+=1
#     for a in range(0,10):
#         add()
#     print(i,s,d,f)

test()
runtime=300
def objectToStyle(code:dict):
    style=''
    styles_obj=code
    # i=0
    for selector, value in styles_obj.items():
        value__ = value
        # if type(value) == dict: 
        # print(selector)
        if 'comment' +unique_char_4_space in selector:
            # print(selector)
            print(value)
            style+=f'/* {value} */'
        else:
            style+= selector + '{'
        # while type(value__) == dict and i<runtime:
        # if selector != 'comment' +unique_char_4_space:
            for a_style, value in value__.items():
                # print(a_style, value)
                value__=value
                if type(value) == str:
                    if 'comment' +unique_char_4_space in a_style:
                        style+=f'/* {value} */'
                    else:
                        style+= a_style + ':'+value+';'
                elif type(value) == dict: # it the value is a object then the key is a selector (i.e a_style var is a selector)
                        # style+='}'# incase there are stykes in the parent style before the child selector
                    style+=a_style+'{'
                    for sty, val in value__.items():
                        style+=sty+':'+val+';'
                    style+='}'
            style+='}'
            # i+=1
    writeInFile(style)
    return style
# objectToStyle(stylesToObject(CODE))


def formatNicely(code, strip=True):
    """Also removes empty selectors :) just a feature code runs 100% without it"""
    new_str=code
    if strip:
        new_str=myStrip(code)
    str_=''
    lenght_of_str = len(new_str)
    i=0
    for char in new_str:
        if (char == '*' and i+1 != lenght_of_str and new_str[i+1] == '/') or (char == '/' and i-1 != 0 and new_str[i-1] == '*'):# this identifies comments ending
            if char == '/':
                str_+=char+'\n\t'
                # in_comment =False
            else:
                str_+=char
                # in_comment=True
        elif char=='}':
            if i>2 and new_str[i-1]=='/' and new_str[i-2] =='*':    # checking if last written last closed comment
                # print(str_[-2])
                str_=str_[0:-2] +'\n'+char+'\n'
                # print(999)
                # str_+=char+'\n'
            else:
                str_+='\n'+char+'\n'
        elif str_ and any(str_[-1] == i for i in ['{',';']): #if last char before this was ; or }
            
            str_+='\n\t'+char
        else:
            str_+=char
        i+=1
    # print(amount_of_open_braces,amount_of_closed_braces)
    writeInFile(str_)#[1:-1]
# formatNicely(objectToStyle(stylesToObject(CODE)),strip=0)
