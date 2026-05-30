import streamlit as st
import time
from pipeline import run_search_agent

st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>
    /* Light lavender background */
    .stApp {
        background-color: #F0EEFF !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #F0EEFF !important;
    }
    [data-testid="stHeader"] {
        background-color: #F0EEFF !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #E4DEFF !important;
    }

    /* Hide default streamlit elements */
    #MainMenu, footer, header { visibility: hidden; }

    /* Main header card */
    .main-header {
        background-color: #F5F3E7;
        border-radius: 20px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid #E8E4D0;
    }
    .main-header .badge {
        display: inline-block;
        background: #EEEDFE;
        color: #534AB7;
        border-radius: 20px;
        padding: 5px 16px;
        font-size: 13px;
        margin-bottom: 14px;
        border: 1px solid #C9BFFF;
    }
    .main-header h1 {
        color: #1a1a2e;
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .main-header p {
        color: #555;
        font-size: 1rem;
    }

    /* Topic tags */
    .tag-row {
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
        margin-top: 10px;
        margin-bottom: 1.5rem;
    }
    .tag {
        background: #FFFFFF;
        border: 1px solid #ddd;
        border-radius: 20px;
        padding: 6px 16px;
        font-size: 13px;
        color: #444;
        cursor: pointer;
    }

    /* Agent cards */
    .agents-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 1.2rem 1.3rem;
        border: 1px solid #e8e8e8;
    }
    .agent-icon {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-bottom: 12px;
    }
    .agent-card h3 {
        font-size: 14px;
        font-weight: 600;
        color: #222;
        margin-bottom: 4px;
    }
    .agent-card p {
        font-size: 12px;
        color: #888;
        line-height: 1.5;
    }
    .dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #ccc;
        margin-right: 6px;
        vertical-align: middle;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: #aaa;
        font-size: 15px;
    }
    .empty-state .icon {
        font-size: 40px;
        margin-bottom: 12px;
    }

    /* Result cards */
    .result-card {
        background: #FFFFFF;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        border: 1px solid #e0d9ff;
        margin-bottom: 1rem;
    }
    .result-card.highlight {
        border: 2px solid #534AB7;
    }
    .result-card h4 {
        color: #3C3489;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .result-card pre {
        white-space: pre-wrap;
        font-size: 13px;
        color: #444;
        line-height: 1.7;
        font-family: inherit;
    }

    /* Score badge */
    .score-badge {
        display: inline-block;
        background: #EAF3DE;
        color: #3B6D11;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Button style */
    .stButton > button {
        background-color: #534AB7 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.55rem 2rem !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        background-color: #3C3489 !important;
    }

    /* Text input */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 1px solid #ddd !important;
        background: #FFFFFF !important;
        padding: 0.65rem 1rem !important;
        font-size: 15px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #534AB7 !important;
        box-shadow: 0 0 0 2px #EEEDFE !important;
    }
</style>
""", unsafe_allow_html=True)


# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="badge">□ Multi-Agent System</div>
    <h1>Research Assistant</h1>
    <p>Powered by LangGraph + Groq · Search · Scrape · Write · Critique</p>
    <p>-Lakshit likhar </p>
</div>
""", unsafe_allow_html=True)


# ── Topic Input ───────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([5, 1])
with col_input:
    topic = st.text_input(
        "Research topic",
        label_visibility="collapsed",
        placeholder="Enter a research topic e.g. Quantum Computing...",
        value=st.session_state.get("topic", "")
    )
with col_btn:
    run = st.button("Research")

# Quick topic tags
st.markdown("""
<div class="tag-row">
    <span class="tag">AI trends</span>
    <span class="tag">Climate change</span>
    <span class="tag">Narendra Modi</span>
    <span class="tag">Space exploration</span>
</div>
""", unsafe_allow_html=True)


# ── Agent Cards ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="agents-grid">
    <div class="agent-card">
        <div class="agent-icon" style="background:#EEEDFE;">🔍</div>
        <h3><span class="dot"></span>Search Agent</h3>
        <p>Finds recent web results via Tavily</p>
    </div>
    <div class="agent-card">
        <div class="agent-icon" style="background:#E1F5EE;">📄</div>
        <h3><span class="dot"></span>Reader Agent</h3>
        <p>Scrapes and extracts page content</p>
    </div>
    <div class="agent-card">
        <div class="agent-icon" style="background:#FAECE7;">✍️</div>
        <h3><span class="dot"></span>Writer Chain</h3>
        <p>Generates structured research report</p>
    </div>
    <div class="agent-card">
        <div class="agent-icon" style="background:#FAEEDA;">⭐</div>
        <h3><span class="dot"></span>Critic Chain</h3>
        <p>Reviews and scores the report</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Run Pipeline ──────────────────────────────────────────────────────────────
if run and topic.strip():
    progress = st.progress(0, text="Starting pipeline...")

    try:
        state = run_search_agent(topic)

        progress.progress(100, text="Done!")

        # Search Result
        with st.expander("🔍 Search Results", expanded=False):
            st.markdown(f"""<div class="result-card"><pre>{state.get('search_result','')}</pre></div>""", unsafe_allow_html=True)

        # Scraped Content
        with st.expander("📄 Scraped Content", expanded=False):
            st.markdown(f"""<div class="result-card"><pre>{state.get('scraped_content','')}</pre></div>""", unsafe_allow_html=True)

        # Report
        with st.expander("✍️ Research Report", expanded=True):
            st.markdown(f"""<div class="result-card highlight"><pre>{state.get('report','')}</pre></div>""", unsafe_allow_html=True)
            st.download_button(
                label="⬇️ Download Report",
                data=state.get('report', ''),
                file_name=f"report_{topic[:30].replace(' ','_')}.txt",
                mime="text/plain"
            )

        # Critic
        with st.expander("⭐ Critic Feedback", expanded=True):
            feedback = state.get('feedback', '')
            score_line = [l for l in feedback.split('\n') if 'Score' in l]
            if score_line:
                st.markdown(f'<div class="score-badge">{score_line[0]}</div>', unsafe_allow_html=True)
            st.markdown(f"""<div class="result-card"><pre>{feedback}</pre></div>""", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

elif run and not topic.strip():
    st.warning("⚠️ Please enter a research topic.")

else:
    st.markdown("""
    <div class="empty-state">
        <div class="icon">🔎</div>
        Enter a topic above and click Research to begin
    </div>
    """, unsafe_allow_html=True)