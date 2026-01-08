# **Enterprise Cortex XSOAR – Python Automations**

## **Overview**

This repository contains **enterprise-grade Palo Alto Cortex XSOAR (Demisto) Python automations** designed to demonstrate how **real Security Operations Centers (SOC)** orchestrate incident response using **Splunk SIEM**, **threat intelligence**, **governance controls**, and **ServiceNow ITSM**.

All automations are written using **native Cortex XSOAR APIs**  
(`demisto.args()`, `demisto.executeCommand()`) and reflect **production-style SOC logic**, not demo or lab scripts.

The scripts in this repository are intended to be executed as **automation tasks inside Cortex XSOAR playbooks**, **after an incident has already been created**.

---

## **1. Enterprise Security Architecture Context**

In a mature enterprise SOC, responsibilities are clearly separated to ensure **scalability, governance, and auditability**, especially in **regulated and public-sector environments**.

### **Platform Responsibilities**

#### **Splunk SIEM**
- **Log ingestion and normalization**
- **Correlation searches and detections**
- **Initial event enrichment**
- **Alert generation**

#### **Cortex XSOAR**
- **Incident creation and lifecycle management**
- **Investigation and decision-making**
- **Threat intelligence enrichment**
- **Orchestration and automation**
- **Governance and analyst control**

#### **ServiceNow ITSM**
- **Official incident tracking**
- **SLA and escalation management**
- **Audit trail and compliance reporting**

This separation of duties supports **regulatory requirements**, **least privilege**, and **controlled response**, which are essential for large enterprises and EU institutions.

---

## **2. Threat Intelligence Sources**

These automations correlate multiple intelligence layers to support **high-confidence incident decisions**:

- **Palo Alto Unit 42**  
  Strategic and tactical external threat intelligence

- **External Threat Intelligence**  
  Reputation and malware intelligence (e.g., VirusTotal-style services)

- **Internal Threat Intelligence**  
  Enterprise allowlists, historical incidents, and prior analyst decisions

Using multiple sources reduces false positives and prevents single-feed dependency.

---

## **3. End-to-End SOC Flow (SIEM → SOAR → ITSM)**

The operational flow implemented by these automations follows a **real enterprise SOC model**:

1. **Event Detection (Splunk)**  
   Splunk detects security-relevant activity (authentication abuse, malware, exploit attempts).

2. **Event Enrichment (Splunk)**  
   Alerts are enriched with:
   - Source IP
   - Hostname
   - Business service
   - Asset criticality
   - Environment (PROD / NON-PROD)

3. **Incident Creation (Cortex XSOAR)**  
   Cortex XSOAR creates an incident and becomes the **central decision point**.

4. **Threat Intelligence Correlation (XSOAR)**  
   The incident is enriched using:
   - Unit 42 intelligence
   - External threat intelligence
   - Internal enterprise context

5. **Decision & Risk Evaluation (XSOAR)**  
   Severity is calculated based on **confidence**, **thresholds**, and **business impact**.

6. **Controlled Escalation (ServiceNow)**  
   Only **validated, high-confidence incidents** are escalated to ServiceNow.

This model ensures **automation with control**, not blind response.

---

## **4. Common Automation Design Pattern**

All Python automations in this repository follow a consistent SOC-approved pattern:

- Receive structured input from Splunk
- Validate detection thresholds
- Perform threat intelligence enrichment
- Assess confidence and business risk
- Decide whether escalation is required
- Enforce analyst approval where required
- Create ServiceNow incidents for confirmed threats

This approach ensures **consistency, repeatability, SOC trust, and auditability**.

---

## **5. Use Case Explanations**

### **5.1 Brute Force Authentication Attack**

**Business Problem**  
Repeated login failures may indicate credential guessing attempts against enterprise applications.

**Detection Logic**
- Multiple failed logins
- Same source IP
- Short time window

**XSOAR Decision Process**
- Validate failure threshold
- Check IP reputation (Unit 42 + external TI)
- Exclude known benign sources (VPNs, corporate IPs)
- Evaluate business service criticality

**Outcome**
- Prevents credential compromise
- Reduces alert noise
- Creates high-quality ServiceNow incidents

---

### **5.2 Password Spraying Attack**

**Business Problem**  
Attackers test a single password across many accounts to bypass lockout controls.

**Detection Logic**
- Same source IP
- Multiple unique user accounts targeted

**XSOAR Decision Process**
- Confirm unique user threshold
- Enrich IP reputation
- Validate malicious intent
- Protect centralized identity systems (AD / IAM)

**Outcome**
- Early detection of credential abuse
- Protection of enterprise identity infrastructure

---

### **5.3 Privileged Account Login Anomaly**

**Business Problem**  
Privileged accounts represent the highest operational risk.

**Detection Logic**
- Privileged account login
- Outside approved business hours

**XSOAR Decision Process**
- Validate account privilege level
- Confirm time-based anomaly
- Check source reputation
- Apply special handling for PAM / break-glass accounts

**Outcome**
- Protects administrative access
- Prevents silent lateral movement

---

### **5.4 Malware Hash Detection**

**Business Problem**  
Endpoint tools often generate noisy malware alerts requiring validation.

**Detection Logic**
- Suspicious or malicious file detected
- File hash available

**XSOAR Decision Process**
- Validate hash using external intelligence
- Resolve conflicting intelligence conservatively
- Escalate only confirmed malware

**Outcome**
- Eliminates false positives
- Improves SOC efficiency
- Provides evidence-backed incidents

---

### **5.5 Exploit Attempt (CVE-Based)**

**Business Problem**  
Newly disclosed vulnerabilities are frequently exploited.

**Detection Logic**
- IDS/IPS detects exploit attempt
- CVE identifier present

**XSOAR Decision Process**
- Validate CVE severity
- Assess impacted asset criticality
- Increase urgency for recently disclosed CVEs

**Outcome**
- Faster response to active exploitation
- Clear linkage between vulnerability and business impact

---

## **6. Governance and Compliance Considerations**

These automations are designed for **regulated enterprise environments**:

- No destructive actions without human approval
- Clear separation of detection and response
- Full audit trail through ServiceNow
- SOC analysts retain decision authority
- Supports post-incident review and KPI analysis (MTTR, false positive rate)

---

## **7. Open-Source and Data Protection**

- No real customer data
- No real IPs, usernames, or systems
- No environment-specific secrets
- Fully anonymized and safe for public sharing

---

## **8. Why This Repository Matters**

This repository demonstrates:

- **Real SOC operational thinking**
- **Native Cortex XSOAR automation design**
- **Threat-intelligence-driven decision making**
- **Enterprise-ready incident handling**
- **Balanced automation, governance, and accountability**

--
