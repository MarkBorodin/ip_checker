import socket


def company(ip):
    try:
        domain_name = socket.gethostbyaddr(ip)[0]
        return domain_name
    except Exception as e:
        print(e)
        return 'Name or service not known'
