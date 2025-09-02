# Demo: Using AWS Cloud9
*Service is unanavailable*

- AWS Cloud9 in an IDE that could be used in-browser

1. Create a Cloud9 environment
- Action:
	- Navigate to Cloud9
	- Environment type: New EC2 Instance 
	- Instance Type: t3.small
	- Create
- Acts as a Linux Server with the CLI automatically configured
- Action: Open Cloud9 IDE 

2. Explore the Cloud9 code editor
- Action: Create file
	- print("Hello Cloud Guru!)
	- Save as hello.py
	- In Console, run file: python hello.py

3. Run some AWS CLI commands
- Create bucket: aws s3 mb s3://bucketName
- Upload file: aws s3 cp hello.py s3://bucketName

4. Exam Tips
- **AWS Cloud9**: Browser based IDE (Integrated Development Environment) that lets developers write, run, and debug code
- **Pre-Installed Tools**: AWS CLI, support for the most popular programming languages (ie. Javascript, Python, etc.)
