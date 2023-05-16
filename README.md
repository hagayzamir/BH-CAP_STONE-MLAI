
# BH-CAP_STONE-MLAI
This project contains the Capstone project files.

# Disclaimer: Content Warning

#### This capstone project involves the analysis of social media content, including tweets that may contain hate speech and offensive language. The objective of this project is to explore methods for identifying and understanding such harmful content, and not to promote or endorse it in any way.

#### The content you will encounter in this project may contain explicit language, discriminatory remarks, or offensive terminologies. This includes but is not limited to slurs related to race, ethnicity, religion, gender, sexuality, or other protected characteristics. I strongly condemn such behavior, but include these data in my project for the purpose of creating models that can help detect and mitigate the spread of hate speech and offensive language online.

#### Please be advised that this project may not be suitable for all audiences due to the sensitive nature of the content. Viewer discretion is strongly advised.

#### The goal of my work is to combat hate speech and offensive language, and to contribute to making online spaces more respectful and inclusive. I appreciate your understanding and support in this endeavor.

# Overview
Automatic detection of hate speech on social media platforms presents a significant challenge, particularly when it comes to distinguishing hate speech from other instances of offensive language. Traditional lexical detection methods often struggle to make this distinction, labeling any messages containing specific terms as hate speech. This lack of precision has been a limiting factor in previous studies using supervised learning models.

# summary of findings
The results illustrates the performance of various machine learning models (Logistic Regression, Decision Tree, Random Forest, SVC, K Neighbors, and XGBoost), each paired with different vectorizers (Count, Tfidf, Hashing, and Binary). The performance metrics evaluated are 'best_score' (displayed as a percentage) and 'fit_time' (expressed in minutes).

The 'best_score' reflects the model's accuracy in predicting the correct outcome, with higher percentages indicating superior accuracy. The 'fit_time', on the other hand, reveals the time taken by the model to train, with lower values indicating faster training times.

For instance, the SVC Tfidf Vectorizer displays the highest 'best_score' at 90.64%, but it also exhibits a substantial training time, with a 'fit_time' of approximately 126.92 minutes. Although it delivers the highest accuracy, its lengthy training time might not make it the best fit for real-time computing environments.

On the other hand, the Decision Tree Hashing Vectorizer, despite having a slightly lower 'best_score' of 89.08%, offers the shortest 'fit_time' of approximately 1.53 minutes. This balance of respectable accuracy and impressive training speed might make it a more suitable choice for applications where swift computations are required.

Two baseline models, Naive Bayes and Logistic Regression, have 'best_score' of 86.91% and 89.75% with 'fit_time' of approximately 0.0024 and 0.0127 minutes respectively. These models offer reasonable accuracy with extremely fast training times, which could be beneficial in certain applications.

In summary, the choice of the optimal model will depend on the specific trade-off between predictive accuracy and computational efficiency required for the task at hand. If maximum accuracy is the prime objective, then the SVC Tfidf Vectorizer could be the best option. However, if fast computation is the priority, then models such as the Decision Tree Hashing Vectorizer or the baseline models could be more appropriate.

## Reccomendations
tbd

## Directory Structure

- code
    - Exploratory_Data_Analysis.ipynb
    - Basic_Model_Exploration.ipynb
    - Advance_Model_Exploration.ipynb
- data
    - original_raw_data.csv
    - processed_tweet.csv
- docs
    - CRISP-DM.txt
    - OriginalPaper.pdf
- images
- plots
- README.md

## Links
There are few files in this project. Each file has a seperate purpose. 

Exploratory Data Analysis [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Exploratory%20Data%20Analysis.ipynb)

Basic Model Exploration [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Basic%20Model%20Exploration.ipynb)

Advance_Model_Exploration [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Advance%20Model%20Exploration.ipynb)
