import csv

with open('file_readed.csv', newline='') as s:
	reader = csv.reader(s)
	for row in reader:
		if(row[3] == "4"):
			print(row[0], row[1])
    #print(row[0], ' ', row[1], ' ', row[2], ' ', row[3], ' ');
		

#            for row in reader:
#                if row[0] != "":
#                    #print(row[0], row[1])
#                    f = open(file_name, 'a')
#                    data = str(row[1]+' ')
#                    #data = str(row[0]+', '+row[1]+'\n')
#                    f.write(data)