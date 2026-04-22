# 🎓 Student Performance Predictor

A Machine Learning web app that predicts student marks based on study habits and past performance.

## 🔗 Live Demo
> Run locally using steps below

## 📊 Features
- Predicts final marks using ML model
- Interactive sliders for input
- Pass/Fail prediction with confidence score
- Built with Python + Streamlit + Scikit-learn

## 🛠️ Tech Stack
| Tool | Usage |
|------|-------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | ML model (Random Forest) |
| Streamlit | Web app UI |
| Matplotlib/Seaborn | Data visualization |

## 🚀 How to Run Locally

```bash
# 1. Clone karo
git clone https://github.com/Vinayakco/student-performance-analysis.git
cd student-performance-analysis

# 2. Install karo
pip install -r requirements.txt

# 3. Run karo
streamlit run app.py
```

## 📁 Project Structure
```
├── data/
│   └── student-mat.csv      # Dataset
├── notebook/
│   └── analysis.ipynb       # EDA & Model training
├── model/
│   └── model.pkl            # Saved ML model
├── app.py                   # Streamlit web app
├── requirements.txt         # Dependencies
└── README.md                # You are here!
```

## 📈 Model Performance
- Algorithm: Random Forest Classifier
- Accuracy: ~85%
- Features used: Study hours, Attendance, Previous scores, Past failures

## 👨‍💻 Author
**Vinayak Chouhan**
- LinkedIn: [linkedin.com/in/vinayak-chouhan-06a1ba292](https://linkedin.com/in/vinayak-chouhan-06a1ba292)
- GitHub: [github.com/Vinayakco](https://github.com/Vinayakco)
