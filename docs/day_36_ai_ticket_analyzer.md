# Day 36 — AI Ticket Analyzer

## Objective

The objective of Day 36 was to connect the reusable traditional machine-learning and LLM components to the Streamlit application.

## Work Completed

I created an AI Ticket Analyzer interface that allows a user to enter a new customer-support ticket description.

The application validates the input before performing analysis.

The same ticket description is processed by two approaches:

### Traditional Machine Learning

The ticket description is transformed using TF-IDF and classified using the Logistic Regression classifier developed earlier in the project.

### LLM Analysis

The ticket description is analyzed using Llama 3.1 through Ollama.

The LLM produces structured information containing:

- Summary
- Category
- Sentiment
- Urgency

The Streamlit interface displays the traditional ML category and LLM category together for comparison.

Because new user-entered tickets do not contain known ground-truth labels, the application does not claim that either prediction is correct.

## Error Handling

The analysis is protected with exception handling so that an LLM or parsing failure produces an error message in the Streamlit interface instead of crashing the entire application.

Blank ticket descriptions are also rejected before either analysis pipeline is executed.

## Application Flow

User enters ticket
→ input validation
→ ML classifier
→ LLM analyzer
→ structured results
→ ML vs. LLM comparison

## Conclusion

On Day 36, I integrated the project's traditional machine-learning classifier and Llama 3.1 ticket analyzer into the Streamlit application.

The AI Ticket Analyzer allows a user to enter a new customer-support ticket description through the web interface.

The traditional ML pipeline predicts a Ticket Type, while the LLM pipeline returns a Summary, Category, Sentiment, and Urgency.

The interface presents the ML and LLM category predictions together while also displaying the additional structured information produced by the LLM.

Error handling was added so that invalid input or an analysis failure can be communicated through the interface instead of causing the entire application to fail.

This completes the main analytical functionality of the Streamlit prototype: historical support-ticket analysis through the Support Dashboard and new-ticket analysis through the AI Ticket Analyzer.

The next step is to test the complete application under edge cases before deployment.
