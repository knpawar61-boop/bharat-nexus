import streamlit as st
import time
import random

# 1. Premium Page Configuration
st.set_page_config(page_title="E-SEVA AUTONOMOUS PORTAL", page_icon="🏛️", layout="wide")

# 2. Premium CSS Custom Styling (Digital Professional Tech Market Theme)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0b1519 !important;
        border-right: 1px solid #1a3a4a;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] h2 {
        color: #ffffff !important;
    }
    h1, h2, h3, h4 {
        color: #00f2fe !important; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput input, .stSelectbox div, .stTextArea textarea, .stNumberInput input {
        background-color: #162a35 !important;
        color: #ffffff !important;
        border: 1px solid #00f2fe !important;
        border-radius: 6px !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%) !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.6rem 2.5rem !important;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: bold !important;
        color: #00f2fe !important;
    }
    /* Style cards for schemes */
    .scheme-card {
        background-color: #112530;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00c6ff;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Secure Side Panel Architecture Credits
st.sidebar.markdown("<h2 style='color:white;'>🏛️ Grid Operations</h2>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style='background-color:#112530; padding:15px; border-radius:10px; margin-bottom:10px; border: 1px solid #00c6ff;'>
    <p style='margin:0; color:#00f2fe; font-size:11px; font-weight:bold;'>FOUNDER & CHIEF SYSTEMS ARCHITECT</p>
    <p style='margin:0; color:white; font-weight:bold; font-size:16px;'>Krishna</p>
</div>
<div style='background-color:#112530; padding:15px; border-radius:10px; border: 1px solid #0072ff;'>
    <p style='margin:0; color:#00f2fe; font-size:11px; font-weight:bold;'>TEAM LEADER & DISPATCH MANAGER</p>
    <p style='margin:0; color:white; font-weight:bold; font-size:16px;'>Omkar</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.write("🌐 *Theme State: Digital Professional Market Active*")

# 4. Global Language Controller Hub
col_title, col_lang = st.columns(2)
with col_lang:
    lang = st.selectbox("🌐 System Language", ["English", "मराठी (Marathi)"])

with col_title:
    if lang == "English":
        st.title("🏛️ E-SEVA AUTONOMOUS PORTAL")
        st.subheader("Central Government Scheme Database Engine")
    else:
        st.title("🏛️ ई-सेवा स्वायत्त पोर्टल")
        st.subheader("केंद्रीय शासकीय योजना डेटाबेस इंजिन")

st.markdown("---")

# 5. Modular Tab Navigation Design Block
if lang == "English":
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Central Schemes Directory", "📝 Citizen Application Desk", "🔍 Real-Time Document Tracker", "⚙️ Automated Verification Matrix"])
else:
    tab1, tab2, tab3, tab4 = st.tabs(["📋 शासकीय योजना निर्देशिका", "📝 नागरिक अर्ज केंद्र", "🔍 रिअल-टाइम अर्ज ट्रॅकर", "⚙️ स्वायत्त पात्रता कॅल्क्युलेटर"])

# --- TAB 1: CENTRAL SCHEMES DIRECTORY ---
with tab1:
    if lang == "English":
        st.write("### 🌐 Live Government Scheme Registry")
        scheme_cat = st.radio("Filter Schemes by Category:", ["🌾 Agriculture & Farmers", "🎓 Student Scholarships", "💼 Business & Startups"])
        
        if scheme_cat == "🌾 Agriculture & Farmers":
            st.markdown("""
            <div class='scheme-card'>
                <h4>1. PM Kisan Samman Nidhi Yojana</h4>
                <p><b>Benefit:</b> ₹6,000 per year directly transferred to bank accounts in 3 equal installments.</p>
                <p><b>Eligibility:</b> All small and marginal landholding farmer families in the state.</p>
            </div>
            <div class='scheme-card'>
                <h4>2. CM Kisan Jalyukt Shivar Abhiyan</h4>
                <p><b>Benefit:</b> Subsidies up to 80% for constructing farm ponds, drip systems, and water wells.</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif scheme_cat == "🎓 Student Scholarships":
            st.markdown("""
            <div class='scheme-card'>
                <h4>1. MahaDBT Post-Matric Scholarship Slabs</h4>
                <p><b>Benefit:</b> 100% tuition fee waiver and monthly accommodation maintenance allowances.</p>
                <p><b>Eligibility:</b> Students from backward social classes with verified income below ₹8 Lakhs.</p>
            </div>
            """, unsafe_allow_html=True)
            
        elif scheme_cat == "💼 Business & Startups":
            st.markdown("""
            <div class='scheme-card'>
                <h4>1. Pradhan Mantri MUDRA Credit Matrix</h4>
                <p><b>Benefit:</b> Collateral-free operational project credit loans up to ₹10 Lakhs for young innovators.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("### 🌐 थेट सरकारी योजना निर्देशिका")
        scheme_cat = st.radio("वर्गीकरणानुसार योजना निवडा:", ["🌾 शेती आणि शेतकरी योजना", "🎓 विद्यार्थी शिष्यवृत्ती", "💼 उद्योग आणि स्टार्टअप योजना"])
        
        if scheme_cat == "🌾 शेती आणि शेतकरी योजना":
            st.markdown("""
            <div class='scheme-card'>
                <h4>१. पीएम किसान सन्मान निधी योजना</h4>
                <p><b>फायदा:</b> प्रति वर्ष ₹६,००० थेट बँक खात्यात ३ समान हप्त्यांमध्ये जमा.</p>
                <p><b>पात्रता:</b> राज्यातील सर्व अल्पभूधारक शेतकरी कुटुंबे.</p>
            </div>
            """, unsafe_allow_html=True)
        elif scheme_cat == "🎓 विद्यार्थी शिष्यवृत्ती":
            st.markdown("""
            <div class='scheme-card'>
                <h4>१. महाडीबीटी (MahaDBT) पोस्ट-मॅट्रिक शिष्यवृत्ती योजना</h4>
                <p><b>फायदा:</b> १००% शिक्षण शुल्क माफी आणि मासिक निर्वाह भत्ता लाभ.</p>
            </div>
            """, unsafe_allow_html=True)
        elif scheme_cat == "💼 उद्योग आणि स्टार्टअप योजना":
            st.markdown("""
            <div class='scheme-card'>
                <h4>१. प्रधानमंत्री मुद्रा बँक योजना</h4>
                <p><b>फायदा:</b> नवीन व्यवसायासाठी विनाहमी ₹१० लाखांपर्यंतचे कर्ज सहाय्य.</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 2: CITIZEN APPLICATIONS ---
with tab2:
    col_form, col_output = st.columns(2)
    with col_form:
        if lang == "English":
            st.write("### 📝 Secure Application Registry")
            applicant_name = st.text_input("Applicant's Full Name")
            service_type = st.selectbox("Required Certificate Type:", ["Select...", "Income Certificate", "Caste Certificate", "Domicile Certificate"])
            annual_income = st.number_input("Annual Income (₹):", min_value=0, value=180000)
            uploaded_docs = st.text_area("List Ready Documents:")
            submit_btn = st.button("Deploy File")
        else:
            st.write("### 📝 सुरक्षित अर्ज नोंदणी")
            applicant_name = st.text_input("अर्जदाराचे पूर्ण नाव")
            service_type = st.selectbox("हवा असलेला दाखला निवडा:", ["निवडा...", "उत्पन्नाचा दाखला", "जातीचा दाखला", "अधिवास प्रमाणपत्र"])
            annual_income = st.number_input("वार्षिक उत्पन्न (₹):", min_value=0, value=180000)
            uploaded_docs = st.text_area("तुमच्याकडे असलेली कागदपत्रे:")
            submit_btn = st.button("सबमिट करा")

    with col_output:
        st.write("### 🧠 AI Core Feed")
        if submit_btn:
            st.success("System Log Registered! Processing Token Transferred to Omkar.")

# --- TAB 3: APPLICATION TRACKER ---
with tab3:
    st.write("### 🔍 Central Network Database Query")
    search_id = st.text_input("Enter 5-Digit Token ID:")
    if st.button("Query Logs" if lang=="English" else "डेटाबेस तपासा"):
        st.info("Awaiting ledger validation check by Omkar.")

# --- TAB 4: AUTOMATED ELIGIBILITY TESTING ---
with tab4:
    st.write("### ⚙️ Autonomous Eligibility Simulation")
    calc_income = st.slider("Adjust Income Tracking Bar", 50000, 1500000, 250000, step=50000)
    if calc_income <= 800000:
        st.success("🟢 Simulation Result: Eligible under Non-Creamy Layer bounds.")
    else:
        st.error("🔴 Simulation Result: Exceeds standard threshold limits.")
