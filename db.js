const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    await mongoose
      .connect(
        "mongodb+srv://AR_007_:ar7legende@cluster0.fpvqcam.mongodb.net/?retryWrites=true&w=majority",
        {
          useNewUrlParser: true,
          useUnifiedTopology: true,
        }
      )
      .then(() => {
        console.log("Connected");
      });
  } catch (error) {
    console.error("Error", error);
    process.exit(1);
  }
};

module.exports = connectDB;
