# WA Animals - EventBridge sign-in

## Slack Setup

![Slack Setup 01](img/slack-setup-01.png)

![Slack Setup 02](img/slack-setup-02.png)

![Slack Setup 03](img/slack-setup-03.png)

![Slack Setup 04](img/slack-setup-04.png)

## Serverless Deploy

```bash
# MFA Workaround
response=$(aws sts assume-role --role-arn arn:aws:iam::XXXXXXXXXXXX:role/DevOpsAdmin --role-session-name "Serverless")

# Set Variables
export AWS_ACCESS_KEY_ID=$(echo $response | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $response | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo ${response} | jq -r '.Credentials.SessionToken')
```

```bash
serverless deploy --stage dev
```

## Event Bridge

![Event Bridge Setup 01](img/event-bridge-setup-01.png)

![Event Bridge Setup 02](img/event-bridge-setup-02.png)

![Event Bridge Setup 03](img/event-bridge-setup-03.png)

## Testing

![Event Bridge Test 01](img/event-bridge-test-01.png)
