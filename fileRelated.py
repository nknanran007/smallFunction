import os

def getFiles(Path):
	ignoreFile = open("ignoreFile.txt","w")
	tmpStr = ""
	files = os.listdir(Path)
	for file in files:
		tmpStr += "%s\n"%file
	ignoreFile.writelines(tmpStr[:-1])

if __name__ == '__main__':
	getFiles('./')
