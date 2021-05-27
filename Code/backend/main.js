const express = require("express");
var cors = require("cors");
const app = express();
const port = 2020;

app.use(cors({ origin: "*" }));

app.get("/", (req, res) => {
  const obj = {
    name: "Rei",
    job: "nona",
  };

  res.send(obj);
});

// To run app you can: npm run dev (see package.json scripts)
// Go to http://localhost:2020

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
