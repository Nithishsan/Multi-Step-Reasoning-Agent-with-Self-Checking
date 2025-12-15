import os
import datetime

class Logger:
    """
    Lightweight logger for both CLI and Streamlit use.
    Produces timestamped logs and optionally writes to a log file.
    """

    def __init__(self, name="Agent", log_to_file=False, logfile_path="logs/agent.log"):
        self.name = name
        self.log_to_file = log_to_file
        self.logfile_path = logfile_path

        if log_to_file:
            os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    def _timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _write(self, level, message):
        formatted = f"[{self._timestamp()}] [{self.name}] [{level}] {message}"

        print(formatted)

        if self.log_to_file:
            with open(self.logfile_path, "a", encoding="utf-8") as f:
                f.write(formatted + "\n")

    # Public Methods
    def info(self, msg):
        self._write("INFO", msg)

    def warn(self, msg):
        self._write("WARNING", msg)

    def error(self, msg):
        self._write("ERROR", msg)

    def success(self, msg):
        self._write("SUCCESS", msg)
