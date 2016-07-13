# lister
This is a simple script to show which ports a remote host attempts to connect to on the local host. This is useful when spoofing DNS so you can see the ports the spoofed host attempts to connect to. This is also helpful when performing mobile assessments when the mobile application may use different ports other than 80 and 443. You can set up a custom DNS server like the one that is built into [https://github.com/summitt/Burp-Non-HTTP-Extension](Burp-Non-HTTP-Extension), configure the mobile device's DNS to the ip of the machine running burp suite, then run the script. If the mobile application is using a different protocol other than 80 or 443 then lister.py will dsiplay the connection information.

Usage


```
$ python ./lister.py -l 192.168.1.129

Listening for connections...
FYI-I will only show new unique connections.
Connection from  192.168.1.128 to port 8888
Connection from  192.168.1.128 to port 443
Connection from  192.168.1.128 to port 33
Connection from  192.168.1.128 to port 100
Connection from  192.168.1.128 to port 500
```

Requirements

```
$ pip install pypcap
$ pip install dpkt
```
