Enterprise Cortex XSOAR – Python Automations
Overview

This repository contains enterprise-grade Palo Alto Cortex XSOAR (Demisto) Python automations designed to demonstrate how real Security Operations Centers (SOC) orchestrate incident response using Splunk SIEM, threat intelligence, governance controls, and ServiceNow ITSM.

All automations are written using native Cortex XSOAR APIs
(demisto.args(), demisto.executeCommand()) and reflect production-style SOC logic, not demo or lab scripts.

The scripts in this repository are intended to be executed as automation tasks inside Cortex XSOAR playbooks, after an incident has already been created.

1. Enterprise Security Architecture Context

In a mature enterprise SOC, responsibilities are clearly separated to ensure scalability, governance, and auditability.

Platform Responsibilities

Splunk SIEM

Log ingestion and normalization

Correlation searches and detections

Initial event enrichment

Alert generation

Cortex XSOAR

Incident creation and lifecycle management

Investigation and decision-making

Threat intelligence enrichment

Orchestration and automation

Governance and analyst control

ServiceNow ITSM

Official incident records

SLA tracking and escalation

Audit trail and compliance reporting

This separation of duties aligns with public-sector and EU regulatory expectations, including auditability, least privilege, and controlled response.

2. Threat Intelligence Sources

These automations correlate multiple intelligence layers to support high-confidence decisions:

Palo Alto Unit 42
Strategic and tactical external threat intelligence

External Threat Intelligence
Reputation and malware intelligence (e.g., VirusTotal-style services)

Internal Threat Intelligence
Enterprise allowlists, historical incidents, and prior analyst decisions

Using multiple sources prevents single-feed dependency and reduces false positives.

3. End-to-End SOC Flow (SIEM → SOAR → ITSM)

The operational flow implemented by these automations follows a real enterprise SOC model:

Event Detection (Splunk)
Splunk detects security-relevant activity (authentication abuse, malware, exploit attempts) using correlation searches.

Event Enrichment (Splunk)
Alerts are enriched with:

Source IP

Hostname

Business service

Asset criticality

Environment (PROD / NON-PROD)

Incident Creation (Cortex XSOAR)
Cortex XSOAR creates an incident and becomes the central decision point.

Threat Intelligence Correlation (XSOAR)
The incident is enriched using Unit 42, external TI, and internal enterprise context.

Decision & Risk Evaluation (XSOAR)
Severity is calculated based on confidence, thresholds, and business impact.

Controlled Escalation (ServiceNow)
Only validated, high-confidence incidents are escalated to ServiceNow.

This model ensures automation with control, not blind response.

4. Common Automation Design Pattern

All Python automations in this repository follow a consistent SOC-approved pattern:

Receive structured input from Splunk

Validate detection thresholds

Perform threat intelligence enrichment

Assess confidence and business risk

Decide whether escalation is required

Enforce analyst approval where needed

Create ServiceNow incidents for confirmed threats

This consistency builds SOC trust, simplifies auditing, and enables scale.

5. Use Case Explanations
5.1 Brute Force Authentication Attack

Business Problem
Repeated login failures may indicate credential guessing attempts against enterprise applications.

Detection Logic

Multiple failed logins

Same source IP

Short time window

XSOAR Decision Process

Validate failure threshold

Check IP reputation (Unit 42 + external TI)

Exclude known benign sources (VPNs, corporate IPs)

Evaluate business service criticality

Outcome

Prevents credential compromise

Reduces noise from benign failures

Creates high-quality ServiceNow incidents

5.2 Password Spraying Attack

Business Problem
Attackers test a single password across many accounts to avoid lockout detection.

Detection Logic

Same source IP

Multiple unique users targeted

Correlation performed by Splunk

XSOAR Decision Process

Confirm unique user threshold

Enrich IP reputation

Validate malicious intent

Protect centralized identity systems

Outcome

Early detection of credential abuse

Protection of AD / IAM infrastructure

5.3 Privileged Account Login Anomaly

Business Problem
Privileged accounts pose the highest risk and require strict monitoring.

Detection Logic

Privileged account login

Outside approved business hours

XSOAR Decision Process

Validate account privilege level

Confirm time-based anomaly

Check source reputation

Apply special handling for PAM / break-glass accounts

Outcome

Protects administrative access

Prevents silent lateral movement

5.4 Malware Hash Detection

Business Problem
Endpoint tools often generate noisy malware alerts requiring validation.

Detection Logic

Suspicious or malicious file detected

File hash available

XSOAR Decision Process

Validate hash using external intelligence

Resolve conflicting intelligence conservatively

Confirm true positive before escalation

Outcome

Eliminates false positives

Provides evidence-backed incidents

Improves SOC efficiency

5.5 Exploit Attempt (CVE-Based)

Business Problem
Newly disclosed vulnerabilities are often actively exploited.

Detection Logic

IDS/IPS detects exploit attempt

CVE identifier present

XSOAR Decision Process

Validate CVE severity

Assess impacted asset criticality

Increase urgency for recently disclosed CVEs

Outcome

Faster response to active exploitation

Clear linkage between vulnerability and business impact

6. Governance and Compliance Considerations

These automations are intentionally designed for regulated environments:

No destructive actions without human approval

Clear separation of detection and response

Full audit trail via ServiceNow

SOC analysts retain decision authority

Supports post-incident review and KPI analysis (MTTR, false positives)

This makes the approach suitable for government, finance, and critical infrastructure environments.

7. Open-Source and Data Protection

No real customer data

No real IPs, usernames, or systems

No environment-specific secrets

Fully anonymized and safe for public sharing

8. Why This Repository Matters

This repository demonstrates:

Real SOC operational thinking

Native Cortex XSOAR automation design

Threat-intelligence-driven decision making

Enterprise-ready incident handling

A balanced approach to automation, governance, and accountability