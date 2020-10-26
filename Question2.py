#This approach uses AWS CLI commands to get access to metadata
#These commands must be used only after configuring the Access key, Secret Access Key and the region of use of the IAM user 
#For the entire Meta data associated with the instance
aws ec2 describe-instances    --instance-ids <Insert Instance ID here> --output json > ec2Instance-metadata.json

#For only specific Meta data associated with the instance use the keyword 'query', for this sample querying Instance ID, Image ID, AZ Name and VPC ID. 
# Like this, any meta data parameter can be entered, and its value will be printed. 
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{Instance:InstanceId,Image:ImageID,AZ:Placement.AvailabilityZone, VPC:VpcId}'  --output json > ec2Instance-metadata.json

#in this method, you can replace 'ec2' with almost any aws service, such as rds, etc. and use the DescribeInstances command to extract the metadata from the console