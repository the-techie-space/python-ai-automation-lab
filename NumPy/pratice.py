str = "aabbbcccaadd"

frequency = []
oldCount = ""

for value in str:
    oldCount += value
    if oldCount == value:
        continue
    else:
        frequency.append(oldCount)


  

    


print(frequency)
