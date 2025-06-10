# 🚀 Deployment Guide - AI FAQ Generator

This guide provides multiple deployment options for your AI FAQ Generator application.

## 📋 Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Git installed on your system

## 🔧 Local Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ai-faq-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run locally:**
   ```bash
   python run.py
   ```

## 🌐 Deployment Options

### 1. GitHub Pages (Static Frontend Only)

Since this is a Flask application, GitHub Pages won't work for the full app, but you can host the frontend separately.

### 2. Heroku Deployment

1. **Install Heroku CLI:**
   ```bash
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Deploy:**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

6. **Open the app:**
   ```bash
   heroku open
   ```

### 3. Railway Deployment

1. **Go to [Railway](https://railway.app/)**
2. **Connect your GitHub repository**
3. **Add environment variable:**
   - `GEMINI_API_KEY`: Your Gemini API key
4. **Deploy automatically**

### 4. Render Deployment

1. **Go to [Render](https://render.com/)**
2. **Create new Web Service**
3. **Connect your GitHub repository**
4. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment Variables:** `GEMINI_API_KEY`
5. **Deploy**

### 5. Docker Deployment

#### Local Docker:
```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build and run manually
docker build -t ai-faq-generator .
docker run -p 5000:5000 -e GEMINI_API_KEY=your_key ai-faq-generator
```

#### Docker Hub:
1. **Build the image:**
   ```bash
   docker build -t yourusername/ai-faq-generator .
   ```

2. **Push to Docker Hub:**
   ```bash
   docker push yourusername/ai-faq-generator
   ```

3. **Deploy anywhere:**
   ```bash
   docker run -p 5000:5000 -e GEMINI_API_KEY=your_key yourusername/ai-faq-generator
   ```

### 6. Vercel Deployment

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Set environment variables in Vercel dashboard**

### 7. DigitalOcean App Platform

1. **Go to DigitalOcean App Platform**
2. **Connect your GitHub repository**
3. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Run Command:** `gunicorn app:app`
   - **Environment Variables:** `GEMINI_API_KEY`
4. **Deploy**

## 🔒 Environment Variables

Set these in your deployment platform:

- `GEMINI_API_KEY`: Your Google Gemini API key (required)
- `FLASK_ENV`: Set to `production` for production deployments

## 📁 Project Structure

```
ai-faq-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── run.py                # Easy startup script
├── env_example.txt       # Environment configuration example
├── .gitignore           # Git ignore rules
├── Procfile             # Heroku deployment
├── runtime.txt          # Python version specification
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose configuration
├── templates/
│   └── index.html       # Main web interface
└── uploads/             # Temporary file storage (auto-created)
```

## 🛠️ Customization

### Changing Port
Edit the port in `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Adding SSL
For production, use a reverse proxy like Nginx with SSL certificates.

### Database Integration
Add database models and configure connection strings for persistent storage.

## 🔍 Troubleshooting

### Common Issues:

1. **Port already in use:**
   ```bash
   # Find and kill the process
   lsof -ti:5000 | xargs kill -9
   ```

2. **Environment variables not set:**
   - Check your deployment platform's environment variable settings
   - Ensure the variable name matches exactly

3. **Dependencies not installed:**
   ```bash
   pip install -r requirements.txt
   ```

4. **File upload issues:**
   - Ensure the `uploads` directory exists
   - Check file permissions

### Logs:
- **Heroku:** `heroku logs --tail`
- **Railway:** View logs in dashboard
- **Docker:** `docker logs <container_id>`

## 📈 Monitoring

Consider adding:
- Application monitoring (e.g., Sentry)
- Performance monitoring (e.g., New Relic)
- Uptime monitoring (e.g., UptimeRobot)

## 🔄 CI/CD

Set up GitHub Actions for automatic deployment:

```yaml
name: Deploy to Heroku
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.12.12
      with:
        heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
        heroku_app_name: "your-app-name"
        heroku_email: "your-email@example.com"
```

## 🎉 Success!

Your AI FAQ Generator is now deployed and ready to use! Share the URL with others to let them generate FAQs from their content.

---

**Need help?** Check the troubleshooting section or create an issue in the repository. 