import argparse
import csv

def build_parser():
	parser = argparse.ArgumentParser(
		description='Apply a specified transform to given rows in a CSV file.')
	parser.add_argument('-i', '--input', required=True,
						help='input file to process. CSV format.')
	parser.add_argument('-c', '--column', action='append', required=True,
						help='The column (or columns) to extract.')
	parser.add_argument('--index', required=True,
						help='A unique index for the output row.')
	parser.add_argument('-o', '--output', required=True,
						help='Output file.')
	parser.add_argument('-t', '--transform', required=False, choices=['wc'], default='wc',
						help='The transform to apply. wc = word count')
	return parser

class WordCountTransformer:
	def __init__(self):
		self.wordCount = 0

	def transform(self, columns):
		self.wordCount += sum([len(c.split()) for c in columns])

	def getTransform(self):
		return [self.wordCount]

def main():
	# Initialise vars
	parser = build_parser()
	parsed = parser.parse_args()
	reader = csv.reader(open(parsed.input))
	columnIndexes, header = None, None
	columns = parsed.column
	index = parsed.index
	# TODO: When more transforms added then make a switch statement
	transform = WordCountTransformer()

	# Main loop
	for row in reader:
		if header is None:
			header = row
			columnIndexes = [header.index(c) for c in columns]
		else:
			processedColumns = [row[i] for i in columnIndexes]
			transform.transform(processedColumns)

	# Output
	outputFile = csv.writer(open(parsed.output,'w'))
	outputFile.writerow(columns+["index"])
	outputFile.writerow(transform.getTransform()+[index])

if __name__ == "__main__":
	main()