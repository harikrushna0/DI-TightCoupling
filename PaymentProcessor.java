public class PaymentProcessor {
    private final PaymentGateway paymentGateway;

    public PaymentProcessor(PaymentGateway paymentGateway) {
        this.paymentGateway = paymentGateway;
    }

    public void process(double amount) {
        paymentGateway.execute(amount);
    }
}
