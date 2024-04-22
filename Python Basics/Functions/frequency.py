
# for i in range(0,26):
#     c = ord('a')+i
#     count=0

# for j in s:
#     if(ord(j)==c):
#         count+=1
# print(count)

        
def countoccurence(s,c):
    count=0
    for j in s:
        if(ord(j)==c):
            count+=1
    return count



s="abcdabcdaacbdd"
for i in range(0,26):
    print(countoccurence(s,ord('a')+i))
     