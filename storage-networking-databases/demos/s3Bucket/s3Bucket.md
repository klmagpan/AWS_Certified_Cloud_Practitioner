# Lab: Creating S3 Buckets with Versioning and Encryption

1. Create an S3 Bucket
- Action: Navigate to S3 section --> Create Bucket
	- Example: Bucket name acgtest8500
	- ACLs disabled
	- Block all public access
	- Action: Enable Bucket versioning
	- Enable default encryption: Server-side encryption with Amazon S3 managed keys (SSE-S3)

2. Upload a File to the Bucket
- Action: Navigate to acttest8500 instance and upload Test.txt file
	- Add files either dragging and dropping or from explorer
	- Then click upload

3. Upload Second Version of the Same File
- Action: Edit Test.txt and upload it to S3 bucket
- Action: Change version of Test.txt back to the first version of it
	- Click on checkbox next to first version --> Download --> Reupload with "correct" file
	