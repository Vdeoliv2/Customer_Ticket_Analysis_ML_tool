# AI-Powered Customer Support Analytics

## Project Overview

This project is a customer-support analytics system developed using Python, Pandas, scikit-learn, Streamlit, and Llama 3.1.

The system analyzes historical customer-support tickets and provides an interactive dashboard for exploring ticket volume, resolution performance, customer satisfaction, and unresolved requests.

It also uses a traditional machine-learning model based on TF-IDF and Logistic Regression to predict the category of newly submitted support tickets.

A separate local Llama 3.1 integration provides additional analysis, including ticket summaries, categories, sentiment, and urgency.

The public Streamlit application includes the dashboard and traditional ML classifier. Llama 3.1 functionality is available in the local version only.

## Problem Statement

Customer-support teams handle large numbers of requests involving different issues and priorities. Manually reviewing these tickets can make it difficult to identify patterns, monitor unresolved requests, and categorize new submissions consistently.

This project explores how data analytics and machine learning can support these tasks while examining the limitations of automated ticket classification.

## Project Objectives

- Clean and analyze historical customer-support data.
- Develop an interactive dashboard to explore support performance.
- Classify incoming tickets using traditional machine learning.
- Explore locally hosted LLM analysis for additional ticket insights.
- Evaluate model performance and document limitations.
- Deploy the dashboard and traditional ML classifier as a publicly accessible application.
