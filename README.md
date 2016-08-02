# lister
This is a simple script to show which ports a remote host attempts to connect to on the local host. This is useful when spoofing DNS so you can see the ports the spoofed host attempts to connect to. This is also helpful when performing mobile assessments when the mobile application may use different ports other than 80 and 443. You can set up a custom DNS server like the one that is built into [https://github.com/summitt/Burp-Non-HTTP-Extension](Burp-Non-HTTP-Extension), configure the mobile device's DNS to the ip of the machine running burp suite, then run the script. If the mobile application is using a different protocol other than 80 or 443 then lister.py will dsiplay the connection information.

You could of course do this with tcpdump or whireshark but this filters the information so its easier to read.

Usage


```
$ sudo python ./lister.py -i en1
Listening on en1 (192.168.1.128)
**Note: Lister.py will only show new unique connections.
Connection from  192.168.1.198 to port 443
Connection from  192.168.1.198 to port 993
Connection from  192.168.1.224 to port 443
Connection from  192.168.1.224 to port 80
Connection from  192.168.1.224 to port 49152
Connection from  192.168.1.224 to port 15000
```

Requirements

```
$ pip install pypcap
$ pip install dpkt
$ pip install netifaces
```
