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
print(client.is_connected())


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
        #exit()
if("ValidatorID" in ValidatorID):
        print("please enter your Validator ID")
        exit()
        
print("Your Validator ID = ",ValidatorID)
print("Your Discord_Web_Hock = ",Discord_Web_Hock)       
print("Any safecoin Donations at 3Vt2aF7ZL1A9e8nPPofp4o5GuhY6EGeeLsfvSM3PmctU")
########################################## Safecoin Donations taken at es7DKe3NyR1u8MJNuv6QV6rbhmZQkyYUpgKpGJNuTTc ############################
###############################################################################################################################################
validatorList = (client.get_vote_accounts()['result']['delinquent'])
for vals in validatorList:
    print(vals['nodePubkey'])
    if("ASGqBtTsxdSPDnop8MjmUgPAoTNzDSXiGGeygqZkGLzo" in vals['nodePubkey']):
        print("^^^^^^^^^^^^found my Validator^^^^^^^^^^")
"""

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
                        proc = subprocess.Popen(["~/Safecoin/target/release/safecoin validators"], stdout=subprocess.PIPE, shell=True)
                        (out, err) = proc.communicate()
                        lines = ""
                        DilValList = []
                        for char in out:
                                #print(chr(char))
                                lines = lines + chr(char)
                        lines = lines.split('\n')
                        for line in lines:
                                linesplit = line.split()
                                try:
                                        if('â' in linesplit[0]):
                                                #print(linesplit)
                                                if(ValidatorID in linesplit[2]):
                                                        print("found my valiadator")
                                                        if(AlarmSent == False):
                                                                DiscordSend()
                                                                AlarmSent = True
                                                print(linesplit[2],linesplit[3])
                                                DilValList.append(linesplit[2])
                                except:
                                        continue
                        
                        


        
"""
