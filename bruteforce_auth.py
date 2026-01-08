def main():
    args = demisto.args()

    source_ip = args.get("source_ip")
    hostname = args.get("hostname")
    business_service = args.get("business_service", "Business-App-1")
    failed_attempts = int(args.get("failed_attempts", 0))

    if failed_attempts < 5:
        demisto.results("No brute force detected")
        return

    unit42 = demisto.executeCommand("unit42-get-indicator", {"indicator": source_ip})
    vt = demisto.executeCommand("vt-get-ip-report", {"ip": source_ip})

    risk_score = 0
    if unit42:
        risk_score += 90
    if vt:
        risk_score += 80

    demisto.executeCommand(
        "servicenow-create",
        {
            "short_description": "Brute force authentication attack detected",
            "severity": "High",
            "comments": f"""
Business Service: {business_service}
Hostname: {hostname}
Source IP: {source_ip}
Failed Attempts: {failed_attempts}
Risk Score: {risk_score}
Threat Intel: Unit42 + VirusTotal
"""
        }
    )

    demisto.results("Brute force incident created")

if __name__ in ("__main__", "builtin", "builtins"):
    main()
