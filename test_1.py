# para verificar os modulos instalados dentro do virtualenv podemos utilizar o comando >>> pip list
# para verificar a versão do modulo >>> pip show "modulo"

# import pandas as pd
# import numpy as np
import tabula as tb
import csv
import os


file_name = ('data/output_data.csv')

for file in os.listdir('data/'):
    if file == "output_data.csv":
        os.remove("output_data.csv")

for file in os.listdir('data/'):
    if file.endswith('.pdf'):
        tb.convert_into(file, "file_readed.csv", output_format="csv", java_options="-Dfile.encoding=UTF8", pages='all')


        #os.remove(file_name)
        f = open(file_name, 'a')
        f.write(file[0]+file[1]+' ')
        with open('file_readed.csv', newline='') as s:
            reader = csv.reader(s)

            for row in reader:
                if(row[3] == "4"):
                    #print(row[0], row[1])
                    f = open(file_name, 'a')
                    data = str(row[1]+' ')
                    #data = str(row[0]+', '+row[1]+'\n')
                    f.write(data)
            f = open(file_name, 'a')
            f.write('\n')
        os.remove('file_readed.csv')
