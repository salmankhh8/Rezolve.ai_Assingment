[# Rezolve.ai_Assingment](https://github.com/salmankhh8/Rezolve.ai_Assingment)

# Text Processing API with .NET Backend

## 📌 Overview
This project is a **text processing API** built using **ASP.NET Core** that integrates **LLM models** (Hugging Face & OpenAI) for:
- **Summarization**
- **Keyword Extraction**
- **Sentiment Analysis**

A **Blazor frontend** is provided to interact with the API and retrieve session-based history.

---

## 🚀 Features
✅ **RESTful API** using ASP.NET Core  
✅ **Text Summarization** using Hugging Face LLM  
✅ **Named Entity Recognition (NER) for Keywords** using NLP libraries  
✅ **Sentiment Analysis** using ML.NET  
✅ **Session-based history retrieval**  
✅ **Blazor UI for User Interaction**  

---

## 📦 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/salmankhh8/Rezolve.ai_Assingment
cd text-processing-api-dotnet
```

### **2️⃣ Install Dependencies**
```sh
dotnet restore
```

### **3️⃣ Build and Run the Application**
```sh
dotnet run
```
This will start the backend on `http://localhost:5000`

---

## 🔥 Running the Application
### **1️⃣ Start ASP.NET Core API**
```sh
dotnet run --project TextProcessingApi
```
This will start the backend on `http://localhost:5000`

### **2️⃣ Start Blazor Frontend**
```sh
dotnet run --project TextProcessingUI
```
This will open the frontend in your browser.

---

## 📡 API Endpoints
### **Process Text**
- **Endpoint:** `POST /api/process`
- **Request:**
  ```json
  {
    "text": "Your input text here"
  }
  ```
- **Response:**
  ```json
  {
    "summary": "Shortened text...",
    "keywords": ["keyword1", "keyword2"],
    "sentiment": "positive"
  }
  ```

### **Retrieve History**
- **Endpoint:** `GET /api/history`
- **Response:** Returns all previously processed texts in the session.

---

## 🎨 Blazor UI
The frontend allows users to:
- **Enter text for processing**
- **Retrieve session-based chat history**
- **Display summarized text, keywords, and sentiment**

---

## 🛠 Tech Stack
- **Backend:** ASP.NET Core, ML.NET, Hugging Face API
- **Frontend:** Blazor
- **Database:** In-memory (Session-based storage)

---

## 📜 License
MIT License

---

## 🤝 Contributing
Feel free to submit issues or pull requests! 🚀

