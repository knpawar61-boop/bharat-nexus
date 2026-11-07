import streamlit as st
import random
import time

st.set_page_config(page_title="BHARAT NEXUS | Smart Public Service Bridge", page_icon="🏛️", layout="wide")

st.markdown("""
<style>
    @keyframes entryFade {
        0% { opacity: 0; filter: blur(6px); transform: translateY(12px); }
        100% { opacity: 1; filter: blur(0px); transform: translateY(0px); }
    }
    @keyframes heartbeat {
        0% { transform: scale(1); opacity: 0.4; }
        50% { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 4px #00e676); }
        100% { transform: scale(1); opacity: 0.4; }
    }
    .stApp { background: linear-gradient(135deg, #0a1118 0%, #121e2d 100%); color: #e2e8f0 !important; }
    [data-testid="stSidebar"] { background-color: #070d14 !important; border-right: 1px solid #1e293b; }
    .hero-title { font-size: 2.8rem; font-weight: 800; color: #00f2fe; letter-spacing: 2px; margin-bottom: 0px; }
    .hero-subtitle { font-size: 1.15rem; color: #94a3b8; font-weight: 400; margin-top: 4px; margin-bottom: 14px; }
    .sidebar-card { background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; border-radius: 8px; padding: 12px; margin-bottom: 12px; }
    .sidebar-role { font-size: 0.7rem; color: #38bdf8; letter-spacing: 1px; font-weight: 600; text-transform: uppercase; margin-bottom: 2px; }
    .sidebar-name { font-size: 0.95rem; font-weight: 600; color: #f8fafc; }
    .info-box { background: rgba(15, 23, 42, 0.6); border-left: 4px solid #00f2fe; padding: 16px; border-radius: 6px; margin-bottom: 16px; }
    .status-pulse { display: inline-block; width: 8px; height: 8px; background-color: #00e676; border-radius: 50%; margin-right: 6px; animation: heartbeat 2s infinite ease-in-out; }
    div.stButton > button { background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%); color: white; font-weight: 600; border: none; border-radius: 6px; width: 100%; transition: all 0.3s; }
    div.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0, 198, 255, 0.3); }
    .terminal-container { background-color: #050a0f; border: 1px solid #00f2fe; border-radius: 8px; padding: 20px; font-family: 'Courier New', Courier, monospace; color: #00ffcc; margin-bottom: 20px; box-shadow: 0 0 20px rgba(0, 242, 254, 0.15); }
</style>
""", unsafe_allow_html=True)

if "booted" not in st.session_state:
    st.session_state.booted = False

if "db_tokens" not in st.session_state:
    st.session_state.db_tokens = {"BN-70421": {"name": "Anoop Sharma", "service": "Consular Passport Pipeline", "status": "Ready for Dispatch Node", "docs": "Aadhaar Card"}}

def render_node(title, desc, reqs, steps, deep_url):
    st.markdown(f"#### {title}")
    st.info(f"**📄 Document Matrix:** {reqs}")
    st.success(f"**🚀 Execution Workflow:** {steps}")
    st.link_button("🚀 Proceed to Direct Government Zero-Margin Form", deep_url)
    st.markdown("---")

if not st.session_state.booted:
    st.markdown('<div class="hero-title" style="text-align:center; margin-top:50px; margin-bottom:20px;">🏛️ BHARAT NEXUS DEPLOYMENT INTERFACE</div>', unsafe_allow_html=True)
    st.markdown('<div class="terminal-container">📡 INITIALIZING SECURE ANTI-CORRUPTION ROUTING NODE...<br>🟢 ESTABLISHING GOVERNMENT COMPLIANCE GATEWAY LINK...<br>🔓 SHIELD ENGINE TERMINAL INITIALIZED COMPLETELY.<br>⌨️ ROOT_USER_ACCESS@BHARAT_NEXUS:~# run portal_launch_sequence.sh</div>', unsafe_allow_html=True)
    if st.button("⚡ EXECUTE BOOT GRID & CONNECT WEB INTERFACE"):
        st.session_state.booted = True
        st.rerun()
else:
    with st.sidebar:
        st.markdown("### 🏛️ System Core")
        st.markdown('<div class="sidebar-card"><div class="sidebar-role">MISSION PHILOSOPHY</div><div class="sidebar-name">Service Before Self (₹0 Fee)</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-card"><div class="sidebar-role">INFRASTRUCTURE</div><div class="sidebar-name">Anti-Corruption Gateway</div></div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("🌐 **Access Mode:** *100% Free & Open*")
        st.markdown('<div><span class="status-pulse"></span><b>Network Status:</b> <i>Operational</i></div>', unsafe_allow_html=True)
        if st.button("🔄 Restart System Session"):
            st.session_state.booted = False
            st.rerun()

    col_head, col_lang = st.columns(2)
    with col_lang:
        lang = st.selectbox("🌐 Interface Language", ["English", "मराठी (Marathi)"])
    is_en = (lang == "English")

    with col_head:
        title_text = "🏛️ BHARAT NEXUS" if is_en else "🏛️ भारत नेक्सस"
        sub_text = "Smart Public Service Bridge & Anti-Corruption Scheme Engine" if is_en else "स्मार्ट सार्वजनिक सेवा सेतू आणि भ्रष्टाचारमुक्त नागरिक योजना केंद्र"
        st.markdown(f'<div class="hero-title">{title_text}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="hero-subtitle">{sub_text}</div>', unsafe_allow_html=True)

    st.markdown('<div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 6px; padding: 12px 16px; margin-bottom: 20px; color: #34d399; font-weight: 500; font-size: 0.95rem;">⚙️ PROD CONFIGURATION: This ecosystem operates with an absolute zero-fee baseline. No commercial tokens, hidden gateways, or third-party agent layers are attached to processing pipelines.</div>', unsafe_allow_html=True)

    st.markdown("### 📝 Mandated Public Rules, Regulations & Terms")
    st.markdown("""* **₹0 Platform Service Charge:** This gateway is completely free of cost. Nobody is authorized to demand money.\n* **Statutory Fee Clearance:** Official government fees are paid straight to official ministry treasuries without agent cuts.\n* **Anti-Bribery Grid:** Bypasses cyber-cafe agents to protect rural and agricultural citizens.""")
    agree = st.checkbox("🟢 I have read and agree to the Rules, Regulations, and Terms of Use of Bharat Nexus.")

    if agree:
        st.markdown("---")
        t1, t2, t3, t4, t5 = st.tabs(["🌐 Government Schemes", "🛂 Passport & Visa Hub", "🪪 Citizen Documents", "📝 Application Desk", "🔍 Live Tracker & Eligibility"])

        with t1:
            st.subheader("🌐 Live Welfare Registry Node")
            cat = st.radio("Category Router:", ["🌾 Agriculture Node", "🎓 Academic Scholarships", "🚀 Youth Opportunities (New Gen)", "🏥 Healthcare Core"], horizontal=True)
            if cat == "🌾 Agriculture Node":
                render_node("PM-KISAN Financial Support System", "Cash support grid for land holders.", "Aadhaar, Land registry extract (7/12 Extract)", "Log in to PM-Kisan portal, type data, submit via OTP verified request.", "https://pmkisan.gov.in")
            if cat == "🎓 Academic Scholarships":
                render_node("National Scholarship Portal Integration", "Central scholarship platform managing grants.", "Institutional bonafide form, annual gross family income statement", "Register on the live central cloud repository below, map matching criteria, and forward.", "https://scholarships.gov.in")
            if cat == "🚀 Youth Opportunities (New Gen)":
                render_node("Digital India National Internship & Skill Scheme", "Direct access to fully free tech skills training.", "Aadhaar Card, 10th or 12th passing mark sheet", "Click the zero-fee connection node below, sign up for free government certification, and submit your profile instantly.", "https://skillindia.gov.in")
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
