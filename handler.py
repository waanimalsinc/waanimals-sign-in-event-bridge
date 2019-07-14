import json
import requests
import os

slack_token = os.environ['SLACK_API_TOKEN']
slack_channel_id = os.environ['SLACK_CHANNEL_ID']


def alert(event, context):
    account = event['account']
    user = event['detail']['userIdentity']['arn']
    data = {
        "channel": slack_channel_id,
        "text": "Login to account %s with the identity %s" % (account, user)
    }
    resp = requests.post("https://slack.com/api/chat.postMessage", headers={
        'Content-Type': 'application/json;charset=UTF-8', 'Authorization': 'Bearer %s' % slack_token}, json=data)

    return {}
