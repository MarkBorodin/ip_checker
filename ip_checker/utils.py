import json
import socket
import urllib.request

from dns import reversename, resolver
from ipwhois import IPWhois


def get_host(ip):
    try:
        domain_name = socket.gethostbyaddr(ip)[0]
        return domain_name
    except Exception as e:
        print(e)
        return 'Name or service not known'


def get_ptr(ip):
    try:
        domain_address = reversename.from_address(ip)
        return domain_address
    except Exception as e:
        print(e)
        return 'Name or service not known'


def get_other_information(ip):
    try:
        result = dict()
        obj = IPWhois(ip)
        res = obj.lookup_whois()

        try:
            url = "https://ipinfo.io/" + ip + "/json"
            getInfo = urllib.request.urlopen(url)
            infoList = json.load(getInfo)
            company = infoList["org"]
            city = infoList["city"]
            try:
                result['company'] = company
            except:
                result['company'] = ''
            try:
                result['city'] = city
            except:
                result['city'] = ''
        except:
            result['company'] = ''
            result['city'] = ''

        try:
            result['description'] = res['nets'][0]['description']
        except:
            result['description'] = ''

        try:
            result['range'] = res['nets'][0]['range']
        except:
            result['range'] = ''

        try:
            result['asn_description'] = res['asn_description']
        except:
            result['asn_description'] = ''

        try:
            result['real_address'] = res['nets'][0]['address']
        except:
            result['real_address'] = ''

        try:
            result['country'] = res['nets'][0]['country']
        except:
            result['country'] = ''

        try:
            result['emails'] = res['nets'][0]['emails']
        except:
            result['emails'] = ''

        return result

    except Exception as e:
        print(e)
        return 'company not known'
