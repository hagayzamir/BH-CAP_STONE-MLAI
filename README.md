
# BH-CAP_STONE-MLAI
This project contains the Capstone project files.

# Disclaimer: Content Warning

#### This project involves the analysis of social media content, including tweets that may contain hate speech and offensive language. The objective of this project is to explore methods for identifying and understanding such harmful content, and not to promote or endorse it in any way.

#### The content you will encounter in this project may contain explicit language, discriminatory remarks, or offensive terminologies. This includes but is not limited to slurs related to race, ethnicity, religion, gender, sexuality, or other protected characteristics. I strongly condemn such behavior, but include these data in my project for the purpose of creating models that can help detect and mitigate the spread of hate speech and offensive language online.

#### Please be advised that this project may not be suitable for all audiences due to the sensitive nature of the content. Viewer discretion is strongly advised.

#### The goal of my work is to combat hate speech and offensive language, and to contribute to making online spaces more respectful and inclusive. I appreciate your understanding and support in this endeavor.

## Overview
Automatic detection of hate speech on social media platforms presents a significant challenge, particularly when it comes to distinguishing hate speech from other instances of offensive language. Traditional lexical detection methods often struggle to make this distinction, labeling any messages containing specific terms as hate speech. This lack of precision has been a limiting factor in previous studies using supervised learning models.

## summary of findings
The results illustrate the performance of various machine learning models (Logistic Regression, Decision Tree, Random Forest, SVC, K Neighbors, and XGBoost) paired with different vectorizers (Count, Tfidf, Hashing, and Binary). The evaluation includes two performance metrics: 'best_score' (expressed as a percentage) and 'fit_time' (measured in minutes).

The 'best_score' metric represents the accuracy of the models in predicting the correct outcome, with higher percentages indicating better accuracy. Conversely, the 'fit_time' metric indicates the training time of the models, with lower values suggesting faster training.

Among the models, the SVC Tfidf Vectorizer achieves the highest 'best_score' at 90.64%. However, it also requires a substantial training time of approximately 126.92 minutes. While it delivers the highest accuracy, its lengthy training time might limit its suitability for real-time computing environments.

On the other hand, the Decision Tree Hashing Vectorizer achieves a slightly lower 'best_score' of 89.08% but offers the shortest 'fit_time' of approximately 1.53 minutes. This model strikes a balance between respectable accuracy and impressive training speed, making it a more suitable choice for applications that require swift computations.

The baseline models, Naive Bayes and Logistic Regression, achieve 'best_score' values of 86.91% and 89.75%, respectively. These models demonstrate reasonable accuracy with extremely fast training times of approximately 0.0024 and 0.0127 minutes, respectively. Such models could be beneficial for specific applications where rapid training is crucial.

In summary, the optimal model choice depends on the trade-off between predictive accuracy and computational efficiency required for the specific task. If maximum accuracy is the primary objective, the SVC Tfidf Vectorizer may be the preferred option. However, if fast computation is a priority, models like the Decision Tree Hashing Vectorizer or the baseline models would be more appropriate.

##### Additional Results:

- The eXtreme Gradient Boosting model achieved a 'best_score' of 91.57% with a training time of 0.915651 minutes. It demonstrates high accuracy, precision, recall, and F1-score values.
- The AdaBoost model achieved a 'best_score' of 90.11% with a training time of 0.380739 minutes. It also showcases commendable accuracy, precision, recall, and F1-score values.
- The Random Forest model achieved a 'best_score' of 89.15% with a training time of 5.282936 minutes. It displays good accuracy, precision, recall, and F1-score values.

These additional results provide further insights into the performance of specific models and can be considered when making the optimal model selection.

## Reccomendations
Based on the results and findings from the performance evaluation of various machine learning models and vectorizers, there are several recommendations for future exploration:

1. Explore ensemble methods: The results indicate that ensemble methods such as eXtreme Gradient Boosting (XGBoost) and AdaBoost show promising performance with high accuracy, precision, recall, and F1-score values. Further exploration of ensemble methods could potentially enhance the predictive capabilities of models.

2. Investigate other vectorization techniques: While the Tfidf vectorizer was commonly used in the evaluation, it would be worthwhile to explore other vectorization techniques such as Word2Vec, GloVe, or Doc2Vec. These techniques may capture more nuanced semantic information and potentially improve the performance of the models.

3. Evaluate deep learning models: The evaluated models primarily belong to traditional machine learning algorithms. Exploring deep learning models, such as Convolutional Neural Networks (CNNs) or Recurrent Neural Networks (RNNs), could provide deeper insights into the data and potentially unlock higher levels of accuracy in predicting outcomes.

4. Consider fine-tuning hyperparameters: The performance of the models could potentially be further improved by fine-tuning their hyperparameters. Conducting a systematic search of hyperparameter space using techniques like grid search or random search might help identify optimal parameter combinations for each model.

5. Incorporate feature engineering: Feature engineering plays a crucial role in improving model performance. Exploring domain-specific features, creating interaction terms, or extracting more meaningful features from the data could lead to better model predictions.

6. Assess model robustness: It is important to evaluate the robustness of the models by testing them on different datasets or performing cross-validation. This will provide a better understanding of how the models generalize to unseen data and ensure their reliability in real-world scenarios.

7. Investigate interpretability: While the focus of the evaluation was on predictive accuracy and computational efficiency, exploring model interpretability techniques can enhance transparency and provide insights into the decision-making process of the models. Techniques like feature importance analysis or model-agnostic interpretability methods could be considered.

By exploring these recommendations, researchers and practitioners can advance the understanding and application of machine learning models in various domains, leading to more accurate and efficient predictions for real-world problems.

### Directory Structure

- code
    - Exploratory_Data_Analysis.ipynb
    - Basic_Model_Exploration.ipynb
    - Advance_Model_Exploration.ipynb
    - A neural network example.ipynb
    - Selected Model - AdaBoost - Testing.ipynb
    - Selected Model.ipynb
- data
    - original_raw_data.csv
    - processed_tweet.csv
- docs
    - Finsl Report.pdf - Final project report.
    - CRISP-DM.txt
    - OriginalPaper.pdf - Originala paper.
- plots - This direc tory contain all the plots from the project.
- streamlit - This directory contain a streasmlit project for testing.
- README.md - This file.

### Links
There are few files in this project. Each file has a seperate purpose. 

Exploratory Data Analysis [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Exploratory%20Data%20Analysis.ipynb)

Basic Model Exploration [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Basic%20Model%20Exploration.ipynb)

Advance Model Exploration [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Advance%20Model%20Exploration.ipynb)

A neural network example [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/A%20neural%20network%20example.ipynb)

Selected Model - AdaBoost - Testing [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Selected%20Model%20-%20AdaBoost%20-%20Testing.ipynb)

Selected Model.ipynb [here](https://github.com/hagayzamir/BH-CAP_STONE-MLAI/blob/main/code/Selected%20Model.ipynb)
