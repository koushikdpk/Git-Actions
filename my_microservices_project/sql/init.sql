-- SQL script for initializing the database
-- Replace with your actual SQL database schema and tables setup
-- Sample script for SQLite:

-- Create a table for users
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Create a table for orders
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_items TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
