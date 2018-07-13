#! /usr/bin/python

import os
import csv

dirpath = '/Users/omerar/Documents/Wind Data/Winddata Modified'
output = 'output_file.csv'
with open(output, 'w') as outfile:
    csvout = csv.writer(outfile)
    # csvout = csv.writer(outfile, quoting=csv.QUOTE_NONE, delimiter=',', quotechar='', escapechar='')


    csvout.writerow(['Date', 'Time', 'Wind Direction', 'Wind', 'Gust', 'Temperature'])

    files = os.listdir(dirpath)

    for filename in files:
        if filename is '.DS_Store':
            print("Found '.DS_Store'")
        else:
            with open(dirpath + '/' + filename) as afile:
                csvout.writerow([afile.read()])
                # csvout.writerows(afile.read())
                afile.close()

    outfile.close()
    print('Succesfully created ' + output)


    f = open(output, 'r')
    text = f.read()
    f.close()
    text = text.replace("\"","")
    f = open('test2.csv', 'w')
    f.write(text)
    f.close()