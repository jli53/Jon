import sys
from subprocess import call

def most_common(count,dic):#count is the number of passwords that you want to retur, dic is the dictionary used for saving all passwords and the number it appears
    sorted_list = sorted(dic, key=dic.get, reverse = True)[0:3]
    print 'top %d most common cracked passwords' % count
    print '-------------------------------------------------------------------------'
    for x in sorted_list:
        print '%s|%d times' %(x, dic[x])
        
def meet_require(name, passwd):
    if len(passwd)<8 or passwd.find(name)>=0: #check length and if contains username
        return 0

    low = up = num = other = False #check if it has 3 of 4 of: low, up ,number, special char
    for x in passwd:
        if x >= 'a' and x <= 'z':
            low = True
        elif x >= 'A' and x<= 'Z':
            up = True
        elif x >= '0' and x<='9':
            num = True
        else:
            other = True
        if (low and up and num or other) or (low and up and other or num) or (low and num and other or up) or (up and num and other or low):
            return 1
    return 0 

blank = 0
same = 0
similar = 0
fail_complexity = 0

if len(sys.argv)!=2:
    print 'usage: '+sys.argv[0]+' passwd_file'
    exit(0)

f1 = open('john_result_lm','w+')
f2 = open('john_result_nt','w+')

call(['john','-show',sys.argv[1],'--format=lm'],stdout=f1)
call(['john','-show',sys.argv[1],'--format=nt'],stdout=f2)

f1.close()
f2.close()

try:
    f1 = open('john_result_lm','r')
except IOError as e:
    print 'the lm result file does not exsit!'
    exit(0)

try:
    f2 = open('john_result_nt','r')
except IOError as e:
    print 'the nt result file does not exsit!'
    exit(0)

for line in f1:
    pass
split = line.split(' ')
total = int(split[0]) + int(split[-2])
cracked = int(split[0])
print '*************************************************************************'
print 'overview'
print '-------------------------------------------------------------------------'
print '%d/%d lm hashes cracked' %(cracked,total)

dic = {}

for line in f2:
    if line.find(':') < 0:
        split = line.split(' ')
	if len(split) < 3:
		continue
        total = int(split[0]) + int(split[-2])
        cracked = int(split[0])
        print '-------------------------------------------------------------------------'
        print '%d/%d nt hashes cracked' %(cracked, total)
        print '*************************************************************************'
        continue
    split = line.strip().split(':')
    name = split[0] # get username
    passwd = split[1] # get passwords, considering passwords may contain ':' character
    for x in split[2:-6]:
        passwd = passwd + ':' + x 

    if dic.has_key(passwd): #record the number of same passwords
        dic[passwd] += 1
    else:
        dic.update({passwd:1}) 

    if len(passwd) == 0: #check if blank
        blank += 1
    if passwd == name: #check if same as username
        same += 1
    #elif passwd.upper() == name.upper(): #check if similar to username
    #    similar += 1    
    if meet_require(name, passwd) == 0:
        fail_complexity += 1

f1.close()
f2.close()

most_common(3,dic)
print '*************************************************************************'
print 'more detailed information about cracked passwords'
print '-------------------------------------------------------------------------'
print 'passwords that are blank: %d' % blank
print 'passwords that are same as username: %d' % same
#print 'passwords that are different from username, only in the case of alphabets: %d' % similar
print 'passwords that failed complexity requirements: %d' % fail_complexity
print '*************************************************************************'
