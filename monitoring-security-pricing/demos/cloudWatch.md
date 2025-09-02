# Lab: Visualize Metrics for Tagged Resources on Amazon CloudWatch

1. Create a CloudWatch Dashboard
- Navigate to CloudWatch --> Create a dashboard (my-ec2-dashboard)
- Open Metrics --> Explorer 
	- Metrics: CPUUtilization
	- From (tag): Environment = Prod
	- Aggregate: Average
	- Columns/Rows: 1

2. Select EC2 CPU Utilization in Metrics Explorer
- ... --> View in Metrics --> Name: Prod EC2 CPUUtilization
		- Widget type: Line
		- Add to Dashboard
		- Hit save!

3. Filter the Aggregated Metrics by Environment Tag and Create One Visual for Each Environment
- Follow the same process but From: Environment = Dev
	- Rename graph: Dev EC2 CPUUtilization