import re, os.path, sys

def erase(path):
	if os.path.isfile(path):
		with open(path, 'rt', encoding="utf-8") as inpf:
			fr = inpf.read()
			fr = re.sub(r"( xmlns:.+?=\".+?\")", "", fr)
			fr = re.sub(r"(<extension.+?>.+?</extension>)", "", fr)
			with open(path, 'wt', encoding="utf-8") as outf:
				outf.write(fr)
		outf.close()
		inpf.close()
	else:
		print('Well, are you sure, that this file exists?\n' + str(path))
def main():
	path = str(sys.argv[1])
	erase(path)
if __name__ == '__main__':
	main()