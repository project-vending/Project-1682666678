
import os

# Define variables
aws_access_key = 'ACCESS_KEY'
aws_secret_key = 'SECRET_KEY'

# Create contents of file as a string
tfvars_content = f"""
aws_access_key = "{aws_access_key}"
aws_secret_key = "{aws_secret_key}"
"""

# Write contents to file
with open(os.path.join('config', 'terraform.tfvars'), 'w') as f:
    f.write(tfvars_content)
