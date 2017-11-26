"""

Problem 1

"""
import re
import csv
input_text = """lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether f4:0f:24:29:df:4d
	inet6 fe80::1cb5:1689:1826:cc7b%en0 prefixlen 64 secured scopeid 0x4
	inet 10.176.85.19 netmask 0xffffff00 broadcast 10.176.85.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
en1: flags=963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX> mtu 1500
	options=60<TSO4,TSO6>
	ether 06:00:58:62:a3:00
	media: autoselect <full-duplex>
	status: inactive
p2p0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 2304
	ether 06:0f:24:29:df:4d
	media: autoselect
	status: inactive"""

input_text = "\n" + input_text  # Add \n at the front to make it easier to split the string
inet_regex = re.compile('inet (\d+\.\d+\.\d+\.\d+)')  # Compile regex for matching ip address
split_text = re.split('\n(\w+): ', input_text)  # Split the text using the given pattern - Example pattern matches: \nlo0: , \ngif0: 
network_info = list()
output_csv = open('network_info.csv', 'wb')  # Output csv
writer = csv.writer(output_csv, delimiter=',')  # Create csv writer
writer.writerow(["interface", "inet", "status"])  # Write csv header
for i, text in enumerate(split_text[1:]):
	if i % 2 == 0:  # Even indices contain the interface names
		interface = text
	else:
		cur_info = list()
		status = ""
		inet = ""
		status_split = text.split("status: ")  # If "status: " is present, split the string
		if len(status_split) > 1:  # Check if "status: " is present or not
			status = status_split[-1]  # If it is, extract the status
		inet_list = inet_regex.findall(text)  # Final all inet IP addresses
		if inet_list != []:
			inet = inet_list[0]
		writer.writerow([interface, inet, status])  # Write a new row into the csv
			
output_csv.close()