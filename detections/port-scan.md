
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

## Investigation

If this detection triggered in a real environment, an analyst would investigate:

1. **Source IP** — Identify the system generating the connection attempts.
2. **Target IP** — Confirm which system was being scanned.
3. **Destination ports** — Examine which ports were targeted and how many different ports were contacted.
4. **Timing and frequency** — Determine whether the connection attempts occurred within a short period, which may indicate scanning activity.
5. **Authorised activity** — Check whether the source system is an approved vulnerability scanner or security-testing system.
6. **Related activity** — Review other network and endpoint events from the source to determine whether scanning was followed by connection attempts or other suspicious activity.
7. **Network evidence** — Use Wireshark or other network telemetry to validate the observed scanning behaviour.

In this lab, the scanning activity was intentionally generated from the Kali Linux VM using Nmap against the Windows VM.
