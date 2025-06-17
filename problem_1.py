paragraph = [
    ["Hello", "world", "hello"],
    ["this", "is", "a", "test"],
    ["STOP", "ignore", "this", "line"],
    ["should", "not", "be", "processed"]
]
d1=dict()
count=1

stop_flag = False
for i in range(0,len(paragraph)):
    for j in range(0,len(paragraph[i])):
        word=paragraph[i][j].lower()
        if word=="stop":
            stop_flag = True
            break
        elif len(word)<3:
            continue
        else:
            if word not in d1:
                d1[word]=count
            else:
                d1[word]=count+1
    if stop_flag:
        break
                
print(d1)