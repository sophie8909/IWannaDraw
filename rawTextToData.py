
import json
import re
import os
from filefunct import *
# 整理所有檔案（txt, json）
def redealFile(folderPath):
	filepattern = r'(^[0-9]+)\.(json)|(txt)$'
	for f in os.listdir( folderPath):
		if re.match( filepattern, f):
			bulidJson(f)

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
	# print( "{}好了！！！！！！！".format(jsonFilePath))
	return {"TYPE": typestr, "PUBLISHER":publisher, "UPLOADTIME": uploadtime,"CONTENT":text}

def bulidJson(path):
	index = getIndexInFolder("./rawData")
	if path.endswith(".txt"):
		jsonDICT = dealrawTxt(path)
		jsonFileWriter( jsonDICT, "./rawData/{}.json".format(index))
	elif path.endswith(".json"):
		jsonDICT = dealrawJson(path)
		# print(jsonDICT)
		jsonFileWriter( jsonDICT, path)
	return

def cutJsonLIST(jsonFilePath):
	with open(jsonFilePath, encoding = "utf-8") as f :
		jsonLIST = f.read()
	jsonLIST = json.loads(jsonLIST)
	index = getIndexInFolder("./rawData")
	for jsonDICT in jsonLIST:
		jsonFileWriter( jsonDICT, "./rawData/{}.json".format(index))
		index += 1
	return

if __name__ == '__main__':
	
	# redealFile("./rawData")
	# while True:
	# 	path = input("filepath:\n(輸入 exit()結束)\n")
	# 	if path == "exit()":
	# 		break
	# 	bulidJson(path)

	# 將爬蟲出來的新檔案切成原本的樣子
	cutJsonLIST( "./new_rawData.json")




