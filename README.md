Job Recommendation System for Vietnam

# Job Recommendation System for Vietnam

A **job recommendation system** tailored for the Vietnamese labor market, combining **Content-Based Filtering (CBF)** with **Natural Language Processing (NLP)**.  

This project was developed as part of the *Web Data Analytics* course final project, and also demonstrates skills in **data collection, NLP, and recommender systems** — directly applicable to real-world applications in **HR Tech, e-commerce, and AI-driven platforms**.

---

## 📖 Project Overview
The Vietnamese labor market faces a paradox: despite thousands of job postings and resumes available online, **job seekers and employers struggle to connect effectively**. Challenges include mismatched expectations, lack of standardized job descriptions, and noisy recruitment data.  

This project addresses these challenges by building a **personalized recommendation system** that:  
- Uses **Content-Based Filtering (CBF)** to match candidate profiles (CVs) with job postings (JDs).  
- Leverages advanced **Vietnamese NLP models** (TF-IDF, Pho2Vec, PhoBERT) to represent text data semantically.  
- Evaluates performance using **real-world datasets**:  
  - **46,000+ candidate profiles** from Timviec365.vn.  
  - **21,000+ job postings** from CareerViet.vn.  

The system demonstrates that **PhoBERT + PCA embeddings** significantly improve recommendation accuracy, reaching:  
- Precision@30: **93%**  
- nDCG@30: **97%**  
- MAP@30: **94%**  


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
+---Dataset
|   +---Cleaned data
|   |   +---Testing data
|   |   |       candidate_data_testing.csv
|   |   |       job_data_testing.csv
|   |   |       
|   |   \---Training data
|   |           cleaned_candidate_data.csv
|   |           cleaned_job_data.csv
|   |
|   \---Uncleaned data
|           candidate_data_TV365.csv
|           job_data_Careerviet.csv
|
+---Demo
|       Job_recommendation_demo.py
|
+---Docs
|       Reports.pdf
|       WEB ANALYSIS.pdf
|
\---Notebooks
    +---Cleaning Data
    |   +---Cleaning Candidate Data
    |   |       Pre_processing_Candidate.ipynb
    |   |
    |   \---Cleaning Job Data
    |           Cleaning_Job_Data.ipynb
    |           Job_Data_Normalize_Time.ipynb
    |
    +---Crawling Data
    |   +---Candidate Data Crawler
    |   |       Crawl_Data_Candidate_TV365.ipynb
    |   |
    |   \---Job Data Crawler
    |           Data_Job_Crawler.ipynb
    |           Data_Job_Crawler_Add_Industry&Type.ipynb
    |
    +---EDA
    |       EDA_Candidate.ipynb
    |       EDA_Job.ipynb
    |
    +---Feature Engineering
    |       Content_based.ipynb
    |       Features Engineering.ipynb
    |
    \---Matching and Evaluation
            Candidate-to-Job Content Similarity_TF_IDF.ipynb
            Candidate_to_Job_Content_Similarity_Pho2Vec100.ipynb
            Candidate_to_Job_Content_Similarity_Pho2Vec300.ipynb
            Candidate_to_Job_Content_Similarity_PhoBERT_NoPCA.ipynb
            Candidate_to_Job_Content_Similarity_PhoBERT_PCA.ipynb
