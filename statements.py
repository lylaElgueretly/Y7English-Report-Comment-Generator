# statements.py

# =========================================
# English Report Comment Generator Statements
# =========================================

# Opening phrases
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,"
]

# Attitude bank: 3 variants per band
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

# Reading bank: 3 variants per band
reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and interpretation skills",
        "interpreted texts thoughtfully and accurately"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "interpreted texts accurately and with understanding",
        "showed good comprehension and reasoning"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "identified key ideas and interpreted them correctly",
        "showed secure understanding of texts"
    ]
    # ... continue for other bands (75, 70, etc.)
}

# Writing bank: 3 variants per band
writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced structured and sophisticated written work"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "expressed ideas clearly in structured writing",
        "produced engaging written work"
    ]
    # ... continue for other bands
}

# Reading target bank: 3 variants per band
reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "develop a nuanced understanding of texts and draw sophisticated conclusions",
        "analyse texts critically, considering alternative viewpoints"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "practise deeper analysis of texts and ideas",
        "consider multiple perspectives when interpreting texts"
    ]
    # ... continue for other bands
}

# Writing target bank: 3 variants per band
writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "refine vocabulary and sentence structures for stronger impact",
        "explore creative techniques to enhance writing style"
    ],
    85: [
        "focus on precise sensory words and 'showing' character emotions",
        "add more varied sentence structures to writing",
        "enhance writing clarity and creativity"
    ]
    # ... continue for other bands
}

# Closer phrases
closer_bank = [
    "Keep up the excellent work!",
    "Continue striving for improvement.",
    "We look forward to seeing continued growth."
]
