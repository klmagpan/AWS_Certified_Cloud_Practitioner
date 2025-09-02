# Demo: Working with AWS CloudShell and the AWS Command Line Interface (AWS CLI)

1. Launch the CloudShell
- Type: aws --version
- Action: Create a new an s3 bucket
	- Example: aws s3 mb s3://mybucket-3479234

2. Use the AWS CLI
- Type: aws s3 ls
- Type: echo "My new file" >>file.txt
	- ls
	- cat file.txt
- Action: Upload text file
	- Example: aws s3 cp file.txt s3://mybucket-3479234
	- Check: aws s3 ls s3://mybucket-3479234
- Command; aws s3 mb help
	- Tells you how to use the comand

3. Review the CLI Documentation
- https://docs.aws.amazon.com/cli/latest/

4. Exam Tips
- **AWS CloudShell**: Browser based **shell** with the **AWS CLI** pre-installed
- **AWS CLI**: A command line tool used to manage AWS services