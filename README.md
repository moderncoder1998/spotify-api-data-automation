# 🎵 Spotify Artist Data Automation using Python

## 📌 Project Overview

This project demonstrates an end-to-end **Data Automation QA Framework** using the **Spotify Web API**.

It authenticates with Spotify, retrieves artist information, cleans the data, validates data quality, and generates reports.

---

## 🚀 Features

* Spotify OAuth Authentication
* Fetch artist data using Spotify Search API
* Convert JSON response into a Pandas DataFrame
* Data Cleaning

  * Extract followers count
  * Convert genres list into comma-separated text
* Data Validation

  * Row Count Validation
  * Required Columns Validation
  * Null Value Validation
  * Duplicate Validation
  * Popularity Range Validation
  * Followers Count Validation
  * Artist Name Validation
* Logging
* Execution Summary Report
* Validation Report
* Export cleaned data to CSV

---

## 🛠️ Technologies Used

* Python
* Pandas
* Requests
* Logging
* Dotenv
* Spotify Web API
* Git & GitHub

---

## 📂 Project Structure

```text
spotify_data_automation/
│
├── main.py
├── spotify_auth.py
├── spotify_api.py
├── data_cleaner.py
├── validations.py
├── logger.py
├── .env
├── .gitignore
├── output/
│   ├── artists.csv
│   ├── execution_summary.csv
│   └── validation_report.csv
└── README.md
```

---

## 📊 Validations Performed

| Test Case | Description                   |
| --------- | ----------------------------- |
| TC_001    | Validate Row Count            |
| TC_002    | Validate Required Columns     |
| TC_003    | Validate Null Values          |
| TC_004    | Validate Duplicate Artist IDs |
| TC_005    | Validate Popularity Range     |
| TC_006    | Validate Followers Count      |
| TC_007    | Validate Artist Name          |

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/<your-username>/spotify-api-data-automation.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
```

Run the project:

```bash
python main.py "A.R. Rahman"
```

---

## 📄 Output

The project generates:

* Cleaned artist data (CSV)
* Execution Summary
* Validation Report
* Execution Log

---

## 🎯 Learning Objectives

This project demonstrates practical skills in:

* API Testing
* Data Validation
* Data Cleaning
* Python Automation
* Pandas
* Logging
* Git & GitHub
* Building a reusable Data Automation QA Framework

---

## 👨‍💻 Author

**Vel**

Data Automation QA Engineer | Python | Pandas | API Testing | SQL
