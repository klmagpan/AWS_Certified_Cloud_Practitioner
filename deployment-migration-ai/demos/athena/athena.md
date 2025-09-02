# Demo: Using Athena to Query Data

1. Configure CloudTrail (audit log)create some Log data
- Navigate to CloudTrail --> Create a quick trail

2. Create an S3 bucket for athena results
- Create S3 bucket: my-athena-results-394732
- Open Athena in a new tab --> Query Editor
- Set up query result location
	- Edit Settings --> Browse S3 --> Select the athena-results bucket

3. Query the data using Athena
- Query1 Editor Commands:
	- CREATE DATABASE athenadb --> Run
	- Create a new query2 (+) and paste Athena_ Query_Create_table.txt code
- Copy CLI of aws-cloudtrail s3 logs
	- S3 --> aws-cloudtrail --> AWSLogs --> account number --> copy S3 URI (used to reference location in s3)
	- Run
- cloudTrail_logs table is now created, now create a third query3 and copy Athena_Query.txt

4. Exam Tips
- **Interactive Query**: Athena is an interactive query service for data in S3
- **Standard SQL**: Allows you to query data stored in S3 using standard SQL
- **Serverless**: You don't need to configure any infrastructure to use Athena
- **Use Cases**: Querying log files or generating reports from S3 data