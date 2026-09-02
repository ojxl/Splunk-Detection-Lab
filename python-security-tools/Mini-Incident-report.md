# Mini Incident Report – Possible Brute Force Attack

## 1. Incident Overview

**Incident Type:** Possible Brute Force Attack  
**Severity:** Medium  
**Status:** Investigating  
**Detection Source:** Windows Security Event Logs  
**Event ID:** 4625 – Failed Logon  

A number of failed login attempts were detected against a Windows system.
The activity was identified using a Python log parser.

---

## 2. Detection

The parser identified multiple Event ID 4625 events in the log file.

Example:

```text
FAILED LOGIN: 4625 Failed Login from 192.168.1.34
FAILED LOGIN: 4625 Failed Login from 192.168.1.34
FAILED LOGIN: 4625 Failed Login from 192.168.1.34
