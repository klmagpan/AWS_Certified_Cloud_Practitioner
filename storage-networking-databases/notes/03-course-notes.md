# Storage, Networking, and Databases

## Database Technology and Services Lecture

### Databases: The Bigger Picture
- A **database** is a systematic collection of data
- Types of AWS Databases
	- Relational databases (ie. AmazonRDS): organized shelves where everything's in order
	- NoSQL databases (ie. DynamoDB): easy access bins
	- In-Memory Databases (ie MemoryDB): chef's table
	- Graph databases (ie. Amazon Neptune): visualization board
- Relational Databases: Stores/provides access to adata that is organized into rows and columns (like a table)
	- Use Cases: E-commerce (inventory), Mobile backends (use authentications, user preferences), Healthcare Applications (records and appointment scheduling)
- NoSQL databases: Each bin might be marked with a unique label/key, with each ingredient having 
- In-Memory Databases: Store data in the computer's main memory in the RAM, instead of slower disk storage --> read much faster than traditional databases
- Graph Databases: Handle data with complex relationships and interconnections
	- Ideal for fraud detection, recommendation systems, or drug discovery
- Exam Tips
	- Understand the difference between
		- Relational: Structured
		- NoSQL: Flexibility
		- In-memory: Speed
			- MemoryDB: An in-memory database
			- ElastiCache: An in-memory data store and cache service
		- Graph

### Understanding AWS Database Migration Services
- **AWS Database Migration Service (DMS)** helps migrate databases to AWS quickly and securely, without losing quality/integrity
		- Example: A specialized moving team for kitchen
	- Can handle Oracle, MySQL, PostgreSQL, Microsoft SQL server
	- **Simple to Use**: No drivers or changes to the source database needed
	- **Minimal Downtime**: Continuously replicate data during migration, keeping the source database operational
	- **Reliable**: Self-healing with constant monitoring
	- **Database Consolidation**: Consolidates multiple databases into one
- **AWS Schema Conversion Tool (SCT)** helps convert database schema, the blueprint of how the database is constructed, of your source database into a format compatible with AWS target databases
	- Schema and Code Conversion: Automatically converts source database schema for AWS compatibility
	- Handling Conversion Challenges: Provides solutions for potential migration challenges
- Use Cases of AWS Database Migration Service (AWS DMS)
	- Migrating b/w database platforms (ie. Oracle to Amazon Aurora)
	- Consolidating Multiple Databases into a Single Database
	- Continuous Data Replication (for disaster recovery)
	- Migrating Data to the AWS Cloud for Analytics
	- Data Center Decommission
- Exam Tips
	- Understand what is DMS (moving service for databases) and SCT (converts database language/schema to be compatible with AWS)
	- Know when and why database migration is necessary and its benefits

### Amazon DynamoDB
- **DynamoDB** is a fully managed NoSQL database service
	- Each bin might be marked with a label/key and inside each bin are the ingredients are correspond to that label
	- It allows you to store/retrieve any amount of data and serve any level of request traffic
	- Automatically scales up and down for performance and capacity
- Key Features
	- Performance at Scale: Maintains consistent, single-digit millisecond response times
	- Fully Manages: No server management or maintenance required
	- Built-in Security: Data is encrypted at rest and in transit
	- Backup and Restore: Supports on-demand and continuous backups
- DynamoDB Use Cases
	- Web and Mobile Applications: Can scale dynamically --> Handle large volumes of traffic/data, making ideal for apps with variable user loads
	- Gaming Applications: Low latency data access for real-time experience
	- IoT Applications: Handle massive volumes of data in scalability (more than relational)
	- E-commerce platforms: inventory, user data, etc. (more than relational data)
- Exam Tips
	- DynamoDB is a NoSQL Service
	- Key Features: Scalability, Performance, Security, Restorability

### Overview of Memory-Based Databases in AWS
- **Memory-based databases** store data in RAM instead of traditional storage (quick access for important items)
	- Faster data retrieval and processing
- **Amazon MemoryDB** is a Redis-compatible fully managed in-memory database service designed for modern applications that require ultra fast data access
	- **Redis** is an open source in-memory data sotre
	- Performance: Delivers data with ultra-fast response times
	- Data Durability: Automatically replicates data across multiple AWS Availability Zones (data safe during failure)
- Amazon MemoryDB for Redis Use Cases
	- Caching for Web Applications: Provides faster data retrieval than relational databases
	- Real-Time Analysitcs: Excels in real-time data processing --> immediate insights
	- Session Store for Applications: Quicker data access for session management than disk-based resources
	- Leaderboards and Gaming: Fast read/write capabilities outperform relational databases
	- Geospatial Data Processing: Supports complex data structures, with faster querying and data manipulation
- Exam Tips
	- MemoryDB offers ultra-fast performance
	- Fully compatible with Redis
	- Automatically replicates data
	- Ideal for real-time analytics, session stores, & gaming leaderboards

### Database Exam Tips
- AWS Database Services
	- Relational databases (Amazon RDS) are structured/Organized
		- Store and provide access to data that is organized into rows/columns
		- Supports vairous database engines: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server
		- Ideal for structured data storage, complex queries, and transactional applications
		- Example Use: E-commerce platforms to manage inventory, customer orders, or product catalogs
	- NoSQL databases (DynamoDB) provide more flexibility with key-value pairs
		- DynamoDB is ideal for applications that need consistent, single-digit millisecond latency
		- Highly scalable and managed --> perfect for mobile, web, and IoT applications
		- Automatically scales up/down to adjust capacity and maintain performance
	- In-memory databases (MemoryDB for Redis) offer rapid data access
		- Automatically replicates data across multiple AWS availability zones
		- Ensures data durability and high availability for real-time session leaderboards
	- Graph databases (Neptune) handle complex relationships and interconnections, ideal for fraud detection or recommendation systems
- AWS Database Migration Service (DMS) migrate databases to AWS cloud with minimal downtime
	- Support homogenous/hetereogenous migrations 
- AWS Schema Conversion Tool (SCT) helps convert the database schema (blueprint of how database is constructed) of your source database into a format compatible with AWS target databases


## Database Technology and Services Quiz