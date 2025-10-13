import json
import boto3

# Initialize the SES client with correct region
ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
     for record in event['Records']:
      try:
            # Parse message from SQS
            message = json.loads(record['body'])

            recipient = message['recipient']
            subject = message['subject']
            body_text = message.get('body_text', '')
            body_html = message.get('body_html', '')

            # Send email
            response = ses.send_email(
                Source='oogunleti@solkeenstechnologies.com',  # Must be verified in SES
                Destination={'ToAddresses': [recipient]},     # Pulled from message
                Message={
                'Subject': {'Data': subject},
                'Body': {
                       'Text': {'Data': body_text},
                        'Html': {'Data': body_html}
                    }
                }
            )

            print(f"✅ Email sent to {recipient}. SES Message ID: {response['MessageId']}")

        except Exception as e:
            print(f"❌ Failed to send email: {str(e)}")
            raise e