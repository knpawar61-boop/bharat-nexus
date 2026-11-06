import streamlit as st
import random

st.set_page_config(page_title="BHARAT NEXUS | Smart Public Service Bridge", page_icon="🏛️", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); color: #ffffff !important; }
    [data-testid="stSidebar"] { background-color: #0b1519 !important; border-right: 1px solid #1a3a4a; }
    .hero-title { font-size: 3rem; font-weight: 800; color: #00e5ff; letter-spacing: 1.5px; margin-bottom: 0px; }
    .hero-subtitle { font-size: 1.2rem; color: #80deea; font-weight: 500; margin-top: 4px; margin-bottom: 14px; }
    .sidebar-card { background: rgba(16, 36, 46, 0.9); border: 1px solid #1e88e5; border-radius: 10px; padding: 14px; margin-bottom: 12px; }
    .sidebar-role { font-size: 0.72rem; color: #80deea; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 4px; }
    .sidebar-name { font-size: 1.1rem; font-weight: 700; color: #ffffff; }
    .info-box { background: rgba(13, 31, 40, 0.85); border-left: 4px solid #00e5ff; padding: 15px; border-radius: 8px; margin-bottom: 12px; }
</style>
""", unsafe_allow_html=True)

if "tokens" not in st.session_state:
    st.session_state.tokens = [("BN-70421", "Demo Citizen", "Fresh Indian Passport (Normal)", "Verified & Forwarded to RPO Desk (Omkar)", "Aadhaar, PAN, 10th Marksheet")]

with st.sidebar:
    st.markdown("### 🏛️ Grid Operations")
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">FOUNDER & CHIEF SYSTEMS ARCHITECT</div><div class="sidebar-name">Krishna</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">TEAM LEADER & DISPATCH MANAGER</div><div class="sidebar-name">Omkar</div></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🌐 **Theme:** *Digital Professional*")
    st.markdown("🟢 **System Grid:** *2026–2027 Active*")

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

if is_en:
    st.markdown('<div style="background: rgba(0, 230, 118, 0.12); border: 1px solid #00e676; border-radius: 8px; padding: 10px 16px; margin-bottom: 18px; color: #b9f6ca; font-weight: 600;">✅ 100% FREE CITIZEN INITIATIVE: BHARAT NEXUS charges ₹0 portal/agent fee. All guidance, eligibility checks, and direct government portal links are completely free for every citizen.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="background: rgba(0, 230, 118, 0.12); border: 1px solid #00e676; border-radius: 8px; padding: 10px 16px; margin-bottom: 18px; color: #b9f6ca; font-weight: 600;">✅ १००% मोफत नागरिक उपक्रम: भारत नेक्सस कोणतेही पोर्टल किंवा एजंट शुल्क (₹०) आकारत नाही. सर्व मार्गदर्शन आणि शासकीय पोर्टल लिंक्स सर्व नागरिकांसाठी पूर्णपणे मोफत आहेत.</div>', unsafe_allow_html=True)

def card(title, summary, docs, steps, url):
    with st.expander(f"📌 {title} — [Click to View Process & Apply]"):
        st.markdown(f"**✨ Benefit / Purpose:** {summary}")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**📄 Required Documents:**")
            st.info(docs)
        with c2:
            st.markdown("**🚀 Step-by-Step Forward Process:**")
            st.success(steps)
        st.link_button("🔗 Open Official Government Portal (₹0 Portal Fee)", url)

t1, t2, t3, t4, t5 = st.tabs([
    "🌐 Government Schemes" if is_en else "🌐 शासकीय योजना",
    "🛂 Passport & Visa Hub" if is_en else "🛂 पासपोर्ट आणि व्हिसा केंद्र",
    "🪪 Citizen Documents" if is_en else "🪪 आवश्यक नागरिक कागदपत्रे",
    "📝 Application Desk" if is_en else "📝 नागरिक अर्ज कक्ष",
    "🔍 Live Tracker & Eligibility" if is_en else "🔍 थेट ट्रॅकर आणि पात्रता"
])

with t1:
    st.subheader("🌐 Live Government Scheme Registry" if is_en else "🌐 थेट शासकीय योजना नोंदणी")
    cat = st.radio("Select Category:", ["🌾 Agriculture & Farmers", "🎓 Student Scholarships", "💼 Business & Startups", "🏥 Healthcare & Housing"], horizontal=True)
    if cat == "🌾 Agriculture & Farmers":
        card("PM-KISAN Samman Nidhi (₹6,000/Year)", "₹6,000/year direct support in 3 installments to farmer families.", "1. Aadhaar Card\n2. Land 7/12 Extract\n3. DBT-enabled Bank Passbook", "1. Visit pmkisan.gov.in -> New Farmer Registration.\n2. Enter Aadhaar & land details.\n3. Complete e-KYC via OTP or CSC.", "https://pmkisan.gov.in")
        card("PM Fasal Bima Yojana (Crop Insurance)", "Insurance cover against drought, flood & unseasonal rain.", "1. Aadhaar & Bank Passbook\n2. Land 7/12 & 8A\n3. Sowing Certificate", "1. Open pmfby.gov.in -> Farmer Corner.\n2. Select Kharif/Rabi crop & area.\n3. Pay nominal premium & download receipt.", "https://pmfby.gov.in")
    elif cat == "🎓 Student Scholarships":
        card("National Scholarship Portal (NSP)", "Central & UGC/AICTE scholarships for school & college students.", "1. Aadhaar & Photo\n2. Previous Marksheet\n3. Income, Caste & Domicile Certificates\n4. Bonafide Certificate", "1. Complete OTR registration on scholarships.gov.in.\n2. Fill academic & bank details.\n3. Submit & verify at institute.", "https://scholarships.gov.in")
        card("MahaDBT State Post-Matric Scholarship", "Tuition & exam fee reimbursement for SC/ST/OBC/EWS/Minority students.", "1. Aadhaar Card\n2. Income (<₹8L) & Caste Certificate\n3. CAP Allotment & Leaving Certificate", "1. Log in at mahadbt.maharashtra.gov.in.\n2. Complete profile & apply under All Schemes.\n3. Track scrutiny status online.", "https://maharashtra.gov.in")
    elif cat == "💼 Business & Startups":
        card("PM MUDRA Yojana (Loans up to ₹20 Lakh)", "Collateral-free business loans (Shishu, Kishore, Tarun).", "1. Aadhaar, PAN & Voter ID\n2. Udyam Registration\n3. 6-Month Bank Statement & Quotation", "1. Register on Udyam portal.\n2. Apply online via jansamarth.in.\n3. Submit KYC to bank for disbursement.", "https://jansamarth.in")
        card("Udyam MSME Registration (Free Govt ID)", "Official MSME certificate for loan subsidies & tenders.", "1. Aadhaar & PAN Card\n2. Bank Account & IFSC", "1. Visit udyamregistration.gov.in.\n2. Verify Aadhaar & PAN via OTP.\n3. Download instant certificate.", "https://udyamregistration.gov.in")
    else:
        card("Ayushman Bharat PM-JAY (₹5 Lakh Health Cover)", "Cashless hospital treatment up to ₹5 lakh/family/year.", "1. Aadhaar Card\n2. Ration Card / Family ID", "1. Log in at beneficiary.nha.gov.in.\n2. Verify family via Aadhaar OTP.\n3. Download Ayushman Golden Card.", "https://nha.gov.in")
        card("Pradhan Mantri Awas Yojana (PMAY)", "Housing subsidy for building or buying a pucca house.", "1. Family Aadhaar Cards\n2. Income Proof & Bank Passbook\n3. No-Pucca-House Affidavit", "1. Visit pmaymis.gov.in -> Citizen Assessment.\n2. Enter Aadhaar & income details.\n3. Save Reference ID for verification.", "https://pmaymis.gov.in")

with t2:
    st.subheader("🛂 Indian Passport & International Visa Services" if is_en else "🛂 भारतीय पासपोर्ट आणि व्हिसा सेवा")
    pv = st.selectbox("Select Passport or Visa Service:", ["📘 Fresh Indian Passport (Normal / Tatkaal)", "🔄 Passport Renewal / Re-issue / Address Change", "🛡️ Police Clearance Certificate (PCC)", "✈️ International Visa (Tourist / Student / Work)", "🇮🇳 Indian e-Visa (For Foreign Visitors)"])
    if "Fresh" in pv:
        tl, fee, url = "Normal: 15–30 Days | Tatkaal: 1–3 Working Days", "₹0 BHARAT NEXUS Fee | Govt Fee: ₹1,500 (36p) / ₹2,000 (60p) [+₹2,000 Tatkaal]", "https://passportindia.gov.in"
        docs, proc = "• Address Proof: Aadhaar / Electricity Bill / Bank Passbook / Voter ID\n• DOB Proof: Birth Certificate / 10th Marksheet / PAN\n• Non-ECR Proof: 10th Pass Marksheet", "1. Register at passportindia.gov.in -> Apply for Fresh Passport.\n2. Fill details, pay govt fee & book PSK appointment.\n3. Visit PSK with ORIGINAL documents for biometrics.\n4. Complete Police Verification; receive passport by Speed Post."
    elif "Renewal" in pv:
        tl, fee, url = "7–20 Working Days", "₹0 BHARAT NEXUS Fee | Govt Fee: ₹1,500 (Normal) / ₹3,500 (Tatkaal)", "https://passportindia.gov.in"
        docs, proc = "• Original Old Passport + Photocopy of first & last 2 pages\n• New Address Proof (Aadhaar/Voter ID) if changing address", "1. Log in to Passport Seva -> Apply for Re-issue of Passport.\n2. Select reason, pay fee & book PSK slot.\n3. Visit PSK with Old Passport & new proofs."
    elif "PCC" in pv:
        tl, fee, url = "7–15 Working Days", "₹0 BHARAT NEXUS Fee | Govt Fee: ₹500", "https://passportindia.gov.in"
        docs, proc = "• Valid Original Passport + Photocopy\n• Present Address Proof & Employment/Immigration Letter", "1. Log in at passportindia.gov.in -> Apply for PCC.\n2. Pay ₹500 & book PSK appointment.\n3. Complete police verification & collect PCC."
    elif "International" in pv:
        tl, fee, url = "3 Days (e-Visa) to 4–8 Weeks (US/UK/Schengen)", "₹0 BHARAT NEXUS Fee | Embassy/VFS fee varies by country", "https://vfsglobal.com"
