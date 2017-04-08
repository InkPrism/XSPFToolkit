import re, os.path, random

def main():
	path = input('>File: ')
	if os.path.isfile(path):
		with open(path, 'rt', encoding='utf-8') as inpf:	
			fr = inpf.read()
			fr = fr.replace("\n", "")
			fr = fr.replace("\t", "")

			with open(path, 'wt', encoding='utf-8') as outf:

				outf.write(re.search(r'(.+?)<track>', fr).group(0))

				lstot = []
				for m in re.finditer(r'(<track>.+?</track>)', fr):
					lstot.append(str(m.group(0)))
				random.shuffle(lstot)
				s = set(lstot)
				outf.write("\n".join(str(e) for e in s))

				for m in re.finditer(r'(</trackList>.+?)\Z', fr, re.IGNORECASE):
					outf.write('%s \n' % (m.group(0)))
			inpf.close()
			outf.close()

	else:
		print('Well, are you sure, that this file exists?\n' + str(path))

if __name__ == '__main__':
	print('>===> XSPFShuffler - The new order <===<')
	main()