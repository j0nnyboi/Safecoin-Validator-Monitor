import subprocess
import requests
from discord import Webhook, RequestsWebhookAdapter
from time import gmtime, strftime
ValidatorID = "#ValidatorIP"#valadator ID easiy pleace to find it is https://araviel.io/consensus-arena/
ValidatorCheckTime = 5 #time in minutes
#create your own discord change and create a webhock then copy it below
webhook = Webhook.from_url("Discord Webhock", adapter=RequestsWebhookAdapter())


def DiscordSend():
        webhook.send("your Validator has gone off line")
        
#hour = strftime("%H", gmtime())
#min = strftime("%M", gmtime())
#day = strftime("%d", gmtime())
Minpre = 0
hourpre = 0
Counter = 99
AlarmSent = False
while True:
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
                        
                        


        

