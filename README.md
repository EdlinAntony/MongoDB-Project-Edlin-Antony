# MongoDB Student Database Management System

## 📖 Project Overview
This project demonstrates the integration of Python with MongoDB, a NoSQL database. It automates CRUD (Create, Read, Update, Delete) operations and executes complex queries on student and course records using the `pymongo` library.

## 🎯 Objective
To build a backend system that can efficiently store, retrieve, and query structured and nested data without the constraints of traditional relational databases.

## 🛠️ Tech Stack
- **Language:** Python
- **Database:** MongoDB (NoSQL)
- **Libraries:** PyMongo, JSON

## ✨ Key Features
1. **Data Insertion:** Bulk insertion of student records and nested course documents.
2. **Complex Querying:** Implementation of MongoDB operators:
   - `$gt` (Greater Than)
   - `$lt` (Less Than)
   - `$eq` (Equal To)
3. **Nested Data Handling:** Managing arrays and sub-documents (e.g., a student enrolled in multiple courses).

## 📊 Database Schema
**Collection: `productdb`**
- `rno`: Roll Number (Integer)
- `sname`: Student Name (String)
- `age`: Age (Integer)
- `course`: Course Name (String)
- `address`: Location (String)

**Collection: `infotechdb` (Nested)**
- `name`: Student Name
- `course`: Array of objects containing `name` and `duration`.

## 🚀 How to Run Locally

### Prerequisites
1. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community).
2. Install Python 3.x.

### Installation Steps
1. **Start the MongoDB Server:**
   Open a terminal and run:
   ```bash
   mongod --dbpath C:\data\db

### Project Screenshots

<img width="1917" height="1015" alt="Screenshot 2026-11-24 134223" src="https://github.com/user-attachments/assets/71505ef6-2a76-463f-ad5e-1c093ebd5269" />
