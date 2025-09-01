# Lab: Launch an EC2 Instance in a Virtual Private Cloud (VPC)

1. Create a VPC
- Action: Navigate to VPC and create VPC manually (instead of VPC wizard)
	- Under virtual private cloud --> Your VPCs --> Create VPC manually
- VPC Settings
	- Name: my-vpc
	- **IPv4 CIDR block**: Specifies a range of IP addresses for the VPC
		- IPV4 CIDR: 10.0.0.0/16 (means over 65000 IP addresses)
		- No IPv6 CIDR block: No need for additional addresses
	- Tenancy: Default (Using shared hardware)

2. Create a Public Subnet
- **Subnets**: Isolated local networks
	- Launch your resources like an EC2 instance into your subnet 
- Action: Create a subnet under virtual private cloud
	- Choose VPC
	- Name: my-public-subnet
	- Subnet CIDR block: 10.0.0.0/24
- A public subnet has to route traffic to the internet via an internet gateway in order for it to be public


3. Create Routes and Configure Internet Gateway
- Action: Click on subnet --> Actions --> Edit subnet settings --> Enable auto-assign public IPv4 address
- **Internet Gateway**: Enables connection all over the internet
	- Name: my-internet-gateway
- Action: Attach internet gateway to VPC
- Configure Routing: Tells traffic in the public subnet how to get to the internet
	- Action: Route tables
		- A default route table is already created which allows traffic to pass to other nodes w/in network, but doesn't allow to go outside of the network to public internet
	- Name: publicRT
	- Action: Create routing table and edit routes
		- Destination: 0.0.0/0 (public internet)
		- Target: Internet Gateway, specifically my-internet-gateway
- Associate the public route table, that shows how to get to the public internet, to public subnet
	- Action: From Route Tables, subnet associations --> edit subnet associations --> add available subnet --> Save

4. Launch EC2 Instance in Subnet
- Action: Create an EC2 Instance
	- Name: my-public-instance
	- Key pairs are needed to ssh into your instance from a local machine
	- Security Group: Determines what traffic can reach the instance

5. Access EC2 Instance
- Action: View made instance (my-public-instance) --> connect --> EC2 Instance Connect