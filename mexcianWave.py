def wave(people):
    if len(people)<1:
        return []
    else:
        names=[]
        for e,i in enumerate(people):
            if i==" ":
                continue
            else:
                names.append(people[:e]+people[e].upper()+people[e+1:])
        return names

print(wave("i am coding"))
#['I am coding', 'i Am coding', 'i aM coding', 'i am Coding', 'i am cOding', 'i am coDing', 'i am codIng', 'i am codiNg', 'i am codinG']
