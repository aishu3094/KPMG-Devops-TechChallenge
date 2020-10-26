# KPMG-Devops-TechChallenge
Solution to Tech Challenge for Cloud DevOps Engineer role at KPMG Bangalore
Question 1

I have built a very simple, bare bones solution as my version of a 3 tier architecture. I have used AWS CloudFormation as my IaC platform, Elastic Beanstalk as my automated application generator which provides a load balanced EC2 deployment of a sample Node JS application. I have attached a MySQL database to this architecture which stores any data taken in from the application. 
Template Structure:
I have made use of CloudFormation Nested Stacks to first build out my Network, which creates a VPC, 2 public and 2 private subnets, Routing tables, Internet Gateways, NACLs and NAT Gateways. This provides Internet access to the public subnets and a connection from the private subnets to the public subnets. 
Once the Network stack is created, there is an Application stack which builds a bare bones Elastic Beanstalk Node.Js application on load balanced EC2 Instances, making use of the Public and Private subnets and the VPC created in the previous step. 
Simultaneously, a database tier is also created which builds a single rds MySQL instance, making use of the VPC and the Private subnets created in the Network tier. 
To deploy, first upload the VPC, Application and Database templates to an S3 bucket, copy and paste the Object URL from the s3 bucket to the Mainstack template URL section, corresponding to each template. Then deploy the Mainstack template to the Cloud Formation console in AWS. 
After the template has been successfully deployed, in the outputs section, you will find the URL for the website. 

Considerations made:
I do not have experience creating a Nodejs application, therefore I have used a sample Node.Js application template available readily. 
Future Scope:
A CodePipeline (CICD pipeline) can be created to automate the deployment
A logging solution can be attached to the application
HTTPS Listener can be used instead of the non secure HTTP Listener for the Elastic Load balancer
The RDS MySQL database can be deployed in Multi AZ for redundancy. 
DynamoDb(NoSQL) Database can be used instead of RDS.
The Nodejs application can be replaced by a PHP application to create a convention LAMP Stack. 


Question 2
A simple AWS CLI Command to extract Metadata from the required Instance/Instances from the AWS Console. This code assumes that you already have configured credentials and region of the IAM user with respect to the account in question. 


Question 3
A simple recursive python code that takes in the nested dictionary and keys as input and prints the value. 
