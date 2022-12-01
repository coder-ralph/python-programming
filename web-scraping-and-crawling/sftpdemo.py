import argparse
import paramiko
import getpass

SOURCE = 'C:\\Users\\ralph\\Music\\python-projects\\file1.txt'
DESTINATION = 'C:\\Users\\ralph\\Music\\python-projects\\backup\\'

def copy_file(hostname,port,username,password,src,dest):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    print("Connecting to %s \n username=%s....\n" %(hostname,username))

    t = paramiko.Transport(hostname,port)
    t.connect(username=username,password=password)
    sftp = paramiko.SFTPClient.from_transport()
    print("Copying file %s to %s" %(src,dest))
    sftp.put(src.dest)
    sftp.close()
    t.close()

# it will run the ff IF this script is called by this file only
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Remote file copy')
    parser.add_argument('--host', action="store",dest="host",default='localhost')
    parser.add_argument('--port', action="store",dest="port",default=22,type=int)
    parser.add_argument('--src', action="store",dest="src",default=SOURCE)
    parser.add_argument('--dst', action="store",dest="dst",default=DESTINATION)
    given_args = parser.parse_args()

    # from args, transfer to variables to use when we call the function
    hostname,port = given_args.host,given_args.port
    src,dest = given_args.src,given_args.port
    username = input("Enter username:")
    password = getpass.getpass("Enter password:")
    copy_file(hostname,port,username,src,dest)
    print("SFTP Transfer ok")
