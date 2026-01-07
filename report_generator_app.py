# =========================================
# STAGE 7 ENGLISH REPORT COMMENT GENERATOR - Streamlit Version
# Only attitude, reading, writing, and next steps
# =========================================

import random
import streamlit as st

MAX_CHARS = 490

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

# ---------- ACHIEVEMENT BANKS ----------
attitude_bank = {
    90: "approached learning with enthusiasm and confidence, showing independence and curiosity",
    85: "demonstrated a highly positive and motivated attitude towards learning",
    80: "showed a positive and motivated attitude towards learning and participated confidently",
    75: "showed consistent effort and engaged well in class activities",
    70: "was generally focused and responded well to guidance",
    65: "showed a steady approach to learning but benefited from encouragement",
    60: "required support to remain focused and engaged in lessons",
    55: "needed regular guidance to remain engaged and confident",
    40: "found it challenging to stay focused and required consistent encouragement",
    0:  "required significant support to engage confidently in learning"
}

reading_bank = {
    90: "understood texts and made insightful interpretations",
    85: "understood texts confidently and made strong interpretations",
    80: "understood texts confidently and interpreted key points",
    75: "understood texts securely and identified key ideas",
    70: "understood main ideas in texts with some support",
    65: "identified key points in texts with guidance",
    60: "showed basic understanding of texts with support",
    55: "understood simple information in texts",
    40: "understood texts with support",
    0:  "recognised familiar words but needed significant support to understand texts"
}

writing_bank = {
    90: "expressed ideas clearly using varied vocabulary and sentence structures",
    85: "wrote confidently using varied sentences and well-chosen vocabulary",
    80: "wrote structured pieces with appropriate vocabulary",
    75: "wrote organised paragraphs with suitable vocabulary",
    70: "wrote clear sentences and simple paragraphs",
    65: "wrote simple sentences with some organisation",
    60: "wrote short sentences with support",
    55: "structured simple written responses",
    40: "expressed ideas with support",
    0:  "required significant support to form sentences in writing"
}

reading_target_bank = {
    90: "Explore subtler inferences and interpret multiple perspectives to deepen analysis.",
    85: "Extend inference skills and examine alternative interpretations.",
    80: "Focus on recognising subtler implications and supporting ideas with evidence.",
    75: "Practice identifying hidden meanings and making connections within the text.",
    70: "Work on identifying implied ideas and summarising main points.",
    65: "Focus on reading for meaning and noting key details.",
    60: "Strengthen comprehension by paraphrasing and asking questions about the text.",
    55: "Build vocabulary and re-read to clarify meaning.",
    40: "Identify key events and main points with guided support.",
    35: "Begin with guided reading and discussion to identify basic ideas."
}

writing_target_bank = {
    90: "Experiment with subtle suspense, varied perspectives, and advanced sensory effects.",
    85: "Refine vocabulary and explore more varied sentence structures for impact.",
    80: "Focus on precise sensory words and 'showing' character emotions.",
    75: "Add more sensory details and actions that reveal character traits.",
    70: "Replace 'telling' statements with descriptive or action-based sentences.",
    65: "Include adjectives, vivid verbs, and sensory details to enhance imagery.",
    60: "Focus on including at least one sensory detail per paragraph.",
    55: "Use sentence starters and story maps to add detail.",
    40: "Begin with simple sentences describing events and character feelings.",
    35: "Start by sequencing events and describing one action per sentence."
}

closer_bank = [
    "Overall, progress was evident over the course of the term."
]

# ---------- HELPERS ----------
def get_band(value):
    try:
        band = int(value)
        return band if band in attitude_bank else 0
    except:
        return 0

def truncate_comment(comment, max_chars=490):
    if len(comment) <= max_chars:
        return comment
    truncated = comment[:max_chars].rstrip(" ,;.")
    if "." in truncated:
        truncated = truncated[:truncated.rfind(".")+1]
    return truncated

def get_pronouns(gender):
    gender = gender.lower()
    if gender == "male":
        return "he", "his"
    elif gender == "female":
        return "she", "her"
    else:
        return "he", "his"

def lowercase_first(text):
    return text[0].lower() + text[1:] if text else ""

def strip_trailing_punct(text):
    return text.rstrip(". ,;")

def generate_comment(name, att, read, write, read_t, write_t, gender, max_chars=490):
    p, _ = get_pronouns(gender)
    opening = random.choice(opening_phrases)

    attitude_sentence = f"{opening} {name} {attitude_bank[att]}."
    reading_sentence = f"In reading, {p} {reading_bank[read]}."
    writing_sentence = f"In writing, {p} {writing_bank[write]}."
    reading_target_sentence = f"For the next term, {p} should {lowercase_first(strip_trailing_punct(reading_target_bank[read_t]))}."
    writing_target_sentence = f"Additionally, {p} should {lowercase_first(strip_trailing_punct(writing_target_bank[write_t]))}."
    closer_sentence = closer_bank[0]

    comment = " ".join([
        attitude_sentence,
        reading_sentence,
        writing_sentence,
        reading_target_sentence,
        writing_target_sentence,
        closer_sentence
    ])

    comment = truncate_comment(comment, max_chars)
    return comment, len(comment)

# =========================================
# STREAMLIT APP
# =========================================

st.title("English Report Comment Generator (Positive)")

st.markdown("Generate report comments for a student based on achieved and next steps. Character count is shown after generation.")

# ---------- FORM ----------
with st.form("report_form"):
    name = st.text_input("Student Name")
    gender = st.selectbox("Gender", ["Male", "Female"])
    att = st.selectbox("Attitude band", [90,85,80,75,70,65,60,55,40])
    read = st.selectbox("Reading achievement band", [90,85,80,75,70,65,60,55,40])
    write = st.selectbox("Writing achievement band", [90,85,80,75,70,65,60,55,40])
    read_t = st.selectbox("Reading target band", [90,85,80,75,70,65,60,55,40])
    write_t = st.selectbox("Writing target band", [90,85,80,75,70,65,60,55,40])
    
    submitted = st.form_submit_button("Generate Comment")

# ---------- DISPLAY COMMENT ----------
if submitted and name:
    comment, char_count = generate_comment(
        name, att, read, write, read_t, write_t, gender
    )
    
    st.text_area("Generated Comment", comment, height=200)
    st.write(f"Character count (including spaces): {char_count} / {MAX_CHARS}")
