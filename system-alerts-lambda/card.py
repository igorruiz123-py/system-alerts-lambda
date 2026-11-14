def build_cpu_alarm_card(ec2_name, timestamp, lambda_function_name, chat_id):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"🚨 **EC2 CPU Usage Alarm**\n\n EC2 instance running with CPU usage above 10%\n\n **Instance Name**: {ec2_name}\n\n **Date**: {timestamp}\n\n **Lambda Name**: {lambda_function_name}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }

    return card


def build_cpu_ok_card(ec2_name, timestamp, lambda_function_name, chat_id):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"✅ **EC2 CPU Usage Alarm**\n\n EC2 instance returned to run with CPU usage under 10%\n\n **Instance Name**: {ec2_name}\n\n **Date**: {timestamp}\n\n **Lambda Name**: {lambda_function_name}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }
    
    return card

def build_system_updates_card(ec2_name, timestamp, chat_id, os_name, lambda_name):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"✅ EC2 System Updated\n\n EC2 instance updated successfully its OS system\n\n Instance Name: {ec2_name}\n\n Date: {timestamp}\n\n Server OS: {os_name}\n\n Lambda Name: {lambda_name}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }

    return card

def build_storage_alarm_card(ec2_name, timestamp, lambda_function_name, chat_id, disk_name, disk_usage):

    card = {
        "chat_id": f"{chat_id}",
        "text": f"🚨 EC2 Storage Usage Alarm\n\n EC2 instance running with SSD storage usage above 50%\n\n Instance Name: {ec2_name}\n\n Date: {timestamp}\n\n Lambda Name: {lambda_function_name}\n\n Disk Name: {disk_name}\n\n Disk Usage: {disk_usage}",
        "parse_mode": "Markdown",
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "Open AWS Console",
                        "url": "https://console.aws.amazon.com/"
                    }
                ]
            ]
        }
    }

    return card