# AI-Powered Customer Support Analytics

**[Live Streamlit Demo](https://customerticketanalysismltool-bjfmpqwqdgbgud3gyrlh4e.streamlit.app/)** | **[GitHub Source Code](https://github.com/Vdeoliv2/Customer_Ticket_Analysis_ML_tool)**

> The public application includes the historical dashboard and TF-IDF/Logistic Regression ticket classifier. Llama 3.1 analysis requires local Ollama.

![Support Dashboard](https://github.com/user-attachments/assets/17108cb9-65b4-48a6-904a-23b12651466c)

![AI Ticket Analyzer](https://github.com/user-attachments/assets/9ccb195d-1d3d-49a3-a3d4-c2207c4f4591)

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
| GitHub | Source-code hosting and version control |
| Streamlit Community Cloud | Hosting the public web application |
| Jupyter Notebook | Data exploration, experimentation, and model evaluation |

### 3.2 System Architecture

The application has two main functions, with an optional local LLM branch:

1. Historical customer-support analytics.
2. New ticket classification using traditional ML.
3. Optional local Llama 3.1 analysis.

#### Workflow A — Historical Customer Support Analytics

```text
Historical Support Tickets (CSV)
              |
              v
       Python / Pandas
              |
              v
       Streamlit Dashboard
              |
              v
    Filters, KPIs, Charts, Tables

Separate project analysis: SQLite / SQL and Excel
(these do not feed the live Streamlit dashboard)
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

The application trains the TF-IDF vectorizer and Logistic Regression classifier from the historical ticket dataset at runtime and uses the fitted components to predict new ticket categories. It does not require saved Joblib model artifacts.

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

---

## 4. Installation and Usage

**Local setup verification (October 23, 2026):** Python 3.12 virtual environment, dependency installation, local Streamlit startup, and traditional ML classification were demonstrated. The optional Ollama workflow was not retested as part of this verification.

The application was launched successfully at `http://localhost:8501` using a Python 3.12 virtual environment. The AI Ticket Analyzer accepted a refund-related description, returned the traditional ML category **Billing Inquiry**, and displayed the expected message indicating that Llama 3.1 analysis was disabled. These checks confirm the tested local ML workflow; optional Ollama functionality was not retested as part of this verification.


### 4.1 Public Streamlit Application

The public application can be accessed without installing Python or downloading the repository.

**Live Application:** https://customerticketanalysismltool-bjfmpqwqdgbgud3gyrlh4e.streamlit.app/

The public version includes:
- Historical customer-support analytics.
- Interactive dashboard filters, metrics, and visualizations.
- Traditional ML ticket classification using TF-IDF and Logistic Regression.
- Ticket description input validation.

Llama 3.1 analysis is not available in the public deployment.

### 4.2 Requirements for Local Installation

To run the application locally, you need:

- Python 3.12 (the version used during local development).
- Git.
- A terminal or command-line interface.
- The Python packages listed in `requirements.txt`.
- Ollama and the Llama 3.1 model (optional, for local LLM analysis).

### 4.3 Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/Vdeoliv2/Customer_Ticket_Analysis_ML_tool.git
cd Customer_Ticket_Analysis_ML_tool
```

### 4.4 Create a Virtual Environment

On Windows:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe --version
```

If Python 3.12 is not installed, install it before creating the environment.

### 4.5 Install Python Dependencies

Run:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

This installs the Python packages required by the application.

### 4.6 Run the Application Without Llama 3.1

In PowerShell, run:

```powershell
$env:LLM_ENABLED = "false"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Streamlit will start a local web server and display a URL, usually:

http://localhost:8501

Open that address in your browser.

With Llama 3.1 disabled, you can use the historical dashboard and traditional ML classifier.

### 4.7 Optional — Enable Local Llama 3.1 Analysis

To enable LLM features, install Ollama:

https://ollama.com/

After installing Ollama, download the Llama 3.1 model:

```bash
ollama pull llama3.1
```

Make sure Ollama is running.

In PowerShell, enable the LLM:

```powershell
$env:LLM_ENABLED = "true"
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The local application can then use Llama 3.1 to generate ticket summaries, categories, sentiment assessments, and urgency assessments.

The local version can also compare traditional ML and LLM classifications.

**Note:** The first Llama 3.1 download may take time and requires sufficient storage and system resources.

### 4.8 How to Use the Application

**Historical Dashboard**

1. Open the application.
2. Navigate to the Support Dashboard.
3. Select the desired Ticket Type and Ticket Priority filters.
4. Review ticket metrics and visualizations.
5. Inspect the filtered ticket details.

**AI Ticket Analyzer**

1. Navigate to the AI Ticket Analyzer.
2. Enter a customer-support ticket description.
3. Click **Analyze Ticket**.
4. Review the traditional ML prediction.
5. If running locally with Ollama enabled, review the additional Llama 3.1 analysis.

### 4.9 Troubleshooting

**Missing Python package**

From the repository directory, run:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Streamlit does not start**

Verify that the terminal is inside the repository folder and that `app.py` exists.

**Ollama connection error**

Confirm that Ollama is installed, running, and has the `llama3.1` model available.

**LLM features are not visible**

Check whether the `LLM_ENABLED` environment variable is set to `true`, then restart Streamlit.

**Incorrect ML prediction**

The classifier is experimental and may misclassify tickets. An incorrect prediction does not necessarily indicate an application installation problem.


---

## 5. Model Evaluation and Limitations

### 5.1 Evaluation Approach

The project explores ticket categorization with a traditional TF-IDF and Logistic Regression classifier and a locally hosted Llama 3.1 model. The results below come from previously recorded experiments. The project is a learning and portfolio demonstration, not a production-ready support automation service.

### 5.2 Recorded Results

| Evaluation | Result |
|---|---:|
| Traditional ML held-out test accuracy | 19.48% |
| Tickets in the separate manual comparison | 25 |
| Traditional ML matches in manual comparison | 14/25 (56%) |
| Llama 3.1 matches in manual comparison | 4/25 (16%) |

The traditional ML evaluation used an approximately 80/20 train/test split. The **19.48% held-out test accuracy** and the **56% match rate on a separate 25-ticket sample** were obtained under different evaluation conditions and should not be compared as equivalent measures. The small comparison does not establish general superiority of either model.

The Llama 3.1 comparison evaluates category matches only; it does not independently measure the quality of generated summaries, sentiment labels, or urgency labels.

### 5.3 Example Application Test

During local testing on October 23, 2026, the input `I am issues with refunding` returned **Billing Inquiry**. This confirmed that the application accepted text and produced a prediction, but one plausible prediction does not demonstrate reliable accuracy.

### 5.4 Known Limitations

- **Low classification accuracy:** The recorded held-out test accuracy of 19.48% is not sufficient for dependable automatic categorization.
- **Small comparison sample:** The 25-ticket comparison is limited and may not represent real-world ticket distributions.
- **Ambiguous labels and ticket descriptions:** Overlapping issues and limited context may affect both approaches.
- **Local-only LLM:** Summarization, sentiment, urgency, and LLM category analysis require a running Ollama server and are not available in the public deployment.
- **No live ticket-system integration:** The app uses historical data and manually entered descriptions.
- **Runtime model training:** The current implementation trains its TF-IDF and Logistic Regression components when processing a valid ticket rather than loading persisted model artifacts, which can add latency.

### 5.5 Potential Improvements

- Review label quality, class distribution, and text preprocessing.
- Compare alternative models and use cross-validation and per-class precision, recall, and F1-score.
- Evaluate the LLM on a larger, consistently labeled sample.
- Assess summary, sentiment, and urgency quality independently.
- Cache or persist fitted ML components to avoid repeated training.
- Add human review for uncertain classifications and consider live support-system integration.

### 5.6 Evaluation Conclusion

The project demonstrates data preparation, model training, evaluation, interactive analytics, local LLM experimentation, and public deployment. Its main contribution is an end-to-end implementation with transparent limitations, not production-grade predictive accuracy.

---

## 6. Application Screenshots

The screenshots at the top of this README show the **Support Dashboard** and **AI Ticket Analyzer**. They illustrate the historical analytics interface and traditional ML ticket-classification workflow.

The public deployment does not run Ollama or Llama 3.1. Screenshots are from the application and are included as visual evidence, not as proof of classification accuracy.

## 7. Live Demo and Source Code

- **[Launch the public Streamlit application](https://customerticketanalysismltool-bjfmpqwqdgbgud3gyrlh4e.streamlit.app/)** — explore the dashboard and submit a ticket for traditional ML classification.
- **[View the GitHub repository](https://github.com/Vdeoliv2/Customer_Ticket_Analysis_ML_tool)** — inspect the source code, documentation, and project files.

**Deployment scope:** The public application provides dashboard analytics and traditional ML classification. Llama 3.1 summarization, category, sentiment, and urgency analysis are available only when running locally with Ollama.

## 8. Project Conclusion

The AI-Powered Customer Support Analytics project demonstrates an end-to-end portfolio workflow that combines historical ticket analysis, an interactive Streamlit dashboard, traditional machine-learning classification, optional local Llama 3.1 experimentation, testing, and public deployment.

The recorded TF-IDF and Logistic Regression held-out test accuracy was **19.48%**. This limits the reliability of automatic classification and makes the application a learning and portfolio demonstration rather than a production-ready support service. The separate 25-ticket comparison is described in Section 5 and should not be treated as an equivalent accuracy test.

### Future Improvements

- Investigate data quality, class distribution, and overlapping ticket categories.
- Evaluate additional classifiers with cross-validation, precision, recall, and F1-score.
- Test Llama 3.1 on a larger, consistently labeled evaluation set.
- Assess summary, sentiment, and urgency quality independently.
- Cache or persist trained model components to reduce runtime training overhead.
- Explore integration with real ticket-management systems, with appropriate data protection.

**Portfolio outcome:** A publicly accessible analytics and ML demonstration, with optional local LLM features and clearly documented performance and deployment limitations.
