# Text Processing API with FastAPI Backend

## 📌 Overview
This project is a **text processing API** built using **FastAPI** that integrates **LLM models** (Hugging Face & OpenAI) for:
- **Summarization**
- **Keyword Extraction**
- **Sentiment Analysis**

A **Streamlit frontend** is provided to interact with the API and retrieve session-based history.

---

## 🚀 Features
✅ **RESTful API** using FastAPI  
✅ **Text Summarization** using Hugging Face LLM  
✅ **Named Entity Recognition (NER) for Keywords** using NLP libraries  
✅ **Sentiment Analysis** using TextBlob  
✅ **Session-based history retrieval**  
✅ **Streamlit UI for User Interaction**  

---

## 📦 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/salmankhh8/Rezolve.ai_Assingment.git
cd Rezolve.ai_Assingment
```

### **2️⃣ Install Dependencies**
Install all dependencies from the `requirements.txt` file:
```sh
pip install -r requirements.txt
```

### **3️⃣ Build and Run the Application**
```sh
uvicorn main:app --reload
```
This will start the backend on `http://127.0.0.1:8000`

---

## 🔥 Running the Application
### **1️⃣ Start API**
```sh
uvicorn main:app --reload
```
This will start the backend on `http://127.0.0.1:8000`

### **2️⃣ Start Frontend**
```sh
streamlit run frontend_stremlit.py
```
This will open the frontend in your browser.

---

## 📡 API Endpoints
### **Process Text**
- **Endpoint:** `POST /process`
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
- **Endpoint:** `GET /history`
- **Response:** Returns all previously processed texts in the session.

---

## 🎨 Streamlit UI
The frontend allows users to:
- **Enter text for processing**
- **Retrieve session-based chat history**
- **Display summarized text, keywords, and sentiment**

---

## 🛠 Tech Stack
- **Backend:** FastAPI, Hugging Face API
- **Frontend:** Streamlit
- **Database:** In-memory (Session-based storage)

---

## 📜 License
MIT License

---

## 🤝 Contributing
Feel free to submit issues or pull requests! 🚀

