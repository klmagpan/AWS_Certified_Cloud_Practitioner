# Cloud Foundations and Compute

## AWS Cloud Adoption Framework and Migration Strategies

### Cloud Adoption Framework (CAF)
- **AWS CAF** provides guidelines to help organizations move to the cloud
- 6 perspectives of AWS CAF
	- **Business perspective**: Business outcomes
	- **People perspective**: Skills, organizational change, and roles
	- **Governance perspective**: Compliance, control, and risk management
	- **Platform perspective**: Infrastructure and application architecture
	- **Security perspective**: Identity, access management, and data protection
	- **Operations perspective**: Operation Efficiency and Resiliency
- Key Benefits of AWS CAF
	- Heavily minimizes service disruption during transition
	- Provides a cloud adoption roadmap
	- Identifies potential challenges
	- Helps optimize costs, performance, and security

### AWS CAF Drives Business Success
- Real World Impact of AWS CAF
	- Accelerated e-commerce expansion
	- Improved risk managements and data governance
	- Faster delivery of digital health services
	- Smart factory solutions using IoT and cloud
	- Improved performance tracking, enhanced security and compliance, smarter innovation, profit tracking
- Strategic Alignment with Business Objectives
	- Business outcomes translated into cloud strategies
	- CAF perspectives, to make sure everything is accounted for
	- Ensures cross-functional collaboration

### Beginner's Guide to AWS Migration Strategies
- AWS migration moves apps and data to the cloud, helping businesses gain flexibility, scalability, and cost savings
- The Three Rs of AWS Migration
	- **Rehost (Lift and Shift)**: Moving an application to the cloud without changing an architecture
		- Example: Planning, tooling, and tracking setup to understand how AWS helps scale to help with less maintenance 
	- **Replatform**: Optimizations, such as moving self-managed databases to manage services (but core app stays the same)
	- **Refactor**: Rearchitecting your application to fully take advantage of cloud features like autoscalin and microservices
- Choosing the Right Strategy
	- Application complexity
		- *Is it easy to life and shift, or does it need a redesign?*
	- Business objectives
		- *Are you optimizing for speed, cost, or innovation?*
	- Budget and resources
		- *Can you support a complex migration*
	- Compliance and risk
		- *With stricter controls, determine how it could be migrated*
- AWS Tools for Easy Migration
	- AWS Migration Hub: Centralized migration tracking
	- AWS Application Migration Service: Simplified lift-and-shift
	- AWS Trusted Advisor: Recommendations on performance, cost, and security

### Moving Data with AWS Snowball and Database Replication
- **AWS Snowball**
	- Secure application for transferring __large datasets__
	- Handles terabytes to petabytes of data
	- Ideal for limited bandwidth scenarios
	- Data is encrypted and tracked end-to-end
- **AWS Database Migration Service**
	- Migrate databases to AWS with minimal downtime
	- Supports homogeneous and heterogenous migrations (SQL)
	- Real-time replication during migration
	- Works with RDS, Aurora, Redshift, and more
- Use Cases in Cloud Migrations
	- Enterprise backup migration
	- Hybrid cloud setup
	- Healthcare data migration
	- Database modernization

### AWS CAF
- Key Topics to Focus On
	- AWS Cloud Adoption Framework
		- Understand the six perspectives: Business, People, Governance, Platforms, Security, and Operations
		- Understand how each one supports cloud readiness and aligns with business goals
	- AWS migration strategies (The 3 Rs)
		- Rehost, Replatform, and Refactor
	- AWS data migration tools
		- AWS Snowball: Used for large offline transfers
		- AWS DMS: Used for real-time database replication
	- Analyze real-world exam scenarios
		- Bandwidth: Limited
		- Downtime: Must be minimized
		- Which migration path would meet a certain business goal