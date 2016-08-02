import pcap
import dpkt
import socket
import sys, getopt
from array import *
import netifaces as ni


def sniff(local, iface):
	print '**Note: Lister.py will only show new unique connections.'
	connections = []
	pc = pcap.pcap(iface, immediate=True)
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
	#local='192.168.1.129'
   	try:
		opts, args = getopt.getopt(argv,"hl:i:",["local=", "interface="])
   	except getopt.GetoptError:
		print 'lister.py -i <interface>'
		sys.exit(2)
   	for opt, arg in opts:
		if opt == '-h':
			print 'lister.py -i <interface>'
			sys.exit()
		elif opt in ("-l", "--local"):
			local = arg
		elif opt in ("-i", "--interface"):
			iface = arg
	ni.ifaddresses(iface)
	local = ni.ifaddresses(iface)[2][0]['addr']
	print 'Listening on ' + iface + " (" + local + ")"

	sniff(local,iface)



if __name__ == "__main__":
   main(sys.argv[1:])
