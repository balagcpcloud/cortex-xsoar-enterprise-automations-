def main():
    args = demisto.args()

    username = args.get("username")
    source_ip = args.get("source_ip")
    is_privileged = args.get("is_privileged", "false").lower() == "true"
    outside_hours = args.get("outside_hours", "false").lower() == "true"

    if not (is_privileged and outside_hours):
        demisto.results("No privileged anomaly detected")
        return

    unit42 = demisto.executeCommand("unit42-get-indicator", {"indicator": source_ip})

    demisto.executeCommand(
        "servicenow-create",
        {
            "short_description": "Privileged account login outside business hours",
            "severity": "High",
            "comments": f"""
Username: {username}
Source IP: {source_ip}
Threat Intel: Unit42
"""
        }
    )

    demisto.results("Privileged login incident created")

if __name__ in ("__main__", "builtin", "builtins"):
    main()
