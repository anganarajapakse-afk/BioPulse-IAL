import streamlit as st

st.set_page_config(page_title="BioPulse IAL", page_icon="🧬")

# --- SYLLABUS DATA STORAGE ---
syllabus_data = {
    "Unit 1: Molecules & Health": {
        "topics": ["1.1 Water & Carbs", "1.2 Lipids & Proteins", "1.3 Heart & CVD"],
        "flashcards": [
            ("Why is water polar?", "Uneven charge distribution; Oxygen is more electronegative."),
            ("Bond in a disaccharide?", "1,4-glycosidic bond."),
            ("Role of Thromboplastin?", "Triggers conversion of Prothrombin to Thrombin.")
        ]
    },
    "Unit 2: Cells & Plants": {
        "topics": ["2.1 Cell Structure", "2.2 Mitosis", "2.3 Plant Structure"],
        "flashcards": [
            ("Function of Nucleolus?", "Synthesis of ribosomal RNA (rRNA)."),
            ("Define Mitosis.", "Cell division resulting in two genetically identical daughter cells."),
            ("Role of Xylem?", "Transport of water and mineral ions up the plant.")
        ]
    },
    "Unit 4: Environment & Survival": {
        "topics": ["4.1 Photosynthesis", "4.2 Ecology", "4.3 Immunity"],
        "flashcards": [
            ("Where does Light Dependent stage occur?", "Thylakoid membranes of chloroplasts."),
            ("Define NPP.", "NPP = GPP - Respiration (R)."),
            ("What are B-cells?", "Lymphocytes that produce specific antibodies.")
        ]
    },
    "Unit 5: Energy & Control": {
        "topics": ["5.1 Respiration", "5.2 Muscles", "5.3 Nervous System"],
        "flashcards": [
            ("Products of Glycolysis?", "2 Pyruvate, 2 ATP (net), 2 reduced NAD."),
            ("Role of Calcium in muscles?", "Binds to troponin to reveal myosin-binding sites."),
            ("What is Saltatory Conduction?", "Impulse jumping between Nodes of Ranvier in myelinated neurones.")
        ]
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🧬 BioPulse IAL")

# REPLACE YOUR OLD LINE WITH THIS ONE:
page = st.sidebar.radio("Go to:", ["Tutor Chat", "Flashcards", "Syllabus Checklist", "Practical Lab", "Student Portal"])

st.sidebar.markdown("---")
# ... (rest of your sidebar code)

# --- 1. TUTOR CHAT ---
if page == "Tutor Chat":
    st.header("💬 Biology PhD Tutor")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Welcome Angana. Which Chapter are we studying today?"}]
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
    
    if "c_idx" not in st.session_state: st.session_state.c_idx = 0
    
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
    
    # Unit 5 Section
    st.subheader("Unit 5: Energy & Control")
    if st.checkbox("5.3 The Nervous System"):
        st.write("### ⚡ The Action Potential")
        st.markdown("""
        **1. Depolarization:** $Na^+$ channels open; $Na^+$ floods in.
        **2. Repolarization:** $Na^+$ channels close; $K^+$ channels open, $K^+$ leaves.
        **3. Hyperpolarization:** Membrane potential drops below -70mV (the 'undershoot').
        **4. Resting Potential:** Restored by the $Na^+/K^+$ pump.
        """)
        # This describes the graph to the students
        st.info("📈 Study Tip: In the exam, the peak of the graph is usually at +40mV.")

# --- 4. PRACTICAL LAB ---
elif page == "Practical Lab":
    st.header("🔬 Core Practical (CP) Guides")
    
    # This creates the dropdown menu
    lab = st.selectbox("Select a Practical:", [
        "CP 1: Vitamin C Content", 
        "CP 2: Caffeine & Daphnia",
        "CP 3: Mitotic Index",
        "CP 4: Tensile Strength",
        "CP 6: Membrane Permeability",
        "CP 7: Respirometer",
        "CP 10: Gel Electrophoresis"
    ])

    # Now we tell Python what to show for EACH choice:
    if lab == "CP 1: Vitamin C Content":
        st.subheader("Determining Vitamin C Concentration")
        st.write("Method: Titrate fruit juice into blue DCPIP until it becomes colorless.")

    elif lab == "CP 2: Caffeine & Daphnia":
        st.subheader("Caffeine and Daphnia Heart Rate")
        st.info("💡 Exam Essential: Return Daphnia to a recovery tank to ensure ethical treatment and recovery from lamp heat.")
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
        **Key Steps:** 1. Use **HCl** to macerate (soften) the tissue.
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
    st.write("Welcome to the Lyceum Biology Portal. Please log your study session below.")
    
    # This 'with st.form' starts the box
    with st.form("progress_form"):
        name = st.text_input("Full Name:")
        unit_completed = st.selectbox("Which Unit did you study today?", ["Unit 1", "Unit 2", "Unit 4", "Unit 5"])
        score = st.slider("Flashcard Score (0-10):", 0, 10, 5)
        comments = st.text_area("What was the hardest concept today?")
        
        # This is the line we fixed:
        submitted = st.form_submit_button("Submit Progress")
        
        if submitted:
            st.success(f"Thank you, {name}! Dr. Rajapakse has received your update.")