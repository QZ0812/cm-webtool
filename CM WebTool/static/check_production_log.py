import sys
import paramiko
import time        

def check_log(logcommand):
    print("printing logs")
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("", port=22, username="web1", password="")   
        time.sleep(3)
        stdin,stdout,stderr = client.exec_command(logcommand)
        return stdout.readlines()

    finally:
            client.close()