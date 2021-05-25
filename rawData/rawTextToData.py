
import json
import re
import os

# 取得當前最新檔案的 index
def getIndexInFolder(folderPath):
	filepattern = r'(^[0-9]+)\.json'
	index = -1
	for f in os.listdir( folderPath):
		tem = re.match( filepattern, f)	
		if tem != None :
			index = max(int(tem.group(1)),index)
	return index+1

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

def txtReader(txtFilePath):
	with open(txtFilePath, encoding = "utf-8") as f :
		returnTXT = f.read()
	return returnTXT	

# 讀取 json
def json2DictReader(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		returnDICT = f.read()
	returnDICT = json.loads(returnDICT)
	return returnDICT
	'''
	設計一個把 .json 檔開啟成 DICT 的函式
	'''


def isTxtFile(txtFilePath):
	text = txtReader(txtFilePath)
	op = input("是否為抽講文？\n\t0. 否\n\t1. 是\n")
	typestr = "OTHER"
	if op == 1:
		typestr = "DRAW"
	return {"TYPE": typestr,"CONTENT":text}

if __name__ == '__main__':
	index = getIndexInFolder("./")
	# print(index)
	path = "./input.json"
	inputSTR = txtReader(path)
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"\}\,\{", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i-1] + '\n' + inputSTR[i+1:]
	print(inputSTR)
	'''	
	# while True:
		# op = input("檔案類型：\n\t0. txt\n\t1. json\n")
		# path = input("檔案路徑:\n")
		jsonDICT = dict()
		# if op == 0:
		jsonDICT = isTxtFile(path)
		# else:
		# 	jsonDICT = isJsonFile(path)
		jsonFileWriter( jsonDICT, "./{}.json".format(index))
		index += 1
	# '''
	# for jsonDICT in jsonLIST:
	# 	jsonFileWriter( jsonDICT, "./{}.json".format(index))
	# 	index += 1






