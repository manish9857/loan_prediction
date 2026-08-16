# 🏦 Loan Approval Prediction App

A machine learning web application that predicts the likelihood of a **loan application being approved** based on applicant financial, demographic, and credit information.

The application is built using **Python, Scikit-learn, and Streamlit**.

## Features

* Interactive Streamlit interface
* Loan approval probability prediction
* Applicant and co-applicant income inputs
* Credit history consideration
* Property-area-based prediction
* Configurable loan amount and loan term
* Probability-based approval decision
* Machine learning model loaded from a serialized `.pkl` file
* Simple and user-friendly prediction interface

## Machine Learning

The project evaluates multiple classification algorithms, including:

* **Random Forest Classifier**
* **Gradient Boosting Classifier**

Hyperparameter tuning is performed using **GridSearchCV** with stratified cross-validation.

Model performance can be evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* ROC Curve

The final trained model is stored as:

```text
models/model.pkl
```

## Input Features

The model uses the following features:

| Feature           | Description                   |
| ----------------- | ----------------------------- |
| Gender            | Gender of the applicant       |
| Married           | Applicant's marital status    |
| Dependents        | Number of dependents          |
| Education         | Graduate / Not Graduate       |
| Self_Employed     | Employment type               |
| ApplicantIncome   | Applicant's income            |
| CoapplicantIncome | Co-applicant's income         |
| LoanAmount        | Requested loan amount         |
| Loan_Amount_Term  | Loan repayment term           |
| Credit_History    | Whether credit history exists |
| Semiurban         | Semi-urban property indicator |
| Urban             | Urban property indicator      |

Property area is one-hot encoded, with **Rural** acting as the reference category.

## Project Structure

```text
loan-prediction/
│
├── app.py
├── models/
│   └── model.pkl
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd loan-prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

A basic `requirements.txt` can contain:

```text
streamlit
pandas
numpy
scikit-learn
```

Make sure the Scikit-learn version is compatible with the version used to train and serialize the model.

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Streamlit will provide a local URL that can be opened in your browser.

## Prediction

The application collects applicant information and converts the inputs into the same feature structure used during model training.

The trained model generates the probability of loan approval using:

```python
model.predict_proba(input_data)
```

The application then compares the approval probability against the selected classification threshold to determine whether the loan is likely to be approved.

## Example

An applicant can provide information such as:

```text
Gender: Male
Marital Status: Married
Dependents: 1
Education: Graduate
Employment: Employed
Applicant Income: 8000
Co-Applicant Income: 3000
Loan Amount: 200
Loan Term: 360
Credit History: Exists
Property Area: Urban
```

The application returns the predicted **loan approval probability** and the corresponding classification.

## Tech Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Pickle**

## Disclaimer

This project is intended for **educational and demonstration purposes**.

The prediction should not be used as the sole basis for real-world lending or credit decisions. Production lending systems require additional validation, fairness testing, regulatory compliance, explainability, security controls, and appropriate human oversight.

