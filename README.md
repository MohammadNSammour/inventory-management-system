# 🛒 Product Manager Pro - Advanced CLI System

> A production-grade, scalable Product Management CLI built with Python using Clean Architecture principles. Designed for maintainability, testability, and easy migration to modern stacks like PERN.
### 🎯 Overview

This is not a simple CRUD script. It's a complete inventory management system built from scratch to demonstrate enterprise-level software design. The system separates concerns into isolated layers, making it easy to test, scale, and migrate to a web stack.

### 🏛️ Architecture

I followed a layered Clean Architecture pattern, similar to what is used in large-scale systems:

* **Models:** Pure Python entities, no business logic.
* **Repositories:** Single responsibility for data access (SQLite). Easy to swap to PostgreSQL.
* **Services:** Core business logic lives here.
* **Validators:** Centralized input validation and sanitization.
* **Exceptions:** Custom exception handling for clean error flow.
* **CLI:** Decoupled user interface - can be replaced with a REST API or React UI.
* **Config & Utils:** Centralized configuration and helper functions.

### ✨ Key Features

* ✅ Full CRUD operations for products
* ✅ Layered architecture (Models, Repos, Services)
* ✅ Centralized validation system
* ✅ Custom exception handling
* ✅ SQLite database with scalable schema
* ✅ Interactive CLI
* ✅ Unit tests included (`/tests`)
* ✅ Ready for migration to PERN Stack

### 📁 Project Structure
<img width="687" height="368" alt="image" src="https://github.com/user-attachments/assets/65cddcd2-2df6-4784-9fcd-f4f6adb69f3e" />

### 🚀 How to Run
python main.py

### By:Mohammad Nafiz Sammour

### IT Specialist | Software Engineer
### Focus: System Design & Flutter & PERN Stack
### Palestine Ahliya University - Honors Graduate (3.57 GPA)

# Feel free to check my other projects and connect!😊❤️
