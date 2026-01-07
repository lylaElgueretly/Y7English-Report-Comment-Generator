import streamlit as st
import random
from docx import Document

# =====================
# CONFIG
# =====================
MAX_CHARS = 490

st.set_page_config(page_title="English Report Comment Generator", layout="centered")
st.title("English Report Comment Generator")

# =====================
# SESSION STATE
# =====================
if "comments" not in st.session_state:
    st.session_state.comments = []

# =====================
# BANKS (UNCHANGED)
# =====================

opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

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
    90: "understanding texts and making insightful interpretations",
    85: "understanding texts confidently and making strong interpretations",
    80: "understanding texts confidently and interpreting key points",
    75: "understanding texts securely and identifying key ideas",
    70: "understanding main ideas in texts with some support",
    65: "identifying key points in texts with guidance",
    60: "showing basic understanding of texts with support",
    55: "understanding simple information in texts",
    40: "understanding texts with support",
    0:  "recognising familiar words but needing significant support to understand texts"
}

writing_bank = {
    90: "expressing ideas clearly using varied vocabulary and sentence structures",
    85: "writing confidently using varied sentences and well-chosen vocabulary",
    80: "writing structured pieces with appropriate vocabulary",
    75: "writing organised paragraphs with suitable vocabulary",
    70: "writing clear sentences and simple paragraphs",
    65: "writing simple sentences with some organisation",
    60: "writing short sentences with support",
    55: "structuring simple written responses",
    40: "expressing ideas with support",
    0:  "requiring significant support to form sentences in writing"
}

reading_target_bank = {
    90: "continue analysing texts in greater depth",
    85: "develop more detailed responses to texts",
    80: "explain ideas in greater detail using evidence",
    75: "develop more detailed responses with closer reference to the text",
    70: "build confidence in explaining ideas when reading",
    65: "focus on identifying and explaining key ideas in texts",
    60: "practise understanding main ideas in short texts",
    55: "develop basic reading comprehension skills",
    40: "practise reading regularly to improve understanding",
    0:  "build confidence in recognising basic words and ideas"
}

writing_target_bank = {
    90: "refine accuracy further and experiment with more complex structures",
    85: "develop more sophisticated vocabulary and sentence variety",
    80: "vary sentence structures and develop ideas more fully",
    75: "expand ideas further and check accuracy carefully",
    70: "develop ideas in more detail and use a wider range of vocabulary",
    65: "organise ideas more clearly and write in full sentences",
    60: "extend written responses beyond short sentences",
    55: "focus on basic sentence structure and spelling",
    40: "practise writing simple sentences",
    0:  "build confidence in writing through regular guided practice"
}

# =====================
# HELPERS
# =====================

def safe_truncate(text, max_chars):
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rsplit(" ", 1)[0]

def generate_comment(name, gender, att, read, write, read_t, write_t):
    p = "he" if gender == "Male" else "she"

    opening = random.choice(opening_phrases)

    reading_phrase = f"demonstrated {reading_bank[read]}"
    writing_phrase = f"demonstrated {writing_bank[write]}"

    comment = (
        f"{opening} {name} {attitude_bank[att]}. "
        f"{p.capitalize()} {reading_phrase} and {writing_phrase}. "
        f"For the next term, {p} should {reading_target_bank[read_t]} and "
        f"{writing_target_bank[write_t]}."
    )

    comment = safe_truncate(comment, MAX_CHARS)
    return comment, len(comment)

# =====================
# INPUTS
# =====================

st.subheader("Student details")

name = st.text_input("Student name")
gender = st.selectbox("Gender", ["Male", "Female"])

att = st.selectbox("Attitude to Learning", sorted(attitude_bank.keys(), reverse=True))
read = st.selectbox("Reading Achieved", sorted(reading_bank.keys(), reverse=True))
write = st.selectbox("Writing Achieved", sorted(writing_bank.keys(), reverse=True))
read_t = st.selectbox("Next Steps – Reading", sorted(reading_target_bank.keys(), reverse=True))
write_t = st.selectbox("Next Steps – Writing", sorted(writing_target_bank.keys(), reverse=True))

# =====================
# GENERATE BUTTON
# =====================

if st.button("Generate comment"):
    if name.strip():
        comment, count = generate_comment(
            name, gender, att, read, write, read_t, write_t
        )

        st.session_state.comments.append({
            "name": name,
            "comment": comment,
            "chars": count
        })
    else:
        st.warning("Please enter a student name.")

# =====================
# DISPLAY COMMENTS
# =====================

if st.session_state.comments:
    st.markdown("### Generated comments")

    for i, entry in enumerate(st.session_state.comments, start=1):
        st.markdown(f"**{i}. {entry['name']}**")
        st.write(entry["comment"])
        st.caption(f"Character count (including spaces): {entry['chars']} / {MAX_CHARS}")
        st.markdown("---")

# =====================
# DOWNLOAD WORD FILE
# =====================

if st.session_state.comments:
    if st.button("Download all comments (Word)"):
        doc = Document()
        doc.add_heading("English Report Comments", level=1)

        for entry in st.session_state.comments:
            doc.add_paragraph(f"{entry['name']}:\n{entry['comment']}\n")

        file_name = "English_Report_Comments.docx"
        doc.save(file_name)

        with open(file_name, "rb") as f:
            st.download_button(
                label="Click to download Word file",
                data=f,
                file_name=file_name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
