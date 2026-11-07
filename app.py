import streamlit as st
import random

st.set_page_config(page_title="BHARAT NEXUS | Smart Public Service Bridge", page_icon="🏛️", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a1118 0%, #121e2d 100%); color: #e2e8f0 !important; }
    [data-testid="stSidebar"] { background-color: #070d14 !important; border-right: 1px solid #1e293b; }
    .hero-title { font-size: 2.8rem; font-weight: 800; color: #00f2fe; letter-spacing: 2px; margin-bottom: 0px; }
    .hero-subtitle { font-size: 1.15rem; color: #94a3b8; font-weight: 400; margin-top: 4px; margin-bottom: 14px; }
    .sidebar-card { background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
    .sidebar-role { font-size: 0.7rem; color: #38bdf8; letter-spacing: 1px; font-weight: 600; text-transform: uppercase; margin-bottom: 2px; }
    .sidebar-name { font-size: 0.95rem; font-weight: 600; color: #f8fafc; }
    .info-box { background: rgba(15, 23, 42, 0.6); border-left: 4px solid #00f2fe; padding: 16px; border-radius: 6px; margin-bottom: 16px; }
    div.stButton > button { background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%); color: white; font-weight: 600; border: none; border-radius: 6px; width: 100%; transition: all 0.3s; }
</style>
""", unsafe_allow_html=True)

if "db_tokens" not in st.session_state:
    st.session_state.db_tokens = {"BN-70421": {"name": "Anoop Sharma", "service": "Consular Passport Pipeline", "status": "Ready for Official Submission", "docs": "Aadhaar Card"}}

with st.sidebar:
    st.markdown("### 🏛️ System Core")
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">MISSION PHILOSOPHY</div><div class="sidebar-name">Service Before Self (₹0 Fee)</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">INFRASTRUCTURE</div><div class="sidebar-name">Autonomous Public Gateway</div></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🌐 **Access Mode:** *100% Free & Open*")
    st.markdown("🟢 **Network Engine:** *Operational*")

col_head, col_lang = st.columns(2)
with col_lang:
    lang = st.selectbox("🌐 Interface Language", ["English", "मराठी (Marathi)"])
is_en = (lang == "English")

with col_head:
    title_text = "🏛️ BHARAT NEXUS" if is_en else "🏛️ भारत नेक्सस"
    sub_text = "Smart Public Service Bridge & Autonomous Citizen Scheme Engine" if is_en else "स्मार्ट सार्वजनिक सेवा सेतू आणि स्वायत्त नागरिक योजना केंद्र"
    st.markdown(f'<div class="hero-title">{title_text}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-subtitle">{sub_text}</div>', unsafe_allow_html=True)

st.markdown('<div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 6px; padding: 12px 16px; margin-bottom: 20px; color: #34d399; font-weight: 500; font-size: 0.95rem;">⚙️ PROD CONFIGURATION: This ecosystem operates with an absolute zero-fee baseline. No commercial tokens, hidden gateways, or third-party agent layers are attached to processing pipelines.</div>', unsafe_allow_html=True)

def render_node(title, desc, reqs, steps, deep_url):
    st.markdown(f"#### {title}")
    st.info(f"**📄 Document Matrix:** {reqs}")
    st.success(f"**🚀 Execution Workflow:** {steps}")
    st.link_button("🌐 Initialize Direct Government Pipeline Form", deep_url)
    st.markdown("---")

t1, t2, t3, t4, t5 = st.tabs(["🌐 Government Schemes", "🛂 Passport & Visa Hub", "🪪 Citizen Documents", "📝 Application Desk", "🔍 Live Tracker & Eligibility"])

with t1:
    st.subheader("🌐 Live Welfare Registry Node")
    cat = st.radio("Category Router:", ["🌾 Agriculture Node", "🎓 Academic Scholarships", "💼 Industrial Startups", "🏥 Healthcare Core"], horizontal=True)
    if cat == "🌾 Agriculture Node":
        render_node("PM-KISAN Financial Support System", "Cash support grid for land holders.", "Aadhaar, Land registry extract (7/12 Extract)", "Log in to PM-Kisan portal, type baseline data, submit via OTP verified request.", "https://pmkisan.gov.in")
    if cat == "🎓 Academic Scholarships":
        render_node("National Scholarship Portal Integration", "Central scholarship platform managing grants.", "Institutional bonafide form, annual gross family income statement", "Register on the live central cloud repository below, map matching criteria, and forward.", "https://scholarships.gov.in")
    if cat == "💼 Industrial Startups":
        render_node("Udyam National Enterprise System", "Framework granting statutory legal status to micro-businesses.", "PAN Card, Holder Aadhaar", "Launch industry registry below, submit validation fields, download instant certificate.", "https://udyamregistration.gov.in")
    if cat == "🏥 Healthcare Core":
        render_node("Ayushman Bharat Cloud Health System", "Statutory medical protection system guaranteeing ₹500,000 coverage.", "Active identity data, Ration Card", "Verify network status via login check, download secure golden registration pass.", "https://nha.gov.in")

with t2:
    st.subheader("🛂 Consular, Passport & Global Entry Portal")
    pv = st.selectbox("Consular Track:", ["📘 Fresh Indian Passport Protocol", "🔄 Passport Re-Issue & Updates", "🛡️ Police Clearance Certificate Node", "✈️ International Entry Visa Setup"])
    if "Passport" in pv or "Updates" in pv:
        render_node("Ministry of External Affairs Passport Issuance System", "Routing information directly to RPO network.", "Residency verification (Aadhaar/Utility) and valid age document (PAN/Birth Record)", "Open official portal link below, fill fields safely, wire standard fee, and book biometric slot.", "https://passportindia.gov.in")
    if "Certificate" in pv or "Node" in pv:
        render_node("Police Clearance Certificate (PCC) Issuance Node", "Statutory background validation for immigration.", "Original Indian Passport asset, corporate placement letter", "Activate application window link below, schedule appointment, and generate verification pass.", "https://passportindia.gov.in")
    if "Setup" in pv:
        render_node("VFS Global Sovereign Appointment Manager", "Connecting citizens to foreign consulates.", "Passport (6 months validity), 6 months bank statement", "Initialize official pipeline below, map tracking specifications, and set slot timeline.", "https://vfsglobal.com")

with t3:
    st.subheader("🪪 Identity Matrix & Vital Records Registry")
    render_node("Aaple Sarkar State Revenue Certificate Engine", "Document processing for income, domicile, and caste.", "Aadhaar, Ration Card, local verification report", "Open state records directory, mount clear image file proofs, pay nominal fee, and download.", "https://mahaonline.gov.in")
    render_node("Protean Income Tax PAN Registry Node", "Allocating account numbers for financial ledger validation.", "Aadhaar card with linked active mobile line", "Launch federal data portal, complete paperless e-KYC steps, extract PAN file via email.", "https://nsdl.com")

with t4:
    st.subheader("📝 Universal Citizen Application Desk")
    c_name = st.text_input("Citizen Full Name")
    c_mob = st.text_input("Linked Contact Mobile Line")
    c_srv = st.selectbox("Select Target Framework Infrastructure:", ["Consular Passport Pipeline", "International Global Entry Visa", "State Revenue Matrix"])
    if st.button("🚀 Initialize Public Ledger System & Token"):
        if not c_name.strip():
            st.error("❌ Profile name is missing.")
        else:
            new_id = f"BN-{random.randint(10000, 99999)}"
            st.session_state.db_tokens[new_id] = {"name": c_name, "service": c_srv, "status": "Pre-Check Validated", "docs": "Standard KYC Proof Set"}
            st.success(f"✅ Token Dispatched: `{new_id}`")

with t5:
    ct, ce = st.columns(2)
    with ct:
        st.subheader("🔍 Real-Time Transaction Tracker")
        search_id = st.text_input("Key-In Tracking Token ID:", value="BN-70421")
        if st.button("📡 Query Decentralized System Ledger"):
            record = st.session_state.db_tokens.get(search_id.strip().upper())
            if record:
                st.success(f"📦 Record Matched: `{search_id.strip().upper()}`")
                st.write(f"Name: {record['name']} | Service: {record['service']}")
                st.info(f"Status: {record['status']}")
            else:
                st.warning("❌ Token structure not found in database session.")
    with ce:
        st.subheader("⚙️ Autonomous Welfare Eligibility Grid")
        income = st.slider("Household Net Gross Income (₹):", 40000, 1200000, 180000, step=20000)
        st.markdown("**🏁 Compatible Infrastructure Matches:**")
        if income <= 250000:
            st.success("• Eligible for **PM Awas Yojana (Housing)** & **Ayushman Bharat Cover**")
        if income <= 800000:
            st.success("• Eligible for **EWS / OBC Non-Creamy Layer Certificate**")
        st.success("• Eligible for **Indian Passport, PAN, and Voter ID**")
