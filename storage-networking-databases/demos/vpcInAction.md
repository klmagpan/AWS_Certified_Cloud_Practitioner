# Demo: Exploring Networking Services - VPC in Action

- Action: Navigate to VPC --> Create VPCs
	- Action: VPC and more
		- Within each availability zone, there is a public and private subnet. A Route table connects to public and private subnet in each AZ
		- Internet Gateway: Allows VPC to connect to the internet through public subnet/route table
- Availability zones are isolated from one another. If one fails, doesn't mean another would
	- Action: 2
- Action: VPC endpoint = None
- Create VPC and remember last 4 digits of VPC
	- A default **Network ACL** would be created alongside VPC
		- Operate at subnet level and are stateless (don't remember), so have extra layer of security
	- A default **Security Group** also created
		- Are stateful 
- Exam Tips
	- VPC Setup Rules
	- **Subnet Types: Public and Private**
		- Public: Access from internet
		- Private: Used for internal resources like databases
	- **Route tables** control traffic within the VPC. **Internet Gateway**  is essential for a vpc to communicate with the internet
