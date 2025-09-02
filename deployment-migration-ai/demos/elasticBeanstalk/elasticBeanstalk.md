# Demo: Deploying an Application Using Elastic Beanstalk

1. Create a service role for Elastic Beanstalk (to be able to deploy AWS Services on your behalf)
- Action:
	- Navigate to IAM --> Roles --> Create role --> 
	- Use Case: Elastic Beanstalk
	- Role Name: CustomServiceRoleForElasticBeanstalk

2. Create an EC2 Instance Role for Elastic Beanstalk (Gives required permissions to interact with Elastic Beanstalk)
- Action:
	- Create role
	- Use Case: EC2
	- Permissions: AWSElasticBeanstalkReadOnly
	- Name: CustomEC2InstanceProfileForElasticBeanstalk

3. Upload the provided code
- Action:
	- Search for ElasticBeanstalk
	- Example Application Name: Hello Cloud Gurus
	- Platform: PHP
	- Application Code:
		- Upload your code
		- Version label: v1
		- Upload local file
		- Next
- Action:
	- Use existing service and EC2 role
	- Configure Updates: Basic System
		- Deactivate Managed Updates

4. Exam tips:
	- **Elastic Beanstalk**: 
		- Deploys and Scales your web applications, including the web application server platform
		- Provisions the AWS resources for you (EC2, RDS, S3, Elastic Load Balancers, Auto Scaling Groups, etc.)
