# Cloud Foundations and Compute

## Building Your Foundational AWS Knowledge

### About the Exam

-   Key Exam Domains
    -   Cloud Concepts: Benefits of Cloud Computing
    -   Security and Compliance: Shared responsibility model, identity, compliance standards
    -   Cloud Technology and Services: Core services
        - Compute
        - Storage networking and databases
    -   Billing, Prices, and Support: AWS pricing models, cost management, support plans

### Types of Cloud Services

- Cloud computing is a collection of different services used to run applications, store data, and manage IT services
- **Infrastructure as a Service (IaaS)**
    - The foundation of cloud computing 
        - Businesses rent computing powers/storage/networking on demand from the cloud provider
    - Delivery of fundamental computing resources, virtualized hardware, storage, and networking
    - How it works
        - Users rent IT infrastructure on a pay-as-you go basis
        - Providers manage the physical hardware while users manage the operating systems and applications
    - *Virtualization, Servers, Storage, and Networking*
    - Control operating system, middleware, and applications, but AWS handles infrastructure beneath
- **Platform as a Service (PaaS)**
    - Builds on top of IaaS by removing the need to manage servers, operating systems, and middleware
    - Cloud computing model that allows customers to develop, run, and manage applications without dealing with underlying infrastructure
    - How it works:
        - Providers offer hardware, software tools, and hosting
        - Developers focus on application logic rather than infrastructure management
    - *Runtime, Middleware, O/S, Virtulization, Servers, Storage, Networking* 
- **Software as a Service (SaaS)**
    - Most user-friendly cloud model
        - Instead of worrying about infrastructure or coding, access directly over the internet
    - Delivery of software applications over the internet on a subscription basis
    - How it works:
        - Third-party cloud provider hosts, maintains, and updates the software
        - End users access the software via a web browser or API
    - *Applications, Data, Runtime, Middleware, O/S, Virtualization, Servers, Storage, Networking*
- Differences Between On-premises and Cloud Services
    - On-premises (Buy/Install/Maintain Own Service)
        - Infrastructure is owned and managed by the organization
        - Requires high upfront Capital Expenditure (CapEx) for hardware setup
        - Scalability is limited by physical capacity and current infrastructure
        - Maintenance, upgrades, and security are managed in-house
        - Deployment is slower and requires extensive planning and physical setup
    - Cloud Services
        - Cloud infrastructure is rented and managed externally
        - Uses a pay-as-you-go model to lower upfront costs
        - Unlimited scalability with on-demand resoures
        - Cloud provider automatically manages maintenance and updates
        - Emables rapid deployment and flexible management to adapt to demand changes

### Cloud Computing
- Cloud computing is a delivery of computing resources including storage, process power, databases
- Cloud computing enables users to access IT resources when needed without handling the underlying infrastructure
    - Computing power: Virtual machines, containers, serverless computing
    - Storage: Object, block storage, even backup solution
    - Networking: Load Balancing, DNS services
    - Applications: Web applications, mobile apps, enterprise software, Software as a Service solutions, etc.
- Core characteristics of Cloud Computing
    - On-demand access: Resources provisioned whenever needed
    - Access from anywhere: Any device with internet access
    - Shared resources: Multi-tenant
    - Scalability: Servers adjust automatically to meet demand of end users
    - Pay as you go: Aligns cost with use

### AWS Shared Responsibility Model
- Don't have to worry about securing the cloud itself, but are responsible for protecting what's inside
- AWS responsibility 
    - Provides a secure foundation
    - Build and maintain hardware, networking, storage, and data centers
- Your responsibility
    - Managing applications/data, controlling access, and keeping software/security settings updated
- **Elastic Cloud Compute (EC2)**
    - Virtual server
    - Get a machine in the cloud that runs like a computer without having to worry about the hardware
        - Responsibile for installing/managing the operating system, updating and securing applications and software, and protecting your data
    - AWS is responsible for physical servers and network connections, the hypervisor
        - A software that runs the virtual machine and keeping data centers safe and operational 
    - Example: EC2 is the apartment and AWS is the landlord
- **Amazon RDS or Relational Database Service**
    - Resposible for configuring the database settings, managing who has access to it, and securing the data
    - AWS is responsible for setting up and running the database engine, patching/updating the system, and automated backups/infrastructure security
    - Example: A managed email service 
- **AWS Lambda**
    - Don't need to worry about the services
    - AWS runs your code only when needed and you don't have to manage infrastructure at all
        - Responsible for writing/uploading code, configuring how/when it runs, and then managing permissions, who/what can trigger it
            - Therefore handling traffic increases and managing the operating system in runtime environment
    - Manage the setup

### AWS and Customer Responsibilities Across Services
- **IaaS**
    - AWS manages networking, stores, virtualization, and physical service
    - Customers manage operating system, middleware, applications and data
- **PaaS**
    - AWS manages OS, database engine, and updates
    - Customers control data security, access management, and configurations
- **SaaS**
    - AWS manages everything except for code and data
    - Customers only write and deploy code without worrying about the infrastructure
- Moving from up to down, AWS takes on more responsibility and your operational burden decreases
    - Reduce operational burden: Handling updates, patches, and security
    - Increased scalability: Automatically adjusts resources on demand
    - Increased reliability: Built-in redundancy and backup to reduce downtime
    - Seamless Integration: AWS services work together, making it easy to move from a server to a software or to a database

### AWS Regions and Availability Zones
- **AWS Regions**: A geographic area that houses multiple availability zones
    - 36 regions world-wide
- **Availability Zones (AZ)**: A data center or a group of data centers within a region with independent power, cooling, and networking
    - 114 availability zones
- If a data center fails, AWS automatically shifts traffic to another AZ
    - Users don't experience downtimes because the AZs keep handling requests
        - Load balancing: Distributes traffic across AZs
    - If entire region goes down, business using multiple regions can still automatically shift to another region AZ

### AWS Edge Locations Deliver Faster Services
- **Edge Locations** are part of a content delivery network and are designed to store and deliver content closest to users
    - Reduces the distance data needs to travel
    - Reduces latency, the delay before data is delivered
- Exist outside of AWS regions placed in cities worldwide
- Cache/serve data outside of AWS regions
- Uses **CloudFront** and **Global Accelerator** to improve speed and reliability
    - CloudFront caches frequently accessed content at Edge Locations and reduces the load on the main AWS region by serving static and dunamic content from the closest edge
        - Distributes content through a network of edge locations worldwide
        - Caches static and dynamic content closer to end-users, reducing latency
        - Works seamlessly w/ other AWS services to enhance scalability and security
    - Global Accelerator optimizes routing for the user traffic by finding the fastest/most reliable path from the user to the AWS service
        - Routes user traffic through the AWS global network for lower latency
        - Provides static IP addresses and rapid failover for resilient application delivery
        - Automatically directs users to the nearest and healthiest endpoints for faster response times

### Building Reliable and Secure Systems and AWS Frameworks
- Pillars of AWS Well-architected Framework
    - Operational excellence, Security, Reliability, Performance Efficiency, Cost Optimization
- Failover mechanisms such as shifting
- Automated monitoring and scaling mechanisms
- Security mechanisms that only allow users to access the infrastructure
- Best Practices for Scalable and Secure Applications
    - Use managed services
    - Employ infrastructure as code
    - Automate your deployments with security checks
    - Conduct regular security reviews

### AWS Account
- AWS Billing: AWS Billing Conductor, Billing and Cost Management
- Monitoring Service: CloudWatch
- CloudShell: Interact through services in a Linux service

### Exam Cloud Concepts
- AWS Well-architected Framework
- AWS Shared Responsibility Model
- How do regions and zones keep your servies running
- How do AWS edge locations deliver faster services
- Common Pitfalls to Avoid
    - Overloading on details
    - Cramming
    - Underestimating time required to take the exam
