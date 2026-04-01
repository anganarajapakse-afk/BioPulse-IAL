import streamlit as st

st.set_page_config(page_title="BioPulse IAL", page_icon="🧬")

# --- SYLLABUS DATA STORAGE ---
syllabus_data = {
    "Unit 1: Molecules, Transport & Health": {
        "topics": [
            "1.1 Water & Carbohydrates",
            "1.2 Lipids & Proteins",
            "1.3 Heart & Cardiovascular Disease",
            "1.4 Transport in Animals",
            "1.5 Transport in Plants"
        ],
        "flashcards": [
            ("Why is water polar?", "Uneven charge distribution; Oxygen is more electronegative."),
            ("Bond in a disaccharide?", "1,4-glycosidic bond."),
            ("Role of Thromboplastin?", "Triggers conversion of Prothrombin to Thrombin."),
            ("What is the role of haemoglobin?", "Carries oxygen from lungs to respiring tissues."),
            ("What is the function of transpiration?", "Movement of water from roots to leaves via xylem, driven by evaporation.")
        ]
    },
    "Unit 2: Cells, Development & Disease": {
        "topics": [
            "2.1 Cell Structure",
            "2.2 Cell Division & Mitosis",
            "2.3 Cell Specialisation",
            "2.4 Plant Structure & Growth",
            "2.5 Infectious Disease"
        ],
        "flashcards": [
            ("Function of Nucleolus?", "Synthesis of ribosomal RNA (rRNA)."),
            ("Define Mitosis.", "Cell division resulting in two genetically identical daughter cells."),
            ("Role of Xylem?", "Transport of water and mineral ions up the plant."),
            ("What is a pathogen?", "A microorganism that causes disease."),
            ("What is the role of lysosomes?", "Contain digestive enzymes to break down old organelles and pathogens.")
        ]
    },
    "Unit 3: Genes & Genetic Engineering": {
        "topics": [
            "3.1 DNA Structure & Replication",
            "3.2 Protein Synthesis",
            "3.3 Gene Mutation",
            "3.4 Genetic Engineering",
            "3.5 Gene Expression"
        ],
        "flashcards": [
            ("What is semi-conservative replication?", "Each new DNA molecule contains one original and one new strand."),
            ("What is a codon?", "A sequence of three bases on mRNA that codes for an amino acid."),
            ("What is a mutation?", "A change in the base sequence of DNA."),
            ("What enzyme cuts DNA in genetic engineering?", "Restriction endonuclease."),
            ("What is transcription?", "The process of making mRNA from a DNA template in the nucleus.")
        ]
    },
    "Unit 4: Biodiversity & Natural Resources": {
        "topics": [
            "4.1 Biodiversity",
            "4.2 Classification",
            "4.3 Natural Selection & Evolution",
            "4.4 Plant Structure & Adaptation",
            "4.5 Ecosystem & Conservation"
        ],
        "flashcards": [
            ("Where does Light Dependent stage occur?", "Thylakoid membranes of chloroplasts."),
            ("Define NPP.", "NPP = GPP - Respiration (R)."),
            ("What are B-cells?", "Lymphocytes that produce specific antibodies."),
            ("What is species richness?", "The number of different species in an ecosystem."),
            ("What is natural selection?", "Process where organisms with favourable traits survive and reproduce.")
        ]
    },
    "Unit 5: Energy, Exercise & Coordination": {
        "topics": [
            "5.1 Respiration",
            "5.2 Muscles & Exercise",
            "5.3 The Nervous System",
            "5.4 Hormonal Control",
            "5.5 Homeostasis"
        ],
        "flashcards": [
            ("Products of Glycolysis?", "2 Pyruvate, 2 ATP (net), 2 reduced NAD."),
            ("Role of Calcium in muscles?", "Binds to troponin to reveal myosin-binding sites."),
            ("What is Saltatory Conduction?", "Impulse jumping between Nodes of Ranvier in myelinated neurones."),
            ("What is the role of insulin?", "Stimulates uptake of glucose by cells and conversion to glycogen."),
            ("What is negative feedback?", "A mechanism that reverses a change to restore normal levels.")
        ]
    },
    "Unit 6: Microbiology, Immunity & Forensics": {
        "topics": [
            "6.1 Microbiology Techniques",
            "6.2 Antibiotics & Resistance",
            "6.3 The Immune System",
            "6.4 Vaccines & Monoclonal Antibodies",
            "6.5 Forensic Biology"
        ],
        "flashcards": [
            ("What is aseptic technique?", "Methods used to prevent contamination of cultures."),
            ("How do bacteria become antibiotic resistant?", "Through random mutation and natural selection."),
            ("What is an antigen?", "A molecule that triggers an immune response."),
            ("How do vaccines work?", "Introduce antigens to stimulate memory cell production without causing disease."),
            ("What is PCR used for in forensics?", "To amplify tiny samples of DNA for analysis.")
        ]
    },
    "Unit 7: Run for Your Life": {
        "topics": [
            "7.1 Exercise Physiology",
            "7.2 Injury & Repair",
            "7.3 Sports Psychology",
            "7.4 Performance Enhancement",
            "7.5 Ethics in Sport"
        ],
        "flashcards": [
            ("What happens to cardiac output during exercise?", "It increases due to increased heart rate and stroke volume."),
            ("What is EPOC?", "Excess Post-exercise Oxygen Consumption — repaying the oxygen debt."),
            ("What is lactic acid?", "Produced during anaerobic respiration when oxygen is limited."),
            ("What is EPO?", "Erythropoietin — a hormone that increases red blood cell production."),
            ("What is the role of synovial fluid?", "Lubricates joints to reduce friction during movement.")
        ]
    },
    "Unit 8: Grey Matter": {
        "topics": [
            "8.1 The Brain & Nervous System",
            "8.2 Neurotransmitters",
            "8.3 Vision",
            "8.4 Brain Development",
            "8.5 Brain Disorders & Drugs"
        ],
        "flashcards": [
            ("What is the role of the cerebellum?", "Coordinates movement and balance."),
            ("What is a synapse?", "A junction between two neurones where signals are transmitted chemically."),
            ("What is the role of rhodopsin?", "Light-sensitive pigment in rod cells that initiates visual signals."),
            ("What is acetylcholine?", "A neurotransmitter released at neuromuscular junctions."),
            ("What does the hypothalamus do?", "Controls homeostasis including temperature and water balance.")
        ]
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🧬 BioPulse IAL")
page = st.sidebar.radio("Go to:", ["Tutor Chat", "Flashcards", "Syllabus Checklist", "Practical Lab", "Student Portal"])
st.sidebar.markdown("---")

# --- 1. TUTOR CHAT ---
if page == "Tutor Chat":
    st.header("💬 Biology PhD Tutor")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Welcome! Which Chapter are we studying today?"}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = f"As your tutor, I suggest focusing on the marking points for '{prompt}'..."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# --- 2. FLASHCARDS (Dynamic) ---
elif page == "Flashcards":
    st.header("🗂️ Active Recall")
    unit_choice = st.selectbox("Select Unit:", list(syllabus_data.keys()))
    cards = syllabus_data[unit_choice]["flashcards"]

    if "c_idx" not in st.session_state:
        st.session_state.c_idx = 0

    q, a = cards[st.session_state.c_idx]
    st.info(f"Question: {q}")
    if st.button("Check Answer"):
        st.success(f"Answer: {a}")
    if st.button("Next Card"):
        st.session_state.c_idx = (st.session_state.c_idx + 1) % len(cards)
        st.rerun()

# --- 3. CHECKLIST (Dynamic) ---
elif page == "Syllabus Checklist":
    st.header("📋 Syllabus Mastery")
    st.write("Track your progress through the IAL Biology syllabus!")

    for unit, data in syllabus_data.items():
        st.subheader(unit)
        for topic in data["topics"]:
            st.checkbox(topic, key=f"{unit}_{topic}")
        st.markdown("---")

# --- 4. PRACTICAL LAB ---
elif page == "Practical Lab":
    st.header("🔬 Core Practical (CP) Guides")

    lab = st.selectbox("Select a Practical:", [
        "CP 1: Vitamin C Content",
        "CP 2: Caffeine & Daphnia",
        "CP 3: Mitotic Index",
        "CP 4: Tensile Strength",
        "CP 6: Membrane Permeability",
        "CP 7: Respirometer",
        "CP 10: Gel Electrophoresis"
    ])

    if lab == "CP 1: Vitamin C Content":
        st.subheader("Determining Vitamin C Concentration")
        st.write("Method: Titrate fruit juice into blue DCPIP until it becomes colorless.")

    elif lab == "CP 2: Caffeine & Daphnia":
        st.subheader("Caffeine and Daphnia Heart Rate")
        st.info("💡 Exam Essential: Return Daphnia to a recovery tank to ensure ethical treatment.")
        st.markdown("""
        **Method:**
        * Use cotton wool fibers to **restrict movement** of the Daphnia.
        * Use a **tally counter** to record heartbeats.

        **Controlled Variables:**
        * Temperature (use a heat shield).
        * Volume of caffeine solution.
        * Age/Size of Daphnia.
        """)

    elif lab == "CP 3: Mitotic Index":
        st.subheader("Onion Root Tip Squash")
        st.markdown("""
        **Key Steps:**
        1. Use **HCl** to macerate (soften) the tissue.
        2. Use **Acetic Orcein** to stain chromosomes.
        3. Squash firmly to get a single layer of cells.
        """)

    elif lab == "CP 4: Tensile Strength":
        st.subheader("Strength of Plant Fibres")
        st.write("Method: Add weights to a suspended plant fibre until it snaps.")

    elif lab == "CP 6: Membrane Permeability":
        st.subheader("Beetroot and Temperature")
        st.write("Concept: High temp increases permeability, leaking red pigment (betalain).")

    elif lab == "CP 7: Respirometer":
        st.subheader("Measuring Respiration Rate")
        st.write("Note: KOH absorbs CO2. Liquid moves purely due to Oxygen uptake.")

    elif lab == "CP 10: Gel Electrophoresis":
        st.subheader("DNA Profiling")
        st.write("Note: Smaller DNA fragments move faster toward the positive anode.")

# --- 5. STUDENT PORTAL ---
elif page == "Student Portal":
    st.header("🎓 Student Progress Tracker")
    st.write("Welcome to the BioPulse IAL Portal. Please log your study session below.")

    with st.form("progress_form"):
        name = st.text_input("Full Name:")
        unit_completed = st.selectbox("Which Unit did you study today?", list(syllabus_data.keys()))
        score = st.slider("Flashcard Score (0-10):", 0, 10, 5)
        comments = st.text_area("What was the hardest concept today?")
        submitted = st.form_submit_button("Submit Progress")

        if submitted:
            st.success(f"Thank you, {name}! Dr. Rajapakse has received your update.")
