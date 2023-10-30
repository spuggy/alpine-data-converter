import csv
from shared import nullMe

filePath = 'data-2023/user-export2-nov-23/seed2023donorsandhelpers-Table 1.csv'
print('use alpines;')
print('truncate seed2023donorsandhelpers;')
print('truncate seed2023suppliedlist;')
print('truncate seed2023suppliedbannedimports;')
# INSERT INTO seed2023donorsandhelpers VALUES (1,'150028G','Anita & Mike','Acton','UK',30);
with open(filePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # pass
        print(f"INSERT INTO seed2023donorsandhelpers VALUES ({row['ID']},'{row['membershipno']}','{row['prename']}','{row['surname']}','{row['country']}',{row['entitlement']});")



filePath = 'data-2023/user-export2-nov-23/seed2023suppliedlist-Table 1.csv'
ids = {}
sources = {
    'Gdn': 'Gdn',
    'Wild' : 'WC',
    'Bulb': 'Bbl',
    'Damp' : 'Damp'
}
# INSERT INTO seed2023suppliedlist VALUES (1,'1001',NULL,'Abelmoschus',NULL,'manihot','','Gdn');
# mainid,id,intergeneric,genus,variant,name,donor,source
with open(filePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        intergeneric = row['intergeneric']
        if intergeneric == 'NULL':
            intergeneric = 'NULL'
        else:
            intergeneric = f"{nullMe(intergeneric)}"
        variant = row['variant']
        if variant == 'NULL':
            variant = 'NULL'
        else:
            variant = f"{nullMe(variant)}"
        ids[row['id']] = row['id']
        source = sources[row['source']]
        print(f"INSERT INTO seed2023suppliedlist VALUES ({row['mainid']},'{row['id']}',{intergeneric},{nullMe(row['genus'])},{variant},{nullMe(row['name'])},{'NULL'},'{source}');")


# INSERT INTO seed2023bannedimporttable VALUES (4,'UNITED STATES',31);


filePath = 'data-2023/user-export2-nov-23/seed2023bannedimporttable-Table 1.csv'

with open(filePath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        check = ids[row['seeditemid']]
        print(f"INSERT INTO seed2023suppliedbannedimports VALUES ({row['id']},{row['Country']},{row['seeditemid']});")

