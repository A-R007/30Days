const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
// const router = require("./routes");
const connectDB = require("./db");

const app = express();

app.use(cors());
app.use(bodyParser.json());

connectDB();


const port = 5000;

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
