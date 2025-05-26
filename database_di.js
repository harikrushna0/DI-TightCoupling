// database_di.js (150 lines)
class Database {
    executeQuery(query, params) {
        throw new Error("Method not implemented");
    }
}

class MySQLDatabase extends Database {
    constructor(config) {
        super();
        const mysql = require('mysql');
        this.connection = mysql.createConnection(config);
    }

    executeQuery(query, params) {
        return new Promise((resolve, reject) => {
            this.connection.query(query, params, (err, results) => {
                if (err) reject(err);
                resolve(results);
            });
        });
    }
}

class UserService {
    constructor(database) {
        this.database = database;
    }

    async getUser(userId) {
        return this.database.executeQuery('SELECT * FROM users WHERE id = ?', [userId]);
    }
}

// DI: Database implementation can be swapped (e.g., SQLiteDatabase).
