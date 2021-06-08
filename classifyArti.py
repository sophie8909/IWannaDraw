from classifyFunct import *
from nlppre import *
def getArti(address):

# 輸入一篇文章，判斷是不是抽獎文
if __name__ == '__main__':
    # 輸入欲判斷的 FB 網址
    address = input("輸入欲判斷的 FB 粉專貼文網址（限　https://mbasic.facebook.com/　文章）：\n")
	inputSTR = getArti(address)
    articut = articutLogIn("./account.info")
    cuttedDICT = articutProcessing(inputSTR,articut,"lv1")
    wordList = articut2cleanWordList(cuttedDICT["result_segmentation"])
    if classify_lv1( wordList) == True:
        print( "他可能是抽獎文喔！！\n")
    else:
        print("我覺得他跟抽獎文沒有關係\n")