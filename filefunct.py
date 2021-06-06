import json
import os
import re
# addkey 可選，表達增加哪些欄位到原本的檔案
def jsonFileWriter(jsonDICT, jsonFileName, addKey = ""):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	print( "\"{}\" has written".format(jsonFileName) + (" with {}".format(addKey) if addKey != "" else ""))
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

# 取得當前最新檔案的 index
def getIndexInFolder(folderPath):
	filepattern = r'(^[0-9]+)\.json'
	index = -1
	for f in os.listdir( folderPath):
		tem = re.match( filepattern, f)	
		if tem != None :
			index = max(int(tem.group(1)),index)
	return index+1