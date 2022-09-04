
from signal import sigpending
import boto3

cidr = ""
ip_protocol = ""
from_port = ""
to_port = ""
from_source = ""

for region in ["eu-central-1"]:
	ec2 = boto3.client('ec2', region )
	sgs = ec2.describe_security_groups()['SecurityGroups']
	for sg in sgs:
		sg_name = sg['GroupName']
		sg_id = sg['GroupId']
		aws_account_id = sg['OwnerId']
		
		print("Group Name:" + sg_name,"\nGroup Id:" + sg_id,"\nAWS Account:" + aws_account_id)

		inbound = sg['IpPermissions']
		print("\nInbound\n")
		for rule in inbound:
			if rule['IpProtocol'] == "-1":
				traffic_type = "All Trafic"
				ip_protocol = "All"
				to_port = "All"
			else:
				ip_protocol = rule['IpProtocol']
				from_port = rule['FromPort']
				to_port = rule['ToPort']
				if to_port == -1:
					to_port = "N/A"

			#IPv4
			if len(rule['IpRanges']) > 0:
				for ip_range in rule['IpRanges']:
					cidr = ip_range['CidrIp']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nCidrIp: " + cidr)

			#IPv6
			if len(rule['Ipv6Ranges']) > 0:
				for ip_range in rule['Ipv6Ranges']:
					cidr = ip_range['CidrIpv6']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nCidrIp: " + cidr)

			#SG
			if len(rule['UserIdGroupPairs']) > 0:
				for source in rule['UserIdGroupPairs']:
					from_source = source['GroupId']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nFromSource: " + from_source)
					

		outbound = sg['IpPermissionsEgress']
		print("\nOutbound\n")
		for rule in outbound:
			if rule['IpProtocol'] == "-1":
				traffic_type = "All Trafic"
				ip_protocol = "All"
				to_port = "All"
			else:
				ip_protocol = rule['IpProtocol']
				from_port = rule['FromPort']
				to_port = rule['ToPort']
				#If ICMP, report "N/A" for port #
				if to_port == -1:
					to_port = "N/A"

			#IPv4
			if len(rule['IpRanges']) > 0:
				for ip_range in rule['IpRanges']:
					cidr = ip_range['CidrIp']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nCidrIp: " + cidr)

			#Ipv6
			if len(rule['Ipv6Ranges']) > 0:
				for ip_range in rule['Ipv6Ranges']:
					cidr = ip_range['CidrIpv6']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nCidrIp: " + cidr)

			#SG
			if len(rule['UserIdGroupPairs']) > 0:
				for source in rule['UserIdGroupPairs']:
					from_source = source['GroupId']
					print("IpProtocol:" + ip_protocol,"\nToPort: " + to_port,"\nFromSource: " + from_source)

