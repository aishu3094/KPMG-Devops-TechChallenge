def getNestedKey(nestedDict, keys):
    if keys and nestedDict:
        element=keys[0]
        print('Element is ',element)
        if element:
            value=nestedDict.get(element)
            print('Value is ', value)
            return value if len(keys)==1 else getNestedKey(value,keys[1:])

nestedDict={'x':{'y':{'z':'a'}}}
ky='x/y/z'
t1=getNestedKey(nestedDict,ky.split('/'))
print("Final Output is: ", t1)
nestedDict1={'a':{'b':{'c':'d'}}}
ky1='a/b/c'
t2=getNestedKey(nestedDict1,ky1.split('/'))
print("Final Output is: ", t2)
