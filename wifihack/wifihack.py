import subprocess

info = subprocess.run("netsh wlan show profile", capture_output=True).stdout.decode()
TempNames = info.split("    All User Profile     : ")
Names = []
Password = []

# Getting all Names:
for name in TempNames:
    if (name.split("\r")[0] != ""):
         Names.append(name.split("\r")[0])

#Getting all Passwords:
for name in Names:
    Profie = subprocess.run(["netsh","wlan","show","profile",'"'+name+'"',"key=clear"],capture_output=True).stdout.decode()
    try: Password.append(Profie.split("    Key Content            : ")[1].split("Cost settings")[0].split("\r")[0])
    except: Password.append("Not Present")
    
# Sending all to file:
File = open("Password", "w")
for i in range(len(Names)):
    line = Names[i] + " :       " + Password[i] + "\n"
    File.write(line)