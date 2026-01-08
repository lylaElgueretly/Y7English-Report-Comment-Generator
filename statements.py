import random

# ---------- OPENING PHRASES ----------
opening_phrases = [
    "This term,",
    "Over the course of this term,",
    "During this term,",
    "Throughout this term,",
    "In this term,",
    "Over the past term,"
]

# ---------- ATTITUDE BANK ----------
attitude_bank = {
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional curiosity and independence in learning",
        "showed great enthusiasm and engaged confidently with all tasks"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "showed strong engagement and motivation in class activities",
        "participated confidently and with curiosity in lessons"
    ],
    80: [
        "showed a positive attitude towards learning and participated confidently",
        "engaged well with tasks and demonstrated a motivated approach",
        "showed interest and steady progress in learning activities"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "completed tasks reliably and participated regularly",
        "demonstrated steady focus and involvement in learning"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "showed effort with some support and guidance",
        "participated with reasonable consistency in class activities"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "needed occasional prompting to remain engaged",
        "made progress with support and guidance"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed frequent guidance to complete tasks",
        "showed some engagement with help from the teacher"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "required frequent encouragement to participate",
        "showed limited engagement without support"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "struggled to engage independently and needed help",
        "required constant support to maintain focus in lessons"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "was unable to engage without one-to-one guidance",
        "needed continual assistance to participate in learning tasks"
    ]
}

# ---------- READING BANK ----------
reading_bank = {
    90: [
        "understood texts and made insightful interpretations",
        "demonstrated deep comprehension and could infer subtle meanings",
        "analyzed texts confidently and interpreted ideas effectively"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "showed good comprehension and could explain ideas",
        "interpreted texts accurately with evidence"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "identified main ideas and some supporting details",
        "showed consistent understanding of texts"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "could summarise main points with guidance",
        "showed developing understanding of texts"
    ],
    70: [
        "understood main ideas in texts with some support",
        "identified key points with occasional help",
        "needed some guidance to interpret texts"
    ],
    65: [
        "identified key points in texts with guidance",
        "showed emerging comprehension with support",
        "needed prompting to notice main ideas"
    ],
    60: [
        "showed basic understanding of texts with support",
        "required guidance to follow texts",
        "could recall simple details with help"
    ],
    55: [
        "understood simple information in texts",
        "needed support to understand passages",
        "showed limited comprehension without help"
    ],
    40: [
        "understood texts with support",
        "required guidance to follow simple ideas",
        "needed help to identify main points"
    ],
    35: [
        "began recognising familiar words and ideas with guidance",
        "could follow basic passages with teacher support",
        "needed full support to identify simple ideas"
    ]
}

# ---------- WRITING BANK ----------
writing_bank = {
    90: [
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "wrote with excellent clarity and creativity",
        "produced well-structured, detailed writing confidently"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "demonstrated clear and structured writing",
        "expressed ideas accurately and with some flair"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "produced organised writing with clear ideas",
        "showed consistent sentence structure and clarity"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "produced writing that communicated ideas adequately",
        "showed developing paragraphing and sentence use"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "used simple vocabulary to express ideas",
        "produced basic structured writing"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "showed emerging clarity and structure in writing",
        "produced short sentences with limited detail"
    ],
    60: [
        "wrote short sentences with support",
        "needed help to structure writing",
        "showed limited clarity without guidance"
    ],
    55: [
        "structured simple written responses",
        "needed assistance to complete writing tasks",
        "showed emerging sentence organisation"
    ],
    40: [
        "expressed ideas with support",
        "needed help to communicate ideas in writing",
        "required guidance to form coherent sentences"
    ],
    35: [
        "began forming simple sentences with help",
        "needed full support to write basic ideas",
        "showed limited ability to write independently"
    ]
}

# ---------- READING TARGET BANK ----------
reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "analyse texts for deeper meanings and multiple viewpoints",
        "develop the ability to make sophisticated interpretations"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "consider different perspectives when reading",
        "analyse ideas beyond the obvious"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "work on drawing conclusions from text details",
        "develop understanding of implied meanings"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "work on linking ideas and interpreting context",
        "identify subtler points in passages"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "focus on main ideas with some guidance",
        "develop summarising skills and identifying key points"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "strengthen understanding of essential ideas",
        "identify main points and simple inferences"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "work on basic understanding and recall",
        "practice identifying key details in text"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "use support to understand texts",
        "practice simple reading comprehension skills"
    ],
    40: [
        "identify key events and main points with guided support",
        "begin focusing on main ideas with help",
        "work on understanding basic passages"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "follow simple texts with teacher support",
        "identify simple information with guidance"
    ]
}

# ---------- WRITING TARGET BANK ----------
writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "use sophisticated vocabulary and sentence variation to enhance writing",
        "refine descriptive techniques and complex structures"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "develop more complex sentence forms",
        "enhance descriptive writing with varied language"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "practice using descriptive and expressive language",
        "develop clarity and precision in written expression"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "work on adding descriptive details to improve writing",
        "enhance characterisation through actions and description"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "develop more detailed sentences to show character or events",
        "focus on showing rather than telling in writing"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "add descriptive words and clear verbs to writing",
        "enhance paragraphs with sensory language and verbs"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "add simple descriptive details to support ideas",
        "practice enhancing writing with small descriptive touches"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "develop basic planning and organisation in writing",
        "practice structuring sentences and paragraphs"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "write short sentences to communicate basic ideas",
        "practice forming clear basic sentences"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "write very simple sentences to communicate ideas",
        "practice sequencing ideas clearly"
    ]
}

# ---------- CLOSER BANK ----------
closer_bank = [
    "Overall, progress was evident over the course of the term.",
    "With continued support, further progress is expected next term.",
    "Confidence improved gradually as the term progressed."
]
