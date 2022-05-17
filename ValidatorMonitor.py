import subprocess
import requests
from discord import Webhook, RequestsWebhookAdapter
from time import gmtime, strftime,sleep

from safecoin.keypair import Keypair
from safecoin.rpc.api import Client
from safecoin.rpc.types import MemcmpOpts
from safecoin.publickey import PublicKey
api_endpoint="https://api.mainnet-beta.safecoin.org"
client = Client(api_endpoint)



########################################## Need to add your Validator ID & Webhock ############################################################
ValidatorID = None
Discord_Web_Hock = None
f = open("Config.txt", "r")
lines = f.readlines()
for line in lines:
    if("##") in line:
        continue
    if("ValidatorID") in line:
        ValidatorID = line.split("=")[1].strip()
        
    if("Discord_Web_Hock") in line:
        Discord_Web_Hock  = line.split("=")[1].strip()
        


if(Discord_Web_Hock == None or ValidatorID == None):
        print("Please enter correct details in the config.txt")
        exit()
if("Discord_Webhock" in Discord_Web_Hock):
        print("please enter discord webhock")
        exit()
if("ValidatorID" in ValidatorID):
        print("please enter your Validator ID")
        exit()
        
print("Your Validator ID = ",ValidatorID)
print("Your Discord_Web_Hock = ",Discord_Web_Hock)       
print("Any safecoin Donations at es7DKe3NyR1u8MJNuv6QV6rbhmZQkyYUpgKpGJNuTTc")
########################################## Safecoin Donations taken at es7DKe3NyR1u8MJNuv6QV6rbhmZQkyYUpgKpGJNuTTc ############################
###############################################################################################################################################



ValidatorCheckTime = 5 #time in minutes
webhook = Webhook.from_url(Discord_Web_Hock, adapter=RequestsWebhookAdapter())

def DiscordSend():
        webhook.send("Your validator has gone off line")
        
#hour = strftime("%H", gmtime())
#min = strftime("%M", gmtime())
#day = strftime("%d", gmtime())
Minpre = 0
hourpre = 0
Counter = 99
AlarmSent = False
while True:
        sleep(10)
        Min = strftime("%M", gmtime())
        hour = strftime("%H", gmtime())
        if(hour != hourpre):
                hourpre = hour
                AlarmSent = False
        if(Min != Minpre):
                Minpre = Min
                Counter += 1
                if(Counter >= ValidatorCheckTime):
                        Counter = 0
                        if(client.is_connected() == True):
                            validatorList = (client.get_vote_accounts()['result']['delinquent'])
                            print("Latest delinquent validators")
                            for vals in validatorList:
                                ValPubkey = vals['nodePubkey']
                                print(ValPubkey)
                                if(ValidatorID in ValPubkey):
                                    print("^^^^^^^^^^^^found my Validator^^^^^^^^^^")
                                    if(AlarmSent == False):
                                        DiscordSend()
                                        AlarmSent = True
                            print("")
                        else:
                            client = Client(api_endpoint)                        
                        
                        
                        
