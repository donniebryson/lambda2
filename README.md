# lambda2
Warning! This is not production ready code nor does it perform any real business function. It is only a test run of using AWS Lambda to detect when a file is uploaded to a S3 bucket, start an EC2 instance, run a python data science script that processes the file, writes out the result to another S3 bucket, then shuts down the EC2 instance. 

## References/Sources
https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
https://n2ws.com/blog/aws-automation/lambda-function-s3-event-triggers

## Highlevel overview
There are two S3 buckets: input and output. There are two lambda functions: startEC2 and stopEC2. The lambda function, startEC2, is triggered when a file is uploaded to the input S3 bucket. The lambda function, stopEC2, is triggered when the processing script uploads the finished file to the output bucket. The EC2 instance is a modified anaconda distribution from the AWS marketplace (free) with the instation of fbprophet. The EC2 instance is also modified to execute the load script after boot. The load script reads the input file of retail sales into a dataframe then uses fbprophet to create a time series of predictions. The script then writes the file to the output S3 bucket. 

## Setup Steps
1. Create an appropriate data science EC2 instance. A good start is the Anaconda image from the AWS Marketplace.
2. Install any additional python libraries such as fbprophet.
3. Add process.py which contains the load script to the ec2-user home directory. At the minimum the script must read the input file from the S3 bucket, perform analytics, and write the output file to another S3 bucket. DO NOT USE THE BUCKET FOR INPUT AND OUTPUT. 
4. Create the S3 buckets. 
5. Create the startEC2 and stopEC2 lambda functions. Make sure to up the number of seconds of the timeout for stopEC2 as the source code inserts a wait of 3 seconds to make sure the file is completely copied before it stops the EC2 instance. 
6. Under Properties option for S3 buckets, create an Event that notifies startEC2 when a file is uploaded into the input bucket and another one that notifies stopEC2 when a file is uploaded into the output bucket. 

### Security roles
There are several points during this process that you will be required to set security roles and rules. I am avoiding that discussion as that will change depending on your installation. 
