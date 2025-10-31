import argparse
import csv
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--files', nargs='*')
    parser.add_argument('--report')

    args=parser.parse_args()

    return args


def read_files(files=None):
    objects=[]
    if files != None:
        for f in files:

            file=f'./Files/{f}'
            try:
                with open(file, mode='r', newline='') as csvfile:
                    csv_reader=csv.reader(csvfile)

                    next(csv_reader)
                    for row in csv_reader:
                        objects.append(row)
            except FileNotFoundError:
                print (f'File {f} not found. Please, choose file/files from ./Files directory.') 
    return objects
    

def calculate_average_rating(objs=[]):

    rating = {}
    for i in objs:
        if i[1] in rating:
            rating[i[1]].append(float(i[3]))
        else:
            rating[i[1]]=[float(i[3])]

    average_rating = [['','brand','rating']]
    id = 1
    for key, value in rating.items():
        average_rating.append([id])
        average_rating[id].append(key)
        average_rating[id].append(round(sum(value)/len(value), 2))
        id+=1
    return average_rating


def output (report='', objects=[]):
    if report == 'average-rating':
        if objects != []:
            result=calculate_average_rating(objects)
        else:
            return print('No data to make report. Please, add at least one file with data.')
    else:
        return print(f'Report {report} is undefined. Please, enter another report.')

    return print(tabulate(result, headers='firstrow', tablefmt="pretty"))

files=[]
report=''

if __name__=="__main__":
    args=main()
    files=args.files
    report=args.report

objects=read_files(files)

output(report, objects)
