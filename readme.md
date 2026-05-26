# Meeting Transcriber

Local AI-powered meeting transcription and summarization tool built with Python, Whisper, and LLMs.

Designed for technical, functional, and management meetings where extracting decisions, risks, tasks, and actionable insights matters more than raw transcription.

---

# Features

## Current Features

* Audio transcription using Faster-Whisper
* Automatic language detection
* Timestamp generation
* Transcript export to TXT and Markdown
* AI-generated meeting summaries
* Extraction of:

  * key points
  * risks
  * agreements
  * pending tasks
  * next steps
* Technical terminology cleanup
* Local-first workflow

---

# Example Use Cases

* BI / Analytics meetings
* Power BI workshops
* Oracle migration discussions
* Scrum ceremonies
* Functional discovery sessions
* Technical interviews
* Stakeholder meetings
* Requirements gathering

---

# Architecture

```text
meeting-transcriber/
│
├── audio/
│
├── output/
│   ├── transcript.txt
│   ├── transcript.md
│   ├── summary.md
│   └── metadata.json
│
├── src/
│   ├── main.py
│   ├── transcriber.py
│   ├── summarizer.py
│   ├── exporter.py
│   ├── cleaner.py
│   ├── prompts.py
│   └── utils.py
│
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# Tech Stack

* Python 3.11
* Faster-Whisper
* Ollama
* FFmpeg
* Markdown exports
* Local processing

---

# Why This Project Exists

Most meeting tools generate raw transcripts but fail to produce actionable outputs.

The objective of this project is to transform unstructured meeting audio into structured operational knowledge.

Focus areas:

* operational efficiency
* technical meeting intelligence
* decision extraction
* project tracking
* AI-assisted documentation

---

# Installation

## 1. Install FFmpeg

### macOS

```bash
brew install ffmpeg
```

---

## 2. Create virtual environment

```bash
python3.11 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create `.env`

```env
WHISPER_MODEL=medium
OLLAMA_MODEL=qwen2.5:7b
OUTPUT_LANGUAGE=es
```

---

# Usage

Place your audio file inside:

```text
audio/
```

Run:

```bash
python src/main.py
```

Generated outputs:

```text
output/
```

---

# Sample Output

## Transcript

```text
[0.0 - 4.5] Good morning, today we will review management KPIs.
[4.5 - 8.1] Oracle will be the primary data source.
```

---

## AI Summary

```markdown
# Executive Summary

The meeting focused on management dashboards using Power BI and Oracle as the primary data source.

# Key Decisions

- Use Power BI for visualization
- Define KPI governance
- Validate Oracle access model
```

---

# Supported Models

| Model    | Speed     | Accuracy   | Recommended |
| -------- | --------- | ---------- | ----------- |
| tiny     | Very Fast | Low        | No          |
| base     | Fast      | Medium-Low | Testing     |
| small    | Good      | Good       | Yes         |
| medium   | Medium    | Very Good  | Recommended |
| large-v3 | Slow      | Excellent  | Advanced    |

---

# Design Decisions

## Faster-Whisper instead of standard Whisper

Reasons:

* lower memory consumption
* faster inference
* better CPU performance
* practical local deployment

---

## Local-first processing

Advantages:

* privacy
* lower operational costs
* offline support
* control over data

Tradeoff:

* higher local resource usage

---

## Modular architecture

The project intentionally separates:

* transcription
* summarization
* exporting
* cleaning
* prompting

This simplifies future scalability.

---

# Known Limitations

## Audio Quality

Poor microphones, echo, interruptions, and overlapping speakers reduce transcription quality.

---

## Technical Vocabulary

Specialized terminology may require manual cleanup or custom dictionaries.

---

## Long Meetings

Meetings longer than 1 hour may require:

* chunking
* incremental summarization
* token optimization

---

# Future Improvements

## Phase 1 — Stability

* Better error handling
* Batch processing
* CLI arguments
* Logging
* Progress bars
* Configuration file

---

## Phase 2 — Usability

* Streamlit web UI
* Drag & drop upload
* DOCX export
* PDF export
* Speaker diarization
* Multi-language support

---

## Phase 3 — Intelligence

* Automatic task extraction
* Decision detection
* Risk classification
* Sentiment analysis
* KPI detection
* Meeting scoring

---

## Phase 4 — AI Knowledge Layer

* Vector database integration
* Semantic search
* Meeting Q&A
* Retrieval-Augmented Generation (RAG)
* Cross-meeting knowledge indexing

---

## Phase 5 — Enterprise Integration

* Microsoft Teams integration
* Google Meet integration
* Zoom ingestion
* SharePoint export
* Azure Blob Storage
* S3 integration

---

# Potential Advanced Features

* Real-time transcription
* Real-time summarization
* Live meeting assistant
* Voice commands
* Action item reminders
* Multi-user collaboration
* Dashboard analytics

---

# Security Considerations

Never commit:

* `.env`
* API keys
* sensitive customer audio
* confidential transcripts

Recommended:

```gitignore
.env
venv/
output/
```

---

# Performance Notes

Model downloads are cached locally and may consume several GB depending on the selected Whisper model.

Typical sizes:

| Model    | Approx Size |
| -------- | ----------- |
| small    | ~500 MB     |
| medium   | ~1.5 GB     |
| large-v3 | ~3 GB       |

---

# Suggested Portfolio Positioning

This project demonstrates experience in:

* AI engineering
* Python automation
* audio processing
* LLM integration
* applied NLP
* data workflows
* system design

---

# Roadmap

## v1.0

* Stable transcription pipeline
* Markdown exports
* AI summarization

## v1.5

* Speaker diarization
* DOCX export
* Streamlit UI

## v2.0

* Semantic search
* Meeting intelligence
* RAG integration

## v3.0

* Enterprise integrations
* Real-time assistant
* Knowledge platform

---

# License

MIT License

---

# Disclaimer

This project is intended for educational, productivity, and operational use.

Always verify compliance with privacy and data governance policies before processing sensitive meetings.
