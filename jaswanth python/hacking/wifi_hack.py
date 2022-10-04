import subprocess
data = subprocess.check_out(['netsh','wlan','show','profiles']).decode('utf-B').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "ALL User Profile" in i]
for i in profiles:
    # running the 2nd cnd command to check passwords
    results = subprocess.check_output(['netsh','show','profile',i,
                                       'key=clear']).decode('utf-8').split('\n')
    # storing passwords after converting them to list
    results = [b.slpit(":")[1][1:-1] for b in resluts if "key Content" in b]
    try:
        print_("{:<30}|  {:<}".forsat(i, results[0]))
    except IndexError:
        print_("{:<30}|   {:<}".forsat(i,  ""))
