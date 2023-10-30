from shared import getCsv, nullMe

#atomic
#MembedrshipNo,MembershipName,OrgName,Address1,Address2,PostTown,PostCode,Country,SingleFamily,Title1,FirstName1,LastName1,Title2,FirstName2,LastName2,CardName1,CardName2,CurrentPrice,ags_subscription_id,ags_subscription_name,ags_subscription_start_date,ags_subscription_end_date,ags_subscription_status,ags_payment_discrepancy,ags_payment_discrepancy_amount

#INSERT INTO `registeredusertable` VALUES (3,'910623F','chris','Chris','McGregor','d11r03b79','mcgregor546@gmail.com','primary'),(
#id   | membershipno | userid     | prename    | surname   | password      | email                        | status
def get_registered_user_insert(id,membership_no,first_name,last_name,password,email,status):
    fname = nullMe(first_name)
    lname = nullMe(last_name)
    userid = membership_no
    if status == 'unverified':
        userid = userid + "-2"
    insert = f"INSERT INTO registeredusertable VALUES({id},'{membership_no}','{userid}',{fname},{lname},'{membership_no}','{email}','{status}');"
    return insert
#id     | MembershipNo | MembershipName                              | OrgName          | Address1                 | Address2                     | Address3 | PostTown                | PostCode | Country        | PublishAddress | HomeTel        | SubTypeID | JoinedDate          | status

def get_registered_user_email_update(id,membership_no,first_name,last_name,password,email,status):
    insert = f"UPDATE registeredusertable set email = 'dummy@deleme.com' where id = {id};"
    return insert

def getSubTypeID(singlefamily , country):
    if "UNITED KINGDOM" in country and singlefamily == "Family":
        return 2
    elif "UNITED KINGDOM" in country and singlefamily == "Single":
        return 1
    elif "UNITED KINGDOM" not in country and singlefamily == "Single":
        return 4
    elif "UNITED KINGDOM" not in country and singlefamily == "Family":
        return 5
    else:
        return 1

def get_mastermembershiptable_user_insert(start_id, item):
    MembershipNo = item["MembershipNo"]
    fullName = nullMe((item["Title1"] + " " + item["FirstName1"] + " " + item["LastName1"]).strip())
    address1 = nullMe(item["Address1"])
    address2 = nullMe(item["Address2"])
    postTown = nullMe(item["PostTown"])
    postCode = nullMe(item["PostCode"])
    country = nullMe(item["Country"])
    telno = nullMe("")
    created_date = item["ags_subscription_start_date"]
    singleFamily = getSubTypeID(item["SingleFamily"],country)
    insert = f"INSERT INTO mastermembershiptable VALUES ({start_id},'{MembershipNo}',{fullName},NULL,{address1},NULL,{address2},{postTown},{postCode},{country},'N',{telno},{singleFamily},'{created_date}','published');"
    return insert

def get_mastermembershiptable_user_update(start_id, item):
    MembershipNo = item["MembershipNo"]
    created_date = item["ags_subscription_start_date"]
    update = f"update mastermembershiptable set JoinedDate = '{created_date}' where MembershipNo = '{MembershipNo}';"
    return update


# INSERT INTO `mastermembertable` VALUES (15702,134745,'Test','Family','Family','Mr','stevefamilytest@atomicsmash.co.uk','01501 762972','','','','');
#id    | MembershipID | Surname     | Forename | Inits    | Title | email                          | TelephoneWork   | TelephoneMobile | dob  | DateCourseEnd | ReasonLeft
def get_mastermembertable_user_insert(mastermembertable_table_start_id, mastermembershiptable_table_start_id, item,email):
    firstName = nullMe(item["FirstName1"].strip())
    lastName = nullMe(item["LastName1"].strip())
    title = nullMe(item["Title1"])
    email = nullMe(email)
    telno = nullMe("")
    mastermembertable_user_insert = f"INSERT INTO mastermembertable VALUES ({mastermembertable_table_start_id}, {mastermembershiptable_table_start_id},{lastName},{firstName},{firstName}, {title},{email},{telno},'','','','');"
    return mastermembertable_user_insert

def is_valid_atomic_smash_user(item):
    if item["MembershipNo"] != '' and item["LastName1"] != '':
        return True
    else:
        return False

atomic_smash_db = getCsv('MembershipNo','data-2023/smash-users/mailing-list-2022-12-10_all-formatted_plus_one.csv',{})
registered_user_table = getCsv('membershipno','data-2023/exp3/registeredusertable-exp.csv', {})
mastermembershiptable_db = getCsv('MembershipNo','data-2023/exp3/mastermembershiptable-exp.csv', {})

registered_user_table_start_id = 7769
mastermembershiptable_table_start_id =   135381
mastermembertable_table_start_id = 16337

diane_list = ['195197X']

print("use alpines;")
#for item in  atomic_smash_db.values():
for id in  diane_list:

    item = atomic_smash_db[id]

    if is_valid_atomic_smash_user(item):
        email = item["Email"]
        if(len(email) < 50):
            if item["MembershipNo"] not in registered_user_table:
                primary_user = get_registered_user_insert(registered_user_table_start_id,item["MembershipNo"],item["FirstName1"],item["LastName1"],"",email,"primary")
                registered_user_table_start_id = registered_user_table_start_id + 1
                print(primary_user)
                if(item["SingleFamily"] == "Family" and item["LastName2"] != ''):
                    secondary_user = get_registered_user_insert(registered_user_table_start_id,item["MembershipNo"],item["FirstName2"],item["LastName2"],"","dummy@delme.com","unverified")
                    secondary_user_email_update = get_registered_user_email_update(registered_user_table_start_id,item["MembershipNo"],item["FirstName2"],item["LastName2"],"",email,"unverified")
                    #print(secondary_user_email_update)
                    registered_user_table_start_id = registered_user_table_start_id + 1
                    print(secondary_user)
            else:
                pass
                #print("existing registered_user_table" + item["MembershipNo"])

            if item["MembershipNo"] not in mastermembershiptable_db:
                mastermembershiptable_user_insert = get_mastermembershiptable_user_insert(mastermembershiptable_table_start_id,item)
                #mastermembershiptable_user_update = get_mastermembershiptable_user_update(mastermembershiptable_table_start_id,item)
                #print(mastermembershiptable_user_update)
                print(mastermembershiptable_user_insert)
                mastermembertable_user_insert = get_mastermembertable_user_insert(mastermembertable_table_start_id, mastermembershiptable_table_start_id,item,email)
                print(mastermembertable_user_insert)
                mastermembershiptable_table_start_id = mastermembershiptable_table_start_id + 1
                mastermembertable_table_start_id = mastermembertable_table_start_id + 1
            else:
                pass
                #print("existing mastermembershiptable" + item["MembershipNo"])
        else:
          pass
          #print("email too long) for " + item["MembershipNo"])

