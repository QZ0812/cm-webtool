
print("starting server")
    # try:
    #     print("starting server")
    #     client = paramiko.SSHClient()
    #     client.load_system_host_keys()
    #     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     client.connect("", port=22, username="web1", password="")
    #     time.sleep(3)
    #     stdin,stdout,stderr = client.exec_command("supervisorctl start mono")
    #     print ("Result: {} {}".format(server, stdout.readlines()))

    # finally:
    #         client.close()