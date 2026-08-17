# Splunk Detection Lab

## Overview

A hands-on home SOC lab designed to simulate attacker activity,
collect security telemetry and develop detections using Splunk.

## Lab Architecture

[architecture diagram goes here]

## Environment

- Kali Linux — attack machine
- Windows VM — target machine
- Splunk — SIEM
- Sysmon — endpoint telemetry
- Wireshark — network traffic analysis
- Nmap — network scanning

## Attacks Simulated

- Brute-force login attempts
- Network/port scanning

## Detections

### Brute Force
Windows Event ID 4625
MITRE ATT&CK: T1110

### Network Scanning
Network scanning activity
MITRE ATT&CK: T1046

## Investigation Workflow

Attack → Telemetry → Splunk → Detection → Investigation

## Key Skills Demonstrated

- SIEM analysis
- Windows Event Log analysis
- Sysmon
- Network traffic analysis
- Detection engineering
- MITRE ATT&CK mapping

## Project Status

Currently developing additional detections and investigation workflows.
