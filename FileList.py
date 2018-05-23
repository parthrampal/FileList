import sys,os,csv

root = "C:\\Users\\Parth Rampal\\Documents"
i = 0
filenames = []
for path, subdirs, files in os.walk(root):
	for name in files:
		filenames.insert(i,name)
		++i
		
with open ("C:\Users\Parth Rampal\Documents\FileList.csv",'w+') as myfile:
	wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
	wr.writerow(filenames)