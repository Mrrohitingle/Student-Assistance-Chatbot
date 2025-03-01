# Sanjivani Student Assist 🏫

A **Streamlit-based AI chatbot** that allows students to ask questions related to their academic materials. It extracts information from university documents like the syllabus and academic calendar and provides **accurate, AI-powered responses**.

## 🚀 Features
- 📄 **PDF Processing:** Extracts text from internal university documents.
- 🔍 **AI-Powered Search:** Uses **FAISS vector search** for quick and relevant document retrieval.
- 🤖 **Conversational AI:** Leverages **Google Generative AI (Gemini Pro)** for answering queries.
- 🌐 **User-Friendly Web App:** Built using **Streamlit** for an interactive experience.

---

## 🛠️ Technologies Used
| **Technology** | **Purpose** |
|--------------|-------------|
| **Streamlit** | Web UI framework |
| **PyPDF2** | Extracts text from PDFs |
| **LangChain** | AI-based question-answering pipeline |
| **FAISS** | Efficient document search using embeddings |
| **Google Generative AI (Gemini Pro)** | Generates AI responses |
| **Python-dotenv** | Manages environment variables |

---

## 📥 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/sanjivani-student-assist.git
cd sanjivani-student-assist
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Create a **.env** file and add your Google Generative AI API Key:
```
GOOGLE_API_KEY=your_api_key_here
```

### 4️⃣ Run the App
```sh
streamlit run app.py
```

---

## 🎯 How It Works
1. **Loads and processes PDFs** 📄.
2. **Stores text embeddings** in FAISS 🧠.
3. **Retrieves relevant information** based on user queries 🔍.
4. **Generates AI-powered answers** using LangChain and Gemini Pro 🤖.

---

## 📌 Usage
- Run the application and enter your question in the chatbot interface.
- The chatbot searches for relevant information in the **syllabus and academic calendar**.
- If an answer is available, it responds based on the documents.
- If no answer is found, it will say **"answer is not available in the context"** to ensure accuracy.

---

## 🛠️ Future Enhancements
✅ Support for **DOCX files** 📄
✅ Integration with **more AI models** 🤖
✅ Enhanced UI with **chat history and voice input** 🎨

---

## 🤝 Contributing
Feel free to fork the repo and submit a pull request! Contributions are welcome. 😊

---

## 📧 Contact
For queries or feedback, reach out at: 
📩 [rohitingle2912@gmail.com](mailto:rohitingle2912@gmail.com)

![image](https://github.com/user-attachments/assets/d840bddb-3975-4a15-86d6-268628826bf6)
