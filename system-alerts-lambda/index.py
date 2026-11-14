import json
import urllib.request
from card import (
    build_cpu_alarm_card,
    build_cpu_ok_card,
    build_system_updates_card,
    build_storage_alarm_card
)
from os import getenv
from datetime import datetime
from zoneinfo import ZoneInfo

dict_ = {
    "i-0e340f85371539836": "cloudsocket-server"
}

TOKEN = getenv("TELEGRAM_TOKEN")
CHAT_ID = getenv("TELEGRAM_CHAT_ID")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def lambda_handler(event, context):

    print(json.dumps(event, indent=2))

    lambda_name = context.function_name

    timestamp = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y - %H:%M:%S")

    message = event["Records"][0]["Sns"]["Message"]
    alarm = json.loads(message)

    if alarm.get("AlarmName") == "EC2 CPU Usage Alarm":

        instance_name = None

        for i in dict_:

            if alarm["AlarmContributorAttributes"]["InstanceId"] == i:
                instance_name = dict_[i]
                break

            else:
                continue

        if alarm["NewStateValue"] == "OK":

            payload = build_cpu_ok_card(
                instance_name,
                timestamp,
                lambda_name,
                CHAT_ID
            )

        elif alarm["NewStateValue"] == "ALARM":

            payload = build_cpu_alarm_card(
                instance_name,
                timestamp,
                lambda_name,
                CHAT_ID
            )

    elif alarm["alarm_id"] == "system_updates_alarm":

        ec2_name = alarm["hostname"]

        os_name = alarm["OS"]

        payload = build_system_updates_card(ec2_name, timestamp, CHAT_ID, os_name, lambda_name)

    elif alarm["alarm_id"] == "storage_alarm":

        ec2_name = alarm["hostname"]

        disk_name = alarm["disk"]

        disk_usage = f"{alarm["usage_percent"]}%"

        payload = build_storage_alarm_card(ec2_name, timestamp, lambda_name, CHAT_ID, disk_name, disk_usage)

    else:

        print(f"Unknown notification format: {alarm}")

        return {
            "statusCode": 400,
            "body": "Unknown notification format"
        }

    if not payload:

        print("No notification payload generated.")

        return {
            "statusCode": 400,
            "body": "Failed to generate notification payload"
        }

    data = json.dumps(payload).encode('utf-8')

    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

    with urllib.request.urlopen(request) as response:

        if response.status == 200:
            print("Message sent successfully!")
        else:
            print(f"Error sending message: {response.status}")