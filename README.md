# TDS - Data Analysis Engine

A FastAPI-based data analysis engine that uses Google Gemini AI to automatically analyze datasets and answer questions through natural language processing.

## 🚀 Features
- Automatically processes multiple data formats (CSV, JSON, PDF, images, URLs)
- Uses Google Gemini AI for intelligent data analysis
- Supports multi-step analysis workflows
- REST API with HTML frontend
- Automatic dependency management
- Railway deployment ready

---

## 🔑 Getting Credentials

### Google API Key
Get your Gemini API key here: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

---

## 🛠️ Local Development

### Prerequisites
- **Python 3.8+** installed
- **pip** installed

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd TDS
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Copy `.env.example` to `.env` and add your API keys:
```bash
cp .env.example .env
```

Edit `.env` file:
```
GOOGLE_API_KEY=your_primary_api_key_here
GOOGLE_API_KEY2=your_secondary_api_key_here
GOOGLE_API_KEY3=your_tertiary_api_key_here
```

### 4. Run the Application
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Access the application at: `http://localhost:8000`

---

## 🚂 Railway Deployment

This project is configured for Railway deployment with the following files:
- `Procfile` - Defines the web process
- `railway.toml` - Railway configuration
- `requirements.txt` - Python dependencies

### Deploy to Railway:

1. **Push to GitHub** (see steps below)
2. **Connect to Railway:**
   - Visit [railway.app](https://railway.app)
   - Connect your GitHub account
   - Select your repository
   - Click "Deploy"

3. **Set Environment Variables:**
   - Go to your Railway project dashboard
   - Click on "Variables" tab
   - Add your Google API keys:
     - `GOOGLE_API_KEY`
     - `GOOGLE_API_KEY2` 
     - `GOOGLE_API_KEY3`

4. **Deploy:**
   - Railway will automatically deploy your application
   - You'll get a public URL like `https://your-app.railway.app`

---

## 🌐 Using the Frontend

A simple HTML frontend is provided for uploading multiple files and viewing API responses.

### How to use:
1. Open your deployed URL in a browser
2. Click "Choose Files" and select your data files
3. Click "Submit" to upload and analyze
4. View the AI-generated analysis results

### API Endpoint
Direct API access: `POST /api`

---

## 📁 Project Structure

```
├── main.py              # FastAPI application
├── task_engine.py       # Python code execution engine
├── gemini.py           # Google Gemini AI integration
├── api_key_rotator.py  # API key rotation system
├── frontend.html       # Web interface
├── requirements.txt    # Python dependencies
├── Procfile           # Railway process definition
├── railway.toml       # Railway configuration
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── sample_questions/  # Example datasets and questions
```

---

## 🔧 Configuration

### API Key Rotation
The system supports multiple Google API keys for rate limiting. Add your keys to the environment variables or modify `api_key_rotator.py`.

### File Upload Directory
- **Local Development:** `uploads/` directory
- **Railway Deployment:** Uses Railway's temporary storage

---

## 🐛 Troubleshooting

### Common Issues:
1. **API Rate Limits:** Add multiple Google API keys
2. **Memory Issues:** Railway has memory limits for free tier
3. **File Upload Size:** Adjust limits in `main.py` if needed

### Logs:
- Check Railway logs in the dashboard
- Local logs are stored in `uploads/<request-id>/app.log`

---

## 📝 License

See `LICENSE` file for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## Video Tutorials
- [Installation Guide](https://www.youtube.com/watch?v=2k1LpRcY85w)
- [Deployment Tutorial](https://www.youtube.com/watch?v=-4QLncypQZ8)
