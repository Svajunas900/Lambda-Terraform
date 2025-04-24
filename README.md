## Description
This project is to simulate real world project workflow <br/>
Development is in dev branch and everything that is working, tested is in branch prod

This project uses IaaC, terraform to create infrastructure + Github workflows CI/CD for testing and deployment.
All attention here is not the actual code but the whole infrastructure around it to make the deployment and testing autonomous

What it does? It creates lambda function in aws after testing and planning with terraform

## HOW TO SECTION:

Installing Application <br/>

Step 1. Navigate to directory where you want to clone application <br/>
   
Step 2. Clone repository using url https://github.com/Svajunas900/Lambda-Terraform.git <br/>
````
git clone https://github.com/Svajunas900/Lambda-Terraform.git
````

If you want to create and push to aws your lambda function create terraform Api, get aws credentials and configure them then just push any changes to your repository and everything will work
