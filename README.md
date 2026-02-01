# Capstone
---

## Introduction

At the end of the 12 weeks of Digital Futures academy, Data Engineering course, I completed my Capstone project. The Capstone project is an Extract Transform Load (ETL) pipeline written in Python that takes a set of tables from the input file through the pipeline and displays the data in a Streamlit local website application. The data was originally sourced from Kaggle, it was synthetic data designed to mimic a gym company's data and consisted of tables of users, gyms, checkin & checkout data and subscription plans. I did adapt/modify it slightly before using it to allow me to demonstrate more of the skills and knowledge I gained form the course. The project was done in a week and included dataset choice, planning, writing code for the ETL pipeline and tests, reflection and a 10 minute presentation showing off my project to the rest of the cohort. To start us off on the project we were given a file structure and some starting files such as the requirements.txt and the pyproject.toml. The file structure and starting files were originally from the etl pipeline that was used as an example to teach us.

Reflction and planning documents can be found in the "docs" folder.

## Dataset

(https://www.kaggle.com/datasets/mexwell/gym-check-ins-and-user-metadata)

I chose my dataset because my main hobby is going to the gym, this data set met the requirements and involved multiple tables with foreign keys allowing me to join them for greater insights. With it being synthetic data it did require some adjustment such as regenerating names as there were many repeats and uncleaning it.

---
---

(the following is inputted and used in the terminal)

## Setup

1. Create a python virtual environment

    - Windowns: python -m venv .venv

    - Mac: python3 -m venv .venv

2. Activate the virtual environment

    - Windowns: source .venv/Scripts/activate

    - Mac: source .venv/bin/activate

3. Install packages

    - Both: pip install -r requirements.txt

    - pip install -e .

## Project running

1. Run the ETL pipeline

    - run_etl

2. Run the tests

    - run_tests all

3. Run the Streamlit app. The app uses the output files from the pipeline so to run the app the data/output folders must be populated, if they are not run the pipeline using "run_etl".

    - cd src

    - cd streamlit

    - streamlit run app.py

    - To leave the streamlit app close the tab and press ctrl + C in the terminal.

