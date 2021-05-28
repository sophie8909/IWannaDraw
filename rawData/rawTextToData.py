
import json
import re
import os

# 整理所有檔案（txt, json）
def redealFile(folderPath):
	filepattern = r'(^[0-9]+)\.(json)|(txt)$'
	for f in os.listdir( folderPath):
		if re.match( filepattern, f):
			bulidJson(f)

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

# 處理完全未處理過的 txt
def dealrawTxt(txtFilePath):
	text = txtReader(txtFilePath)
	op = input("是否為抽獎文？\n\t0. 否\n\t1. 是\n2. 不人工分類\n")
	typestr = "OTHER"
	if op == 1:
		typestr = "DRAW"
	cutIndex = text.find("\n")
	publisher = text[:cutIndex]
	text = text[cutIndex+1:]
	cutIndex = text.find("  · \n")
	uploadtime = text[:cutIndex]
	cutIndex = text.find("\n")
	text = text[cutIndex+1:]
	return {"TYPE": typestr, "PUBLISHER":publisher, "UPLOADTIME": uploadtime,"CONTENT":text}

# 完整半處理的 json
def dealrawJson(jsonFilePath):
	jsonDICT = json2DictReader(jsonFilePath)
	typestr = jsonDICT["TYPE"]
	text = jsonDICT["CONTENT"]
	if "PUBLISHER" not in jsonDICT:
		cutIndex = text.find("\n")
		publisher = text[:cutIndex]
		text = text[cutIndex+1:]
	else:
		publisher = jsonDICT["PUBLISHER"]

	if "UPLOADTIME" not in jsonDICT:
		cutIndex = text.find("  · \n")
		uploadtime = text[:cutIndex]
		cutIndex = text.find("\n")
		text = text[cutIndex+1:]
	else:
		uploadtime = jsonDICT["UPLOADTIME"]
	print( "{}好了！！！！！！！".format(jsonFilePath))
	return {"TYPE": typestr, "PUBLISHER":publisher, "UPLOADTIME": uploadtime,"CONTENT":text}

def bulidJson(path):
	index = getIndexInFolder("./")
	if path.endswith(".txt"):
		jsonDICT = dealrawTxt(path)
		jsonFileWriter( jsonDICT, "./{}.json".format(index))
	elif path.endswith(".json"):
		jsonDICT = dealrawJson(path)
		# print(jsonDICT)
		jsonFileWriter( jsonDICT, path)
	return

if __name__ == '__main__':
	

	# redealFile("./")
	while True:
		path = input("filepath:\n(輸入 exit()結束)\n")
		if path == "exit()":
			break
		bulidJson(path)
	






