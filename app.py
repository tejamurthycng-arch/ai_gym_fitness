import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configure the Streamlit page
st.set_page_config(page_title="AI Gym Assistant", page_icon="🏋️", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🏋️ AI Fitness")
st.sidebar.write("Unified AI-powered fitness ecosystem[cite: 45].")

# Mapping to the Core AI Modules from the project document 
menu = st.sidebar.radio(
    "Select Module:",
    [
        "Dashboard (Habit Tracker)", # Maps to Module 4 [cite: 16]
        "AI Gym Trainer",            # Maps to Module 1 [cite: 8]
        "AI Dietician",              # Maps to Module 2 [cite: 11]
        "Virtual Gym Buddy",         # Maps to Module 5 [cite: 18]
        "Gym Recommender"            # Maps to Module 7 [cite: 22]
    ]
)

# --- 1. Dashboard & Habit Tracker ---
if menu == "Dashboard (Habit Tracker)":
    st.title("📊 AI Fitness Habit Tracker")
    st.write("Analyzes behavior and tracks your performance score[cite: 16, 21].")
    
    # Mock data for Performance Score [cite: 21]
    dates = pd.date_range(start="2023-10-01", periods=10)
    scores = np.random.randint(60, 100, size=10)
    df = pd.DataFrame({"Date": dates, "Performance Score": scores})
    
    # Visualization using Plotly (as proposed in tech stack) 
    fig = px.line(df, x="Date", y="Performance Score", title="Weekly Progress Report", markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("💡 **Behavioral AI Insight:** You usually skip leg day on Thursdays. Let's schedule a lighter workout to keep you engaged! [cite: 17]")

# --- 2. AI Gym Trainer ---
elif menu == "AI Gym Trainer":
    st.title("📷 AI Gym Trainer")
    st.write("Uses computer vision (MediaPipe) to analyze posture and correct form.")
    
    # Streamlit camera input for workout detection
    img_file_buffer = st.camera_input("Take a picture to analyze your starting pose")
    
    if img_file_buffer is not None:
        st.success("Image captured! In a full implementation, OpenCV and MediaPipe would process this to check your joint angles and count reps.")
        st.metric(label="Detected Reps", value="0", delta="Keep going!")
        st.warning("Feedback: Keep your back straight! [cite: 10]")

# --- 3. AI Dietician ---
elif menu == "AI Dietician":
    st.title("🥗 AI Dietician & Calorie Coach")
    st.write("NLP-driven chatbot for diet plans and nutritional tracking[cite: 12, 13].")
    
    col1, col2 = st.columns(2)
    with col1:
        bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=50.0, value=22.0)
        goal = st.selectbox("Weight Goal", ["Lose Weight", "Maintain", "Build Muscle"])
    with col2:
        diet_pref = st.selectbox("Dietary Preference", ["Vegan", "Keto", "Standard", "Vegetarian"])
    
    if st.button("Generate Diet Plan"):
        st.success("Plan Generated based on your inputs! [cite: 12]")
        st.write("### Today's Grocery List [cite: 13]")
        if diet_pref == "Vegan":
            st.write("- Tofu\n- Spinach\n- Quinoa\n- Almond Milk")
        else:
            st.write("- Chicken Breast\n- Eggs\n- Rice\n- Broccoli")

# --- 4. Virtual Gym Buddy ---
elif menu == "Virtual Gym Buddy":
    st.title("🤖 Virtual Gym Buddy")
    st.write("An AI companion that motivates you and provides personalized guidance[cite: 18, 19].")
    
    # Simple chat interface using Streamlit's chat elements
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How are you feeling about your workout today?"):
        # Display user message
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Mock AI Response (In reality, this would connect to an LLM via Hugging Face/OpenAI APIs) 
        response = f"I hear you saying '{prompt}'. Don't give up! You've got this. Let's push through together!"
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# --- 5. Gym Recommender ---
elif menu == "Gym Recommender":
    st.title("📍 Gym Recommender & Planner")
    st.write("Suggests nearby gyms or fitness challenges based on location and goals[cite: 22, 23].")
    
    location = st.text_input("Enter your city or zip code:")
    if location:
        st.write(f"Finding the best gyms near **{location}**...")
        # Mock recommendation data
        gyms = pd.DataFrame({
            'Gym Name': ['Iron Paradise', 'FitLife Studio', 'CrossFit Central'],
            'Distance (miles)': [1.2, 2.5, 3.0],
            'Rating': [4.8, 4.5, 4.9]
        })
        st.table(gyms)
        st.button("Join Fitness Challenge in this area [cite: 23]")