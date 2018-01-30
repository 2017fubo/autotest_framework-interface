from socket import *
from time import ctime

if __name__=="__main__":

    HOST = "localhost"
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST,PORT)

    tcpSerSock = socket(AF_INET,SOCK_STREAM)
    tcpSerSock.bingd(ADDR)
    tcpSerSock.listen(5)

    while True:
        print("waiting for connectiong...")
        tcpCliSock , addr = tcpSerSock.accept()
        print("...connected from: %s" %addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            tcpCliSock.send("[%s] %s" %(ctime(),data))
        tcpCliSock.close()
    tcpSerSock.close()

# def retBanner(ip, port):
#     try:
#         socket.setdefaulttimeout(2)
#         s = socket.socket()
#         s.connect((ip, port))
#         banner = s.recv(1024)
#         return banner
#     except:
#         return

# def checkVlns(banner):
#     if 'Free' in banner:
#         print('[+] FreeFloat FTP Server is vulnerable')
#
#     elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
#         print("[+] 3Com 3CDaemon Server Version 2.0")
#
#     return
#
# def main():
#     portList = [21, 22, 25, 80, 110, 443]
#
#     for x in range(1, 255):
#         ip = '192.168.1' + str(x)
#         for port in portList:
#             banner = retBanner(ip, port)
#             if banner:
#                 print('[+]' + "ip:" + banner)
#                 checkVlns(banner)

# if __name__ == '__main__':
#     main()