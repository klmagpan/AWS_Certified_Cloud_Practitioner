# Lab: Create and Subscribe to an AWS SNS Topic

1. Create and SNS Topic
- Navigate to SNS (Simple Notification Service)
- Create Topic: EC2 State
	- Standard --> Create topic

2. Subscribe to the SNS Topic
- Create subscription
	- Protocol: How you're going to get information when you attach the topic
		- Email
	- If anything is pushed to that specific SNS topic, you'd get pushed from the protocol that you input

3. Test the SNS Topic
- Navigate to EC2
	- Instances
	- Copy the instance ID
	- Instance state: stop instance
- Navigate to Cloudwatch
	- Create alarm
	- Select Metric: Instance ID
		- EC2 > Per Instance Metrics
		- Statuscheck: failed_instance
	- Period: 1 minute
	- >= 1
	- Treat missing data as bad (breaching threshold)
- Send notification EC2State and add notification
	- OK - EC2 State
	- Insufficient - EC2 State
	- Alarm Name: EC2 State --> Create alarm