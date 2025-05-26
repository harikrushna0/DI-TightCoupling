// logger_di.js (110 lines)
class Logger {
    log(message) {
        throw new Error("Method not implemented");
    }
}

class ConsoleLogger extends Logger {
    log(message) {
        console.log(message);
    }
}

class OrderService {
    constructor(logger) {
        this.logger = logger;
    }

    placeOrder(order) {
        this.logger.log(`Order placed: ${order.id}`);
        // DI: Logger can be swapped (e.g., FileLogger).
    }
}
