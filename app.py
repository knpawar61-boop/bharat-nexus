import streamlit as st
import random

# 1. Page Configuration
st.set_page_config(
    page_title="BHARAT NEXUS | Smart Public Service Bridge",
    page_icon="🏛️",
    layout="wide"
)

# 2. Custom Styling
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
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #00e5ff;
        letter-spacing: 1.5px;
        margin-bottom: 0px;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #80deea;
        font-weight: 500;
        margin-top: 4px;
        margin-bottom: 14px;
    }
    .sidebar-card {
        background: rgba(16, 36, 46, 0.9);
        border: 1px solid #1e88e5;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .sidebar-role {
        font-size: 0.72rem;
        color: #80deea;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 4px;
    }
    .sidebar-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
    }
    .info-box {
        background: rgba(13, 31, 40, 0.85);
        border-left: 4px solid #00e5ff;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #00b4db 0%, #0083b0 100%);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Session State for Tokens
if "tokens" not in st.session_state:
    st.session_state.tokens = [
        ("BN-70421", "Demo Citizen", "Fresh Indian Passport (Normal)", "Verified & Forwarded to RPO Desk (Omkar)", "Aadhaar, PAN, 10th Marksheet")
    ]

# 3. Sidebar
with st.sidebar:
    st.markdown("### 🏛️ Grid Operations")
    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-role">FOUNDER & CHIEF SYSTEMS ARCHITECT</div>
        <div class="sidebar-name">Krishna</div>
    </div>
    <div class="sidebar-card">
        <div class="sidebar-role">TEAM LEADER & DISPATCH MANAGER</div>
        <div class="sidebar-name">Omkar</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🌐 **Theme State:** *Digital Professional*")
    st.markdown("🟢 **System Grid:** *2026–2027 Active*")

# 4. Header & Language Switcher
col_head, col_lang = st.columns([3, 1])

with col_lang:
    lang = st.selectbox("🌐 System Language", ["English", "मराठी (Marathi)"])

is_en = (lang == "English")

with col_head:
    if is_en:
        st.markdown('<div class="hero-title">🏛️ BHARAT NEXUS</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">Smart Public Service Bridge & Autonomous Citizen Scheme Engine</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="hero-title">🏛️ भारत नेक्सस</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">स्मार्ट सार्वजनिक सेवा सेतू आणि स्वायत्त नागरिक योजना केंद्र</div>', unsafe_allow_html=True)

# 100% Free Citizen Initiative Banner
if is_en:
    st.markdown('<div style="background: rgba(0, 230, 118, 0.12); border: 1px solid #00e676; border-radius: 8px; padding: 10px 16px; margin-bottom: 18px; color: #b9f6ca; font-weight: 600;">✅ 100% FREE CITIZEN INITIATIVE: BHARAT NEXUS charges ₹0 portal/agent fee. All guidance, eligibility checks, and direct government portal links are completely free for every citizen.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="background: rgba(0, 230, 118, 0.12); border: 1px solid #00e676; border-radius: 8px; padding: 10px 16px; margin-bottom: 18px; color: #b9f6ca; font-weight: 600;">✅ १००% मोफत नागरिक उपक्रम: भारत नेक्सस कोणतेही पोर्टल किंवा एजंट शुल्क (₹०) आकारत नाही. सर्व मार्गदर्शन आणि शासकीय पोर्टल लिंक्स सर्व नागरिकांसाठी पूर्णपणे मोफत आहेत.</div>', unsafe_allow_html=True)

# Helper Function to Render Clickable Cards Cleanly
def show_service_card(title, summary, docs, steps, url):
    with st.expander(f"📌 {title}  —  [Click to Open Full Guide & Apply]"):
        st.markdown(f"**✨ Key Benefit / Purpose:** {summary}")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**📄 Required Documents:**")
            st.info(docs)
        with c2:
            st.markdown("**🚀 Step-by-Step Forward Process:**")
            st.success(steps)
        st.link_button("🔗 Open Official Government Portal (₹0 Portal Fee)", url)

# 5. Main Navigation Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌐 Government Schemes" if is_en else "🌐 शासकीय योजना",
    "🛂 Passport & Visa Hub" if is_en else "🛂 पासपोर्ट आणि व्हिसा केंद्र",
    "🪪 Essential Citizen Documents" if is_en else "🪪 आवश्यक नागरिक कागदपत्रे",
    "📝 Citizen Application Desk" if is_en else "📝 नागरिक अर्ज कक्ष",
    "🔍 Live Tracker & Eligibility" if is_en else "🔍 थेट ट्रॅकर आणि पात्रता"
])

# TAB 1: CLICKABLE GOVERNMENT SCHEMES
with tab1:
    st.subheader("🌐 Live Government Scheme Registry (Click Any Scheme to View Process)" if is_en else "🌐 थेट शासकीय योजना नोंदणी")
    category = st.radio(
        "Filter Schemes by Category:",
        ["🌾 Agriculture & Farmers", "🎓 Student Scholarships", "💼 Business & Startups", "🏥 Healthcare & Housing"],
        horizontal=True
    )

    if category == "🌾 Agriculture & Farmers":
        show_service_card(
            "PM-KISAN Samman Nidhi Yojana (₹6,000/Year)",
            "Direct financial support of ₹6,000 per year in 3 equal installments to landholding farmer families.",
            "1. Aadhaar Card (linked to mobile & bank)\n2. Land Ownership Records (7/12 Extract / Khatauni)\n3. Bank Passbook (NPCI/DBT enabled)",
            "Step 1: Visit official PM-KISAN portal & click 'New Farmer Registration'.\nStep 2: Enter Aadhaar number, State, and Captcha.\nStep 3: Fill land details (Survey/Khata number) and upload 7/12 extract.\nStep 4: Complete e-KYC via OTP or nearest CSC center.",
            "https://pmkisan.gov.in"
        )
        show_service_card(
            "Pradhan Mantri Fasal Bima Yojana (Crop Insurance)",
            "Low-premium insurance coverage against crop loss due to drought, flood, hailstorm, or unseasonal rain.",
            "1. Aadhaar Card\n2. Land Records (7/12 & 8A)\n3. Sowing Certificate (Peera Patrak)\n4. Bank Account Details",
            "Step 1: Open PMFBY portal and click 'Farmer Corner'.\nStep 2: Register with mobile OTP and bank details.\nStep 3: Select crop season (Kharif/Rabi), district, and insured area.\nStep 4: Pay nominal farmer share premium and download policy receipt.",
            "https://pmfby.gov.in"
        )

    elif category == "🎓 Student Scholarships":
        show_service_card(
            "National Scholarship Portal (NSP) — Central & State Schemes",
            "Pre-Matric, Post-Matric, and Merit-cum-Means scholarships covering tuition fees and maintenance allowance.",
            "1. Aadhaar Card & Student Photo\n2. Previous Year Marksheet\n3. Family Income Certificate\n4. Caste & Domicile Certificate\n5. Bonafide Certificate from Institute",
            "Step 1: Complete One-Time Registration (OTR) on NSP with Face/OTP authentication.\nStep 2: Log in with OTR ID and select eligible Central/UGC/AICTE scheme.\nStep 3: Fill academic & bank details and upload scanned documents.\nStep 4: Submit form and print copy for college/school verification.",
            "https://scholarships.gov.in"
        )
        show_service_card(
            "MahaDBT / State Post-Matric Scholarship Portal",
            "Full tuition fee reimbursement and exam fee waiver for SC/ST/OBC/EWS/Minority students.",
            "1. Aadhaar Card\n2. Caste Validity & Income Certificate (under ₹8 Lakh)\n3. CAP Allotment Letter (for professional courses)\n4. Ration Card & Leaving Certificate",
            "Step 1: Register on MahaDBT using Aadhaar OTP.\nStep 2: Complete Profile (Personal, Address, Qualification, Hostel details).\nStep 3: Click 'All Schemes', check eligibility, and click 'Apply'.\nStep 4: Track scrutiny status under 'My Applied Scheme'.",
            "https://maharashtra.gov.in"
        )

    elif category == "💼 Business & Startups":
        show_service_card(
            "Pradhan Mantri MUDRA Yojana (Loans up to ₹20 Lakh)",
            "Collateral-free micro-enterprise loans under Shishu (up to ₹50k), Kishore (up to ₹5L), and Tarun (up to ₹20L).",
            "1. Aadhaar, PAN & Voter ID\n2. Business Registration / Udyam Certificate\n3. Last 6 Months Bank Statement\n4. Quotation of machinery/equipment to purchase",
            "Step 1: Register your business on Udyam Registration portal.\nStep 2: Apply online via JanSamarth Portal or visit your nearest PSU/Private bank.\nStep 3: Submit business project report and KYC documents.\nStep 4: Bank verifies unit and disburses loan directly to account.",
            "https://jansamarth.in"
        )
        show_service_card(
            "Udyam MSME Registration (Free Government Business ID)",
            "Official MSME status unlocking lower loan interest rates, subsidy on patent/ISO, and tender preferences.",
            "1. Entrepreneur Aadhaar Number\n2. PAN Card & GSTIN (if applicable)\n3. Bank Account Number & IFSC",
            "Step 1: Visit official Udyam portal and enter Aadhaar + Name.\nStep 2: Validate OTP and verify PAN details.\nStep 3: Enter business activity (NIC code), investment, and employee count.\nStep 4: Submit with final OTP to download instant Udyam Certificate.",
            "https://udyamregistration.gov.in"
        )

    elif category == "🏥 Healthcare & Housing":
        show_service_card(
            "Ayushman Bharat PM-JAY (₹5 Lakh Free Health Cover)",
