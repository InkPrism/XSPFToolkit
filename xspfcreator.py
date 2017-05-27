import os.path, sys

def main():
	for k in range(1, len(sys.argv)):
		path = str(sys.argv[k])
		if '--only-print' in sys.argv:
			with open(path, 'rt', encoding="utf-8") as inpf:
				fr = inpf.read()
				lines = fr.split()
				print('<?xml version="1.0" encoding="UTF-8"?><playlist version="1" xmlns="http://xspf.org/ns/0/">\n\t<trackList>\n')
				for line in lines:
					print(line)
				print('\t</trackList>\n</playlist>')
			inpf.close()
			return
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
		else:
			print('Well, are you sure, that this file exists?\n' + str(path))

if __name__ == '__main__':
	main()