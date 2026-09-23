
# Port Scan Detection

## Objective

Detect potential network/port scanning activity agaisnt windows. 

## Attack Simulation

Nmap was executed from Kali Linux against the Windows VM. The scan generated network traffic that was observed using Wireshark and corresponding telemetry was examined in Splunk

## Network Evidence

As mentioned before, Wireshark was used to observe SYN traffic generated during scanning.

## MITRE ATT&CK

T1046 — Network Service Scanning

## Detection Logic

The detection looks for repeated network connection attempts from a source IP to multiple destination ports on my Windows VM. A high number of connection attempts across different ports within a short period can indicate network scanning activity.

## Splunk Query

index=main sourcetype=firewall
| rex field=_raw "^\S+\s+\S+\s+(?<action>\S+)\s+(?<protocol>\S+)\s+(?<src_ip>\S+)\s+(?<dst_ip>\S+)\s+(?<src_port>\S+)\s+(?<dst_port>\S+)"
| stats count by src_ip, dst_ip, dst_port
| sort - count

## Evidence

![Nmap Scan](../screenshots/nmap.png)

![Nessus Scan](../screenshots/nessus.png)

![Wireshark Traffic](screenshots/wireshark.png)

![Splunk Detection](../screenshots/splunk.png)

## Investigation

The detection looks for repeated network connection attempts from a source IP to multiple destination ports on the Windows VM. A high number of connection attempts across different ports within a short period can indicate network scanning activity.
