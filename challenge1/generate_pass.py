pass_john = open('password.lst','r')
pass_my = open('passlist.txt','w')
count = 0
index = 0
last = ''
for line in pass_john:
    index += 1
    if index%10 == 0 and count < 300:
        print 'index is %d\n' % index
        pair = line.strip()
        count += 1
        if count<=20:
            pair = pair+ ' '+line
        if count>20 and count<=75:
            pair = pair +' '+'Winter14\n'
        if count>75 and count<=110:
            pair = pair +' '+pair+'Acme2016\n'
        if count>110 and count<=130:
            pair = pair+' '+pair+'Acme!\n'
        if count>130 and count<=150:
            pair = pair+' '+pair+':Acme\n'
        if count>150 and count<=205:
            pair = pair+' '+last
        if count>205 and count<=250:
            pair = pair+' '+pair+'Bank!\n'
        if count>250 and count<=270:     
            pair = pair +' '+pair+'Bank2016\n'
        if count>270 and count<=280:
            pair = pair +' \n'
        if count>280 and count<=298:
            pair = pair+' '+'Password\n'
        if count == 299:
            pair = pair+' '+'letmeinAcme\n'
        if count == 300:
            pair = pair+' '+'secret:Acme\n'
        pass_my.write(pair)
        last = line 
    elif count >= 300:
        break
print 'index is %d' % index
print count
pass_john.close()
pass_my.close()
