# statements.py

# Opening phrases
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,"
]

# Attitude bank (key = band, value = list of 3 variants)
attitude_bank = {
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed excellent participation and initiative in all learning tasks"
    ],
    85: [
        "approached learning with confidence and curiosity",
        "demonstrated good engagement and interest in class activities",
        "showed strong participation and initiative in learning"
    ],
    80: [
        "showed a positive and motivated attitude towards learning",
        "engaged well and participated confidently in lessons",
        "showed consistent effort and interest in class activities"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "responded well to guidance and contributed in class",
        "maintained steady participation in learning tasks"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "maintained interest but sometimes needed support",
        "showed steady engagement with teacher guidance"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "needed occasional reminders to stay focused",
        "participated with support and encouragement"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed guidance to maintain attention in class",
        "participated when prompted and guided"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "showed limited independence in class activities",
        "required teacher support to complete tasks"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "needed constant support to engage in lessons",
        "struggled to participate without guidance"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "was unable to complete tasks without extensive guidance",
        "showed very limited engagement in lessons"
    ]
}

# Similarly update reading_bank, writing_bank, reading_target_bank, writing_target_bank
# Each with 3 variants per band (for brevity, not all shown here)

# Closer phrases
closer_bank = [
    "Keep up the excellent work!",
    "Continue striving for improvement.",
    "We look forward to seeing continued growth."
]
