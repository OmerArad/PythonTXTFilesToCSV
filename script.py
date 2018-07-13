#! /usr/bin/python

import os
import csv

dirpath = '/Users/omerar/Documents/Wind Data/Winddata Modified'
tempfile = 'temp_data.csv'
output = 'merged_data.csv'

with open(tempfile, 'w') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(['Date', 'Time', 'Wind Direction', 'Wind', 'Gust', 'Temperature'])
    files = os.listdir(dirpath)

    for filename in files:
        if filename is '.DS_Store':
            print("Found '.DS_Store'")
        else:
            with open(dirpath + '/' + filename) as afile:
                csvout.writerow([afile.read()])
                afile.close()

    outfile.close()
    print('Successfully created ' + tempfile)

    f = open(tempfile, 'r')
    text = f.read()
    f.close()
    text = text.replace("\"","")
    f = open(tempfile, 'w')
    f.write(text)
    f.close()

    with open(tempfile) as infile, open(output, 'w') as outfile:
        for line in infile:
            if not line.strip(): continue  # skip the empty line
            outfile.write(line)  # non-empty line. Write it to output

    if os.path.exists(tempfile):
        os.remove(tempfile)
    else:
        print("The file does not exists")