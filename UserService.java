public class UserService {
    private EmailSender emailSender = new EmailSender(); // tightly coupled

    public void registerUser(String email) {
        emailSender.sendEmail(email);
    }
}
