# Device Management And Log Analyser with Issue Resolver (Architecture)
![UML Diagram](https://github.com/krishnachourasia/AWS-BigData-Architecture/blob/master/Architecture%20Diagram.jpeg)

## Creating Things, Certificates, and Policies
1. Go to IoT Core
2. Create a thing called `device-sensor-1`
    Name it `device-sensor-1` 
3. Create a certificate for the thing
    Certificate for the thing
        One-click certificate
        Download everything
        Download the first AWS certificate SA-1
4. Create a policy for the thing and attach it to the certificate
 
## Test subscribing and publishing to an IoT topic
    1. Subscribe and publish to a topic
    2. Setup a Python virtual environment for the IoT Script

```bash
python3 -m venv venv
source venv/bin/activate
pip install AWSIoTPythonSDK
```


3. Publish to the same topic with the python script
    Edit the script (medical_script.py)
        Change the BROKER_PATH
        Change the Root CA, Private Key and Certificate paths
    Use the script to publish to the topic and see it publish live in the browser

## Create a Rule to Process the Data
        Add action
        Review integrations
        Send message to Amazon Kinesis Firehose
    

## Creating a Firehose Delivery Stream for IoT Rule
    Enter Kinesis or "Create new Resource" on the Configure Action stuff in IoT
    Create the Stream
    Process records 
        Transform Records for Glue - On
    Destination 
        Glue ETL, Kinesis Analytics
    Settings 
        IAM Role - Create a new one 
    Review and create


## Kinesis Analytics Streams
1. Go to Kinesis
2. Create the Analytics Stream using

```sql
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
   
);

CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM   
    
FROM "SOURCE_SQL_STREAM_001"
GROUP BY 
    FLOOR(("SOURCE_SQL_STREAM_001".ROWTIME - TIMESTAMP '1970-01-01 00:00:00') SECOND / 10 TO SECOND);
```
-> It will show data in every 10 Seconds.

## Lambda Function for Continous Monitoring and Alerting
1. Go to Lambda
2. Create a Lambda Function from the blueprints for taking data from Firehouse and creating an SNS alert.
3. Grant the required permission and create a role.
4. Name the Handler and Upload the package details with the files.
5. Use the SNS topic to send notifications from inside the Lambda Function

## Setting up the SNS for Alert
1. Go to SNS
2. Create the topic for Alerting the user
3. Set up the subscriptions with the sms or Email configurations 
4. Or setup a HTTP notification

## Setting up Glue for Incoming Kinesis Stream
1. Go to AWS Glue
2. Create a new Job
3. Configure Job properties
3. Specify the source as the Kinesis Firehouse
4. Transform as required.
5. Specify the Data Target as the S3, (Made by Lake Formation)
6. Set-up the Schema

## Setting up the Lake Formation
1. Go to Lake Formation
2. Register Location, by creating the S3 bucket.
3. Set-up the IAM role for the S3 bucket.
4. Create a database for storing the data and set-up the IAM role.
5. Grant Permissions as required.


## Setting up a Lambda Function for inerting data into Elastic Search from data lake.
1. Go to Lambda
2. Create a Lambda Function from the blueprints for taking data from S3 and to Elastic Search.
3. Grant the required permission and create a role.
4. Name the Handler and Upload the package details with the files.
5. Use the Lambda function to send the data to Elastic Search Service.

## Setting up Elastic Search and Kibana
1. Go to Elastic Search Service
2. Create a domain.
3. Choose the deployment type.
4. Configure the Cluster and access policies as necessary.
5. Set-up the Access and VPC settings.
6. Use the generated end-points to access the Elastic Search.
7. Use the generated Kibana URL to go to the Kibana
8. Register or Log In the Kibana
9. Create Index
10. Discover and Visualize the data as required.

## Setting up Glue for Fetching the data from given Knowledge Base
1. Go to AWS Glue
2. Create a new Job
3. Configure Job properties
3. Specify the source as the the given data source.
4. Transform as required.
5. Specify the Data Target as the S3, (Made by Lake Formation)
6. Set-up the Schema

## Setting up the Amazon Athena
1. Go to Amazon Athena.
2. Create a database and table.
3. Specify the dataset source and name as in S3 Bucket.
4. Create the Data format
5. Set-up the columns and partitions.
6. Use the SQL queries to analyse the data.

## Creating a Machine Learning Model using Amazon Machine Learning or SageMaker

1. Go to Amazon Machine Learning
2. Create a model.
	Specify the dataset source and name as in the S3 bucket Knowledge Base data.
        Set-up the Schema.
        Set the target Column to be predicted.
        Set the Row Id, Review and launch.
        After training test and the model.
3. Get the generated endpoints for the model.
4. Use the endpoints in the Lambda function for classifying the issue and finding the solution with the help of knowledge base.

OR

1. Go to SageMaker
2. Create a model
	Using the Notebooks.
	Train the model.
	Fine tune the model by testing.
	Store the model.
3. Get the generated endpoints for the model.
4. Use the endpoints in the Lambda function for classifying the issue and finding the solution with the help of knowledge base.


## Setting up the DynamoDB Table and Stream
1. Go to DynamoDB Dashboard.
2. Create a new table.
3. Provide the Partition key and sort key as required.
4. On the Overview tab, choose Manage Stream.
5. Choose the information that will be written to the stream whenever the data in the table is modified.
6. After the setting, click Enable.   


## Setting up a Lambda Function for resolving the service desk issue tickets
1. Go to Lambda
2. Create a Lambda Function from the blueprints for taking data from DynamoDB Stream and to generate the SNS Notification.
3. Grant the required permission and create a role.
4. Name the Handler and Upload the package details with the files.
5. Use the Lambda function to use the API endpoints of the ML Model and classify the issue.
6. After classifying, send the required steps docuemnt from the knowledge base using the SNS Topic.

## Setting up the SNS for Replying the solution
1. Go to SNS
2. Create the topic for Replying the user about the steps to perform for solving the issue.
3. Set up the subscriptions with the sms or Email configurations.
4. Or setup a HTTP notification to the caller SDK user.
