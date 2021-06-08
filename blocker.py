# in first run, we will feed it our history for it to learn from. after that, it will constantly run in the background. when it detects a request to a domain that is not in the adlist, it will whitelist that domain

# libs
import os
import json
import time

# get only domain name from a full url
def getdomain(url):
    domain=""
    numslash = 0
    for c in url:
        if (c == '/'):
            numslash += 1
            continue
        if (numslash == 2):
            domain = domain + c
        elif (numslash >= 2):
            break
    return domain

# whitelists the following domains
def whitelistdomains(domains):
    whitelistcommand = 'pihole -w '
    for domain in domains:
        whitelistcommand += domain + ' '
    os.system(whitelistcommand)

# a function to parse the history.json file obtained from google chrome, and extract just the domains from the long list of urls accessed.
# also reads the hosts file containing the adlist, and appends that to the adlist array
def init(histpath, whitelist, hostspath, adlist):
    # initialize whitelists first
    print("initial run. whitelisting all domains in browser history")
    f = open(histpath)
    data = json.load(f)
    urls = []
    for i in data['Browser History']:
        urls.append(i['url'])
    f.close()
    for url in urls:
        dom = getdomain(url)
        whitelist.append(dom)
    whitelist = list(set(whitelist))
    whitelistdomains(whitelist)
    # initialize adlist
    f = open(hostspath, 'r')
    lines = f.readlines()
    for line in lines:
        adlist.append(line[0:-1])

# checks whether domain is in adlist, or already whitelisted
def whitelistable(domain, adlist, whitelist):
    wable = True
    for ad in adlist:
        if (domain == ad):
            return False
    for whitelist in whitelist:
        if (domain == whitelist):
            return False
    return True

# read logs, and add any regex blacklisted domains to the whitelist
def readlogs(whitelist, adlist, logpath):
    temp = []
    stream = os.popen("cat " + logpath + " | grep regex | cut -f 8 -d ' ' | uniq")
    output = stream.read()
    output = output.strip()
    logged = output.split()
    print(logged)
    for line in logged:
        if (whitelistable(line, adlist, whitelist)):
            whitelist.append(line)
            temp.append(line)
    if (len(temp) > 0):
        print("whitelisting new domains")
        whitelistdomains(temp)

def main():
    #vars
    histpath = "history.json"
    whitelist = []
    hostspath = "hosts"
    adlist = []
    logpath = "/var/log/pihole.log"
    timeout = 30
    
    init(histpath, whitelist, hostspath, adlist)
    
    # infinite loop that the program will run in
    while 1:
        # run the program every $timeout seconds
        time.sleep(timeout)
        readlogs(whitelist, adlist, logpath)

if __name__ == "__main__":
    main()
