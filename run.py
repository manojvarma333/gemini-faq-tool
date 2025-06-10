#!/usr/bin/env python3
"""
AI FAQ Generator - Run Script
Simple script to start the Flask application
"""

import os
import sys
from app import app

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import flask
        import google.generativeai
        import requests
        import PyPDF2
        import docx
        import markdown
        import bs4
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if Gemini API key is configured"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_gemini_api_key_here':
        print("⚠️  Gemini API key not configured")
        print("Please create a .env file with your GEMINI_API_KEY")
        print("See env_example.txt for reference")
        return False
    print("✅ Gemini API key configured")
    return True

def main():
    """Main function to run the application"""
    print("🤖 AI FAQ Generator (Gemini) Starting...")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check API key
    if not check_api_key():
        print("\nYou can still run the app, but FAQ generation won't work without an API key.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print("\n🚀 Starting Flask application...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 40)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == '__main__':
    main() 