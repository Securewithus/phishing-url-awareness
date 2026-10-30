import re
from urllib.parse import urlparse

# Messages are kept in one place so the code and the explanations stay in sync.
MSG_AT = "Contains an @ symbol; inspect carefully."
MSG_LONG = "Unusually long URL (over 100 characters)."
MSG_IP = "Uses an IP address instead of a familiar domain."
MSG_MANY = "Contains many hostname segments/subdomains."
MSG_PUNY = "Contains a punycode-style hostname."
MSG_HTTP = "Uses HTTP. HTTPS alone does not prove trust."
MSG_NONE = "No listed warning signs found. This does NOT prove safety."

# Improvement D: a short reason for each warning.
REASONS = {
    MSG_AT: "The browser ignores the text before @, so the link can look like one site but go to another.",
    MSG_LONG: "A long link can hide the real destination far to the right.",
    MSG_IP: "Honest services normally use readable names; a bare number hides who owns the site.",
    MSG_MANY: "Stacking many names can make a link look official.",
    MSG_PUNY: "Look-alike foreign letters can imitate a real name.",
    MSG_HTTP: "HTTP is not encrypted, so data can be seen on the way.",
}

# These results are information messages, not real warnings.
INFO_MESSAGES = ("No URL entered", "Could not identify", "This text is not a valid", "No listed warning")


def inspect_url(raw_url):
    """Check the visible text of a URL for selected warning signs. Never opens the URL."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Improvement C: malformed input such as "http://[bad" must not crash the program.
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not host:
        return ["Could not identify a hostname."]

    if "@" in candidate:
        findings.append(MSG_AT)
    if len(url) > 100:
        findings.append(MSG_LONG)
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(MSG_IP)
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append(MSG_MANY)
    if "xn--" in host:
        findings.append(MSG_PUNY)
    if parsed.scheme.lower() == "http":
        findings.append(MSG_HTTP)

    if not findings:
        findings.append(MSG_NONE)
    return findings


def has_warnings(findings):
    """Improvement B helper: True only when the list holds real warnings."""
    return not findings[0].startswith(INFO_MESSAGES)


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    # Improvement A: keep checking URLs until the user quits.
    while True:
        raw_url = input("\nEnter a sample URL (or type q to quit): ")
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye! Stay alert online.")
            break

        findings = inspect_url(raw_url)
        print("\nResult:")
        for number, item in enumerate(findings, start=1):
            print(f"{number}. {item}")
            if item in REASONS:
                print(f"   Why: {REASONS[item]}")

        if has_warnings(findings):
            print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")
        print("Never enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
