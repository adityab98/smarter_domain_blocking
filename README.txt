## Abstract

Ads are becoming a major nuisance when it comes to browsing the web. 
Computers today are exponentially faster than computers 20 years ago, 
yet the web browsing experience is just as slow as ever. 
Furthermore, these days, the internet is not as open as it once was. 
People tend to swarm and coalesce around a few websites. If a person 
only uses Instagram and Facebook, there is no need to expose his systems 
to the billions of other domains on the internet - some of which may 
potentially infect his systems. For these reasons, we have created a 
unified framework for blocking domains. Using Pi-Hole, we can set up a 
local network-wide DNS server - blocking ads at the network level for 
all devices that connect to the network. Along with this, we have added 
additional functionality in the form of scripts to further protect 
the user’s network. With both these components combined, the user 
will only be able to access the domains and websites he truly cares 
about and uses, and will cut off any additional sources of malware. 
Further, the system will learn the user’s habits and update the domain 
whitelist if he accesses a new domain. Preliminary testing shows that 
this additional functionality has almost no impact on the system usage. 
This makes our framework perfectly suitable for small embedded 
devices - the kind that Pi-Hole was built to run on.

## Usage

1. please ensure you have Pi-Hole up and running within a raspbian VM in VMWare Workstation
2. please supply your own history.json file

*Instructions for both are provided within the report
