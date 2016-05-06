"""
#========================================================================="
# https://github.com/schadow1/osm-contributor-stats/blob/master/Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py
# Jared Cortez, 05-2016
# Filtering to remove unwanted users from the changeset comment hashtag and format the output file
#========================================================================="
#========================================================================="
"""
__author__ = 'jed'
import ast, csv, OsmApi, OsmContributorStats

def in_noah(user,comparison_file):
	line_dict = []
	noah_users = []
	with open(comparison_file) as readthis:
		for l in readthis.readlines():
			line_dict.append(ast.literal_eval(l))

	for line in line_dict:

		for key,value in line.iteritems():
			try:
				if "#ProjectNOAH" in value["tag"]["comment"]:
					#print value["tag"]["comment"]
					if user == value["user"]:
						return True
			except KeyError:
				#print "No comment"
				continue
			#print key,value
	return False

def open_csv(output_file,input_file,comparison_file):
	csv_file_copy = []
	indeces_to_be_removed = []
	#writer = open(input_file,'wb')
	with open(input_file) as csvfile:
		reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in reader:
			clean = filter(None, row)
			csv_file_copy.append(clean)
			#print clean
		#return csv_file[:-9]
		for index, c in enumerate(csv_file_copy[2:-9]):
			if not (in_noah(c[2],comparison_file)):
				indeces_to_be_removed.append(index+2)
		csvfile.close()
	print indeces_to_be_removed

	with open(input_file, 'rt') as infile, open(output_file, 'wt') as outfile:
		outfile.writelines(row for row_num, row in enumerate(infile) if row_num not in indeces_to_be_removed)
#open_csv()
