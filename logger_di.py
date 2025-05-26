# logger_di.py (110 lines)
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        with open("app.log", "a") as f:
            f.write(f"{message}\n")

class PaymentProcessor:
    def __init__(self, logger: Logger):
        self.logger = logger

    def process_payment(self, amount):
        self.logger.log(f"Payment processed: ${amount}")
        # DI: Can swap logger implementation (e.g., FileLogger, DatabaseLogger).
