const express = require("express");
const router = express.Router();
const User = require("../models/user");
const authMiddleware = require("../middleware/auth");

router.post("/signup", async (req, res) => {});

router.post("/login", async (req, res) => {});

router.get("/me", authMiddleware, async (req, res) => {});

router.put("/:userId", authMiddleware, async (req, res) => {});

module.exports = router;
