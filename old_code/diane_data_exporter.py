from shared import getCsv, nullMe

supplied_list_csv = getCsv('mainid', '../data/new_diane/xxxxseed2018suppliedlist2.txt-Table 1.csv', {})
donars_list_csv = getCsv('ID', '../data/new_diane/seed2122donorsandhelpers.csv', {})
# id_db = getCsv('mainid','data/new_diane/seed2022suppliedlist2-exp.csv',{})

#INSERT INTO seed2022suppliedlist VALUES (4566,'5611',NULL,'Tristagma',NULL,'''Rolf Fiedler'' ','','Bbl');
#INSERT INTO seed2022suppliedlist VALUES (3334,'4068',NULL,'Zephyranthes',NULL,'primulina','','Gdn');
#mainid	id	intergeneric	genus	variant	name	donor	source	US Banned
def get_supplied_list_insert(item):
    mainid = item["mainid"]
    intergeneric = nullMe(item["intergeneric"])
    if intergeneric == "'\\N'":
        intergeneric = "NULL"
    variant = nullMe(item["variant"])
    if variant == "'\\N'":
        variant = "NULL"
    id = item["id"]
    genus = nullMe(item["genus"])
    name = nullMe(item["name"])
    source = nullMe(item["source"])

# +--------------+--------------+------+-----+---------+-------+
# | Field        | Type         | Null | Key | Default | Extra |
# +--------------+--------------+------+-----+---------+-------+
# | mainid       | double       | YES  |     | NULL    |       |
# | id           | varchar(255) | YES  |     | NULL    |       |
# | intergeneric | varchar(255) | YES  |     | NULL    |       |
# | genus        | varchar(255) | YES  |     | NULL    |       |
# | variant      | varchar(255) | YES  |     | NULL    |       |
# | name         | varchar(255) | YES  |     | NULL    |       |
# | donor        | varchar(255) | YES  |     | NULL    |       |
# | source       | varchar(255) | YES  |     | NULL    |       |
# +--------------+--------------+------+-----+---------+-------+
#`seed2020suppliedlist` VALUES (7,'001',NULL,'Acaena',NULL,'caesiiglauca ',NULL,'WC')
    insert = f"INSERT INTO seed2022suppliedlist VALUES ({mainid},{id},{intergeneric},{genus},{variant},{name},'',{source});"
    return insert

#ID,prename,surname,membershipno,country,entitlement,Field6
#INSERT INTO `seed2021donorsandhelpers` VALUES (1,'881525J','Saad','Abdalla','UK',15)
def get_helpers_insert(item):
    ID = item["ID"]
    prename = nullMe(item["prename"])
    surname = nullMe(item["surname"])
    membershipno = nullMe(item["membershipno"])
    country = nullMe(item["country"])
    entitlement = item["entitlement"]

    insert = f"INSERT INTO seed2022donorsandhelpers VALUES ({ID},{membershipno},{prename},{surname},{country},{entitlement});"
    return insert

def get_banned_list_insert(record_id,item):
    id = item["id"]
    insert = f"INSERT INTO seed2022suppliedbannedimports VALUES ({record_id},'UNITED STATES',{id});"
    return insert

print("use alpines;")
print("truncate table seed2022donorsandhelpers;")
print("truncate table seed2022suppliedlist;")
print("truncate table seed2022suppliedbannedimports;")


for item in supplied_list_csv.values():
    print(get_supplied_list_insert(item))

banned_id = 1
for item in supplied_list_csv.values():
    if(item["US Banned"].lower() == "y"):
        print(get_banned_list_insert(banned_id,item))
        banned_id = banned_id + 1


for item in  donars_list_csv.values():
    print(get_helpers_insert(item))
