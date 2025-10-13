import boto3
import json

# Initialize SQS client
sqs = boto3.client('sqs',region_name='us-east-1') # Set your region
queue_url = 'https://sqs.us-east-1.amazonaws.com/043309324225/trans-queue'

# Example transactional mail payload
transaction_payload = {
    "recipient": "solkeens@yahoo.com",
    "subject": "Your Transaction Alert",
    "body_text": "You just withdrew $500 from your account.",
    "body_html": "<h1>Transaction Alert</h1></p>You withdrew <b>$500</b>.</p>"

}

# Send message to SQS
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(transaction_payload)
)

print("Message sent to SQS.Message ID:", response['MessageId'])

