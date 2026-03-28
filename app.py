import streamlit as st

st.set_page_config(page_title="BioPulse IAL", page_icon="🧬")

# Sidebar navigation
st.sidebar.title("🧬 BioPulse IAL")
st.sidebar.markdown("---")
choice = st.sidebar.radio("Go to:", ["Tutor Chat", "Flashcards", "Syllabus Checklist", "Practical Lab"])

# 1. Tutor Chat (The Claude-style interface)
if choice == "Tutor Chat":
    st.header("💬 Biology PhD Tutor")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ex: Explain the Cardiac Cycle"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            response = f"That is a great question about the IAL syllabus. Regarding '{prompt}', let's look at the key marking points..."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# 2. Flashcard Logic
elif choice == "Flashcards":
    st.header("🗂️ Active Recall")
    # Sample question from Chapter 1
    st.info("Question: What type of bond forms between water molecules?")
    if st.button("Flip Card"):
        st.success("Answer: Hydrogen Bonds")
        st.write("How did you do?")
        col1, col2, col3 = st.columns(3)
        col1.button("🔴 Hard")
        col2.button("🟠 Good")
        col3.button("🟢 Easy")

# 3. Interactive Checklist
elif choice == "Syllabus Checklist":
    st.header("📋 Master Checklist")
    st.subheader("Unit 1: Molecules & Health")
    st.checkbox("1.1 Water & Carbohydrates")
    st.checkbox("1.2 Lipids & Proteins")
    st.checkbox("1.3 The Heart & CVD")
    
    st.subheader("Unit 2: Cells & Plants")
    st.checkbox("2.1 Cell Structure & Organelles")
    st.checkbox("2.2 Mitosis & Meiosis")

# 4. elif choice == "Practical Lab":
    st.header("🔬 Unit 3 & 6: The Core Practicals")
    
    # Dropdown for all 18 Practicals
    lab_choice = st.selectbox("Select a Core Practical (CP):", [
        "CP 1: Vitamin C Content", 
        "CP 2: Caffeine and Daphnia Heart Rate",
        "CP 3: Mitotic Index (Root Tip Squash)",
        "CP 4: Tensile Strength of Plant Fibers",
        "CP 5: Plant Ion Deficiencies",
        "CP 6: Membrane Permeability (Beetroot)",
        "CP 7: Gas Exchange in a Respirometer",
        "CP 8: Rate of Photosynthesis (Pondweed)",
        "CP 9: Antibiotic Effectiveness (Inhibition Zones)"
    ])

    # Content for CP 1
    if lab_choice == "CP 1: Vitamin C Content":
        st.subheader("Determining Vitamin C Concentration")
        st.markdown("""
        **Method:** * Titrate a fruit juice into 1 cm³ of 1% **DCPIP** solution. 
        * Stop when the blue dye turns **colorless**.
        
        **Variables:**
        * **Independent:** Type/Age of fruit juice.
        * **Dependent:** Volume of juice needed to decolorize DCPIP.
        * **Controlled:** Concentration and volume of DCPIP.
        """)

    # Content for CP 2
    elif lab_choice == "CP 2: Caffeine and Daphnia Heart Rate":
        st.subheader("Caffeine's Effect on Heart Rate")
        st.warning("⚠️ Ethical Note: Return Daphnia to a recovery tank immediately after use.")
        st.markdown("""
        **Method:** * Place a Daphnia on a slide with a few strands of cotton wool to restrict movement.
        * Add 1-2 drops of caffeine solution.
        * Count heartbeats under a microscope for 15 seconds (multiply by 4).
        
        **Common Question:** Why use Daphnia? They are transparent (heart is visible) and have a simple nervous system.
        """)

    # Content for CP 3
    elif lab_choice == "CP 3: Mitotic Index (Root Tip Squash)":
        st.subheader("Calculating the Mitotic Index")
        st.latex(r"Mitotic\ Index = \frac{n}{N} \times 100")
        st.markdown("""
        **Steps:** 1. Cut 5mm from the tip of an onion root.
        2. Place in **HCl** to soften the cell walls (maceration).
        3. Stain with **Acetic Orcein** to highlight chromosomes.
        4. Squash firmly under a coverslip to create a single layer of cells.
        """)

    # Content for CP 9
    elif lab_choice == "CP 9: Antibiotic Effectiveness":
        st.subheader("Investigating Antibiotic Resistance")
        st.markdown("""
        **Aseptic Technique:** * Use a Bunsen burner to create a sterile updraft.
        * Flame the neck of the bacteria bottle.
        
        **Measurement:** * Measure the **diameter** of the clear 'Zone of Inhibition' around each disc.
        * Calculate area using $\pi r^2$.
        """)