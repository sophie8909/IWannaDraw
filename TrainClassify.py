import os




def main(folderPath):
	filepattern = r'(^[0-9]+)_articut\.(json)$'
	for f in os.listdir( folderPath):
		if re.match( filepattern, f):
			buildkeyword(f)
	return 			

def buildkeyword( filepath):



if __name__ == '__main__':
	main()

	