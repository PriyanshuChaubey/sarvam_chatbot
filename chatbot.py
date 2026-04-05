import os
import re
import streamlit as st
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()
client = SarvamAI(api_subscription_key=os.environ["SARVAM_API_KEY"])

st.set_page_config(
    page_title="Sarvam AI • Indian Language Chatbot",
    page_icon="🪔",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Plus+Jakarta+Sans:wght@400;500;600&family=Tiro+Devanagari+Hindi&display=swap');

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }

.stApp {
    background-color: #fdfaf5;
    background-image:
        radial-gradient(ellipse at 0% 0%, rgba(255,153,51,0.12) 0%, transparent 55%),
        radial-gradient(ellipse at 100% 0%, rgba(19,136,8,0.09) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 100%, rgba(255,153,51,0.08) 0%, transparent 50%);
    min-height: 100vh;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; padding-bottom: 2rem !important; max-width: 800px !important; }

.hero {
    background: linear-gradient(135deg, #0d3b1e 0%, #1a5e2f 40%, #0d3b1e 100%);
    border-radius: 0 0 40px 40px;
    padding: 3rem 2rem 2.2rem;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(13,59,30,0.25);
}
.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 5px;
    background: linear-gradient(90deg, #FF9933 33.3%, #ffffff 33.3% 66.6%, #138808 66.6%);
}
.hero-diya { font-size: 3rem; display: block; margin-bottom: 0.6rem; }
.hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
    color: #ffffff;
    margin: 0 0 0.3rem;
    text-shadow: 0 2px 20px rgba(0,0,0,0.3);
}
.hero-devanagari {
    font-family: 'Tiro Devanagari Hindi', serif;
    font-size: 1.05rem;
    color: #a3e4b0;
    display: block;
    margin-bottom: 1rem;
}
.hero-tags { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; }
.hero-tag {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: rgba(255,255,255,0.75);
    padding: 4px 14px;
    border-radius: 30px;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.hero-tag.saffron {
    background: rgba(255,153,51,0.15);
    border-color: rgba(255,153,51,0.35);
    color: #ffc280;
}

.lang-badge-wrap { text-align: center; margin: -0.5rem 0 1.2rem; }
.lang-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: #fff;
    border: 1.5px solid #138808;
    color: #0d3b1e;
    padding: 6px 18px;
    border-radius: 40px;
    font-size: 0.78rem;
    font-weight: 600;
    box-shadow: 0 3px 12px rgba(19,136,8,0.12);
}

.tricolor-divider {
    height: 3px;
    border-radius: 3px;
    background: linear-gradient(90deg, #FF9933 0% 33%, #f0f0f0 33% 66%, #138808 66% 100%);
    margin: 1.2rem 0;
    opacity: 0.55;
}

.chat-card {
    background: #ffffff;
    border-radius: 28px;
    padding: 1.8rem;
    margin-bottom: 1.2rem;
    border: 1px solid rgba(19,136,8,0.1);
    box-shadow: 0 4px 6px rgba(0,0,0,0.02), 0 12px 40px rgba(0,0,0,0.06);
    min-height: 200px;
}

.empty-state { text-align: center; padding: 3rem 1rem 2rem; }
.empty-icon { font-size: 3.5rem; display: block; margin-bottom: 1rem; }
.empty-state h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.5rem; color: #1a3a2a; margin-bottom: 0.4rem;
}
.empty-state p { color: #8a9e8f; font-size: 0.88rem; margin-bottom: 1.2rem; }
.chip-row { display: flex; flex-wrap: wrap; gap: 7px; justify-content: center; }
.chip {
    background: #f0faf2; border: 1px solid #a8d5b0;
    color: #1a5e2f; padding: 5px 14px;
    border-radius: 30px; font-size: 0.75rem; font-weight: 500;
}

.msg-block-user { margin: 14px 0; overflow: hidden; }
.msg-block-bot  { margin: 14px 0; overflow: hidden; }
.msg-meta { font-size: 0.68rem; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase; margin-bottom: 4px; }
.msg-meta-user { text-align: right; color: #aab4ae; }
.msg-meta-bot  { color: #138808; }

.bubble-user {
    background: linear-gradient(135deg, #1a5e2f 0%, #138808 100%);
    color: #ffffff;
    padding: 13px 18px;
    border-radius: 22px 22px 5px 22px;
    display: inline-block;
    float: right;
    max-width: 78%;
    font-size: 0.95rem;
    line-height: 1.65;
    box-shadow: 0 6px 20px rgba(19,136,8,0.25);
}
.bubble-bot {
    background: #f5fbf6;
    border: 1.5px solid #c8eacc;
    color: #0d2d17;
    padding: 13px 18px;
    border-radius: 22px 22px 22px 5px;
    display: inline-block;
    float: left;
    max-width: 78%;
    font-size: 0.95rem;
    line-height: 1.65;
    box-shadow: 0 4px 16px rgba(19,136,8,0.07);
}
.clearfix::after { content: ''; display: table; clear: both; }

/* Input */
.stTextInput > div > div {
    background: #ffffff !important;
    border: 2px solid #c8eacc !important;
    border-radius: 22px !important;
    padding: 4px 12px !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.07) !important;
}
.stTextInput > div > div:focus-within {
    border-color: #138808 !important;
    box-shadow: 0 4px 24px rgba(19,136,8,0.15) !important;
}
.stTextInput > div > div > input {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #111111 !important;
    font-size: 0.97rem !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    padding: 6px 4px !important;
}
.stTextInput > div > div > input::placeholder { color: #b0c9b5 !important; font-style: italic; }
.stTextInput > div { border: none !important; box-shadow: none !important; }

/* Send button — saffron */
.stButton > button {
    background: linear-gradient(135deg, #FF9933, #e07b10) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 16px !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    padding: 13px 20px !important;
    width: 100% !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    box-shadow: 0 4px 18px rgba(255,153,51,0.4) !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(255,153,51,0.5) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fafdf8 !important;
    border-right: 2px solid #d4edda !important;
}
section[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: 'Cormorant Garamond', serif !important;
    color: #0d3b1e !important;
    font-size: 1.2rem !important;
}
section[data-testid="stSidebar"] .stMarkdown p {
    color: #5a7a60 !important;
    font-size: 0.82rem !important;
}
section[data-testid="stSidebar"] .stButton > button {
    background: #ffffff !important;
    color: #1a5e2f !important;
    border: 1.5px solid #a8d5b0 !important;
    border-radius: 12px !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    box-shadow: none !important;
    padding: 8px 14px !important;
    transition: all 0.15s !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: #138808 !important;
    color: #fff !important;
    border-color: #138808 !important;
    transform: none !important;
}
.active-lang-btn > button {
    background: #138808 !important;
    color: #fff !important;
    border-color: #138808 !important;
}
.sidebar-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #FF9933 50%, transparent);
    margin: 1rem 0; border-radius: 2px; opacity: 0.5;
}

.footer {
    text-align: center; margin-top: 1.5rem; padding-bottom: 1rem;
    font-size: 0.75rem; color: #9aad9e;
}
.footer b { color: #138808; }
.footer .made { color: #FF9933; }
</style>
""", unsafe_allow_html=True)

# ── Language map ──────────────────────────────────────────────
LANGUAGE_NAMES = {
    "hi-IN": "Hindi 🇮🇳", "ta-IN": "Tamil 🌴", "te-IN": "Telugu",
    "ml-IN": "Malayalam", "kn-IN": "Kannada", "bn-IN": "Bengali",
    "mr-IN": "Marathi", "gu-IN": "Gujarati", "pa-IN": "Punjabi",
    "od-IN": "Odia", "as-IN": "Assamese", "ur-IN": "Urdu", "en-IN": "English 🌐"
}

LANG_OPTIONS = {
    "Hindi 🇮🇳": "hi-IN", "Tamil 🌴": "ta-IN", "Telugu": "te-IN",
    "Malayalam": "ml-IN", "Kannada": "kn-IN", "Bengali": "bn-IN",
    "Marathi": "mr-IN", "Gujarati": "gu-IN", "Punjabi": "pa-IN",
    "Odia": "od-IN", "Assamese": "as-IN", "Urdu": "ur-IN", "English 🌐": "en-IN"
}

# ── Session state ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_lang" not in st.session_state:
    st.session_state.last_lang = None
if "forced_lang" not in st.session_state:
    st.session_state.forced_lang = None
if "forced_lang_name" not in st.session_state:
    st.session_state.forced_lang_name = None
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# ── Helper functions ──────────────────────────────────────────
def detect_language(text: str) -> str:
    try:
        response = client.text.identify_language(input=text)
        return response.language_code
    except Exception:
        return "hi-IN"

def clean_reply(text: str) -> str:
    """Remove any thinking/reasoning paragraphs — keep only the actual answer."""
    # Remove <think>...</think> blocks
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    # If reply has multiple paragraphs and first one looks like reasoning, drop it
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    # Find first line that looks like actual answer (not "The user is..." etc.)
    skip_patterns = [
        "the user", "i should", "let me", "i need to", "i'll", "i will",
        "so i", "they want", "they asked", "they are", "they said",
        "according to", "based on", "note that", "it seems"
    ]
    final_lines = []
    found_answer = False
    for line in lines:
        lower = line.lower()
        is_reasoning = any(p in lower for p in skip_patterns)
        if not is_reasoning:
            found_answer = True
        if found_answer:
            final_lines.append(line)
    result = '\n'.join(final_lines).strip()
    return result if result else text

def get_ai_reply(user_message: str, lang_name: str) -> str:
    """Call Sarvam AI and return clean reply."""
    system = {
        "role": "system",
        "content": f"""You are a friendly Indian language chatbot called Sarvam.
Reply ONLY in {lang_name}. Use proper {lang_name} script.
STRICT: Output ONLY the answer. No thinking. No reasoning. No explanation of what you are doing.
Remember everything the user has said in this conversation."""
    }

    # Build history from messages
    history = []
    for msg in st.session_state.messages[-16:]:
        role = "user" if msg["role"] == "user" else "assistant"
        history.append({"role": role, "content": msg["content"]})

    # Add current message
    history.append({"role": "user", "content": user_message})

    # Ensure alternating turns
    clean = []
    for msg in history:
        if clean and clean[-1]["role"] == msg["role"]:
            clean[-1]["content"] = msg["content"]  # overwrite duplicate
        else:
            clean.append(msg)

    # Must start with user
    if clean and clean[0]["role"] != "user":
        clean = clean[1:]

    response = client.chat.completions(
        model="sarvam-m",
        messages=[system] + clean
    )
    return clean_reply(response.choices[0].message.content)

# ── Sidebar ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌐 Choose Language")
    st.markdown("Force bot to reply in a specific language:")
    st.markdown("")

    for label, code in LANG_OPTIONS.items():
        is_active = st.session_state.forced_lang == code
        btn_label = f"✅ {label}" if is_active else label
        if st.button(btn_label, key=f"sb_{code}", use_container_width=True):
            if is_active:
                # Toggle off
                st.session_state.forced_lang = None
                st.session_state.forced_lang_name = None
            else:
                st.session_state.forced_lang = code
                st.session_state.forced_lang_name = label.split(" ")[0]
            st.rerun()

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    if st.session_state.forced_lang:
        st.success(f"🔒 Locked: **{st.session_state.forced_lang_name}**\nClick again to unlock")
    else:
        st.info("🔍 Auto-detecting language")

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown("### ℹ️ How it works")
    st.markdown("Type in any Indian language — bot auto-detects and replies in the same language. Click a language above to force a specific one.")
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_lang = None
        st.session_state.forced_lang = None
        st.session_state.forced_lang_name = None
        st.session_state.input_key += 1
        st.rerun()

# ── Hero ──────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <span class="hero-diya">🪔</span>
    <h1>Indian Language Chatbot</h1>
    <span class="hero-devanagari">भारतीय भाषाओं में बात करें • बोलो अपनी भाषा में</span>
    <div class="hero-tags">
        <span class="hero-tag saffron">🔶 Sarvam AI</span>
        <span class="hero-tag">🇮🇳 13 Languages</span>
        <span class="hero-tag">⚡ Auto Detect</span>
        <span class="hero-tag">🧠 Memory Enabled</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Language badge ────────────────────────────────────────────
if st.session_state.forced_lang:
    name = st.session_state.forced_lang_name
    st.markdown(f'<div class="lang-badge-wrap"><span class="lang-badge">🔒 Forced: {name}</span></div>', unsafe_allow_html=True)
elif st.session_state.last_lang:
    lang_display = LANGUAGE_NAMES.get(st.session_state.last_lang, "Hindi")
    st.markdown(f'<div class="lang-badge-wrap"><span class="lang-badge">🔍 Detected: {lang_display}</span></div>', unsafe_allow_html=True)

st.markdown('<div class="tricolor-divider"></div>', unsafe_allow_html=True)

# ── Chat messages ─────────────────────────────────────────────
if not st.session_state.messages:
    chat_html = """
    <div class="chat-card">
        <div class="empty-state">
            <span class="empty-icon">🙏</span>
            <h3>Namaste! Start your conversation</h3>
            <p>Type in any Indian language — I'll detect and reply automatically</p>
            <div class="chip-row">
                <span class="chip">🇮🇳 Hindi</span>
                <span class="chip">🌴 Tamil</span>
                <span class="chip">⭐ Telugu</span>
                <span class="chip">🌊 Malayalam</span>
                <span class="chip">🏰 Kannada</span>
                <span class="chip">🌸 Bengali</span>
                <span class="chip">🌾 Punjabi</span>
                <span class="chip">🌐 English</span>
            </div>
        </div>
    </div>"""
else:
    msgs_html = ""
    for msg in st.session_state.messages:
        content = msg["content"].replace("<", "&lt;").replace(">", "&gt;")
        if msg["role"] == "user":
            msgs_html += f"""
            <div class="msg-block-user">
                <div class="msg-meta msg-meta-user">You</div>
                <div class="clearfix"><div class="bubble-user">{content}</div></div>
            </div>"""
        else:
            msgs_html += f"""
            <div class="msg-block-bot">
                <div class="msg-meta msg-meta-bot">🪔 Sarvam AI</div>
                <div class="clearfix"><div class="bubble-bot">{content}</div></div>
            </div>"""
    chat_html = f'<div class="chat-card">{msgs_html}</div>'

st.markdown(chat_html, unsafe_allow_html=True)

st.markdown('<div class="tricolor-divider"></div>', unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        label="message",
        placeholder="यहाँ टाइप करें... | Type here in any language...",
        label_visibility="collapsed",
        key=f"user_input_{st.session_state.input_key}"
    )
with col2:
    send = st.button("Send 🚀")

# ── Handle send ───────────────────────────────────────────────
if send and user_input.strip():
    with st.spinner("🪔 सोच रहा हूँ..."):
        # Determine language
        if st.session_state.forced_lang:
            lang_code = st.session_state.forced_lang
            lang_name = st.session_state.forced_lang_name
        else:
            lang_code = detect_language(user_input)
            lang_name = LANGUAGE_NAMES.get(lang_code, "Hindi").split(" ")[0]

        reply = get_ai_reply(user_input, lang_name)

    st.session_state.last_lang = lang_code
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.input_key += 1
    st.rerun()

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <span class="made">Made with ❤️</span> using <b>Sarvam AI</b> &nbsp;•&nbsp; भारत की अपनी AI &nbsp;•&nbsp; 🇮🇳
</div>
""", unsafe_allow_html=True)