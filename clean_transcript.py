import csv
import argparse
import re
import os

def format_file(lecture, output):
	reader = open (lecture, 'r')
	temp = open ('temp.txt', 'a')
	for line in reader:
		line = re.sub('\d{1}:\d{2}:\d{2}', ' ', line).strip() 
		#line = line.replace('.', '. ', line.count('.')).replace(',', ', ', line.count(','))
		temp.write(line + '\n')	
	reader.close()
	temp.close()
	
	to_read = open ('temp.txt', 'r')
	writer = open (output, 'w')
	for line in to_read:
		if not line.strip():     
			continue
		line = line.replace('\n', ' ')
		writer.write(line)
	to_read.close()
	writer.close()

	os.remove('temp.txt')
			
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('original')
	parser.add_argument('clean')
	args = parser.parse_args()
	format_file(args.original, args.clean)
	
if __name__ == '__main__':
	main()