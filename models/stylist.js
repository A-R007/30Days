const mongoose = require("mongoose");

const stylistSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  services: {
    type: [String],
    required: true,
  },
  availability: {
    type: Object,
  },
});

module.exports = mongoose.model("Stylist", stylistSchema);
