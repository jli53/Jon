import smbpasswd
pass_john = open('password.lst','r')
pass_my = open('dumppass.txt','w')
count = 0
index = 0
last = ''
passwd = ''
pair = ''
for line in pass_john:
    index += 1
    if index%10 == 0 and count < 300:
        print 'index is %d\n' % index
        name = line.strip()
        count += 1
        if count<=20:
            passwd = name 
        if count>20 and count<=75:
            passwd = 'Winter14'
        if count>75 and count<=110:
            passwd = name+'Acme2016'
        if count>110 and count<=130:
            passwd = name+'Acme!'
        if count>130 and count<=150:
            passwd = name+':Acme'
        if count>150 and count<=205:
            passwd = last
        if count>205 and count<=250:
            passwd = name+'Bank!'
        if count>250 and count<=270:     
            passwd = name+'Bank2016\n'
        if count>270 and count<=280:
            passwd = '' 
        if count>280 and count<=298:
            passwd = 'Password'
        if count == 299:
            passwd = 'letmeinAcme'
        if count == 300:
            passwd = 'secret:Acme'
        pair = name + "::" + smbpasswd.lmhash(passwd)+":"+smbpasswd.nthash(passwd)+":::\n" 
        pass_my.write(pair)
        last = name 
    elif count >= 300:
        break
print 'index is %d' % index
print count
pass_john.close()
pass_my.close()
