const express = require("express");
const app = express();
const port = 3003;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

// To run app you can: npm run dev (see package.json scripts)
// Go to http://localhost:3003

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
