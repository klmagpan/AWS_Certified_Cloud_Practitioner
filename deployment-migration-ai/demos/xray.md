# Demo: Using AWS X-Ray to Identify Performance Issues

- X-Ray is a tool which helps developers analyze and debug distributed applications
	- Allows you to troubleshoot the root cause of performance issues and errors
	- Provides a visualization of your application's underlying components

1. Install a sample TicTacToe application
- Action:
	- Navigate to X-ray --> Setup demo app --> Create sample application with CloudFormation
- After it's done creating the sample,
	- Head to sample and to the "Outputs" tab, where you'll find the URL for the load balancer for the application
	- Open the ink to a new tab

2. Play a game of Tic Tac Toe
- Create --> Tic Tac Toe Rules --> Play

3. Use X-Ray to view the application performance and health
- View service map
	- View Errors and examine its trace details
- Metrics: Show's average latency which helps identifies bottlenecks in the application
	- In the case where it's "10s" instead of "ms", then that is an indication that the application is overloaded or doesn't ahve enough capacity --> performance issue

4. Exam Tips:
	- The X-Ray service map provides an end-to-end view of requests as they travel through your application
	- This information can be used to troubleshoot connectivity and performance issues