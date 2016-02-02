f = open('passlist.txt','r')
total = 0
less_8 = 0
same = 0
contain = 0
winter = 0
blank = 0
col = 0
letmein = 0
good = 0

for line in f:
    total += 1
    user = line.split(' ')[0]
    passwd = line.split(' ')[1].strip()
    if len(passwd) == 0:
        blank += 1
    if len(passwd)<8 and len(passwd)>0:
        less_8 += 1
    if passwd == user:
        same += 1
    if passwd == 'Winter14':
        winter +=1
    if passwd.find('Acme') >= 0:
        contain +=1
    if passwd.find(':') >=0:
        col += 1
    if passwd == 'letmeinAcme':
        letmein += 1
    if len(passwd) >= 8:
        for i in passwd:
            if not ((i>='a' and i<='z') or (i<='Z' and i>='A')):
                good += 1
                break
            
print "the number of passwords is: %d" % total
print "the number of passwords whose length less than 8 is: %d" % less_8
print "the number of blank passwords is: %d" % blank
print "the number of passwords that are same as username is: %d" % same
print "the number of passwords that are 'Winter14' is: %d" % winter
print "the number of passwords that are 'letmeinAcme' is: %d" % letmein
print "the number of passwords that contain 'Acme' is: %d" % contain
print "the number of passwords that contain ':' is: %d" % col
print "the number of good passwords is: %d" % good 
