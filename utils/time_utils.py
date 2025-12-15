import re


def compute_time_difference(text: str) -> str:
    """
    Extracts two HH:MM times from text and returns duration.
    Example:
    'A train leaves at 14:30 and arrives at 18:05'
    → '3 hours 35 minutes'
    """
    times = re.findall(r"(\d{1,2}):(\d{2})", text)
    if len(times) != 2:
        return ""

    (h1, m1), (h2, m2) = [(int(h), int(m)) for h, m in times]

    start = h1 * 60 + m1
    end = h2 * 60 + m2
    diff = end - start

    hours = diff // 60
    minutes = diff % 60

    return f"{hours} hours {minutes} minutes"
