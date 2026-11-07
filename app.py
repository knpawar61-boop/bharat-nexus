import streamlit as st
import random

st.set_page_config(page_title="BHARAT NEXUS | Smart Public Service Bridge", page_icon="🏛️", layout="wide")

# Sophisticated Global CSS Injection
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
    div.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(0, 198, 255, 0.3); }
</style>
""", unsafe_allow_html=True)

if "db_tokens" not in st.session_state:
    st.session_state.db_tokens = {
        "BN-70421": {"name": "Anoop Sharma", "service": "Consular Passport Pipeline", "status": "Ready for Official Submission", "docs": "Aadhaar Card, PAN Card, 10th Certificate"}
    }

with st.sidebar:
    st.markdown("### 🏛️ System Core")
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">MISSION PHILOSOPHY</div><div class="sidebar-name">Service Before Self (₹0 Fee)</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-card"><div class="sidebar-role">INFRASTRUCTURE</div><div class="sidebar-name">Autonomous Public Gateway</div></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("🌐 **Access Mode:** *100% Free & Open*")
    st.markdown("🟢 **Network Engine:** *Operational*")

col_head, col_lang = st.columns()
with col_lang:
    lang = st.selectbox("🌐 Interface Language", ["English", "मराठी (Marathi)"], label_visibility="collapsed")
is_en = (lang == "English")

with col_head:
    title_text = "🏛️ BHARAT NEXUS" if is_en else "🏛️ भारत नेक्सस"
    sub_text = "Smart Public Service Bridge & Autonomous Citizen Scheme Engine" if is_en else "स्मार्ट सार्वजनिक सेवा सेतू आणि स्वायत्त नागरिक योजना केंद्र"
    st.markdown(f'<div class="hero-title">{title_text}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-subtitle">{sub_text}</div>', unsafe_allow_html=True)

banner_html = '<div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; border-radius: 6px; padding: 12px 16px; margin-bottom: 20px; color: #34d399; font-weight: 500; font-size: 0.95rem;">'
if is_en:
    st.markdown(banner_html + "⚙️ **PROD CONFIGURATION:** This ecosystem operates with an absolute zero-fee baseline. No commercial tokens, hidden gateways, or third-party agent layers are attached to processing pipelines.</div>", unsafe_allow_html=True)
else:
    st.markdown(banner_html + "⚙️ **अधिकृत निर्देश:** हे पोर्टल पूर्णपणे विनामूल्य चालते. कोणत्याही स्तरावर अतिरिक्त कमर्शियल शुल्क किंवा एजंट कमिशन समाविष्ट नाही.</div>", unsafe_allow_html=True)

def render_node(title, desc, reqs, steps, deep_url):
    st.markdown(f"#### {title}")
    st.markdown(f"<p style='color:#94a3b8; font-size:0.95rem; margin-top:-5px;'>{desc}</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"**📄 Document Matrix:**\n\n{reqs}")
    with c2:
        st.success(f"**🚀 Execution Workflow:**\n\n{steps}")
    st.link_button("🌐 Initialize Direct Government Pipeline Form", deep_url)
    st.markdown("<hr style='border-color: #1e293b; margin: 20px 0;' />", unsafe_allow_html=True)

t1, t2, t3, t4, t5 = st.tabs([
    "🌐 Government Schemes" if is_en else "🌐 शासकीय योजना",
    "🛂 Passport & Visa Hub" if is_en else "🛂 पासपोर्ट आणि व्हिसा केंद्र",
    "🪪 Citizen Documents" if is_en else "🪪 आवश्यक नागरिक कागदपत्रे",
    "📝 Application Desk" if is_en else "📝 नागरिक अर्ज कक्ष",
    "🔍 Live Tracker & Eligibility" if is_en else "🔍 थेट ट्रॅकर आणि पात्रता"
])

with t1:
    st.subheader("🌐 Live Welfare Registry Node" if is_en else "🌐 थेट शासकीय योजना केंद्र")
    cat = st.radio("Category Router:", ["🌾 Agriculture Node", "🎓 Academic Scholarships", "💼 Industrial Startups", "🏥 Healthcare Core"], horizontal=True, label_visibility="collapsed")
    
    if "Agriculture" in cat:
        render_node("PM-KISAN Financial Support System", "Direct annual cash transfer grid for authenticated agricultural land holders.", "• Aadhaar card with active mobile tie-in\n• Land registry document (7/12 Extract or State Khatauni)\n• Bank passbook mapped to NPCI clearing house", "1. Access the official registration system through our secure routing engine node below.\n2. Key in the Aadhaar baseline info, extract land coordinates, and submit via automated OTP check.", "https://pmkisan.gov.in")
        render_node("Pradhan Mantri Fasal Bima Subsidies", "State-backed financial defense matrix protecting agrarian yield against micro-climate disruptions.", "• System verified Aadhaar card\n• Formal sowing certificate signed by village supervisor\n• Active bank statements", "1. Open the verified state crop insurance ledger link below.\n2. Match coordinates to map yield risks, execute premium share balance, and store configuration.", "https://pmfby.gov.in")
    if "Scholarships" in cat:
        render_node("National Scholarship Portal Integration", "Central administrative platform managing performance grants for active academic candidates.", "• Standard institutional bonafide clearance form\n• Verified household annual gross revenue report\n• Previous academic milestone scorecards", "1. Secure your One-Time Token (OTR) profile on the live central cloud repository below.\n2. Pinpoint target scheme based on baseline criteria, mount proofs, and forward to college panel.", "https://scholarships.gov.in")
    if "Industrial" in cat:
        render_node("Udyam National Enterprise System", "Instant government framework granting statutory legal status and tender advantages to micro-businesses.", "• Executive identity card (PAN)\n• Primary system holder Aadhaar\n• Bank transaction matrix details", "1. Launch the legal federal industry registration platform below.\n2. Complete data validation fields via double OTP check, download enterprise certificate instantly.", "https://udyamregistration.gov.in")
    if "Healthcare" in cat:
        render_node("Ayushman Bharat Cloud Health System", "Statutory medical protection system guaranteeing ₹5,000,000 coverage across associated private medical nodes.", "• Active identity baseline data\n• Official civil supply index card (Ration Card)", "1. Verify network status on the national healthcare matrix page below via biometric OTP check.\n2. Download secure golden verification passport instantly.", "https://nha.gov.in")

with t2:
    st.subheader("🛂 Consular, Passport & Global Entry Portal" if is_en else "🛂 पासपोर्ट आणि व्हिसा विभाग")
    pv = st.selectbox("Consular Track:", ["📘 Fresh Indian Passport Protocol", "🔄 Passport Re-Issue & Updates", "🛡️ Police Clearance Certificate Node", "✈️ International Entry Visa Setup", "🇮🇳 Electronic India Entry Visa (Inbound)"])
    
    st.markdown(f'<div class="info-box"><b>🔧 Transaction Config:</b> 100% Secure MEA Node | <b>💳 Cost Metric:</b> ₹0 Portal Surcharge</div>', unsafe_allow_html=True)
    
    if "Fresh" in pv or "Re-Issue" in pv:
        render_node("Ministry of External Affairs Passport Issuance System", "Official legal framework routing biometric information directly to the Regional Passport Officer network.", "• Universal residency verification (Aadhaar, Voter ID, or Active utilities statement)\n• Valid legal age baseline documentation (PAN, Matriculation verification document, or Birth record)\n• Non-ECR authentication matrix certificate", "1. Engage the official server page below to establish a clean login state.\n2. Deploy form details, wire standard legal fees securely via digital banking, and reserve biometric capture slot at closest PSK.", "https://passportindia.gov.in")
    if "PCC" in pv or "Police" in pv:
        render_node("Police Clearance Certificate (PCC) Issuance Node", "Statutory background validation for employment or immigration pathways.", "• Original valid Indian Passport asset\n• Address confirmation and corporate placement documentation", "1. Activate application ledger link below.\n2. Schedule biometric verification window, execute local dispatch check, and generate verification pass.", "https://passportindia.gov.in")
    if "International" in pv:
        render_node("VFS Global Sovereign Appointment Manager", "Direct channel connecting citizen profiles to individual foreign consulates and secure biometric validation facilities.", "• Valid passport data matrix with minimum two blank leaves remaining\n• Verified 6 months clean capital account banking records and tax evaluation history\n• Valid structural proof of accommodation matching global travel regulations", "1. Initialize the official route pipeline below, select destination country profile, and map processing specifications.\n2. Set processing timeline parameters, mount financial proofs, and schedule biometric handshakes.", "https://vfsglobal.com")
    if "Electronic" in pv:
