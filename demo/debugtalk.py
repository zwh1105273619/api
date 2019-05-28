




def parser_cookie(cookie):
    return cookie.get('JSESSIONID',None)







def add(a,b):
    return int(a)+int(b)





def create_account(number):
    accounts=[]
    for index in range(1,number):
        accounts.append({'username':str(800001+index),'password':str(800001+index)})
    return accounts