import logging
import time

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[94m',    # Blue
        'INFO': '\033[92m',     # Green
        'WARNING': '\033[93m',  # Yellow
        'ERROR': '\033[91m',    # Red
        'RESET': '\033[0m'      # Reset color
    }
    def format(self, record):
        log_message = super().format(record)
        log_level_color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        log_date = time.strftime('%H:%M:%S | %m/%d/%Y', time.localtime(record.created))
        return f'[{log_date}]\t::\t{log_level_color}{record.levelname}{self.COLORS["RESET"]}\t::>\t{log_message}'