import json

crontable = []
outputs = []

import requests

postData = {
    "parameter": [
        {
            "name": "ConfigureFile",
            "value": "TestSuite-failed.xml"
        },
        {
            "name": "Mode",
            "value": "Engineer"
        },
        {
            "name": "TESTFOLDER",
            "value": "T:\\Integration_Linkdrill"
        },
        {
            "name": "APK_HOME",
            "value": "T:\\Integration_Linkdrill\\Apps"
        },
        {
            "name": "mail_recipients",
            "value": "rgu@microstrategy.com"
        },
        {
            "name": "Comment",
            "value": ""
        },
        {
            "name": "DeviceGroup",
            "label": "android_geny_N7"
        }
    ],
    "statusCode": "303",
    "redirectTo": "."
}
hostURL = "http://10.197.84.226:8011/jenkins/job/mstr_Android_Integration_Linkdrill/build?delay=0sec"


def process_message(data):
    payload = {'json': 'value1', 'key2': 'value2'}
    if data['channel'].startswith("D"):
        if data['text'].startswith("run all"):
            trigger_build('TestSuite-origin.xml')
            outputs.append([data['channel'], "I will rerun failed cases"])
        elif data['text'].startswith("run fail"):
            trigger_build('TestSuite-failed.xml')
            outputs.append([data['channel'], "I will rerun failed cases"])
        elif data['text'].startswith("run"):
            trigger_build('TestSuite-one.xml')
            outputs.append([data['channel'], "I will do the tests"])
        # else:
        #     outputs.append([data['channel'], "from repeat1 \"{}\" in channel {}".format(data['text'], data['channel'])])


def trigger_build(test_suit_name):
    postData['parameter'][0]['value'] = test_suit_name
    payload = {'json': json.dumps(postData), 'Submit': 'Build'}
    requests.post(hostURL, data=payload)
