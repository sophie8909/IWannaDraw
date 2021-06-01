import os
from filefunct import *
from nlppre import *
def main(folderPath):
	filepattern = r'(^[0-9]+)_articut\.(json)$'
	for f in os.listdir(folderPath):
		if re.match(filepattern, f):
			jsonDICT = json2DictReader(f)
			buildkeyword(jsonDICT)
	return 			

def buildkeyword(jsonDICT):
	inputSTR = jsonDICT[result_segmentation]
	inputCountDICT = wordCounter(inputSTR)
	word_sum = sum( value for key,value in inputCountDICT.items())
	print( word_sum)

if __name__ == '__main__':
	main("./rawData")

	