public class NotificationService {
    private HttpClient httpClient = new HttpClient(); // fixed implementation

    public void notifyUser(String message) {
        httpClient.post("/notify", message);
    }
}
