def selectionSort(anArray):
    for x in range(len(anArray) - 1):
        minIndex = x
        for i in range(x+1, len(anArray)):
            if anArray[i]["title"].lower() < anArray[minIndex]["title"].lower():
                minIndex = i
        anArray[x], anArray[minIndex] = anArray[minIndex], anArray[x]