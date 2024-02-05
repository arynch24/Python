dict={"key1":31,"key2":"aryan","key3":True}
print(type(dict))

print(dict['key1'])

d2 = {'name' : "sudhanshu" , "mo_no" :3454354353 , "mail_id" :"sudhanshu@xyz.com",'key1':[4,5,6,7] , "key2" :(3,4,5,6),"key3" : {3,4,5,4,3,3,3,3,3,3,3},'key4':{1:5,4:6}}
print(type(d2['key3']))


print(d2.keys())
print(d2.values())

print(d2['key4'][4])

#addind key and value
d2[(1,2,3)] = "ineuron"

print(d2)
