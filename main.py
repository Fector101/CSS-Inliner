# ADD ability to remove empty selectors (style_section)

unique_char_4_space="defiohf;qebio;gofhwe9-fpweffopefo"
with open('input/small.css', mode='r') as data:
    file_code=data.read()
    CODE=file_code
    # print(CODE.count('\n'))
  
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

def removeWhiteSpaces():
    no_comments=removeComments(CODE)    # Doesn't make sense to have comments when no whitespaces it won't be visible
    #ADD Function to remove empty selectors (style_section)
    no_whitespaces=myStrip(no_comments)

    with open('ouput/without_whitespace/style.css','w')as file:
        file.write(no_whitespaces)

# removeWhiteSpaces()
def stylesToObject(code:str):
    """Works when comments are removed withy myStrip
    and semi-column added when a selector has another selector within
    """
    code_=myStrip(code)
    code_=removeComments(code_)
    
    list_of_selectors=[]
    styles={}
    found_selector_end=False # found end of selector e.g "hr","h1","div", ".class-name","#id"
    found_a_style_name_start=False
    found_a_style_name_end=False # i.e ":"
    selector=''
    style_des_name='' #'background-color'
    style_des_value='' #'#FF0AAA'
    new_selector=''
    found_a_style_value_start=False
    # found_a_style_value_end=False # i.e ";" or '}'
    found_animation=False
    # current_selecto
    # def start4newSelector():
    #     global found_end,style_des_name, style_des_value,selector
    #     found_end=False
    #     style_des_name=''
    #     style_des_value=''
    #     selector=''
    all=''
    for char in code_:
        # print(found_end,found_a_style_name_end,found_a_style_name_start,found_a_style_value_start)
        # if found_end == True and char == '{':
          #  ...
        # print(char)
        if found_selector_end == False and char !='{':
            selector+=char
            # print(111)
        elif found_selector_end == False and char == '{':
            styles[selector]={}
            found_selector_end=True
            # print(222)
        elif char == '{' and found_selector_end == True:    # for animations and selctor with parent selector
            # """
            #     e.g this will get the new selector 'h1 when it spilts
            #     "color: red; display: flex; h1".split(';')
            #     div{
            #         color: red;
            #         display:flex;
            #         h1{
            #             text-algin:center;
            #         }
            #     }
            # """
            # print(style_des_name)
            found_styles=';'.join(style_des_name.split(';')[0:-1])  #returns -->> e.g color: red; display: flex; and takes out h1
            styles[selector][style_des_name]=found_styles
            new_selector=style_des_name.split(';')[-1].lstrip()
            # print(new_selector,'---',style_des_value.split(';'))
            style_des_value=''
            style_des_name=''
            found_a_style_name_end=False
            styles[selector][new_selector]={}

        elif found_selector_end == True and found_a_style_name_end == False and char != ':': # added (and each != ':') to move (elif found_a_style_name_start and each == ':':) section after this elif statement:
            style_des_name+=char
            found_a_style_name_start=True
            # print(333)
        elif found_a_style_name_start and char == ':':
            found_a_style_name_end=True
        elif found_a_style_name_end and char != ';' and char != '}':
            style_des_value+=char
            found_a_style_value_start=True
            # print(555)
        elif found_a_style_name_end and found_a_style_value_start and (char == ';' or char == '}'):
            # print(666)
            found_a_style_name_end=False
            # print('test')
            # print(new_selector,'||',style_des_name,'||',style_des_value)
            if new_selector:
                styles[selector][new_selector][style_des_name]=style_des_value
            else:
                styles[selector][style_des_name]=style_des_value
            style_des_name=''
            style_des_value=''
        
        if found_selector_end and char == '}' : # if statement so it can come here if last written style does not have ";" and it's captured by `(char == ';' or (char == '}'))`
            if 0==1:#'{' in style_des_value and (style_des_value.count('{') != style_des_value.count('}')):  # for animations and selctor with parent selector
                pass
            else:
                if new_selector:
                    new_selector=''
                else:    
                    found_selector_end=False
                    selector=''
                style_des_name=''
                style_des_value=''
    return styles
    # writeInFile(str(styles))
    # print(styles)
    # for each in styles:
    #     print(each)
    #     list_of_selectors.append(each)
    # print(list_of_selectors)
    # list_of_styles=[]
    # for each in styles.values():
    #     list_of_styles.append(each)
    # print(list_of_styles)
# stylesToObject(CODE)
runtime=300
def removeEmptySelectors(code:str):
    style=''
    # def extract(str_or_obj):
    #     value=''
    #     type()
    #     # for key, value in styles_obj.items():

    #     return value
    styles_obj=stylesToObject(code)
    # print(styles_obj)
    # return
    i=0
    for selector, value in styles_obj.items():
        style+= selector + '{'
        value__ = value
        if type(value) == dict:  
            # while type(value__) == dict and i<runtime:
            for a_style, value in value__.items():
                # print(a_style, value)
                value__=value
                if type(value) == str:
                    style+= a_style + ':'+value+';'
                elif type(value) == dict: # it the value is a object then the key is a selector (i.e a_style var is a selector)
                        # style+='}'# incase there are stykes in the parent style before the child selector
                    style+=a_style+'{'
                    for sty, val in value__.items():
                        style+=sty+':'+val+';'
                    style+='}'
            style+='}'
            # i+=1

            # style+=

        # style+='}'
    writeInFile(style)
    #     # style+=key+{
    #     print(key,'||',value)
        
    #     for e,e1 in value.items():
    #         print(e,'--',e1)
    #         for e,e1 in e1.items():
    #             print(e,'--',e1)

removeEmptySelectors(CODE)
# print(';'.join("color: red; display: flex; h1".split(';')[0:-1]))
# print(';'.join("color: red display: flex h1".split(';')[0:-1]))

# d={'rr':'aa','gg':'bb','ff':'cc'}
# print('\n')
# for e in d.values():
#     print(e)
# p='o'
# print(p!=';' and p!='{')
def formatNicely(code):
    """Also removes empty empty selectors :) just a feature code runs 100% without it"""
    # new_str=CODE.replace('\n','').replace(';',';\n').replace('}','}\n')
    # writeInFile(removeComments(new_str))
    new_str=myStrip(code)
    # new_str=CODE.replace('{','{\r')#
    str_=''
    lenght_of_str = len(new_str)
    i=0
    for char in new_str:
        if (char == '*' and i+1 != lenght_of_str and new_str[i+1] == '/') or (char == '/' and i-1 != 0 and new_str[i-1] == '*'):
            if char == '/':
                str_+=char+'\n\t'
            else:
                str_+=char
        elif char=='}':
            # print(len(new_str))
            if i>2 and new_str[i-1]=='/' and new_str[i-2] =='*':
                # print(str_[-2])
                str_=str_[0:-2] +'\n'+char+'\n'
                # print(999)
                # str_+=char+'\n'
            else:
                str_+='\n'+char+'\n'
        elif str_ and any(str_[-1] == i for i in ['{',';']):
            str_+='\n\t'+char
            # print(str_)
        else:
            str_+=char
        i+=1
    # new_str=str_.replace('}','}\n').replace('{','{\n').replace('*/','*/\n').replace(';',';\n')#.replace(';',';\n')
    # new_str=str_#.replace('}','}\n')#.replace(';',';\n')#.replace(';',';\n')
    # new_str=str_.replace('}','}\n').replace('{','{\n')#.replace(';',';\n')#.replace(';',';\n')

    writeInFile(str_)#[1:-1]

# formatNicely(CODE)
# print('poph'[0:-1])
#  if found_end and char == '}' : # if statement so it can come here if last written style does not have ";" and it's captured by `(char == ';' or (char == '}'))`
#             # if statment so current selector and values don't eraser if it's an animations or selctor with parent selector
#             # print(found_end)
#             if char=='}'and'{' in style_des_value and (style_des_value.count('{') != style_des_value.count('}')):  # for animations and selctor with parent selector
#                 # print(33,style_des_value)
#                 all+=char
#                 #(style_des_value.count('{') != style_des_value.count('}')) checks if done with the child selectors
#                 style_des_value+='}'
#                 # found_animation=True
#                 pass
#             elif char=='}' and '{' in style_des_value and (style_des_value.count('{') == style_des_value.count('}')):  # for animations and selctor with parent selector
#                 print(888)
#                 styles[selector][style_des_name]=style_des_value
#                 start4newSelector()
#             else:
#                 start4newSelector()