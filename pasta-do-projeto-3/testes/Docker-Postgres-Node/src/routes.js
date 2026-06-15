import express from "express";
import { createUser, getAlluser, deleteUser } from "./controllers/userController.js";

const router = express.Router();

router.post("/cadastro", createUser)
router.get("/todos", getAlluser)
router.delete("/deletar", deleteUser)

export default router;