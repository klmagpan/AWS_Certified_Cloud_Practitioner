# Demo: Lambda Function within the Console

- Action: Navigate to Lambda --> Create a function
	- Action: Author from Scratch
	- Name: my_Name_Function
	- Runtime: Python 3.13
	- Architecture: x86_64
- Permissions: By default, Lambda will create an execution role to uploadlogs to CloudWatch
	- Used to see errors, or why functions aren't working properly
- Change Default Execution Role
	- Action: Basic Lambda Permissions
- Functions Tab
	- Code: Lambda Function Code
	- Test: Create/pass test event code needed for the function to rely on
	- Monitor: CloudWatch metrics (duration, throttles, success, etc.)
	- Configurations: Triggers for permissions, destination, function URL, tags, etc.
	- Aliases: Name pointers used to create to point to a version that you may have of your Lambda function
	- Versions: versions
- Action: Write code --> Deploy (saves changes)
- Action: Test --> Name My_event_test --> Edit code --> Save --> Test --> Check Details