# breast_cancer_diagnosis


---

## 🛠️ Technologies & Libraries

- Python 3.10.13
- Pandas, NumPy
- Scikit-learn
- Seaborn, Matplotlib
- Jupyter Notebooks

---

## 🔍 Key Steps

### 1. Load Data Set
- Read CSV and validate feature structure
- Strip unnecessary or unnamed columns

### 2. Data Preprocessing
- Encode target label (`M` = 1, `B` = 0)
- Remove irrelevant features (e.g., `id`)
- Scale features for SVM/LogReg

### 3. Exploratory Data Analysis (EDA)
- Class distribution
- Correlation matrix
- Boxplots and pairplots of key features

### 4. Model Building
- Logistic Regression (baseline)
- Random Forest
- Model evaluation using accuracy, recall, F1-score

### 5. Model Tuning
- `GridSearchCV` used for hyperparameter tuning
- Best models compared visually (bar charts, ROC)

### 6. Model Evaluation
- Final selection based on **F1-score (malignant)**

---

### 7. Model Selection

| Model                   | F1-Score (Malignant) |
|------------------------|----------------------|
| Logistic Regression     | 0.951                |
| Random Forest (Tuned)   | 0.937                |

> 📌 The model with the highest recall and F1 for malignant classification is preferred.

---

## 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/jsavla16yourusername/breast_cancer_diagnosis.git
cd breast_cancer_diagnosis

# Set up virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
