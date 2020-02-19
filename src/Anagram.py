import math
def anagram(s) :
    ## Test if the string can be divided evenly
    if(len(s)%2 == 0):
        mid = math.ceil(len(s)/2)
        left = s[0:mid]
        right = s[mid: len(s)]
        count = 0
        for l in left :
            if l in right:
                right =right.replace(l,'',1)
            else :
                count += 1
        return count
    else:
        return -1

if __name__ == '__main__':
    test = 'fdhlvosfpafhalll'
    print(anagram(test))