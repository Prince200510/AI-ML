# AI Ml from Beginner to Advanced
This repository is a comprehensive guide to Artificial Intelligence (AI) and Machine Learning (ML), covering concepts from basic to advanced levels.  
# 🏡 House Price Prediction - Linear Regression

This repo contains my **House Price Prediction Model** using **Linear Regression** as part of my **ML Learning Journey**.  
I have built and improved the model through multiple iterations to enhance accuracy.

---

## 🎯 About the Models
1. **Part 1 - Accuracy 55.68%**  
   - Basic feature engineering with minimal improvements.
   - Simple encoding and no scaling.
   
2. **Part 2 - Accuracy 64.37%**  
   - Improved accuracy using feature scaling and outlier removal.
   - Better preprocessing for higher R² score.
     
2. **Part 3 - Accuracy 76.00%**
   - Feature Engineering Enhanced:
    - Added advanced features like:
        - `area_per_room`, `bathroom_ratio`, `total_amenities`
        - Polynomial and log-transformed features (`area_squared`, `log_area`)
    - Included interaction terms for capturing non-linear relationships.
- Outlier Treatment:
    - Used IQR-based outlier removal for better data consistency.
- Model Optimization:
    - Tuned model hyperparameters using grid search and cross-validation.
- Validation Techniques:
    - Applied cross-validation to ensure generalization.

---

## ⚡️ Run the Models
```bash
# Clone the repo
git clone https://github.com//Prince200510/AI-ML.git
cd regression/linearregression

