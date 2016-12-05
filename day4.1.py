import re
import collections

idsum = 0

def alphacount(first):
    letters = collections.Counter(first)
    llist = list(letters)
    print(letters)



def addup(number):
    global idsum
    int(number)
    idsum = idsum + number

with open('room2.txt') as rawinfo:
    for line in rawinfo:
        number = re.sub('[^0-9]','', line)
#        print(number)
        checksum = [item.strip() for item in line.split('[')]
        checksum[1] = re.sub('[^a-zA-Z]+', '', checksum[1])
        checksum[0] = re.sub('[^a-zA-Z]+', '', checksum[0])
#        print(checksum[0])
#        print(checksum[1])
        alphacount(checksum[0])
