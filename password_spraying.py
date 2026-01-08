def main():
    args = demisto.args()

    source_ip = args.get("source_ip")
    unique_users = int(args.get("unique_users", 0))

    if unique_users < 5:
        demisto.results("No password spraying detected")
        return

    vt = demisto.executeCommand("vt-get-ip-report", {"ip": source_ip})

    demisto.executeCommand(
        "servicenow-create",
        {
            "short_description": "Password spraying attack detected",
            "severity": "High",
            "comments": f"""
Source IP: {source_ip}
Unique Users Targeted: {unique_users}
Threat Intel: VirusTotal
"""
        }
    )

    demisto.results("Password spraying incident created")

if __name__ in ("__main__", "builtin", "builtins"):
    main()
