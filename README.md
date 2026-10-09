# 🛒 BigMart-sales-prediction
### Machine Learning-Based Sales Prediction Using KNN Regression and Flask

## 📌 Project Overview

The **BigMart Sales Prediction System** is a Machine Learning web application designed to predict outlet sales based on product characteristics and store-related information.

The application uses a trained **K-Nearest Neighbors (KNN) Regression** model to generate sales predictions. It provides a user-friendly web interface built with HTML, CSS, JavaScript, and Flask, allowing users to enter product and outlet details and view the estimated sales.

## 🎯 Problem Statement

Retail businesses need to understand how product attributes and outlet characteristics influence sales. Estimating sales can help retailers make informed decisions about inventory planning, product availability, and store operations.

This project demonstrates how Machine Learning can be used to estimate outlet sales from relevant product and outlet information.

## 🎯 Objectives

* Develop a Machine Learning model for sales prediction.
* Apply KNN Regression to estimate outlet sales.
* Build an interactive web application using Flask.
* Accept product and outlet details through a web form.
* Display predicted sales through a professional user interface.
* Integrate a saved model and data scaler into the prediction workflow.

## ✨ Features

* 📊 **Sales Prediction:** Estimate outlet sales using a trained KNN regression model.
* 🛍️ **Product Information:** Enter weight, fat content, visibility, MRP, and item type.
* 🏪 **Outlet Information:** Select outlet identifier, size, location, type, and establishment year.
* 🎨 **Professional Interface:** Modern layout with styled form fields, icons, and responsive design.
* ⚙️ **Flask Integration:** Connect the frontend to the Machine Learning model.
* 🔢 **Data Preprocessing:** Prepare input features and apply the saved scaler before prediction.
* 📈 **Prediction Results:** Display the estimated sales value on the webpage.

## 🧠 Machine Learning Algorithm

**K-Nearest Neighbors (KNN) Regression**

KNN Regression estimates a numerical target by examining nearby examples in the training dataset and combining their target values.

In this project, KNN Regression is used to estimate outlet sales based on the selected product and outlet characteristics.

A saved `MinMaxScaler` is also used to scale the input features before they are passed to the model.

## 📥 Input Features

The application accepts the following inputs:

| Feature                   | Description                          |
| ------------------------- | ------------------------------------ |
| Item Weight               | Weight of the product                |
| Item Fat Content          | Fat-content category of the item     |
| Item Visibility           | Visibility of the item in the outlet |
| Item MRP                  | Maximum retail price                 |
| Item Type                 | Category of the product              |
| Outlet Identifier         | Unique identifier of the outlet      |
| Outlet Size               | Size category of the outlet          |
| Outlet Location Type      | Outlet location tier                 |
| Outlet Type               | Type of retail outlet                |
| Outlet Establishment Year | Year the outlet was established      |

**Output:** Predicted outlet sales value.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn, KNN Regression
* **Backend Framework:** Flask
* **Data Processing:** Pandas, NumPy
* **Frontend:** HTML5, CSS3, JavaScript
* **Model Storage:** Pickle
* **Development Environment:** VS Code / Jupyter Notebook

## 🏗️ Project Architecture

```text
User
  |
  v
Web Interface (HTML + CSS + JavaScript)
  |
  v
Flask Application (app.py)
  |
  v
Input Collection and Preprocessing
  |
  v
Saved MinMaxScaler
  |
  v
Trained KNN Regression Model
  |
  v
Predicted Outlet Sales
  |
  v
Prediction Result on Webpage
```

## 📂 Project Structure

```text
bigmart-sales-prediction/
│
├── app.py
├── KNN Regression.ipynb
├── KNN_reg_outlet_sales.csv
├── bigmart_knn_model.pkl
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

### File Description

* `app.py` — Flask application and prediction logic.
* `bigmart_knn_model.pkl` — Saved KNN regression model and scaler.
* `requirements.txt` — Python dependencies.
* `README.md` — Project documentation.
* `templates/index.html` — Webpage structure and prediction form.
* `static/style.css` — Styling and responsive layout.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/bigmart-sales-prediction.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Navigate to the Project Directory

```bash
cd bigmart-sales-prediction
```

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Enter the required product and outlet information, then click **Predict Outlet Sales** to view the estimated result.

## 📦 Requirements

Your `requirements.txt` should include the libraries used by the application:

```text
Flask
pandas
numpy
scikit-learn
```

For reproducible results, use package versions compatible with the environment in which the model was trained and saved.

## 📊 Applications

* Retail sales estimation
* Outlet performance analysis
* Product sales planning
* Inventory management support
* Educational demonstrations of Machine Learning and web development

## 🔮 Future Enhancements

* Interactive sales analytics and charts
* Prediction history and CSV export
* Comparison of multiple regression algorithms
* Model performance metrics and evaluation
* Improved input validation and error handling
* Deployment to a cloud hosting platform
* Additional sales insights and recommendations

## 🎓 Learning Outcomes

Through this project, I explored:

* Applying Machine Learning to a regression problem.
* Integrating a trained model with a Flask application.
* Preprocessing input data for prediction.
* Using HTML, CSS, and JavaScript to build a web interface.
* Connecting frontend forms to backend prediction logic.
* Organizing and documenting a Python project for GitHub.

