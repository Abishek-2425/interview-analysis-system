import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pandas as pd
import plotly.express as px
import whisper

from analysis.filler_check import analyze_filler_words
from analysis.sentiment_check import analyze_sentiment
from analysis.keyword_extractor import extract_keywords
from analysis.feedback_generator import generate_feedback
from analysis.utils import read_text_file, clean_text, format_keywords

st.set_page_config(page_title="IAS",page_icon="🎯", layout="wide")
st.markdown(
    """
    <h1 style='text-align: center; font-size: 3em;'>🎯 Interview Analysis System</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;font-size:1.5em ;'>Upload your interview transcript, audio, or paste text below to analyze tone, fillers, and key insights.</p>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 16px;
    }
    .css-1d391kg, .css-1v3fvcr {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stExpander h2 {
        font-size: 1.3em;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Upload a text file (.txt)", type=["txt"])

with col2:
    uploaded_audio_file = st.file_uploader(
        "🎤 Upload audio file (.mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"]
    )

audio_source = None
if uploaded_audio_file:
    audio_source = uploaded_audio_file

text_input_area = st.text_area("Or paste transcript here:", height=200)

audio_text = ""
if audio_source:
    placeholder = st.empty()
    with placeholder:
        st.info("🎤 Transcribing audio, please wait...")

    try:
        if isinstance(audio_source, str):
            audio_path = audio_source
            st.audio(audio_path)
        else:
            extension = audio_source.name.split(".")[-1]
            audio_path = f"temp_audio.{extension}"
            with open(audio_path, "wb") as f:
                f.write(audio_source.read())
            st.audio(audio_source)

        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        audio_text = result.get("text", "")

        placeholder.empty()
        st.success("✅ Audio transcription complete!")
        st.text_area("Transcribed Text:", audio_text, height=200)

    except Exception as e:
        placeholder.empty()
        st.error(f"❌ Audio transcription failed: {e}")

    finally:
        if not isinstance(audio_source, str) and os.path.exists(audio_path):
            os.remove(audio_path)

if audio_text:
    text_to_analyze = audio_text
elif uploaded_file:
    text_to_analyze = read_text_file(uploaded_file)
else:
    text_to_analyze = text_input_area

text_to_analyze = clean_text(text_to_analyze)

if not text_to_analyze.strip():
    st.warning("⚠️ No valid input provided. Please upload a file, audio, or paste text.")
else:
    filler_counts, total_fillers = analyze_filler_words(text_to_analyze)
    sentiment_score, sentiment_label = analyze_sentiment(text_to_analyze)
    keywords = extract_keywords(text_to_analyze, top_n=10)
    feedback_summary = generate_feedback(sentiment_score, filler_counts, keywords)

    st.subheader("🔍 Analysis Results")
    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Sentiment", sentiment_label, f"{sentiment_score:.2f}")
    col2.metric("Total Filler Words", total_fillers)
    col3.metric("Top Keyword", keywords[0][0] if keywords else "N/A")

    st.markdown("---")

    with st.expander("📊 Filler Word Frequency Chart"):
        if filler_counts:
            filler_df = pd.DataFrame(list(filler_counts.items()), columns=["Filler Word", "Count"])
            filler_chart = px.bar(
                filler_df,
                x="Filler Word",
                y="Count",
                color="Count",
                color_continuous_scale="blues",
                title="Filler Word Frequency",
            )
            st.plotly_chart(filler_chart, use_container_width=True)
        else:
            st.info("No filler words detected.")

    with st.expander("📊 Top Keywords Chart"):
        if keywords:
            keyword_df = pd.DataFrame(keywords, columns=["Keyword", "Frequency"])
            keyword_chart = px.bar(
                keyword_df,
                x="Keyword",
                y="Frequency",
                color="Frequency",
                color_continuous_scale="greens",
                title="Top Keywords",
            )
            st.plotly_chart(keyword_chart, use_container_width=True)
        else:
            st.info("No keywords extracted.")

    with st.expander("💬 Feedback Summary"):
        st.success(feedback_summary)
