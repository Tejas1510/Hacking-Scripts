from urllib import request

file_url = r'#put the url the of the here'

def download_file(url):
    fileOpen = request.urlopen(url) #open the url file
    fileInfo = fileOpen.read()  #read the file
    fileInfoStr = str(fileInfo) #convert into string
    fileLines = fileInfoStr.split('\\n')    #split the lines into the file

    newfile = open('file.txt',"w")  #creating a new file to store information
    for info in fileLines:  #store all information of the file we have read
        newfile.write(info + '\n')
    
    newfile.close() #close the file

download_file(file_url)

