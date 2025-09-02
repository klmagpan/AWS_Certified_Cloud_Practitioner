# Lab: Troubleshooting an IAM Policy on an EC2 Instance

1. Upload an object to the S3 bucket
- Navigate to S3
	- Copy the name of the already generated bucket
- Upload an object: Text.txt

2. Connect to the EC2 instane and attempt to get the object
- Navigate to EC2
- Click on already running instance ID
- Connect: Connect using EC2 Instance Connect
	- Command: aws s3api get-object --bucket bucketName --key test.txt my-test.txt
		- my-test.txt is the destination file
		- Though don't have permissions...

3. Edit the instance's IAM Policy to allow access to the S3 Bucket
- Within the instnace summary in the EC2 dashboard, the IAM Role contains the permission policies that the IAM is using in the instance profile
- Add Permissions: AmazonS3ReadOnlyAccess

4. Connect to the EC2 instance to verify the new permissions
- Rerun above command and see the my-test.txt saved to the EC2 instance

Notes
- In the real world, only give access to the S3 bucket that contains the desired objects
	- Challenge: access to a specific bucket