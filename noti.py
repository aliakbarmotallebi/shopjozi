from pynotifier import Notification
import requests
import time
import json
import os

import debugger

def send_notification(descr):
    Notification(
        title='http://ShopJozi.ir',
        description=descr,
        icon_path='app_icon.ico',
        duration=0,
        urgency=Notification.URGENCY_CRITICAL
    ).send()


def main():
    url = "http://shopjozi.ir/orders"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        resp = json.loads(request.text)
        count = resp['count']
        if count > 0:
            text = f"""
			تا سفارش جدید دارید ({str(count)})
			آخرین سفارش مشتری
			({resp['customer']['first_name']} {resp['customer']['last_name']})
			می باشد.
			"""
            send_notification(text)

    except (requests.ConnectionError, requests.Timeout) as exception:
        logging.debug('internet problem')


if __name__ == '__main__':
    main()
