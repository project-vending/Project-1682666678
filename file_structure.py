
import os

# Create file structure
if not os.path.exists('config'):
    os.makedirs('config')
if not os.path.exists('terraform'):
    os.makedirs('terraform')
if not os.path.exists('airflow'):
    os.makedirs('airflow')
if not os.path.exists('scripts'):
    os.makedirs('scripts')

# Create empty files in each folder
with open('config/terraform.tfvars', 'w'): pass
with open('config/airflow.cfg', 'w'): pass
with open('terraform/main.tf', 'w'): pass
with open('airflow/dags/__init__.py', 'w'): pass
with open('scripts/deploy.sh', 'w'): pass
