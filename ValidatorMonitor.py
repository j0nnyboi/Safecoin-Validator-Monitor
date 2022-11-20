
import requests
from discord import SyncWebhook
from time import gmtime, strftime,sleep

from safecoin.keypair import Keypair
from safecoin.rpc.api import Client
from safecoin.rpc.types import MemcmpOpts
from safecoin.publickey import PublicKey

api_endpoint="https://api.mainnet-beta.safecoin.org"
client = Client(api_endpoint)



########################################## Need to add your Validator ID & Webhock in config.txt ############################################################

ValidatorID = None
Discord_Web_Hock = None
f = open("Config.txt", "r")
lines = f.readlines()
for line in lines:
    if("##") in line:
        continue
    elif("ValidatorIDENTITY") in line:
        ValidatorID = line.split("=")[1].strip()
        
    elif("Discord_Web_Hock") in line:
        Discord_Web_Hock  = line.split("=")[1].strip()
        
    elif("ValidatorVOTE") in line:
        ValidatorVote = line.split("=")[1].strip()
        
    elif("VoteBalanceWarn") in line:
        VoteBalanceWarn = int(line.split("=")[1].strip())

    elif("IdentityBalanceWarn") in line:
        IdentityBalanceWarn = int(line.split("=")[1].strip())
        


if(Discord_Web_Hock == None or ValidatorID == None):
        print("Please enter correct details in the config.txt")
        exit()
if("Discord_Webhock" in Discord_Web_Hock):
        print("please enter discord webhock")
        exit()
if("ValidatorIDENTITY" in ValidatorID):
        print("please enter your Validator Identity")
        exit()
if("ValidatorVOTE" in ValidatorVote):
        print("please enter your Validator Vote")
        exit()

print("Safecoin Donations at es7DKe3NyR1u8MJNuv6QV6rbhmZQkyYUpgKpGJNuTTc")        
print("Your Validator Identity = ",ValidatorID)
print("Your Validator Vote = ",ValidatorVote)
print("Vote account warn amount = ",VoteBalanceWarn)
print("Vote account warn amount = ",IdentityBalanceWarn)
print("Your Discord_Web_Hock = ",Discord_Web_Hock)
print()


########################################## Safecoin Donations taken at es7DKe3NyR1u8MJNuv6QV6rbhmZQkyYUpgKpGJNuTTc ############################
###############################################################################################################################################


ValidatorCheckTime = 5 #time in minutes between checking for you validator is off line

def DiscordSend(StringToSend):
        webhook.send(StringToSend)


webhook = SyncWebhook.from_url(Discord_Web_Hock)

Minpre = 0
Daypre = 0
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
                day = strftime("%d", gmtime())
                if(day != Daypre):
                    Daypre = day
                    if(client.is_connected()): 
                        VoteBalance = int(client.get_balance(ValidatorVote)['result']['value'])/1000000000
                        print("Vote account balance = ",VoteBalance)
                        if(VoteBalance > VoteBalanceWarn):
                            DiscordSend("you have earnt to much safe, to be on your validator, time to move it,amount is %s use (~/Safecoin/target/release/safecoin withdraw-from-vote-account VoteAddress DesternationWallet amount)"% VoteBalance)
                        IDBalance = int(client.get_balance(ValidatorID)['result']['value'])/1000000000
                        print("Identity account balance = ",IDBalance)
                        if(IDBalance < IdentityBalanceWarn):
                            DiscordSend("Running out of safe, you only have %s left to vote with, please add some to address %s" % (IDBalance,ValidatorID))
                    else:
                        client = Client(api_endpoint)
                
        if(Min != Minpre):
                Minpre = Min
                Counter += 1
                if(Counter >= ValidatorCheckTime):
                        Counter = 0
                        if(client.is_connected() == True):
                            validatorList = (client.get_vote_accounts()['result']['delinquent'])
                            print("Latest delinquent validators")
                            for vals in validatorList:
                                nodePubkey = vals['nodePubkey']
                                votePubkey = vals['votePubkey']
                                print(nodePubkey,votePubkey)
                                if(ValidatorID in nodePubkey or ValidatorID in votePubkey):
                                    print("^^^^^^^^^^^^^^^^^^^found my Validator^^^^^^^^^^^^^^^^^^")
                                    if(AlarmSent == False):
                                        DiscordSend("Your validator has gone off line")
                                        AlarmSent = True
                            print("")
                        else:
                            client = Client(api_endpoint)                        
                        
                        
                        

