import re
from typing import List, Dict

class CodeReviewer:
    SECRET_PATTERNS = [
        re.compile(r'(?i)(api[_-]?key|secret|token|password)s*=s*["'][^"']+["']'),
        re.compile(r'ghp_[A-Za-z0-9]{36}')
    ]

    def review_diff(self, diff_text: str) -> List[Dict[str, str]]:
        findings = []
        for line_num, line in enumerate(diff_text.splitlines(), 1):
            for pat in self.SECRET_PATTERNS:
                if pat.search(line):
                    findings.append({
                        "line": line_num,
                        "severity": "CRITICAL",
                        "message": "Potential hardcoded credential detected!"
                    })
        return findings

if __name__ == "__main__":
    rev = CodeReviewer()
    findings = rev.review_diff('apiKey = "ghp_1234567890abcdef"')
    print("Review Findings:", findings)
