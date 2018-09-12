import re

re_email=re.compile(r'^([<>\w\s]+)@([\w]+).org$')

def is_valid_email(addr):
    return re_email.match(addr)

def name_of_email(addr):
    result=re_email.match(addr).group(1)
    result=re.split(r'[<>]',result)
    if result[0]:
        return result[0]
    else:
        return result[1]
    


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')