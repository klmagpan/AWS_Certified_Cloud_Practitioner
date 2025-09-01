# Demo: Exploring Storage Services (S3 in Action)

- S3 provides robust security features: bucket/IAM/encyrption policies

- Action: Navigate to S3 --> Create a bucket
	- Name has to be globally unique (any bucket, from any account, anywhere, has to be different)
	- Bucket Versioning: Used to recover previous version 
- Action: Upload Object (either drag/drop or upload)
- Action: Versioning
- **Bucket Policy**: Controls permissions from any user to access bucket
- **Management Tab**: Create lifecycle policies
	- Example: Move object b/w storage classes from S3 to S3 Glacier
- Exam Tips
	- Understand **Bucket Naming**: No two buckets, regardless of AWS account, can have same name
	- Understand Permissions
		- AWS uses a default deny all appraoch (if not explicitly allowed, will be denied)
	- Understand different b/w Bucket policy and IAM policy
	- Understand Encyrption is default
	- Understand Versioning
	- Understand **Lifecycle Policies**: Automate the process of transitioning objects b/w storage classes or deleting objects