const express = require("express");
const mysql = require("mysql");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "olakkente mood@9011",
    database: "inventory_db"
});

db.connect(err => {
    if (err) throw err;
    console.log("MySQL Connected...");
});

// Fetch Products
app.get("/products", (req, res) => {
    db.query("SELECT * FROM products", (err, results) => {
        if (err) throw err;
        res.json(results);
    });
});

// Add Product
app.post("/products", (req, res) => {
    const { name, category, quantity, price, supplier } = req.body;
    const sql = "INSERT INTO products (name, category, quantity, price, supplier) VALUES (?, ?, ?, ?, ?)";
    db.query(sql, [name, category, quantity, price, supplier], (err, result) => {
        if (err) throw err;
        res.json({ message: "Product added successfully" });
    });
});

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
