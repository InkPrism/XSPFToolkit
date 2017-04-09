import os.path

def main():
	path = input('>File: ')
	if os.path.isfile(path):
		with open(path, 'rt', encoding="utf-8") as inpf:
			fr = inpf.read()
			lines = fr.split()
			with open(path, 'wt', encoding="utf-8") as outf:
				outf.write('<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/">\n\t<trackList>\n')
				for line in lines:
					outf.write('\t\t<track><location>' + str(line) + '</location></track>\n')
					print(line)
				outf.write('\t</trackList>\n</playlist>')
		outf.close()
		inpf.close()

if __name__ == '__main__':
	main()