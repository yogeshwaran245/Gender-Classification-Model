# Gender Classification Using Face Measurements

This project is a gender classification model built using Logistic Regression, with a front-end developed using Flask, HTML, and CSS. The model predicts gender based on various facial measurements provided by the user.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to classify gender based on facial features such as hair length, forehead dimensions, nose dimensions, and the distance between the nose and lips. The project leverages a Logistic Regression model, which has been trained on a dataset of facial measurements.

## Features

- **Logistic Regression Model:** Predicts gender based on input facial measurements.
- **Web Interface:** User-friendly web interface built with Flask, HTML, and CSS.
- **Input Validation:** Ensures that user inputs are in the expected format before making predictions.

## Project Structure

Here's the project structure section formatted properly for GitHub:

markdown
Copy code
## Project Structure

├── dataset.csv # Dataset used for training the model <br>
├── gender_classification.ipynb # Jupyter Notebook with the model training code <br>
├── app.py # Flask application code <br>
├── templates/ <br>
│ ├── index.html # Main page for user inputs <br>
│ └── predict.html # Result page displaying the prediction <br>
├── static/ <br>
│ └── index.css # CSS styling for the web interface <br>
└── README.md # Project documentation<br><br>



## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/gender-classification.git
   cd gender-classification

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   
This will ensure the necessary dependencies for your project are installed.


4. **Run the Flask application:**
   ```bash
   python app.py
   
This will start the Flask application so you can interact with your web interface.

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/home`.
This will allow you to view and interact with your Flask application in a web browser.

## Usage

- **Home Page:** Enter the required facial measurements.
- **Prediction:** The result page displays the predicted gender based on the inputs.

## Results

The Logistic Regression model achieves satisfactory performance on the given dataset, providing accurate gender classification based on the input features.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

