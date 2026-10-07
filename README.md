# 🚀 Lead Intent Classifier CRM

### 🤖 AI-Powered Lead Management & Intent Classification System

> Automatically understand incoming lead messages, predict their intent, and organize them inside a simple CRM workflow.

---

## 🌟 About The Project

**Lead Intent Classifier CRM** is a Machine Learning based CRM application that automatically analyzes incoming lead messages and identifies what the customer is looking for.

The system uses **NLP + TF-IDF + Logistic Regression** to classify leads into four categories:

| Intent | Purpose |
|---|---|
| 🎯 Demo Request | Customer wants a product demo |
| 💰 Pricing | Customer wants pricing information |
| 🛠️ Support | Customer needs technical/help support |
| 📧 General Enquiry | Customer wants general information |
## 🌐 Live Demo
👉 [Open Live App]https://lead-intent-classifier-crm-amishakeshri.streamlit.app

## ✨ Key Features

- 🤖 **AI-based Intent Classification**
- 🧠 **Natural Language Processing**
- 🔤 **TF-IDF Text Vectorization**
- 📊 **Machine Learning Prediction**
- 💾 **Automatic CRM Lead Storage**
- 📈 **Admin Dashboard**
- 📋 **Lead Records Management**
- ⚡ **Real-time Prediction with Streamlit**
- 🎯 **Intent-based Follow-up Actions**

---

## 🔄 How It Works

```text
             📩 Lead Message
                    │
                    ▼
          🧹 Text Preprocessing
                    │
                    ▼
          🔤 TF-IDF Vectorization
                    │
                    ▼
        🤖 Logistic Regression
                    │
                    ▼
           🎯 Intent Prediction
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Demo      Pricing    Support
          │         │         │
          └─────────┼─────────┘
                    ▼
             💾 Save to CRM
                    │
                    ▼
             📊 Admin Dashboards
