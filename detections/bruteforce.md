# Brute Force Detection

## Objective

Detect repeated failed authentication attempts that may indicate brute-force activity against the Windows VM.

## Data Source

Windows Security Event Logs.

## Attack Simulation

Multiple incorrect login attempts were intentionally generated against the Windows VM to produce Windows Security Event ID 4625 events.

## Event ID

4625 — Failed Logon

## MITRE ATT&CK

T1110 — Brute Force

## Detection Logic

The detection searches Windows Security logs for Event ID 4625, which represents a failed logon attempt. Multiple failed attempts associated with the same account or source IP within a short period can indicate possible brute-force activity.

## Splunk Query

index=* EventCode=4625
| stats count by Account_Name

## Evidence

![Failed Login](../screenshots/4625.png)

## Investigation

If this detection triggered in a real environment, an analyst would investigate:

Target account — Identify which account received the failed login attempts.
Number of attempts — Determine how many failed logons occurred and whether they were repeated.
Time of activity — Check when the attempts occurred and whether they happened within a short period.
Source information — Identify the computer or IP address responsible for the attempts, where available.
Successful logons — Check for successful Event ID 4624 logons around the same time to determine whether an account was eventually accessed.
Related activity — Review other Windows Security and Sysmon events from the same source or around the same time for additional suspicious activity.

In this lab, the failed logons were intentionally generated as part of the controlled brute-force simulation.
