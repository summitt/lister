import pcap
import dpkt
import socket
import sys, getopt
from array import *


def sniff(local):
	print 'Listening for connections...'
	print 'FYI-I will only show new unique connections.'
	connections = []
	pc = pcap.pcap(immediate=True)
	pc.setfilter('tcp')
	for dual in pc:
		if(dual ==None):
			continue

		ts = dual[0]
		pkt = dual[1]
		try:
			eth = dpkt.ethernet.Ethernet(pkt)
			ip = eth.data
			srcIp = socket.inet_ntoa(ip.src)
			dstIp = socket.inet_ntoa(ip.dst)
			if dstIp == local :
				tcp=ip.data
				port = tcp.dport
				if tcp.flags == 2 :
					line = "Connection from  " + srcIp + " to port " + str(port) 
					if line not in connections:
						connections.append(line)
						print line
		except:
			pass
			#print ""
			#print "Errorish things happened. Probably nothing to worry about."


def main(argv):
	local='192.168.1.129'
   	try:
		opts, args = getopt.getopt(argv,"hl:",["local="])
   	except getopt.GetoptError:
		print 'lister.py -l <localIp>'
		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-h':
			print 'lister.py -l <localIp>'
			sys.exit()
		elif opt in ("-l", "--local"):
			local = arg

	sniff(local)



if __name__ == "__main__":
   main(sys.argv[1:])
