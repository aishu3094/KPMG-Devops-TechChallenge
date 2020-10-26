def getNestedKey(nestedDict, keys):
    if keys and nestedDict:
        element=keys[0]
        print('element is ',element)
        if element:
            value=nestedDict.get(element)
            print('value is ', value)
            return value if len(keys)==1 else getNestedKey(value,keys[1:])

nestedDict={'x':{'y':{'z':'a'}}}
ky='x/y/z'
t1=getNestedKey(nestedDict,ky.split('/'))
print("output is: ", t1)

