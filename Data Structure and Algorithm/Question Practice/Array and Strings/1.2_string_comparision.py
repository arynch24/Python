s1=input()
s2=input()

s1=''.join(sorted(s1))
s2=''.join(sorted(s2))

if(s1==s2):
    print("permutation")
else:
    print("no permutation")