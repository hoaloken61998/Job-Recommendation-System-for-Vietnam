Job Recommendation System for Vietnam

# 🇻🇳 Job Recommendation System for Vietnam

A **job recommendation system** tailored for the Vietnamese labor market, combining **Content-Based Filtering (CBF)** with **Natural Language Processing (NLP)**.  

This project was developed as part of the *Web Data Analytics* course final project, and also demonstrates skills in **data collection, NLP, and recommender systems** — directly applicable to real-world applications in **HR Tech, e-commerce, and AI-driven platforms**.

---

## ✨ Features
- 🔎 **Data Crawling**: Automated scraping of 46,000 candidate CVs (Timviec365.vn) and 21,000 job postings (CareerViet.vn).  
- 🧹 **Preprocessing**: Text cleaning, tokenization (ViTokenizer), normalization of salary & experience.  
- 🧠 **NLP Models**:  
  - TF-IDF (baseline)  
  - Pho2Vec (100d & 300d)  
  - PhoBERT + PCA (best performance)  
- 📊 **Evaluation Metrics**: Precision@K, Recall@K, nDCG@K, MAP@K.  
- 🌐 **Demo Web App**: Simple interface where a candidate uploads their CV and receives job recommendations.  

---

## 🚀 Results
- **PhoBERT + PCA** achieved:  
  - Precision@30: **93%**  
  - nDCG@30: **97%**  
  - MAP@30: **94%**  

These results show strong potential for real-world deployment in Vietnam’s job market.  

---

## 🛠️ Tech Stack
- **Languages**: Python  
- **Libraries**: Scikit-learn, PyTorch, HuggingFace Transformers, Pandas, NumPy, Matplotlib  
- **Tools**: Selenium, BeautifulSoup, Playwright (data crawling)  
- **Deployment**: Flask / Streamlit  



## 📂 Repository Structure
