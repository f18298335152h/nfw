from scapy.all import *

t=[]
timestamp=[]
# pcaps = PcapReader("/root/tcpdump/udp.pcap")
pcaps = PcapReader("/root/tcpdump/wang2007.pcap")


#except two packets
# i=0
# # s = 0
# for p in pcaps:
#     if i <= 1:
#         i = i + 1
#         continue
#     elif i == 2:
#         start = p.time
#         i = i + 1
#     else:
#         timestamp.append(round(p.time*1000-start*1000,2))
# print timestamp

#udp
i=0
# s = 0
start = 0
for p in pcaps:
    if i == 0:
        start = p.time
        i = i + 1
    else:
        t.append(p.time*1000-start*1000)

timestamp.append(round(t[0],3))
for i in range(len(t) - 1):
    timestamp.append(round(t[i + 1] - t[i],3))
print timestamp
print len(timestamp)