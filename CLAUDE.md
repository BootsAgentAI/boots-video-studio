# Boots Video Studio

## Project Overview
A Streamlit-based video prompt architect tool for Boots On The Ground AI. This application uses Google's Gemini AI to analyze brand images and generate professional video prompts optimized for AI video generation tools like Kling AI or Runway Gen-3.

## Tech Stack
- **Frontend**: Streamlit
- **AI**: Google Gemini 1.5 Pro
- **Image Processing**: Pillow (PIL)
- **Deployment**: Streamlit Community Cloud

## Project Structure
```
boots-video-studio/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── CLAUDE.md           # Project documentation (this file)
└── .streamlit/         # Streamlit configuration (for secrets)
    └── secrets.toml    # API keys (not committed)
```

## Key Features
- Upload up to 10 brand images
- Configurable aspect ratios (16:9, 9:16, 1:1)
- Custom project narrative input
- AI-powered video story arc generation following Hook → Problem → Solution → CTA structure
- Optimized for Squarespace Hero videos (under 15MB)

## Development

### Local Setup
```bash
# Clone repository
git clone https://github.com/BootsAgentAI/boots-video-studio.git
cd boots-video-studio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### Environment Variables
The app requires a Google Gemini API key. Users provide this via the sidebar input.

For Streamlit Cloud deployment, secrets can be configured in:
- `.streamlit/secrets.toml` (local, not committed)
- Streamlit Cloud dashboard → App settings → Secrets

## Deployment

### Streamlit Community Cloud
1. Push code to GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository: `BootsAgentAI/boots-video-studio`
4. Set main file path: `app.py`
5. Deploy

### Repository
- **GitHub**: https://github.com/BootsAgentAI/boots-video-studio

## Brand Guidelines
- **Mascot**: Boots - a tan dog wearing a BOOTS cap
- **Video Structure**: 30-second story arc
  - Hook (0-3s)
  - Problem (3-10s)
  - Solution (10-24s)
  - CTA (24-30s)

## Commands Reference
```bash
# Run app locally
streamlit run app.py

# Install dependencies
pip install -r requirements.txt

# Check Streamlit version
streamlit --version
```

## Notes for Claude
- Main application logic is in `app.py`
- The system prompt defines the AI's behavior for video prompt generation
- API key is provided by users at runtime (not stored in code)
- Keep total video file size logic under 15MB for Squarespace compatibility
