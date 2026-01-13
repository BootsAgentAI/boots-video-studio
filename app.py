import streamlit as st
from PIL import Image

import google.generativeai as genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Boots Video Architect", page_icon="🐾", layout="wide")

# --- SYSTEM PROMPT (The "Brain") ---
SYSTEM_PROMPT = """
You are the elite Video Prompt Architect for Boots On The Ground AI.
Your mission: Transform image sequences into a professional 30s video story arc.
CORE RULES:
1. MASCOT: Always identify 'Boots' (Tan dog, BOOTS cap). Ensure character consistency.
2. STORY: Map images to: Hook (0-3s), Problem (3-10s), Solution (10-24s), CTA (24-30s).
3. TECH: Optimize for Squarespace Hero. Keep total file size logic under 15MB.
4. OUTPUT: Provide high-fidelity prompts for Kling AI or Runway Gen-3.
"""

# --- UI ELEMENTS ---
st.title("🐾 Boots Video Prompt Architect")
st.markdown("### Transform your brand images into a high-performance video story.")

with st.sidebar:
    st.header("1. Configuration")
    api_key = st.text_input("Gemini API Key", type="password", help="Get your key at aistudio.google.com")
    ratio = st.selectbox("Aspect Ratio", ["16:9 (Web Hero)", "9:16 (Mobile/Social)", "1:1 (Square)"])
    
    st.header("2. Project Narrative")
    project_name = st.text_input("Project Name", "Never Miss Another Call")
    narrative_focus = st.text_area("Specific Narrative Goals", "Focus on Boots as an AI Receptionist handling missed calls.")

# --- FILE UPLOADER ---
uploaded_images = st.file_uploader("Upload up to 10 Brand Images", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

if st.button("Architect My Video") and uploaded_images:
    if not api_key:
        st.error("Please enter an API Key in the sidebar.")
    else:
        try:
            # Setup Gemini
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name="gemini-2.0-flash", system_instruction=SYSTEM_PROMPT)
            
            # Prepare images for the AI
            img_objects = [Image.open(img) for img in uploaded_images]
            
            # The Request
            user_request = f"Project: {project_name}. Ratio: {ratio}. Goals: {narrative_focus}. Analyze these {len(img_objects)} images and build the shot list."
            
            with st.spinner("Boots is drafting your production plan..."):
                response = model.generate_content([user_request] + img_objects)
            
            st.success("🎉 Video Architecture Complete!")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            