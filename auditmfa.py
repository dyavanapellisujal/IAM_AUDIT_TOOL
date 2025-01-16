import boto3 , sys , csv 
import pandas as pd

def audit_mfa(file_ext):

    
        

        iam = boto3.client('iam')

        response = iam.get_paginator('list_users') #This will return a object 'Users'
        data_list=[]

        for user in response.paginate():

            for j in range (0,len(user['Users'])): #Iterates over all the users present in the Users object


                a= dict((user['Users'])[j]) #Gets the user 
                
                
                get_mfa=iam.list_mfa_devices(UserName=a['UserName']) #Gets the mfa field
                
                if len(get_mfa['MFADevices']) > 0: #if mfa is ena'bled this will contain data , if not 'then empty hence check if greater than 0

                    pass
                    #data={'IAM_USER':a['UserName'],'UserId':a['UserId'],'ARN':a['Arn'],'CreateDate':a['CreateDate'],'MFA_STATUS':'Enabled'}

                else:
                    
                
                    data={'IAM_USER':a['UserName'],'UserId':a['UserId'],'ARN':a['Arn'],'CreateDate':a['CreateDate'],'MFA_STATUS':'Disabled'}
                
                data_list.append(data)
        
            try:
                if 'csv' in file_ext:
                    print("Creating a csv file for mfa-disabled IAM-Users")
                    csv_file='iam-mfa-audit.csv'
                    with open(csv_file,'w',newline="") as csvfile:    #creates the csvfile with the provided name
                        fieldnames = ['IAM_USER', 'UserId', 'ARN', 'CreateDate','MFA_STATUS']
                        write_csv = csv.DictWriter(csvfile,fieldnames=fieldnames)
                        write_csv.writeheader()
                        write_csv.writerows(data_list)
                
                if 'excel' in file_ext:
                    print("Creating a excel file for mfa-disabled IAM-Users")
                    csv_file='iam-mfa-audit.csv'
                    df = pd.read_csv("./"+csv_file)
                    df.to_excel(csv_file[:-4]+'.xlsx', sheet_name="Testing", index=False)
        

                
    
            except Exception as e:
                print(e)

   


if __name__=='__main__':
    pass
