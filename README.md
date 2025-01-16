
---

# AWS IAM Auditing Automation Tool

A tool to automate the auditing of AWS IAM services, helping identify security misconfigurations and enforce best practices.

## Features  
- 🔑 Access Key Audit: Detects IAM access keys older than 30 days(Can be modified in the script).  
- 🔒 MFA Enforcement Check: Verifies if MFA is enabled for IAM users.  
- 📊 Customizable Reports: Export results in CSV or Excel formats.  

## Usage  
```bash
python iam_audit.py --audit=iam-access-keys,iam-mfa --output=csv,excel
```  
### Available Flags  
- `--audit=iam-access-keys,iam-mfa` → Select audit type(s)  
- `--output=csv,excel` → Choose output format  

## Tech Stack  
- Python (Boto3)  
- Bash  
- AWS IAM  

## Coming Soon  
- More IAM security checks and automated remediation.  

---

