from filefunct import *

# 確認是否提及抽獎，使用關鍵字字典確認
def classify_lv1(wordLIST) -> bool: 
    #  這邊的 keyword 必須讓所有抽獎文都過 lv1，但可能會混入其他東西
	keywordLIST = json2DictReader("drawKeyword.json")["CONTENT"]
	# 確認同一組的關鍵字是否皆出現在 wordlist 中
	for keywordSet in keywordLIST:
		chk = True
		for i in keywordSet:
			if i not in wordLIST:
				chk = False
				break
		if chk == True:
			return True
	return False