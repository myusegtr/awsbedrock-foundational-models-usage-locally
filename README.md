# 🤖 Chat with PDF using AWS Bedrock

## 🧠 AIM of the Project

To create a fully functional local application that allows users to **ask questions about PDF documents** using powerful **AWS Bedrock foundation models**, such as Mistral and LLaMA 3. The project combines text ingestion, vector embedding, and retrieval-based question answering using LangChain and Streamlit.

---

## 📘 Description of the Project

This project integrates **AWS Bedrock-hosted LLMs** with local document processing to deliver an intuitive **Chat with PDF interface**. Users can upload one or more PDF files, generate vector embeddings from the content using **Amazon Titan Embedding models**, and ask natural language questions based on the uploaded documents.

The app performs the following key tasks:

1. **Document Ingestion** – PDF files are read and split into text chunks.
2. **Vector Store Creation** – Text chunks are embedded using AWS Titan models and stored in a FAISS vector store.
3. **Prompting & Question Answering** – A customized prompt ensures answers are grounded in the document context.
4. **Model Invocation** – Users can choose between Mistral and LLaMA 3 models deployed via AWS Bedrock to generate responses.
5. **Optional Standalone Prompting** – Code also includes standalone usage of AWS Bedrock models for querying external topics (e.g., AI news).

---

## 🛠️ Tools & Technologies Used

- **AWS Bedrock**: For accessing foundation models (Mistral, LLaMA 3, Titan Embeddings)
- **LangChain**: For chaining prompts, retrieval, and QA logic
- **FAISS**: For local vector similarity search
- **Streamlit**: For creating a simple and interactive web UI
- **boto3**: AWS SDK for Python
- **PyPDFDirectoryLoader**: To read and process PDF files

---

## 💼 Use Case Explanation

### 🗂️ Chat with PDF (via Streamlit UI)

- Users upload PDFs into the `document/` directory.
- Click **“Vectors Update”** to generate vector embeddings for the document.
- Enter any natural language query in the text box.
- Click **“Mistral Output”** or **“Llama Output”** to get context-aware answers from the document using AWS Bedrock models.

This setup allows **enterprise-scale document Q&A** locally while leveraging secure and scalable AWS-hosted LLMs.

---

## 📌 Conclusion / Inference

This project showcases how **serverless LLMs from AWS** can be effectively integrated into local applications using open-source tooling like Streamlit and LangChain. It also highlights the practical value of embedding-based retrieval to deliver **accurate, context-sensitive answers** from custom documents.

---

## 🚀 Further Enhancements Possible

- 🔒 Add **authentication** and **file upload controls** to manage user input securely.
- 📁 Support **multi-file PDFs** and **hierarchical document views**.
- 🧠 Add **metadata filtering** (e.g., document title, author) in vector search.
- 🗃️ Persist Q&A history for reference or exporting.
- 🔍 Introduce **semantic search UI** or chatbot-style interface.
- ☁️ Deploy Streamlit on **AWS EC2 / Lambda** for wider access.



![App Screenshot](screenshot.UI_screenshot)
---


### Notes:-
# mykey
 mykey is a placeholder name used to refer to your AWS access key, which is needed to use AWS Bedrock models from your local machine.

✅ What it's for:
It allows you to authenticate as a specific user in your AWS account.

With the key, you can access and interact with foundation models (FMs) provided by AWS Bedrock.

🛠️ How to get it:
Go to the AWS Console → IAM (Identity and Access Management).

Select the IAM user you’ll use to access Bedrock.

Under Security credentials, generate a new Access key (you'll get an Access Key ID and Secret Access Key).

Save these securely.

🚀 How to use it:
Once you have the keys, you can use them in your terminal or scripts to access Bedrock models:

bash
```
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

aws configure --to run through local terminal

```
python mistral.py
streamlit run app.py
```


