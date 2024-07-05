# Sentiment Analysis on Movie Reviews

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Web Application](#web-application)
  - [Installation](#installation)
  - [Usage](#usage)
- [Acknowledgments](#acknowledgments)

## Introduction

With the advent of social media, movie reviews have become a popular means of expressing opinions about films. This project aims to develop a natural language processing (NLP) system that can analyze movie reviews and determine the overall sentiment towards a movie (positive or negative).

## Project Structure

    ├── templates

        ├── index.html

    ├── app.py

    ├── analyze.py

    ├── model.py

    ├── preprocess.py

    ├── NLP_Model_Development.ipynb

    ├── requirements.txt

    ├── README.md

## Data Collection

The movie reviews data were collected from the research paper:

Maas, A. L., Daly, R. E., Pham, P. T., Huang, D., Ng, A. Y., & Potts, C. (2011). Learning word vectors for sentiment analysis. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics (pp. 142-150). Association for Computational Linguistics. https://www.cs.cornell.edu/people/pabo/movie-review-data/

## Data Preprocessing 

The following preprocessing steps were applied to the dataset:
- Cleaning: Removed HTML tags and special characters.
- Tokenization: Split text into words.
- Stop Words Removal: Eliminated common words that do not contribute to sentiment.
- Lemmatization: Reduced words to their base form.
- Encoding: Converted text to numerical format using TF-IDF.

## Model Training and Evaluation

Four models were trained and evaluated:
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- Long Short-Term Memory (LSTM)

Models were evaluated using accuracy, ROC-AUC, and classification reports, shown in NLP_Model_Development.ipynb file. LSTM performed the best after optimization. Therefore, web application was build using trained LSTM model. 

## Web Application

A web application was developed using Flask to allow users to input a movie review and get a sentiment analysis result (positive or negative).

### Installation

To run this project locally, follow these steps:

1. **Clone the repository**

``` bash
git clone https://github.com/Achshah-RM/-Sentiment-Analysis-on-Movie-Reviews.git
cd Sentiment-Analysis-on-Movie-Reviews
```

2. **Create and activate a virtual environment**

``` bash
conda create --name nlp_project python=3.11
conda activate nlp_project
```

3. **Install the required packages**

``` bash
pip install -r requirements.txt
```

4. **Run the Flask app**

``` bash
python app.py
```

### Usage

1. Open your browser and navigate to http://127.0.0.1:5000.
2. Enter a movie review in the text box and click the "Analyze" button.
3. The app will display the sentiment of the review (positive or negative).

## Acknowledgments

The Sentiment Analysis on Movie Reviews project was developed as a learning exercise in natural language processing and machine learning. It serves as a starting point for building more complex sentiment analysis systems.

Enjoy using the Sentiment Analysis application!
