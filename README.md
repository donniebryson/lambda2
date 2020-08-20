# lambda2
Warning! This is not production ready code nor does it perform any real production business function. It is only a test run of using AWS Lambda to detect when a file is uploaded to a S3 bucket, start an EC2 instance, run a python data science script that processes the file, writes out the result to another S3 bucket, then shuts down the EC2 instance. 

## References/Sources
https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
https://n2ws.com/blog/aws-automation/lambda-function-s3-event-triggers

## Highlevel overview
There are two S3 buckets: input and output. There are two lambda functions: startEC2 and stopEC2. The lambda function, startEC2, is triggered when a file is uploaded to the input S3 bucket. The lambda function, stopEC2, is triggered when the processing script uploads the finished file to the output bucket. The EC2 instance is a modified anaconda distribution from the AWS marketplace (free) with the instation of fbprophet. The EC2 instance is also modified to execute the load script after boot. The load script reads the input file of retail sales into a dataframe then uses fbprophet to create a time series of predictions. The script then writes the file to the output S3 bucket. 

