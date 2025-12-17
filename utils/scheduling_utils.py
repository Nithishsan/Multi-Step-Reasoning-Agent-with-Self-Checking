import re

def find_fitting_slots(text: str, required_minutes: int = 60):
    """
    Extracts time slots and returns those that fit the required duration.
    """
    slots = re.findall(r"(\d{1,2}:\d{2})\s*–\s*(\d{1,2}:\d{2})", text)

    fitting = []

    for start, end in slots:
        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))

        duration = (eh * 60 + em) - (sh * 60 + sm)
        if duration >= required_minutes:
            fitting.append(f"{start}–{end}")

    return fitting
