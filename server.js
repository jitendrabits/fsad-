const express = require("express");
const jwt = require("jsonwebtoken");
const bodyParser = require("body-parser");
const bcrypt = require("bcrypt");
const authenticateToken = require("./middlewares/authenticateToken");
const app = express();
const port = process.env.PORT||5000;
const secretKey = process.env.SECRET_KEY || "elearnwilpbitspilani";
const saltRounds = 5;
app.use(bodyParser.json());

// Dummy user data for demonstration
const users = [
  { id: 1, username: "userA", password: "pwd1" },
  { id: 2, username: "userB", password: "pwd2" },
];


// Register route
app.post("/register", (req, res) => {
  // Mocked registration logic
  const { username, password } = req.body;
  const user = users.find((u) => u.username === username);

  if (user) {
    return res.status(400).json({ message: "User already exists" });
  }

  // Create new user
  const newUser = {
    id: users.length + 1,
    username,
    password: bcrypt.hashSync(password, saltRounds),
  };
  users.push(newUser);

  res.json({ message: "User registered successfully" });
});

// Login route
app.post("/login", (req, res) => {
  // Mocked authentication logic
  const { username, password } = req.body;
  const user = users.find(
    (u) => u.username === username && bcrypt.compareSync(password, u.password)
  );

  if (!user) {
    return res.status(401).json({ message: "Invalid credentials" });
  }
  // Generate JWT token
  const token = jwt.sign({ userId: user.id }, secretKey, { expiresIn: "6h" });

  res.json({ token });
});

// Dummy protected route
app.get("/protected", authenticateToken, (req, res) => {
  res.json({ message: "Protected route accessed successfully" });
});



app.get("/", (req, res) => {
  res.send("This is unprotected route.");
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});