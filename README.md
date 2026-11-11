# Machine Learning Midterm Project

This project compares classification and clustering methods using two datasets from scikit-learn: Breast Cancer Wisconsin and Wine Classification.

## Datasets
- Breast Cancer: 569 samples, 30 features, 2 classes.
- Wine: 178 samples, 13 features, 3 classes.

## Methods
I used Decision Tree, K-Nearest Neighbors (KNN), and Gaussian Naive Bayes for classification. I also used K-Means for clustering.

I compared scaled and unscaled data with three random seeds (42, 52, 62). I kept 20% of each dataset for final testing and used the remaining data for training and validation.

In total, I completed 132 classification fits and 12 K-Means fits (144 model fits).

## Results
The best classification model for both datasets was scaled KNN.

- Breast Cancer: KNN with 7 neighbors, test accuracy 97.37%.
- Wine: KNN with 11 neighbors, test accuracy 100%.

Scaling also improved the K-Means ARI scores for both datasets.

## How to Run
1. Install Python and the packages in `requirements.txt`.
2. Open `breast_cancer.ipynb` and `wine.ipynb` in Jupyter Notebook or VS Code.
3. Run the cells from top to bottom.
4. The notebooks generate results and figures. Run `combine_results.py` to combine the CSV files.

## Project Files
- `breast_cancer.ipynb` — Breast Cancer experiments.
- `wine.ipynb` — Wine experiments.
- `report.docx` — Project report.
- `figures/` — Saved graphs.
- `*.csv` — Experiment results.
- `requirements.txt` — Required Python packages.
- `AI_DISCLOSURE.md` — AI assistance disclosure.

## Links

GitHub: https://github.com/neva4434/ML_Midterm_Project

Presentation Video: https://youtu.be/Xi4llmR6L9s