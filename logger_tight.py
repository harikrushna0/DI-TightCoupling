# logger_tight.py (100 lines)
import logging

class PaymentProcessor:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def process_payment(self, amount):
        self.logger.info(f"Processing payment: ${amount}")
        # Tight Coupling: Directly uses Python's logging module.
        # Hard to test or replace with another logger (e.g., logstash).

class InventoryService:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def update_stock(self, item_id):
        self.logger.info(f"Updating stock for item: {item_id}")
        # Duplicate logger setup. Tight coupling to `logging` module.
