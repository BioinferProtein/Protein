import csv

def readFile(filename):
    lines= csv.reader(open(filename,'r',newline =''))
    dataset =list(lines)
    #dataset.remove('')
    addData = []
    tempData=''
    for i in range(len(dataset)):
        if(str(dataset[i]).startswith('[\'>')):
            addData.append(tempData)
            tempData=''
            continue
        tempData = tempData+(str(dataset[i])[2:-2])
    addData.append(tempData)
    addData.remove('')
    for i in range(len(addData)):
        print(addData[i])
    return dataset
    
def main():
    filename = "D:/dataset/test.txt"
    readFile(filename)
    
main()