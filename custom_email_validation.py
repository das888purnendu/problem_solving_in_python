''' Custom email validation =>
A valid email address meets the following criteria:

    It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
    The username starts with an English alphabetical character, and any subsequent characters consist of one or more
    of the following: alphanumeric characters, -,., and _.
    The domain and extension contain only English alphabetical characters. '''


for _ in range(int(input())):
    a=input().split()
    name=a[0]
    mail=a[1][1:len(a[1])-1]

    pass_char=[".","-","_"]
    st=False
    if(mail.find("@")!=-1 and mail[0].isalpha()):
        temp_name=mail[0:mail.find("@")]
        if (temp_name.lower().find(name.lower())!=-1):
            st=True

            for i in temp_name:
                if(i.isalnum() or i in pass_char):
                    st=True
                else:
                    st=False
                    break

            if(st):
                domain = mail[(mail.find("@"))+1:]
                domain_name = domain[:domain.find(".")]
                if(domain_name.isalpha()):
                    st=True
                else:
                    st=False
                    
                    
                if(st):
                    extn = domain[len(domain_name)+1:]
                    if(extn.isalpha() and (1<=len(extn)<=3)):
                        st=True
                    else:
                        st=False
        if(st):
            print("{} <{}>".format(name,mail))
            
            
            
            
            
# input = anku <anku_123@gmail.com.com>
# output = anku <anku_123@gmail.com.com>

# input = anku <1anku@anku.com>
# output =""
