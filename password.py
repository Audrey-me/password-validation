""" password validation

. input as string
. minimum of 2 numbers
. contains 2 or more special character
. minimum length is 7

"""
pass_word =input('enter your password')
special_count=0
num_count=0
num=['0','1','2','3','4','5','6','7','8','9']
special=['!','@','#','$','%','&','*']
for i in pass_word:
    if i in num:
       num_count +=1
    elif i in special:
        special_count +=1
if len(pass_word)>=7 and num_count>=2 and special_count>=2:
    print('strong')
    print('valid password')
else:
    print('weak')
    print('invalid password')