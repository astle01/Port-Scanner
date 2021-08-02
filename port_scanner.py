import socket

p = input("Enter ports range (eg. 1-1000): ")

start,end = p.split("-")
start = int(start)
end = int(end)

for i in range(start,end+1):
    
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('ip_address',i)) #add your target ip address
        print("Port {} is open".format(i))
        s.close()

    except:
        #pass
        print("port {} is closed".format(i))
