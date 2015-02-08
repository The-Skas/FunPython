import csv
# All file modes in Python
# -------
# r for reading
# w for writing
# r+ opens for reading and writing (cannot truncate a file)
# w+ for writing and reading (can truncate a file)
# rb+ reading or writing a binary file
# wb+ writing a binary file
# a+ opens for appending

csvfile = open('names.csv','w')

header_high_score = ["First Name", "Last Name", "Score"]
user_scores = [
		["Salman", "Khalifa", 130],
		["Ali",    "Mulla",   139],
		["Joe",	   "Biden",   503]
	]

writer = csv.writer(csvfile)

# Writes the header
writer.writerow(header_high_score)
for x in user_scores:
	print x
	writer.writerow(x)

