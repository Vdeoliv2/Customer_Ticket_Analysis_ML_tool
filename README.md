# AI-Powered Customer Support Analytics

## 1. Project Overview

This project is a customer-support analytics system developed using Python, Pandas, scikit-learn, Streamlit, and Llama 3.1.

The system analyzes historical customer-support tickets and provides an interactive dashboard for exploring ticket volume, resolution performance, customer satisfaction, and unresolved requests.

It also uses a traditional machine-learning model based on TF-IDF and Logistic Regression to predict the category of newly submitted support tickets.

A separate local Llama 3.1 integration provides additional analysis, including ticket summaries, categories, sentiment, and urgency.

The public Streamlit application includes the dashboard and traditional ML classifier. Llama 3.1 functionality is available in the local version only.

### Problem Statement

Customer-support teams handle large numbers of requests involving different issues and priorities. Manually reviewing these tickets can make it difficult to identify patterns, monitor unresolved requests, and categorize new submissions consistently.

This project explores how data analytics and machine learning can support these tasks while examining the limitations of automated ticket classification.

### Project Objectives

- Clean and analyze historical customer-support data.
- Develop an interactive dashboard to explore support performance.
- Classify incoming tickets using traditional machine learning.
- Explore locally hosted LLM analysis for additional ticket insights.
- Evaluate model performance and document limitations.
- Deploy the dashboard and traditional ML classifier as a publicly accessible application.

---

## 2. Project Features

### 2.1 Historical Customer Support Dashboard

The Streamlit dashboard allows users to explore historical customer-support tickets through interactive filters, metrics, and visualizations.

**Interactive filters:**
- Ticket Type
- Ticket Priority

**Key performance indicators:**
- Total Tickets
- Unresolved Tickets
- High Unresolved Tickets
- Critical Unresolved Tickets
- Average Customer Satisfaction
- Average Resolution Time

**Data visualizations:**
- Ticket Volume by Type
- Average Satisfaction by Type
- Average Resolution Time by Type

**Additional functionality:**
- View historical ticket details.
- Examine unresolved customer-support requests.
- Update dashboard metrics and charts using the selected filters.

### 2.2 Traditional Machine Learning Ticket Classification

The system includes a traditional machine-learning classifier that predicts the category of a newly submitted customer-support ticket.

**Technologies:**
- TF-IDF Vectorization
- Logistic Regression
- scikit-learn

**Classification workflow:**

1. The user enters a customer-support ticket description.
2. The application validates the input.
3. The description is transformed into numerical TF-IDF features.
4. The trained Logistic Regression model predicts the Ticket Type.
5. The predicted category is displayed in the application.

The classifier supports automated categorization but is experimental and may generate inaccurate predictions.

### 2.3 Local Llama 3.1 Ticket Analysis

The local application integrates Llama 3.1 through Ollama to provide additional natural-language analysis.

**LLM capabilities:**
- **Summary:** Generate a concise summary of the customer's issue.
- **Category:** Identify the ticket's likely category.
- **Sentiment:** Analyze the sentiment expressed in the ticket.
- **Urgency:** Estimate how urgently the issue may require attention.

The local application also allows comparison between traditional ML classification and LLM-generated categorization.

**Important:** Llama 3.1 requires a locally running Ollama server and is not available through the public Streamlit deployment.

### 2.4 Input Validation and Error Handling

The application includes input validation and error handling to improve usability.

Implemented safeguards include:

- Rejecting empty ticket descriptions.
- Rejecting whitespace-only descriptions.
- Rejecting descriptions without alphabetic characters.
- Displaying error messages when ticket analysis fails.
- Handling Ollama connection failures in the local version.

These safeguards reduce common input and execution problems but do not guarantee that every possible failure is handled.

### 2.5 Public Streamlit Deployment

The public version is deployed using Streamlit Community Cloud.

**Publicly available features:**
- Historical customer-support dashboard.
- Interactive filtering and visualizations.
- Traditional ML ticket classification.
- Input validation.

**Local-only features:**
- Llama 3.1 ticket summarization.
- LLM sentiment analysis.
- LLM urgency analysis.
- LLM ticket categorization.
- Traditional ML versus LLM comparison.

The project uses a hybrid deployment approach to demonstrate traditional machine learning publicly without requiring a hosted LLM service.

---

## 3. Technologies and System Architecture

### 3.1 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Pandas | Data cleaning, transformation, and analysis |
| SQLite | Storage and querying of structured customer-support data |
| SQL | Querying and aggregating historical ticket records |
| Microsoft Excel | Spreadsheet-based analysis and dashboard development |
| scikit-learn | Traditional machine-learning model development |
| TF-IDF Vectorizer | Converting ticket descriptions into numerical features |
| Logistic Regression | Predicting ticket categories |
| Streamlit | Building the interactive web application |
| Ollama | Running the Llama 3.1 model locally |
| Llama 3.1 | Generating summaries and analyzing category, sentiment, and urgency |
| Joblib | Loading serialized machine-learning artifacts |
| GitHub | Source-code hosting and version control |
| Streamlit Community Cloud | Hosting the public web application |
| Jupyter Notebook | Data exploration, experimentation, and model evaluation |

### 3.2 System Architecture

The system has two primary workflows:

1. Historical customer-support analytics.
2. New ticket classification and AI analysis.

#### Workflow A — Historical Customer Support Analytics

```text
Historical Customer Support Dataset
                |
                v
       Python and Pandas
                |
                v
    Data Cleaning and Processing
                |
                v
       Structured Ticket Data
                |
       +--------+--------+
       |                 |
       v                 v
  SQLite / SQL      Excel Analysis
       |                 |
       +--------+--------+
                |
                v
       Streamlit Dashboard
                |
                v
   Filters, KPIs, Charts, Tables
```

This workflow prepares historical customer-support data and makes it available for analysis.

The Streamlit dashboard uses the processed ticket dataset to calculate metrics and generate visualizations. SQLite and Excel are additional components of the broader analytics project; the dashboard does not require a live database connection.

#### Workflow B — New Ticket Classification

```text
       User Enters Ticket
                |
                v
         Input Validation
                |
                v
       Ticket Description
                |
                v
        TF-IDF Vectorizer
                |
                v
       Logistic Regression
                |
                v
      Predicted Ticket Type
                |
                v
       Streamlit Interface
```

This workflow uses traditional machine learning to classify newly submitted customer-support tickets.

The TF-IDF vectorizer converts text into numerical features, and Logistic Regression predicts the most likely ticket category.

The public deployment uses saved machine-learning artifacts so the classifier can perform inference without retraining the model for every prediction.

#### Workflow C — Local Llama 3.1 Analysis

```text
       User Enters Ticket
                |
                v
         Input Validation
                |
                v
       Ticket Description
                |
                v
       Local Ollama Server
                |
                v
           Llama 3.1
                |
                v
      Structured AI Analysis
                |
       +--------+--------+
       |        |        |
       v        v        v
    Summary  Sentiment  Urgency
                |
                v
        Ticket Category
                |
                v
       Streamlit Interface
```

This workflow sends a ticket description to the locally hosted Llama 3.1 model.

The LLM generates a structured response containing a summary, category, sentiment, and urgency assessment.

These results can be compared with the traditional machine-learning classifier in the local application.

### 3.3 Main Project Components

| Component | Responsibility |
|---|---|
| `app.py` | Streamlit interface, dashboard, ticket input, and result presentation |
| `src/data_processing.py` | Loading and processing customer-support data |
| `src/database.py` | Database-related operations |
| `src/classifier.py` | TF-IDF vectorization, model training, and ticket classification |
| `src/ai_analyzer.py` | Llama 3.1 ticket analysis through Ollama |
| `data/` | Historical and processed datasets |
| `notebooks/` | Data exploration and machine-learning experiments |
| `sql/` | SQL-related project work |
| `excel/` | Excel dashboard and analysis |
| `docs/` | Project documentation and testing records |
| `requirements.txt` | Python dependency specifications |

### 3.4 Public vs. Local Architecture

| Capability | Public Streamlit Cloud | Local Application |
|---|---|---|
| Historical dashboard | Available | Available |
| Ticket filtering | Available | Available |
| Traditional ML classifier | Available | Available |
| Ticket input validation | Available | Available |
| Llama 3.1 analysis | Not available | Available with Ollama |
| LLM sentiment and urgency | Not available | Available with Ollama |
| ML versus LLM comparison | Not available | Available with Ollama |

The public deployment intentionally excludes local Ollama functionality because Streamlit Community Cloud cannot directly access the Ollama server running on a user's personal computer.

### 3.5 Design Decisions

**Traditional ML for public deployment**

TF-IDF and Logistic Regression were selected as a relatively lightweight approach to ticket classification. The public application can perform inference without depending on a locally hosted LLM.

**Llama 3.1 for local experimentation**

Llama 3.1 provides additional natural-language analysis, including summarization, sentiment, and urgency. Keeping this functionality local avoids the need for a paid hosted LLM API.

**Streamlit for application development**

Streamlit provides an interactive interface for presenting historical analytics and demonstrating machine-learning predictions.

**Separate processing and analysis modules**

The project separates data processing, machine-learning classification, LLM analysis, and user-interface logic into different Python modules to improve organization and maintainability.
