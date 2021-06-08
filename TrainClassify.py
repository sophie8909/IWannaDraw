import os
from filefunct import *
from nlppre import *
from classifyFunct import *
def main(folderPath: str):
	filepattern = r'(^[0-9]+)\.(json)$'
	
	for f in os.listdir(folderPath):
		if re.match(filepattern, f):
			filePath = folderPath+'/'+f
			print(filePath)
			jsonDICT = json2DictReader(filePath)
			# print( jsonDICT)
			# 初步判斷是否可能為抽獎文
			wordList = articut2cleanWordList(jsonDICT["WORDS"])
			# print(wordList)
			if classify_lv1( wordList) == True:
				jsonDICT["CLF1"] = "DRAW"
			else:
				jsonDICT["CLF1"] = "OTHER"
			jsonFileWriter( jsonDICT, filePath, "CLF1")
	return 			


if __name__ == '__main__':
	main("./rawData")

	