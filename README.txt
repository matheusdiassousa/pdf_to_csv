Python Modules used in this project:

tabula-py - https://pypi.org/project/tabula-py/
	tabula-py requires Java8+ and Python3.5+
**make sure: 
- That you have a python3.5+ installed
- That you have java8+ installed and the environment variable configured as 'java' with the appropriate path. (for Windows users)


Usage guide: 
1 - Put the .pdf files from the pull_test_machine in the folder "data/". Open a powerShell starting from 'pdf_to_csv/'.
2 - Activate the virtualenv executing the command (for Windows OS): 
>>> .\p2c_rp\Scripts\activate
3 - Now, execute the main software to extract the data from the pdf files, by using the following command 
>>> python pull_test_extractor.py
4 - Check the result at the following path 'data/output_data.csv'