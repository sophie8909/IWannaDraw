import os
from filefunct import *
from nlppre import *

# 確認是否提及抽獎，使用關鍵字字典確認
def classify_lv1(wordLIST, keywordLIST) -> bool: 
	for i in keywordLIST:
		for word in wordLIST:
			if i in word:
				return True
	return False
def main(folderPath: str):
	filepattern = r'(^[0-9]+)\.(json)$'
	#  這邊的 keyword 必須讓所有抽獎文都過 lv1，但可能會混入其他東西
	keywordLIST = json2DictReader("drawKeyword.json")["CONTENT"]
	for f in os.listdir(folderPath):
		if re.match(filepattern, f):
			filePath = folderPath+'/'+f
			print(filePath)
			jsonDICT = json2DictReader(filePath)
			# print( jsonDICT)
			# 初步判斷是否可能為抽獎文
			if classify_lv1( jsonDICT["WORDS"], keywordLIST) == True:
				jsonDICT["CLF1"] = "DRAW"
			else:
				jsonDICT["CLF1"] = "OTHER"
			jsonFileWriter( jsonDICT, filePath, "CLF1")
	return 			


if __name__ == '__main__':
	main("./rawData")

	