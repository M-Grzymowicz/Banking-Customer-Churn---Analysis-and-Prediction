# Banking Customer Churn: Analysis and Prediction
Project: Detection of churners among bank customers

### Project Overview
Objective: The goal of the project is to detect customer churn based on different features, e.g., account balance, tenure, estimated salary  etc.

Context: Based on the research data-set, which is given on [Kaggle: Banking Customer Churn Prediction Dataset ](https://www.https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset), I developped a classification model to identify customers which are at risk of leaving the bank. As the finansial data of  bank customers are sensitive, the dataset is not a real world data. It describes hypothetical bank. 

Significance: This kind of prediction models can be very helpful to any financial institutions to keep their clients. As studies referenced by Harward Business Review wskazuja:   *“Acquiring a new customer can cost 5 to 25 times more than retaining an existing one.”* 


Goal: prediction of customer churn

## Author

[Marcin Grzymowicz](https://github.com/M-Grzymowicz)

## Jupyter Notebooks

This project consists of different Jupyter Notebooks that serve different purposes:

1. **banking_eda.ipynb**: 
This notebook focuses on explorative analysis of the dataset, showing statistics, distrihbution of certain features and their correlation to output behaviour (retain /churn). Apart of this analysis the final outcome of the notebook is data cleaning function which will be used in the banking_modeling.ipynb notebook.


3. **banking_modelig.ipynb**: 
This notebook focuses on all possible models, e.g., KNN, logistic regression, random forest, which are applyed to the results of the EDA in previous notebooks. We could derive and optimal model, which is stored in rf_after_grid_search.pkl. 



## Installation and Setup using conda and environment.yml

To set up the project locally, follow these steps:

1. Clone the repository:
```
git clone git@github.com:M-Grzymowicz/Banking_Customer_Churn-Analysis_and_Prediction .git
```
2. Navigate to the project directory:
```
cd your-repository
```
3. Install the required environment (you will obtain a new environment called: dpp-2501)

conda env create --file environment.yml

4. Activate your environment (dpp-2501):
```
conda activate dpp-2501

or use Visual Code and activate this enviroment

```
5. Download the modified dataset and place it in the project directory. The original dataset can be acquired from the link [Kaggle: Banking Customer Churn Prediction Dataset  ](https://www.https://www.kaggle.com/datasets/saurabhbadole/bank-customer-churn-prediction-dataset) and save it to the directory: data/raw

**Note:** If any of the above files are missing, the corresponding functionality may not work as expected.

