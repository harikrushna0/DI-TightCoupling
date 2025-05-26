// logger_tight.js (100 lines)
const winston = require('winston');

class OrderService {
    constructor() {
        this.logger = winston.createLogger({
            transports: [new winston.transports.Console()]
        });
    }

    placeOrder(order) {
        this.logger.info(`Order placed: ${order.id}`);
        // Tight Coupling: Hardcoded Winston logger.
    }
}
