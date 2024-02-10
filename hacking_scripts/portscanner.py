import socket as s
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print(f'\n[-_0 Scanning Target] {target}')
    print(f'[+] Scanning Port : Service Version')
    print('------------------------------------')
    port_list = [21,22,23,53,80,8080,3306,443,445,111,3386]
    #for port in range(1,100):
    for port in port_list:
        port_scan(converted_ip,port)

def check_ip(ip_address):
    try:
        IP(ip_address)
        return ip_address
    except ValueError:
        return s.gethostbyname(ip_address)

def port_scan(ip_address,ports): 
    try:
        sock = s.socket()
        sock.settimeout(1)
        sock.connect((ip_address,ports))
        try:
            banner = get_banner(sock)
            print(f'[+] Port {ports} Is Open : ' + banner.decode().strip("\n"))
        except:
            print(f'[+] Port {ports} Is Open')
    except:
        #print(f'[-] Port {ports} is closed')
        pass

def get_banner(socket_created):
    return socket_created.recv(1024)


targets = input('[+] Enter Your Targets(Split multiple targets with ","): ')

if ',' in targets:
    for ip in targets.split(','):
        scan(ip.strip(' '))
else:
    scan(targets.strip(' '))
