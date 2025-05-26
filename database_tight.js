// database_tight.js (140 lines)
const mysql = require('mysql');

class UserService {
    constructor() {
        this.connection = mysql.createConnection({
            host: 'localhost',
            user: 'root',
            password: 'password',
            database: 'mydb'
        });
    }

    getUser(userId) {
        return new Promise((resolve, reject) => {
            this.connection.query('SELECT * FROM users WHERE id = ?', [userId], (err, results) => {
                if (err) reject(err);
                resolve(results[0]);
            });
        });
    }
}

// Tight Coupling: Direct MySQL dependency. Hard to switch to PostgreSQL.
