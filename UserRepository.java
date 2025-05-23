public class UserRepository {
    private final DataSource dataSource;

    public UserRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    public void getUser(String id) {
        // use dataSource to fetch user
    }
}
