import csv
import boto3 
import datetime

import pandas as pd 
def run_audit(file_ext):
    
    current_time=datetime.datetime.now()
    client=boto3.client('iam')

    response=client.get_paginator('list_users')
    users_list=[]
    for page in response.paginate():
        current_user = page['Users']
        
        
        for j in range(0,len(current_user)):
            current_iam_user=current_user[j]
            username=current_iam_user['UserName']
            
            get_access_key_status = client.list_access_keys(UserName=username)
            
            access_key_metadata=get_access_key_status['AccessKeyMetadata']
            
            if len(access_key_metadata)>0:
                
                for i in access_key_metadata:
                    
                    createdate=i['CreateDate']
                    current_time=current_time.replace(tzinfo=createdate.tzinfo)
                    diff=current_time-createdate
                    
                    days=diff.days
                    if days>=15:
                        temp_dict={"IAM_USER":username,"Days":days}
                        users_list.append(temp_dict)
                        # print(username)
                        
                        
        try:
                if 'csv' in file_ext:
                    print("Creating a csv file with IAM-Users having access-keys over 15 days")
                    csv_file='iam-access-key-audit.csv'
                    with open(csv_file,'w',newline="") as csvfile:
                        fieldnames = ['IAM_USER', "Days"]
                        write_csv = csv.DictWriter(csvfile,fieldnames=fieldnames)
                        write_csv.writeheader()
                        write_csv.writerows(users_list)
                
                if 'excel' in file_ext:
                    print("Creating a excel file with IAM-Users having access-keys over 15 days ")
                    csv_file='iam-access-key-audit.csv'
                    df = pd.read_csv("./"+csv_file)
                    df.to_excel(csv_file[:-4]+".xlsx", sheet_name="Testing", index=False)
        
        
        except Exception as e:
            print(e)
if __name__=='__main__':
    pass
# print(users_list)