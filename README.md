# 🎙️ InterviewIQ AI

An AI-powered Interview Evaluation System that analyzes complete interview recordings and generates recruiter-style feedback using Deep Learning, NLP, and Large Language Models.

---

## 📌 Overview

InterviewIQ AI is designed to evaluate interview performance by processing an entire interview recording instead of evaluating isolated question-answer pairs.

The system transcribes interview audio, analyzes speech characteristics, detects filler words, performs sentiment analysis, and leverages Google's Gemini model to understand interview conversations, separate interviewer and candidate interactions, evaluate responses, and generate structured recruiter-style feedback.

Unlike traditional interview evaluators that rely on rigid question-answer extraction, InterviewIQ AI treats interviews as natural conversations and reconstructs the interview flow using semantic understanding.

---

# 🚀 Features

### 🎤 Speech Recognition
- Whisper-based speech transcription
- Supports complete interview recordings
- Automatic transcript generation

### 📊 Speech Analytics
- Words Per Minute (WPM)
- Average Sentence Length
- Speaking Speed Analysis

### 🗣️ Communication Analysis
- Filler Word Detection
- Speech Fluency Metrics

### 😊 Sentiment Analysis
- RoBERTa-based sentiment classification
- Positive / Neutral / Negative detection
- Confidence score

### 🤖 AI Interview Intelligence
- Interviewer & Candidate Identification
- Conversation Understanding
- Follow-up Question Grouping
- Answer Evaluation
- Technical Assessment
- Communication Assessment
- Recruiter-style Feedback
- Hiring Recommendation

---

# 🧠 Architecture

```
                   Interview Audio
                          │
                          ▼
          Whisper (Speech Recognition)
                          │
                          ▼
                     Transcript
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
 Speech Analytics              Sentiment Analysis
 (Rule-based)                  (RoBERTa)
          │                               │
          └───────────────┬───────────────┘
                          ▼
            Structured Interview Context
                          │
                          ▼
             Gemini Interview Intelligence
                          │
                          ▼
          Recruiter-style Structured Report
```

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Deep Learning

- OpenAI Whisper
- PyTorch
- Transformers
- RoBERTa

## Generative AI

- Google Gemini 2.5 Flash

## NLP

- Hugging Face Transformers

## Audio Processing

- FFmpeg
- Librosa

---

# 📂 Project Structure

```
InterviewIQ_AI/

│
├── audio/
│
├── outputs/
│
├── prompts/
│   ├── system_prompt.md
│   ├── evaluation_rubric.md
│   ├── output_schema.json
│   └── examples.md
│
├── utils/
│   ├── whisper_utils.py
│   ├── speech_metrics.py
│   ├── filler_detector.py
│   ├── sentiment.py
│   ├── gemini_client.py
│   ├── interview_context.py
│   ├── json_parser.py
│   └── prompt_loader.py
│
├── test_whisper.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Khushii-exe/InterviewIQ_AI.git
```

Move inside the project

```bash
cd InterviewIQ_AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install FFmpeg

macOS

```bash
brew install ffmpeg
```

Windows

Download FFmpeg and add it to your system PATH.

---

# ▶️ Run

Add your Gemini API Key

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

Run

```bash
python test_whisper.py
```

---

# 📈 Current Pipeline

- ✅ Audio Transcription
- ✅ Speech Metrics
- ✅ Filler Detection
- ✅ Sentiment Analysis
- ✅ Interview Context Generation
- ✅ Prompt Engineering Framework
- ✅ Gemini Interview Evaluation
- ✅ Structured JSON Output

---

# 📌 Example Output

The system generates:

- Complete Interview Transcript
- Speech Analytics
- Sentiment Analysis
- Question-wise Evaluation
- Strengths & Weaknesses
- Communication Score
- Technical Assessment
- Hiring Recommendation

---

# 🔮 Future Enhancements

- Streamlit Dashboard
- Interactive Visualizations
- PDF Report Generation
- Video Interview Analysis
- Resume Evaluation
- Role-specific Interview Modes
- Personalized Learning Recommendations
- Cloud Deployment

---

# 👩‍💻 Author

**Khushi Singh**

B.Tech Computer Science Engineering

Interested in Artificial Intelligence, Machine Learning, NLP, and Software Development.

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.