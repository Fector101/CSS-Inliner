unique_char_4_space="defiohf;qebio;gofhwe9-fpweffopefo"
with open('input/main.css', mode='r') as data:
    file_code=data.read()
    CODE=file_code
    # list_of_group_styles=file_code.replace('\n','').split('}')
    # print(list_of_group_styles)
# for each in list_of_group_styles:
#     print('pp'+each+'}','\n')
# import string
def removeAllFromList(input:str,list_:list):
    if input == '' or input == unique_char_4_space:
        return ''
    output=unique_char_4_space
    for each in list_:
        # output = unique_char_4_space 
        if(output==unique_char_4_space):
            output=input.replace(each,'')
        else:
            output=output.replace(each,'')
    return output

def removeWhiteSpaces():
    remove_whitespaces=CODE.replace('\n','')#.replace('\n','')
    # print(remove_whitespaces+'ppp')
    with open('ouput/without_whitespace/style.css',mode='w')as file:
        file.write('')
    list_of_styles=[]
    # print(remove_whitespaces)
    for style_section in remove_whitespaces.split('}')[0:-1]:
        print(style_section)
        if style_section.replace(' ',unique_char_4_space) != unique_char_4_space:
            if '/*' in style_section:
                # print('|||',style_section)
                new_str=''
                found_comment_end=True
                # if style_section.count('/*') != style_section.count('*/'): #Checking if commented correctly
                #     print('Comments not formatted correctly')
                #     return
                i = 0
                for char in style_section:
                    if char == '/' and i+1 != len(style_section) and style_section[i+1] == '*':
                        found_comment_end = False
                    elif (char == '*' and i+1 != len(style_section) and style_section[i+1] == '/') or (char == '/' and i-1 != 0 and style_section[i-1] == '*'):
                        found_comment_end=True
                    elif found_comment_end:
                        new_str+=char
                    i+=1
                style_section=new_str
            # print(style_section)
            # else:
            formatted=style_section
            if formatted !='':
                formatted=formatted+'}'
            formatted=removeAllFromList(formatted,[''])
            list_of_styles.append(formatted)
    # print(list_of_styles)
    for style_section in list_of_styles:
        with open('ouput/without_whitespace/style.css',mode='a')as file:
            file.write(style_section)

removeWhiteSpaces()
# print('ss'.)
# print(40%2)
# for each in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16][0:-1:2]:
#     print(each)
# print('pw/*pwk/*')