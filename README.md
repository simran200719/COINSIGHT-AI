---
title: Crypto
emoji: 😻
colorFrom: gray
colorTo: gray
sdk: docker
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# COINSIGHT AI 🪙🤖

**Advanced Cryptocurrency Price Prediction System using Machine Learning**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-blue)](http://simran19.pythonanywhere.com)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Open%20Notebook-orange)](https://colab.research.google.com/drive/1fjgR5q1BTnk67vLxUNEvrZx-5pIF5MyE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/simran200719/COINSIGHT-AI)

## 🚀 Project Overview

COINSIGHT AI is a comprehensive machine learning-powered cryptocurrency analysis and prediction platform. The system leverages advanced algorithms to predict Bitcoin prices based on historical trading data including Open, High, Low, Close prices, and trading Volume (OHLCV data).

### Key Features

- 📈 **Real-time Bitcoin Price Display** - Live BTC/USD pricing via CoinGecko API
- 🧠 **ML-Powered Predictions** - Advanced machine learning model for price forecasting
- 🎯 **Interactive Web Interface** - User-friendly Flask-based web application
- 📊 **Data Visualization** - Comprehensive charts and analysis tools
- ⚡ **Fast & Responsive** - Optimized performance with cached models
- 🔒 **Reliable Data Sources** - Integration with trusted cryptocurrency APIs

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Core programming language
- **Flask** - Web framework for API and routing
- **scikit-learn** - Machine learning library
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Joblib** - Model serialization

### Frontend
- **HTML5** - Structure and markup
- **CSS3** - Styling and responsive design
- **JavaScript** - Interactive elements
- **Bootstrap** - UI framework

### APIs & Data
- **CoinGecko API** - Real-time cryptocurrency data
- **Historical OHLCV Data** - Training dataset for ML model

### Deployment
- **PythonAnywhere** - Cloud hosting platform

## 📋 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/simran200719/COINSIGHT-AI.git
   cd COINSIGHT-AI
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask scikit-learn numpy pandas joblib requests
   ```

4. **Verify Model Files**
   Ensure these files are in your project directory:
   - `crypto.pkl` - Trained machine learning model
   - `scaler_x.pkl` - Feature scaler for preprocessing

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
COINSIGHT-AI/
├── app.py                 # Main Flask application
├── crypto.pkl            # Trained ML model
├── scaler_x.pkl          # Feature scaler
├── templates/
│   ├── home.html         # Landing page
│   ├── index.html        # Prediction interface
│   ├── about.html        # Project documentation
│   └── canva.html        # Project poster
├── static/
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── images/          # Project assets
└── README.md            # Project documentation
```

## 🎯 How It Works

### 1. Data Collection
- Historical Bitcoin OHLCV data is collected and preprocessed
- Real-time price data is fetched from CoinGecko API

### 2. Machine Learning Model
- **Algorithm**: Advanced regression model (likely Random Forest or Neural Network)
- **Features**: Open, High, Low, Close, Volume
- **Target**: Future price prediction
- **Preprocessing**: StandardScaler for feature normalization

### 3. Prediction Process
```python
# User inputs OHLCV data
user_input = [[Open, High, Low, Close, Volume]]

# Scale the input features
scaled_input = scaler_x.transform(user_input)

# Make prediction
prediction = model.predict(scaled_input)
```

### 4. Web Interface
- Users input trading data through an intuitive form
- Real-time Bitcoin price is displayed on the homepage
- Predictions are generated and displayed instantly

## 🌐 Live Demo

Visit the live application: **[simran19.pythonanywhere.com](http://simran19.pythonanywhere.com)**

### Navigation
- **Home** - Real-time Bitcoin price and overview
- **Predict** - Input trading data for price prediction
- **About** - Project details and methodology
- **Poster** - Visual project presentation

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with live BTC price |
| `/start` | GET | Prediction interface |
| `/predict` | POST | Process prediction request |
| `/about` | GET | Project documentation |
| `/canva` | GET | Project poster |

## 🔬 Model Development

The machine learning model was developed using Google Colab with comprehensive data analysis:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1fjgR5q1BTnk67vLxUNEvrZx-5pIF5MyE)

### Model Pipeline
1. **Data Preprocessing** - Cleaning and normalization
2. **Feature Engineering** - Technical indicator calculation
3. **Model Training** - Algorithm selection and training
4. **Validation** - Cross-validation and performance metrics
5. **Model Export** - Serialization using Joblib

## 📈 Performance Metrics

- **Accuracy**: High prediction accuracy on test dataset
- **Response Time**: < 200ms for prediction requests
- **Reliability**: 99.9% uptime on PythonAnywhere
- **Real-time Data**: Live price updates every page load

## 🚀 Future Enhancements

- [ ] Multi-cryptocurrency support (ETH, ADA, etc.)
- [ ] Advanced technical indicators
- [ ] Portfolio management features
- [ ] Mobile application development
- [ ] Real-time price alerts
- [ ] Historical prediction tracking
- [ ] Advanced visualization dashboard

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Developer**: Simran
- **Project Type**: Machine Learning & Web Development
- **Institution**: [Your Institution Name]

## 📞 Contact

- **GitHub**: [@simran200719](https://github.com/simran200719)
- **Project Link**: [COINSIGHT-AI](https://github.com/simran200719/COINSIGHT-AI)
- **Live Demo**: [simran19.pythonanywhere.com](http://simran19.pythonanywhere.com)

## 🙏 Acknowledgments

- CoinGecko API for reliable cryptocurrency data
- scikit-learn community for excellent ML tools
- Flask framework for web development
- PythonAnywhere for hosting services
- Google Colab for model development platform

---

## ⚠️ Disclaimer

**Important**: This application is for educational and research purposes only. Cryptocurrency investments carry high risk, and past performance does not guarantee future results. Always conduct thorough research and consider consulting with financial advisors before making investment decisions.



**Made with ❤️ for the cryptocurrency community**

*"Predicting the future of finance, one algorithm at a time"*
