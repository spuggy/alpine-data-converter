import csv

def nullMe(str):
    if(str == '' or str == None):
        return "NULL"
    else:
        if "'" in str:
            str = str.replace("'","''")

        return "'"+str.strip()+"'"

def getCsv(key,filePath,database):
    with open(filePath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[key] not in database:
                database[row[key]] = row

    return database