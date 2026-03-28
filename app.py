import streamlit as st

st.set_page_config(page_title="BioPulse IAL", page_icon="🧬")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=100)
st.sidebar.title("BioPulse IAL")
choice = st.sidebar.radio("Go to:", ["Tutor Chat", "Flashcards", "Checklist", "Practical Lab"])

# --- 1. TUTOR CHAT ---
if choice == "Tutor Chat":
    st.header("💬 Biology PhD Tutor")
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Welcome Angana. Ask me anything about IAL Biology!"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = f"Expert Insight: {prompt} is a key topic. In the IAL marking scheme, ensure you mention..."
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

# --- 2. FLASHCARDS ---
elif choice == "Flashcards":





    st.header("🗂️ Active Recall")
    q_list = ["What bond forms between water molecules?", "What is the role of KOH in a respirometer?", "Define Mitotic Index."]
    a_list = ["Hydrogen Bonds", "Absorbs Carbon Dioxide (CO2)", "Ratio of cells in mitosis to total cells."]
    
    if "card_index" not in st.session_state: st.session_state.card_index = 0
    
    st.info(f"Question: {q_list[st.session_state.card_index]}")
    if st.button("Check Answer"):
        st.success(f"Answer: {a_list[st.session_state.card_index]}")
    
    if st.button("Next Card"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(q_list)
        st.rerun()

# --- 3. CHECKLIST ---
elif choice == "Checklist":
    st.header("📋 Syllabus Mastery")
    units = {"Unit 1": ["Water", "Carbs", "Heart"], "Unit 2": ["Cells", "Mitosis", "Plants"]}
    for unit, topics in units.items():
        st.subheader(unit)
        for t in topics: st.checkbox(t, key=f"{unit}_{t}")

# --- 4. PRACTICAL LAB ---
elif choice == "Practical Lab":
    st.header("🔬 Core Practical Guides")
    lab = st.selectbox("Choose Lab:", ["CP 1: Vitamin C", "CP 2: Daphnia", "CP 7: Respirometer"])
    if lab == "CP 1: Vitamin C":
        st.write("Method: Titrate juice into blue DCPIP until colorless.")
    elif lab == "CP 7: Respirometer":
        st.write("Note: KOH absorbs CO2. Liquid moves due to O2 uptake.")
elif lab == "CP 7: Respirometer":
        st.write("Note: KOH absorbs CO2. Liquid moves due to O2 uptake.")

# --- PASTE THE NEW SECTION HERE ---
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍🏫 About the Developer")
st.sidebar.write("**Dr. Angana Rajapakse**")
st.sidebar.write("PhD in Biology | IAL Expert")
st.sidebar.info("Visit 'Hypnotic Science' on YouTube for more!")
st.sidebar.image("https://i.ibb.co/3Wf4QW3/BioPulse-Logo.png", width=200)
st.sidebar.title("BioPulse IAL")
st.sidebar.info("Visit 'Hypnotic Science' on YouTube for more!")
st.sidebar.image("https://i.ibb.co/3Wf4QW3/BioPulse-Logo.png", width=200)
st.sidebar.markdown("---")
st.sidebar.subheader("👨‍🏫 About the Developer")
st.sidebar.write("**Dr. Angana Rajapakse**")
st.sidebar.write("PhD in Biology | IAL Expert")