import json
import ArticutAPI
from pprint import pprint
from filefunct import *
from rawTextToData import *
from TrainClassify import *
from nlppre import *

def jsonFileWriter(jsonDICT, jsonFileName):
	"""轉換 jsonDICT 為 json 格式的檔案，並存檔。檔名由 jsonFileName 指定。"""
	with open(jsonFileName, mode="w", encoding="utf-8") as f:
		json.dump(jsonDICT, f, ensure_ascii=False)
	return None

if __name__ == '__main__':

	articut = articutLogIn("./account.info")

	# 讀取 rawData 的資料
	filepattern = r'(^[0-9]+)\.(json)$'
	folderPath = "./rawData/"
	for f in os.listdir( folderPath):
		if re.match( filepattern, f):
			curDataPath = folderPath + f
			dataDict = json2DictReader(curDataPath)
			# 將讀出 json 的 CONTENT 斷句存在 "SENTENCE"
			if "SENTENCE" not in dataDict:
				dataDict["SENTENCE"] = text2Sentence(dataDict["CONTENT"])
				jsonFileWriter( dataDict, curDataPath)
			
			# 用 articut lv2 斷詞
			# 下面那個註解到時候用好了要記得拿掉嘿 我還在等他給我一個月 我覺得我寫好了
			#if "WORDS" not in dataDict:
			cuttedDICT = articutProcessing(dataDict["CONTENT"],articut,"lv2")
			dataDict["WORDS"] = wordCounter(cuttedDICT["result_segmentation"])
			jsonFileWriter( dataDict, curDataPath)

		
	# 把 articut 出來結果存成 .json（更改CONTENT的內容）
    