import socket
from datetime import datetime
import sys
import pyfiglet

banner = pyfiglet.figlet_format("port scanner")
print(banner)
f = open("Report.txt", "w+")
target = input(print("Enter target : "))
print("scanning {}".format(target))
host = socket.gethostbyname(target)

x = int(input("Enter starting port : "))
y = int(input("Enter Ending port : "))

f.write("\nScanned {} From port {} to {}".format(target, x, y))

fqdn = socket.getfqdn(target)
print("\nFQDN : {}".format(fqdn))
f.write("\nFQDN : {}".format(fqdn))

start_time = datetime.now()
print("Started at : {}".format(start_time.strftime("%H:%M:%S")))

f.write("\nstart time :{}".format(start_time.strftime("%H:%M:%S")))

print("\nPort \tState \tServices")
f.write("\n\nPort \tState \tServices")

try:
    for port in range(x, y):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                # print("Scanning port : {}".format(port, socket.getservbyport(port, "tcp")))
                print("{} \topen \t{}".format(port, socket.getservbyport(port, "tcp")))
                f.write("{} \n\topen \t{}".format(port, socket.getservbyport(port, "tcp")))
            except socket.error:
                print("{} \topen \t{}".format(port, "unknown"))
                f.write("{} \n\topen \t{}".format(port, "unknown"))
except socket.gaierror:
    print("Hostname couldn't resolved....Exiting")
    f.write("\n\nHostname couldn't resolved....Exiting")
    sys.exit()
except socket.error:
    print("Could not connect to the server....Exiting")
    f.write("\n\nCould not connect to the server....Exiting")
    sys.exit()

end_time = datetime.now()
print("\nEnded at : {}".format(end_time.strftime("%H:%M:%S")))
f.write("\nEnded at : {}".format(end_time.strftime("%H:%M:%S")))
total_time = end_time - start_time
print("Total time taken :{}".format(total_time))
f.write("\n\nTotal time taken :{}".format(total_time))
