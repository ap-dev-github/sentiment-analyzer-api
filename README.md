#  Sentiment Analyzer API

## 📝 Overview
> The **Sentiment Analyzer API** intelligently processes text input via a **path parameter**, utilizing **NLTK's SentimentIntensityAnalyzer** to extract **negative, positive, and neutral scores**. Based on these values, it determines the **dominant emotion** and classifies the **sentiment in real time**.  

>Designed for **efficiency and scalability**, this API **automatically tests and deploys** any code changes to **AWS Lambda** using the **Serverless Framework**. It seamlessly **balances load** with **AWS API Gateway**, ensuring **high availability and performance** under varying traffic loads.  

>With its **serverless architecture**, the API **scales down to zero cost** when idle (**for Lambda alone**). When used with **API Gateway and S3**, operational costs can **reduce by up to 98%**, making it a **lightweight, cost-effective, and highly scalable** sentiment analysis solution.  
 
## 🎯 Use Cases
-  **Review Categorization**: Automatically classifies reviews as **Positive, Negative, or Neutral**.
-  **Automated Customer Support**: Negative reviews trigger **AWS SNS notifications** to notify the **QA team** and send a **custom apology email** to the customer.
- **Recommendation System**: Uses **positive reviews** to suggest the best-rated products or services.
-  **Scalability & Serverless**: Designed to work **seamlessly** with **AWS Lambda**, ensuring **cost efficiency and  automatic scaling**.

## 📊 Scalability Optimization & Cost Efficiency
- Uses **AWS API Gateway** for **auto-scaling** and **load balancing** under high traffic.
-  **Cold Start Prevention**: Removes unnecessary dependencies after testing to ensure **fast startup times**.
- The API **scales down** to nearly **zero cost** for **up to 1 million requests/month** (including AWS services like **S3, EC2, DynamoDB**).

## ⚙️ Deployment Pipeline (CI/CD)
The API is **fully serverless** and **automatically deploys** when updates are pushed to the repository.

### 🏗 **GitHub Actions Workflow**
🔹 **Triggers:**  
   - 📌 Push to `main` or `dev` branches  
🔹 **Deployment Jobs:**  
   -  Sets up **Python 3.9**  
   -  Installs dependencies  
   -  Runs **security testing** using `run_checks.sh`  
   -  Deploys the API to **AWS Lambda using Serverless Framework**  
   -  Prunes old deployments, keeping only the last **two versions**  

## 🔐 Security & Testing Pipeline
Each deployment runs a **test script** that performs:  
- ✅ **Unit Tests** (`pytest`) 
- 🔍 **Linting** (`flake8`)  
- 🗂 **Import Organization** (`isort`)  
- 📏 **Static Type Checking** (`mypy`)  
- 🛡 **Security Scans** (`bandit`)  

## 🚀 API Endpoints
### 📡 1. Analyze Sentiment
```http
GET /analyze/<text>
```
#### Parameters:
| Parameter | Type   | Description               |
|-----------|--------|---------------------------|
| `text`    | string | Input text for sentiment analysis |

#### Example Response:
```json
{
  "positive": 0.8,
  "neutral": 0.1,
  "negative": 0.1,
  "dominant_sentiment": "Positive"
}
```

## Conclusion
The **Sentiment Analyzer API** is a **highly scalable**, **serverless** solution designed for **real-time sentiment analysis**. It is ideal for **customer feedback management**, **recommendation systems**, and **automated customer support workflows**.

🚀 **Built with Flask | Serverless | AWS Lambda | GitHub Actions | Passion :)**
## Developer and Maintainer

# **Ayush Pandey**
[🔗 Connect on LinkedIn](https://www.linkedin.com/in/linkedap/)  
📧 **Email:** [ayushpandey.cs@gmail.com](mailto:ayushpandey.cs@gmail.com)  
