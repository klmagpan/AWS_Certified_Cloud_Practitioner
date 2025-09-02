# Lab: Creating an S3 Storage Lifecycle

1. Upload an object to the S3 bucket
- Navigate to already existing S3 bucket and upload a text document (test.txt)

2. Create an S3 lifecycle for the S3 bucket
- Navigate to Management tab and create a lifecycle rule
	- Name: my-lifecycle-rule
	- Apply to all objects in the bucket (and acknowledge)
	- Lifecycle rule actions
		- Move current versions of objects b/w storage classes
		- Expire current versions of objects

3. Add relevant transitions to the S3 lifecycle policy
- Transition current versions of objects between storage classes
	- Choose storage class transitions: Standard-IA
	- Days after object creation: 30
		- Minimum of 30 days anyway
- Expiration: 365 days
- Create rule

4. Verify your lifecycle policy
- Check test.txt
- View expiration rule