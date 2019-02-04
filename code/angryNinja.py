import configparser
import slackclient
import os
import argparse

# variable definitions
configFile = '../conf.d/angryNinja.ini'
conf = configparser.ConfigParser ()
conf.read(configFile)

#slack_token = SLACK_API_TOKEN
slack_token = os.environ['SLACK_API_TOKEN']
print(slack_token)
sc = slackclient.SlackClient(slack_token)


try:
    parser = argparse.ArgumentParser(usage="This bot posts messages to desired slack channel")
    parser.add_argument('-c',\
                        '--channel',\
                        required=True,\
                        help="Enter slack channel name")
    parser.add_argument('-m',\
                        '--msg',\
                        required=False,\
                        default="Hello world - this is default message from bot",\
                        help='Enter a message to post')
    args = parser.parse_args()

except Exception as e:

    print("Failed to parse args, Error is : ", str(e))


def postmessage(channel, msg):

    '''this function posts a message to found slack channel'''

    try:

        sc.api_call('chat.postMessage',channel=channel, text=msg)
        print("posted to slack channel")

    except Exception as e:

        print("not able post it to channel, Error is : {}".format(str(e)))


def findchannel(channel):

    ''' This function finds existence of channel '''

    get_channel_list = sc.api_call("channels.list")
    for i in get_channel_list['channels']:
        if i['name'] == channel:
            print("Found channel with name '{}' and id '{}'".format(channel, i['id']))
            print("trying to post to channel")
            postmessage(channel,args.msg)
            break
    else:
        print("no channel found with name '{}'".format(channel))


if __name__ == '__main__':

    print("finding channel from Org, wait a sec..")
    findchannel(args.channel)

