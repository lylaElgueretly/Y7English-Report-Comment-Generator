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

# ---------- ACHIEVEMENT BANKS (3 variants each) ----------
attitude_bank = {
    90: [
        "approached learning with enthusiasm and confidence, showing independence and curiosity",
        "demonstrated exceptional engagement and curiosity in class activities",
        "showed outstanding commitment and eagerness to learn independently"
    ],
    85: [
        "demonstrated a highly positive and motivated attitude towards learning",
        "approached lessons with strong focus and positive engagement",
        "consistently showed interest and active participation in class"
    ],
    80: [
        "showed a positive and motivated attitude towards learning and participated confidently",
        "engaged well in lessons and contributed positively",
        "responded well to challenges and participated actively"
    ],
    75: [
        "showed consistent effort and engaged well in class activities",
        "followed class activities attentively and made steady progress",
        "participated regularly and demonstrated reliable effort"
    ],
    70: [
        "was generally focused and responded well to guidance",
        "followed instructions and contributed appropriately",
        "showed reasonable engagement with support"
    ],
    65: [
        "showed a steady approach to learning but benefited from encouragement",
        "required occasional prompting to stay on task",
        "worked steadily with support from the teacher"
    ],
    60: [
        "required support to remain focused and engaged in lessons",
        "needed frequent guidance to participate effectively",
        "struggled to remain on task without support"
    ],
    55: [
        "needed regular guidance to remain engaged and confident",
        "depended on reminders to complete tasks",
        "required consistent assistance to stay involved"
    ],
    40: [
        "found it challenging to stay focused and required consistent encouragement",
        "struggled with concentration and needed motivation",
        "required ongoing prompting to engage in activities"
    ],
    0: [
        "required significant support to engage confidently in learning",
        "was largely dependent on teacher support to participate",
        "struggled significantly to complete tasks independently"
    ]
}

reading_bank = {
    90: [
        "demonstrated deep comprehension and interpretation skills",
        "understood texts and made insightful interpretations",
        "analysed texts with thorough understanding and clarity"
    ],
    85: [
        "understood texts confidently and made strong interpretations",
        "demonstrated good comprehension and interpretive skills",
        "read texts accurately and identified key points"
    ],
    80: [
        "understood texts confidently and interpreted key points",
        "interpreted key ideas with reasonable understanding",
        "demonstrated comprehension of main points"
    ],
    75: [
        "understood texts securely and identified key ideas",
        "picked out main ideas from texts with confidence",
        "showed clear understanding of essential points"
    ],
    70: [
        "understood main ideas in texts with some support",
        "identified main ideas when prompted",
        "showed developing understanding of text content"
    ],
    65: [
        "identified key points in texts with guidance",
        "needed help to highlight main ideas",
        "showed basic understanding of text with support"
    ],
    60: [
        "showed basic understanding of texts with support",
        "relied on guidance to comprehend texts",
        "understood simple passages with help"
    ],
    55: [
        "understood simple information in texts",
        "read simple texts with comprehension",
        "needed support to understand straightforward passages"
    ],
    40: [
        "understood texts with support",
        "relied heavily on guidance to interpret texts",
        "struggled with comprehension without help"
    ],
    0: [
        "recognised familiar words but needed significant support to understand texts",
        "had difficulty understanding texts independently",
        "required extensive help to make sense of texts"
    ]
}

writing_bank = {
    90: [
        "wrote with excellent clarity and creativity",
        "expressed ideas clearly using varied vocabulary and sentence structures",
        "produced sophisticated written work with flair"
    ],
    85: [
        "wrote confidently using varied sentences and well-chosen vocabulary",
        "crafted clear and well-structured writing",
        "expressed ideas with strong sentence control"
    ],
    80: [
        "wrote structured pieces with appropriate vocabulary",
        "produced coherent paragraphs with suitable words",
        "demonstrated logical organisation in writing"
    ],
    75: [
        "wrote organised paragraphs with suitable vocabulary",
        "showed clear paragraph structure and sentence control",
        "expressed ideas in a structured way"
    ],
    70: [
        "wrote clear sentences and simple paragraphs",
        "produced understandable sentences with some organisation",
        "wrote basic paragraphs and sentences clearly"
    ],
    65: [
        "wrote simple sentences with some organisation",
        "produced short sentences that conveyed ideas",
        "wrote basic ideas with minimal structure"
    ],
    60: [
        "wrote short sentences with support",
        "needed help to structure sentences",
        "produced very simple written work"
    ],
    55: [
        "structured simple written responses",
        "needed guidance to write coherent sentences",
        "relied on templates to write simple responses"
    ],
    40: [
        "expressed ideas with support",
        "needed support to form sentences",
        "wrote short phrases with teacher guidance"
    ],
    0: [
        "required significant support to form sentences in writing",
        "could not write without substantial help",
        "needed full support to complete writing tasks"
    ]
}

reading_target_bank = {
    90: [
        "explore subtler inferences and interpret multiple perspectives to deepen analysis",
        "extend inference skills and consider alternative perspectives in texts",
        "analyse texts with deeper interpretation and explore multiple viewpoints"
    ],
    85: [
        "extend inference skills and examine alternative interpretations",
        "focus on recognising subtler implications in texts",
        "practice interpreting texts with guidance and identify multiple perspectives"
    ],
    80: [
        "focus on recognising subtler implications and supporting ideas with evidence",
        "identify implied ideas and provide textual evidence",
        "develop analysis of key points with examples"
    ],
    75: [
        "practice identifying hidden meanings and making connections within the text",
        "summarise main points and relate them to context",
        "focus on connecting ideas in texts"
    ],
    70: [
        "work on identifying implied ideas and summarising main points",
        "focus on extracting main ideas with minimal support",
        "develop skills in identifying key concepts"
    ],
    65: [
        "focus on reading for meaning and noting key details",
        "highlight key information from texts",
        "practice reading comprehension with guidance"
    ],
    60: [
        "strengthen comprehension by paraphrasing and asking questions about the text",
        "practice understanding texts through questioning",
        "develop comprehension by summarising passages"
    ],
    55: [
        "build vocabulary and re-read to clarify meaning",
        "practice decoding words and understanding meaning",
        "reinforce comprehension through repeated reading"
    ],
    40: [
        "identify key events and main points with guided support",
        "read and note main points with help",
        "highlight important events with guidance"
    ],
    35: [
        "begin with guided reading and discussion to identify basic ideas",
        "start identifying main ideas with support",
        "follow guided activities to extract simple points"
    ]
}

writing_target_bank = {
    90: [
        "experiment with subtle suspense, varied perspectives, and advanced sensory effects",
        "refine vocabulary and explore complex sentence structures for impact",
        "focus on advanced narrative techniques and character portrayal"
    ],
    85: [
        "refine vocabulary and explore more varied sentence structures for impact",
        "add detail to sentences and vary sentence beginnings",
        "practice more sophisticated vocabulary use"
    ],
    80: [
        "focus on precise sensory words and 'showing' character emotions",
        "enhance descriptive writing with details",
        "practice showing emotions through writing"
    ],
    75: [
        "add more sensory details and actions that reveal character traits",
        "practice adding descriptive actions to characters",
        "improve imagery and detail in sentences"
    ],
    70: [
        "replace 'telling' statements with descriptive or action-based sentences",
        "work on showing rather than telling in writing",
        "practice writing sentences that describe actions"
    ],
    65: [
        "include adjectives, vivid verbs, and sensory details to enhance imagery",
        "add descriptive words to make writing vivid",
        "practice enriching sentences with details"
    ],
    60: [
        "focus on including at least one sensory detail per paragraph",
        "add one descriptive element to each paragraph",
        "practice inserting sensory details in writing"
    ],
    55: [
        "use sentence starters and story maps to add detail",
        "organise sentences with planning tools",
        "practice structured sentence writing"
    ],
    40: [
        "begin with simple sentences describing events and character feelings",
        "write basic sentences about actions and feelings",
        "practice simple descriptive writing"
    ],
    35: [
        "start by sequencing events and describing one action per sentence",
        "practice ordering events in writing",
        "write step-by-step actions in sentences"
    ]
}

closer_bank = [
    "Overall, progress was evident over the course of the term",
    "With continued support, further progress is expected next term",
    "Confidence improved gradually as the term progressed"
]
