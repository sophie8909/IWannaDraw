import json
import ArticutAPI
from pprint import pprint
from filefunct import *
from rawTextToData import *
from TrainClassify import *



def articutLogIn(inforpath):
	userDICT = json2DictReader(inforpath)
	username = userDICT["username"]
	apikey = userDICT["apikey"]
	articut = ArticutAPI.Articut( username, apikey)
	return articut

def articutProcessing(inputSTR, nlptool, levelop):
	resultDICT = articut.parse(inputSTR, level=levelop)
	return resultDICT

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；",'"',"'", '“'):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112>")
	return inputLIST[:-1]




if __name__ == '__main__':

	# 讀取 rawData 的資料
	filepattern = r'(^[0-9]+)\.(json)$'
	folderPath = "./rawData/"
	for f in os.listdir( folderPath):
		if re.match( filepattern, f):
			curDataPath = folderPath + f
			dataDict = json2DictReader(curDataPath)
			# 將讀出 json 的 CONTENT 斷句存在 "SENTENCE"
			# if "SENTENCE" not in dataDict:
				dataDict["SENTENCE"] = text2Sentence(dataDict["CONTENT"])
				jsonFileWriter( dataDict, curDataPath)
			# # 用 articut lv2 斷詞
			# if "WORDS" not in dataDict:
			# 	dataDict["WORDS"] = 
			# 	jsonFileWriter()

		
	# 把 articut 出來結果存成 .json（更改CONTENT的內容）
    