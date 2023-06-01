

bookInfoFilePath ='.\\files\\Book_Info.txt'

def searchTitle(title):
    
    # title.lower()
    with open(bookInfoFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines:
            # line.lower()
            # check if string present on a current line
            if line.find(title) != -1:
                print( line)
                status = 1
                # break
        if status == 0: 
           print('No Results Found')
    
def searchID(ID):
    
    # title.lower()
    with open(bookInfoFilePath, 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        status = 0
        for line in lines:
            # line.lower()
            # check if string present on a current line
            line = line[0:14]
            if line.find(ID) != -1:
                # print(id, 'string exists in file')
                # print('Line Number:', lines.index(line))
                # print('Line:', line)
                status = 1
                break

    return status


