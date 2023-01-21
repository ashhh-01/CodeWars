def change(text):
    #The first letter of each word is placed in the end and "ay" is added.
    splitText=text.split(" ")
    new=""
    for i in splitText:
        word=i[1:]+i[0]+"ay"
        new=new+word+" "
    return new

print(change("I am coding"))

## Output: "Iay maay odingcay"