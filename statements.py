# statements.py
# This file contains ONLY text banks (no logic)

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
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed highly motivated behaviour, actively contributing and exploring ideas"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "showed great interest and engagement in lessons",
        "maintained consistent enthusiasm and curiosity throughout the term"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "was engaged and contributed well in class activities",
        "demonstrated good focus and motivation in learning tasks"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "participated reliably in lessons and activities",
        "completed tasks with steady effort and attention"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "needed occasional support to maintain focus",
        "engaged with the work when prompted"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "needed regular prompts to stay engaged",
        "required guidance to maintain focus on tasks"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "benefited from consistent guidance in class activities",
        "needed assistance to maintain attention and confidence"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "struggled to stay focused without support",
        "relied heavily on teacher direction to complete tasks"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "needed frequent support to participate",
        "required help to engage with tasks"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "was largely dependent on guidance to complete work",
        "needed constant support to participate in lessons"
    ]
}

reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and interpretation skills",
        "confidently interpreted texts and inferred meaning beyond the literal"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "showed good comprehension and could explain main ideas clearly",
        "made sound inferences and explained the text effectively"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "could identify key ideas and support them with evidence",
        "demonstrated understanding of main points and some details"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "recognized main ideas and some supporting details",
        "could summarize key points with teacher guidance"
    ],
    70: [
        "understood main ideas in texts with some support",
        "identified general ideas with guidance",
        "needed prompts to recognize main points"
    ],
    65: [
        "identified key points in texts with guidance",
        "recognized simple ideas with support",
        "required help to understand key details"
    ],
    60: [
        "showed basic understanding of texts with support",
        "needed assistance to follow simple texts",
        "relied on guidance to comprehend text"
    ],
    55: [
        "understood simple information in texts",
        "recognized familiar ideas but needed support",
        "needed repeated explanations to understand texts"
    ],
    40: [
        "understood texts with support",
        "needed help to identify ideas",
        "required guidance to understand text content"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "required constant help to follow text",
        "could only understand text with heavy guidance"
    ]
}

writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced writing with sophistication and depth"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "structured ideas well and used expressive language",
        "demonstrated clarity and varied sentence forms in writing"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "organized paragraphs effectively",
        "showed good control over sentence structure and vocabulary"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "structured ideas adequately in sentences and paragraphs",
        "used vocabulary appropriately to convey meaning"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "expressed ideas in basic sentences with clarity",
        "constructed simple paragraphs with understandable meaning"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "needed support to structure writing",
        "used basic sentences and some connecting words"
    ],
    60: [
        "wrote short sentences with support",
        "required assistance to develop ideas in writing",
        "needed guidance to structure sentences and paragraphs"
    ],
    55: [
        "structured simple written responses",
        "wrote very basic sentences with teacher help",
        "required support to form coherent sentences"
    ],
    40: [
        "expressed ideas with support",
        "needed guidance to convey thoughts in writing",
        "required help to communicate simple ideas"
    ],
    0: [
        "required significant support to form sentences in writing",
        "could only write with heavy guidance",
        "needed constant help to complete writing tasks"
    ]
}

reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "extend inference skills and examine alternative interpretations",
        "analyze texts considering different viewpoints"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "focus on identifying implied ideas and supporting them with evidence",
        "practice deeper comprehension and critical reading"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "practice inference and identify key details",
        "strengthen comprehension and analysis of text"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "work on summarising main points with evidence",
        "identify and explain key ideas in texts"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "focus on comprehension and extracting main ideas",
        "practice understanding texts with support"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "strengthen understanding of basic text points",
        "practice comprehension with guidance"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "re-read to clarify meaning and understanding",
        "practice reading with support"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "practice simple comprehension exercises",
        "work on understanding familiar words and ideas"
    ],
    40: [
        "identify key events and main points with guided support",
        "practice reading and summarising events",
        "work with teacher guidance to understand texts"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "start with simple comprehension exercises",
        "practice identifying main points with help"
    ]
}

writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "develop complex narrative techniques and sensory writing",
        "refine style to include nuanced expression and perspective"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "enhance expression using varied sentence types",
        "improve descriptive writing with richer vocabulary"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "add more details to enhance imagery and meaning",
        "practice expressing ideas through action and description"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice using showing rather than telling",
        "enhance descriptive writing and character portrayal"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "develop clarity through description and action",
        "use adjectives and verbs to improve writing"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "practice sentence starters and descriptive phrases",
        "enhance clarity and detail in writing"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "practice adding descriptive elements",
        "work on developing sentences with detail"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "practice sequencing events in writing",
        "enhance sentences with supporting details"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "write basic sentences about events and characters",
        "practice simple descriptive sentences"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "write events step by step using simple sentences",
        "practice describing events in order"
    ]
}

closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
