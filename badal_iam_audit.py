import sys
import check_access_keys
import auditmfa

allowed_flags=['--output','--audit']
allowed_file_types=['csv','excel']
invalid_flag=[]
provided_flags=[]
provided_operations=[]
provided_filetypes=[]
def invalid_flag_exit(invalidflag):
    if len(invalidflag)>0:
            for flag in range (0,len(invalidflag)):
                print("Error with the flag "+invalidflag[0])

                sys.exit()

def check_audit_operation():
     allowed_audit_operations=['iam-access-keys','iam-mfa']
     for f in sys.argv:
        if f.startswith('--audit'):
            operations=f.split('=')[1].split(',')
            for operation in operations:
                    if operation not in allowed_audit_operations:
                            print("Error "+operation+" is not a valid operation")
                            sys.exit()
                    else:
                            provided_operations.append(operation)
            return provided_operations
            
            
def set_output_file():
    for f in sys.argv:
        if f.startswith('--output'):
            file_types=f.split('=')[1].split(',')
            for file_type in file_types:
                if file_type not in allowed_file_types:
                    print("Error "+file_type+" is not a supported file type by this script")
                    sys.exit()
                else:
                    provided_filetypes.append(file_type)
            return provided_filetypes
        
if len(sys.argv) < 2:
    print("Provide flags check wrapper --help")

else:
    args=[]
    for i in range(len(sys.argv)):
        args.append(sys.argv[i])
    # print(args)
    for i in range(1, len(args)):
        
        provided_flags.append(str(args[i]).split('=')[0])
        # print(provided_flags)
        if str(args[i]).split('=')[0] not in allowed_flags:
            invalid_flag.append(args[i])
            invalid_flag_exit(invalid_flag)
    
    for flag in provided_flags:
        if flag=='--output':
            provided_filetypes=set_output_file()
        if flag=='--audit':
            provided_operations=check_audit_operation()


        
    for execute_operation in provided_operations:
        if execute_operation=='iam-access-keys':
            # print(file_ext)
            print("Auditing IAM  Access-Keys")
            for file_type in provided_filetypes:
                
                check_access_keys.run_audit(file_type)
                
        if execute_operation=='iam-mfa':
            print("Auditing IAM-Users for MFA")
            # print(file_ext)
            for file_type in provided_filetypes:
                auditmfa.audit_mfa(file_type)
