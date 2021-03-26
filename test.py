import socket


# #!!!!!!!!!!!!!!!!!!!!!!!!
# # socket
# def company(ip):
#     try:
#         domain_name = socket.gethostbyaddr(ip)[0]
#         # domain_name = socket.getfqdn(ip)
#         return domain_name
#     except Exception as e:
#         print(e)
#         return 'Name or service not known'
#
#
# ip = '195.201.201.32'
#
#
# print(company(ip))
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# # SCAPY
# #!!!!!!!!!!!!!!!!
# from scapy.all import *
# from scapy.layers.dns import DNS, DNSQR
# from scapy.layers.inet import IP, ICMP, UDP, traceroute
# from scapy.layers.l2 import Ether
# import os
#
# answer = sr1(IP(dst="8.8.8.8")/UDP()/DNS(rd=1, qd=DNSQR(qname="ec2-13-59-238-215.us-east-2.compute.amazonaws.com")))
# print(answer[DNS].summary())
# #!!!!!!!!!!!!!!!!


# #!!!!!!!!!!!!!!!!!!!!
# # ipinfo
# import requests
#
# r = requests.get('http://ipinfo.io/178.197.204.139/json')
# print(r.json())
# print(r.json()['org'])
# # print(r.json()['hostname'])
# #!!!!!!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!!!!!!!!
# from ipwhois import IPWhois
# from pprint import pprint
#
# obj = IPWhois('217.172.27.95')
#
# res = obj.lookup_whois(inc_nir=True)
#
# pprint(res)
# #!!!!!!!!!!!!!!!!!!!!!!


# # !!!!!!!!!!!!!!!!!!!!!!
# # PTR_record
# import dns.resolver
# from dns import reversename, resolver
#
# domain_address = reversename.from_address('194.230.147.29')
# print(domain_address)
# domain_name = str(resolver.resolve(domain_address, "PTR")[0])
# print(domain_name)
# # !!!!!!!!!!!!!!!!!!!!!!



# !!!!!!!!!!!!!!!!!!!!!!
# # SCANING
# r = '195.201.201.32'
# ips = r.split(".")
# ipc = ips[0] + "." + ips[1] + "." + ips[2] + "."
# for i in range(0, 256):
#     ipm = ipc + str(i)
#     ip = str(ipm)
#     try:
#         res = socket.gethostbyaddr(ip)[0]
#         print(f'{ip}: {res}')
#     except Exception as e:
#         print(ip)
# !!!!!!!!!!!!!!!!!!!!!!
