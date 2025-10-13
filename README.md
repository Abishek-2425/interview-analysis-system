# 🎯 Interview Analysis System

**Overview:**
The Interview Analysis System is a Python-based Streamlit application that analyzes interview transcripts to provide actionable insights. It evaluates filler word usage, overall sentiment, top keywords, and generates human-readable feedback. This MVP is designed for a **smooth local demo**, allowing judges to see instant visual and textual insights from an uploaded transcript or pasted text.

---

## 🧩 Features

1. **Filler Word Analysis** – Detects and counts common filler words like “um”, “uh”, “like”, “you know”, etc.
2. **Sentiment Analysis** – Uses TextBlob to evaluate the overall tone of the transcript (Positive, Neutral, Negative).
3. **Keyword Extraction** – Uses spaCy to extract the most frequent keywords from the transcript.
4. **Feedback Summary** – Combines sentiment, filler words, and keywords to generate actionable human-readable feedback.
5. **Interactive Dashboard** – Streamlit + Plotly charts visualize filler word frequency and keyword distribution.
6. **Flexible Input** – Supports uploaded text files or direct transcript pasting.

---

## 🏗️ Folder Structure

```
interview_analysis/
├── app.py                     # Main Streamlit app
├── analysis/
│   ├── filler_check.py         # Counts filler words
│   ├── sentiment_check.py      # Uses TextBlob for sentiment
│   ├── keyword_extractor.py    # Extracts top keywords using spaCy
│   ├── feedback_generator.py   # Generates textual feedback
│   └── utils.py                # Helper functions (clean text, read file)
├── sample_data/
│   └── sample_transcript.txt   # Sample transcript for demo
├── requirements.txt            # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd interview_analysis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download necessary NLP corpora:

```bash
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
```

---

## 🖥️ Running the App

Run Streamlit locally:

```bash
streamlit run app.py
```

- **Upload a transcript**: Click “Upload a text file (.txt)” and select a transcript.
- **Or paste text**: Paste your interview transcript into the text area.
- **Results**: Metrics, filler word chart, keyword chart, and textual feedback will display instantly.

---

## 🧠 How It Works

1. **Input Processing**:

   - Transcript is uploaded or pasted.
   - Text is cleaned (lowercased, punctuation removed) using `utils.clean_text()`.

2. **Filler Word Analysis** (`filler_check.py`):

   - Counts predefined filler words (single & multi-word phrases).
   - Returns a dictionary of counts and total filler occurrences.

3. **Sentiment Analysis** (`sentiment_check.py`):

   - Uses TextBlob to compute polarity (-1 to +1).
   - Maps polarity to sentiment label (Positive, Neutral, Negative).

4. **Keyword Extraction** (`keyword_extractor.py`):

   - spaCy tokenizes the text, removes stopwords and punctuation.
   - Returns top N frequent keywords as a list of tuples `(keyword, frequency)`.

5. **Feedback Generation** (`feedback_generator.py`):

   - Integrates sentiment, filler counts, and keywords.
   - Produces a concise, human-readable feedback summary for the candidate.

6. **Visualization & Dashboard** (`app.py`):

   - Displays metrics for sentiment, total fillers, and top keyword.
   - Filler words and keywords visualized as bar charts (Plotly).
   - Feedback shown in an info box for quick actionable insight.

---

## 🧪 Demo Ready Transcript

Use `sample_data/sample_transcript.txt` for instant demo. It includes:

- Filler words to trigger the analysis module.
- Positive sentiment statements for sentiment detection.
- Keywords like “project management”, “teamwork”, and “problem-solving”.

---

## 📈 Future Enhancements

- **Audio Input → Transcription**: Integrate OpenAI Whisper to convert recorded interviews into text.
- **Sentence-level Analysis**: Highlight most positive/negative sentences.
- **Role-specific Keyword Matching**: Compare transcript keywords to job descriptions.
- **Export Reports**: Generate PDF reports summarizing analysis.
