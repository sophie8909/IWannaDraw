import json
import ArticutAPI
from filefunct import *
from pprint import pprint
import os
import re

def wordCounter(inputSTR):
	inputLIST = inputSTR.split("/")

	wordDICT = {}
	for w in inputLIST:
		if w in wordDICT:
			pass
		else:
			wordDICT[w] = inputLIST.count(w)
	
	wordCountLIST = []
	for i in wordDICT.items():
		wordCountLIST.append(i)

	wordCountLIST.sort(key = lambda c: c[1], reverse = True)
	return wordCountLIST

def articutLogIn(inforpath):
	userDICT = json2DictReader(inforpath)
	username = userDICT["username"]
	apikey = userDICT["apikey"]
	articut = ArticutAPI.Articut( username, apikey)
	return articut

def articutProcessing(inputSTR, nlptool, levelop):
	articut = articutLogIn("./account.info")
	resultDICT = articut.parse(inputSTR, level=levelop)
	return resultDICT

#將字串轉為「句子」列表的程式
def text2Sentence(inputSTR):
	for i in ("...", "…"):
		inputSTR = inputSTR.replace( i, "")
	for i in range(len(inputSTR)):
		if inputSTR[i] == ",":
			if  re.match( r"[0-9],[0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ' ' + inputSTR[i+1:] 
	for i in ( "、", "，", "。", ",",";","；",'"',"'", '“','\n','·'):
		inputSTR = inputSTR.replace( i, "<MyCuttingMark@CSIE112>")
	for i in range(len(inputSTR)):
		if inputSTR[i] == " ":
			if re.match( r"[0-9] [0-9]", inputSTR[i-1:i+2]):
				inputSTR = inputSTR[0:i] + ',' + inputSTR[i+1:]
	inputLIST = inputSTR.split("<MyCuttingMark@CSIE112>")
	for i in inputLIST:
		if i == "":
			inputLIST.remove("")
	return inputLIST
