# AI-Powered FAQ Generator (Gemini)

An intelligent web application that automatically generates comprehensive FAQ sections from various content sources using Google's Gemini Pro AI model.

## 🚀 Features

- **Multiple Input Sources**: 
  - Direct text input
  - File upload (PDF, DOCX, TXT, MD)
  - Website URL scraping
- **AI-Powered Generation**: Uses Google Gemini Pro for intelligent FAQ creation
- **Customizable Options**:
  - Number of questions (5-20)
  - Writing styles (Professional, Casual, Technical, Simple)
- **Export Options**: HTML and JSON formats
- **Modern UI**: Beautiful, responsive design with intuitive user experience
- **Real-time Processing**: Instant FAQ generation with loading indicators

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Setup Instructions

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Gemini API key**:
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   To get a Gemini API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated API key

4. **Run the application**:
   ```bash
   python run.py
   # or
   python app.py
   ```

5. **Access the application**:
   Open your browser and go to `http://localhost:5000`

## 📖 Usage Guide

### 1. Choose Input Method

**Text Input**: Paste or type your content directly into the text area.

**File Upload**: Upload supported file types:
- PDF files (.pdf)
- Word documents (.docx)
- Text files (.txt)
- Markdown files (.md)

**Website URL**: Enter any website URL to automatically extract and process its content.

### 2. Configure Options

- **Number of Questions**: Select how many FAQ items to generate (5-20)
- **Writing Style**: Choose the tone and style:
  - Professional: Formal, business-like language
  - Casual: Friendly, conversational tone
  - Technical: Detailed explanations with technical terms
  - Simple: Easy-to-understand, basic explanations

### 3. Generate FAQ

Click the "Generate FAQ" button and wait for the AI to process your content and create relevant questions and answers.

### 4. Export Results

Once generated, you can export your FAQ in two formats:
- **HTML**: Ready-to-use HTML file with styling
- **JSON**: Structured data format for further processing

## 🔧 Technical Details

### Architecture
- **Backend**: Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **AI Integration**: Google Gemini Pro API
- **File Processing**: PyPDF2, python-docx, BeautifulSoup
- **Styling**: Custom CSS with gradient backgrounds and modern design

### API Endpoints
- `GET /`: Main application page
- `POST /generate_faq`: Generate FAQ from content
- `POST /upload_file`: Process uploaded files
- `POST /scrape_website`: Extract content from URLs
- `POST /export_faq`: Export FAQ in various formats

### File Structure
```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── run.py                # Easy startup script
├── env_example.txt       # Environment configuration example
├── templates/
│   └── index.html        # Main web interface
└── uploads/              # Temporary file storage (auto-created)
```

## 🎯 Use Cases

- **Business Documentation**: Generate FAQs for product manuals, service guides
- **Educational Content**: Create study materials and learning resources
- **Website Content**: Automatically generate FAQ sections for websites
- **Customer Support**: Develop comprehensive help documentation
- **Content Marketing**: Create engaging FAQ content for blogs and articles

## ⚙️ Configuration

### Environment Variables
- `GEMINI_API_KEY`: Your Google Gemini API key (required)

### Customization Options
You can modify the following in `app.py`:
- Maximum file upload size (default: 16MB)
- Supported file types
- AI model parameters (temperature, model selection)
- Content processing limits

## 🔒 Security & Privacy

- Files are processed temporarily and automatically deleted
- No content is stored permanently on the server
- API calls are made securely to Google Gemini
- Input validation and sanitization implemented

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
For production deployment, consider using:
- Gunicorn as WSGI server
- Nginx as reverse proxy
- Environment variable management
- SSL/TLS certificates

Example with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

**"No module named 'google.generativeai'"**
- Run: `pip install -r requirements.txt`

**"Gemini API key not found"**
- Ensure `.env` file exists with your API key
- Check that `python-dotenv` is installed

**"File upload failed"**
- Check file size (max 16MB)
- Verify file type is supported
- Ensure uploads directory exists

**"Website scraping failed"**
- Check if URL is accessible
- Some websites may block scraping
- Verify URL format is correct

**"API quota exceeded"**
- Check your Gemini API usage limits
- Consider upgrading your Google AI Studio plan

### Getting Help
If you encounter issues:
1. Check the console for error messages
2. Verify your Gemini API key is valid
3. Ensure all dependencies are installed
4. Check file permissions for uploads directory

## 🔮 Future Enhancements

- Support for more file formats
- Multiple language support
- Custom AI model fine-tuning
- Batch processing capabilities
- Advanced export formats (PDF, Word)
- User authentication and history
- API rate limiting and caching
- Integration with other Google AI services

## 🌟 Why Gemini?

- **Cost-Effective**: Often more affordable than other AI APIs
- **High Quality**: Google's latest AI model with excellent performance
- **Reliable**: Backed by Google's infrastructure
- **Easy Integration**: Simple API with good documentation
- **Multimodal**: Can handle text, images, and other content types

---

**Happy FAQ Generating with Gemini! 🎉** 