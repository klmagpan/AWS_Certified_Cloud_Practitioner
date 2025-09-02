# Demo: Getting to Know CloudWatch Dashboards

- Navigate to Dashboards
	- Create a new dashboard: my-ec2-dashboard
- Add Line Graph Widget 
	- Metrics: EC2
	- Per Instance Metrics -> CPUUtilization
	- Rename Graph: EC2 CPU Utilization
- Note: Autosave is off
- Capture custom logs
	- Logs --> Log groups --> Create log group
	- Log group name: my-ec2-app-log-group
		- By default, these logs store indefinitely (and cost money to store it)

- Exam Tips
	- Understand how to create a CloudWatch dashboard from the console
		- You'll be adding widgets, that display metrics that you're getting from your AWS services or log groups
	- By default CloudWatch log groups are retained indefinitely
		- Can customize the amount of time you retain those logs in your log groups
