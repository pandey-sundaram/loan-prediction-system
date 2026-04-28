# 🏦 Loan Default Prediction System

## 📌 Full Project Explanation
Welcome to the **Loan Default Prediction System**! This is an end-to-end Machine Learning project designed to solve a real-world financial problem: predicting whether a loan applicant is likely to pay back their loan or default (fail to pay). 

When banks or financial institutions lend money, they take on risk. To minimize this risk, this system evaluates an applicant's financial background and uses Artificial Intelligence to make an instant, data-driven recommendation. 

**How it works:**
1. **The Brain (Machine Learning):** I trained a **Random Forest Classifier** using a historical dataset of 20,000 loan records. The model learned the patterns of people who successfully paid back their loans versus those who defaulted.
2. **The Interface (Web App):** I built an interactive web application using **Streamlit**. Instead of looking at raw code, users can simply type in an applicant's details (like income and credit score) into a clean, easy-to-use website.
3. **The Result:** The moment the user clicks "Predict", the web app sends the data to the trained AI model, which instantly returns a risk assessment: either a green **Approved** (Low Risk) or a red **High Risk** warning.

---

## 🚀 Features
* **Predictive AI:** Uses a highly accurate Random Forest algorithm to evaluate financial risk.
* **Streamlined Inputs:** Focuses on the 5 most critical financial indicators to save the user time:
  * Annual Income
  * Loan Amount
  * Interest Rate
  * Credit Score
  * Debt-to-Income Ratio
* **Interactive UI:** A beautifully simple, modern web interface.
* **Instant Results:** Real-time predictions displayed clearly on the screen.

---

## 🛠️ Technology Stack
* **Python:** The core programming language.
* **Pandas:** Used for data cleaning, manipulation, and analysis.
* **Scikit-Learn:** The machine learning library used to train and test the Random Forest model.
* **Joblib:** Used to save the trained model into a `.pkl` file so it can be reused without retraining.
* **Streamlit:** The framework used to turn the Python script into a fully functioning web application.

---

## 📁 Project Structure
* `app.py`: The main Python script that runs the Streamlit web application.
* `web_model.pkl`: The saved Machine Learning model that acts as the "brain" of the app.
* `requirements.txt`: A list of the required Python libraries needed to run the project.
* `README.md`: This document, explaining the project.

---

## 💻 How to Run This Project Locally

If you want to run this application on your own computer, follow these simple steps:

**1. Clone the repository**
Download or clone this project to your local machine.

**2. Open your Terminal or Command Prompt**
Navigate to the folder where you saved this project.

**3. Install the required dependencies**
Run the following command to install the necessary tools:
```bash
pip install -r requirements.txt

4. Run the application
Start the Streamlit server by typing:

Bash
streamlit run app.py
5. View the App
A new tab will automatically open in your default web browser displaying the application!