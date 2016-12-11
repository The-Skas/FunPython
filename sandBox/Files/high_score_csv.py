import csv
import pdb
# All file modes in Python
# -------
# r for reading
# w for writing
# r+ opens for reading and writing (cannot truncate a file)
# w+ for writing and reading (can truncate a file)
# rb+ reading or writing a binary file
# wb+ writing a binary file
# a+ opens for appending

def writeFresh():
	csvfile = open('names.csv','w')

	header_high_score = ["First Name", "Last Name", "Score"]
	user_scores = [
			["Salman", "Khalifa", 130],
			["Ali",    "Mulla",   20],
			["Joe",	   "Biden",   503],
			["Dude",   "Wilson",   13]
		]

	writer = csv.writer(csvfile)

	# Writes the header
	writer.writerow(header_high_score)
	for x in user_scores:
		writer.writerow(x)

def readFile():
	csvfile = open('names.csv','r')
	rd = csv.reader(csvfile)

	values = list()
	for row in rd:
		values.append(row)

	return values

writeFresh()
data = readFile()

data = sorted(data[1::], key = lambda x : int( x[2]))

print data


