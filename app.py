import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="PhishNet",
    page_icon="🎣",
    layout="wide"
)

# -----------------------------
# CONFIG
# -----------------------------
GITHUB_URL = "https://github.com/ameyer135/ds-210-2026-spring-scam-ham"

NAV_ITEMS = [
    "Home",
    "Motivation",
    "Demo",
    "Data",
    "Architecture",
    "Methodology",
    "About Us",
    "GitHub",
]

# -----------------------------
# HELPERS
# -----------------------------
def img_to_base64(path_str: str) -> str:
    path = Path(path_str)
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode()

def section_eyebrow(text: str):
    st.markdown(f'<div class="section-eyebrow">{text}</div>', unsafe_allow_html=True)

def section_title(text: str):
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)

def section_body(text: str):
    st.markdown(f'<div class="section-body">{text}</div>', unsafe_allow_html=True)

def render_card(title: str, body_html: str):
    st.markdown(
        f"""
        <div class="content-card">
            <div class="card-title">{title}</div>
            <div class="card-body">{body_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def render_team_card(name: str, image_path: str, linkedin_url: str):
    encoded = img_to_base64(image_path)
    if encoded:
        image_html = f'<img class="team-photo" src="data:image/png;base64,{encoded}" alt="{name}"/>'
    else:
        image_html = '<div class="team-photo team-photo-placeholder"></div>'

    st.markdown(
        f"""
        <div class="team-card">
            {image_html}
            <div class="team-name">{name}</div>
            <a href="{linkedin_url}" target="_blank" class="linkedin-link" aria-label="{name} LinkedIn">
                <svg class="linkedin-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M4.98 3.5C4.98 4.88 3.87 6 2.49 6S0 4.88 0 3.5 1.11 1 2.49 1s2.49 1.12 2.49 2.5zM.5 8h4V24h-4V8zm7 0h3.83v2.19h.05c.53-1.01 1.84-2.08 3.79-2.08 4.05 0 4.8 2.67 4.8 6.13V24h-4v-7.35c0-1.75-.03-4-2.44-4-2.44 0-2.81 1.9-2.81 3.87V24h-4V8z"/>
                </svg>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# STYLES
# -----------------------------
st.markdown("""
<style>
:root {
    --navy-1: #07111F;
    --navy-2: #0B1E33;
    --navy-3: #14314D;
    --aqua: #82dacb;
    --teal: #5ED3C6;
    --text: #F6F8FB;
    --muted: #C9D5E3;
    --line: rgba(255,255,255,0.08);
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 15% 18%, rgba(130, 218, 203, 0.16), transparent 28%),
        radial-gradient(circle at 84% 18%, rgba(95, 132, 174, 0.22), transparent 30%),
        radial-gradient(circle at 50% 88%, rgba(130, 218, 203, 0.10), transparent 28%),
        linear-gradient(160deg, var(--navy-1) 0%, var(--navy-2) 48%, var(--navy-3) 100%);
    color: var(--text);
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1240px;
    padding-top: 0.55rem !important;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    letter-spacing: -0.02em;
}

p, li {
    font-size: 1.03rem;
    line-height: 1.7;
}

a {
    text-decoration: none !important;
}

/* nav */
.nav-shell {
    position: sticky;
    top: 0.5rem;
    z-index: 999;
    margin-bottom: 1.2rem;
    background: rgba(8, 19, 34, 0.62);
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border-radius: 999px;
    padding: 0.35rem 0.8rem 0.15rem 0.8rem;
    box-shadow: 0 14px 40px rgba(0,0,0,0.18);
}

div[data-testid="stRadio"] > div {
    gap: 0.5rem;
}

div[role="radiogroup"] {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

div[role="radiogroup"] label {
    background: transparent;
    border: 1px solid transparent;
    border-radius: 999px;
    padding: 0.55rem 0.95rem;
    margin: 0 !important;
    color: var(--text) !important;
    font-weight: 600;
    transition: all 0.18s ease;
}

div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.06);
    color: var(--aqua) !important;
}

div[role="radiogroup"] label:has(input:checked) {
    background: rgba(130, 218, 203, 0.16);
    color: var(--aqua) !important;
    border-color: rgba(130, 218, 203, 0.24);
}

div[role="radiogroup"] label p {
    margin: 0;
    font-size: 0.98rem !important;
}

/* hero */
.hero-shell {
    min-height: 28vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding-top: 0.2rem;
}

.hero-logo-wrap {
    display: flex;
    justify-content: center;
    align-items: flex-start;
}

.hero-logo-card {
    background: rgba(255,255,255,0.035);
    border: 1px solid var(--line);
    border-radius: 28px;
    padding: 18px;
    backdrop-filter: blur(8px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.18);
}

.hero-copy {
    text-align: left;
    padding-top: 0.1rem;
}

.hero-title {
    font-size: 4.2rem;
    font-weight: 800;
    line-height: 1.0;
    margin-bottom: 0.7rem;
    letter-spacing: -0.04em;
}

.hero-title .accent {
    color: var(--aqua);
}

.hero-tagline {
    font-size: 1.35rem;
    font-weight: 600;
    color: var(--muted);
    margin-bottom: 1rem;
}

.hero-body {
    font-size: 1.16rem;
    color: #e7edf5;
    max-width: 760px;
    line-height: 1.8;
}

.hero-footer {
    margin-top: 1.3rem;
    color: var(--muted);
    font-size: 0.98rem;
}

.section-wrap {
    margin-top: 0.2rem;
}

.section-eyebrow {
    color: var(--teal);
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.section-title {
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.08;
    margin-bottom: 1rem;
    letter-spacing: -0.03em;
}

.section-body {
    color: var(--muted);
    font-size: 1.12rem;
    max-width: 980px;
    margin-bottom: 1.2rem;
}

.content-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 1.3rem 1.35rem;
    backdrop-filter: blur(8px);
    box-shadow: 0 16px 32px rgba(0,0,0,0.16);
    height: 100%;
}

.card-title {
    font-size: 1.28rem;
    font-weight: 800;
    margin-bottom: 0.7rem;
}

.card-body {
    color: var(--muted);
    font-size: 1rem;
    line-height: 1.75;
}

.card-body ul {
    padding-left: 1.1rem;
    margin: 0.2rem 0 0 0;
}

.card-body li {
    margin-bottom: 0.45rem;
}

.metric-row {
    margin-top: 1rem;
}

[data-testid="metric-container"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.055), rgba(255,255,255,0.03));
    border: 1px solid var(--line);
    padding: 18px;
    border-radius: 20px;
    box-shadow: 0 16px 32px rgba(0,0,0,0.12);
}

.arch-img img, .method-img img {
    border-radius: 20px;
    border: 1px solid var(--line);
    box-shadow: 0 20px 36px rgba(0,0,0,0.18);
}

.team-card {
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 1.6rem 1rem 1.3rem 1rem;
    text-align: center;
    min-height: 290px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    box-shadow: 0 16px 32px rgba(0,0,0,0.14);
}

.team-photo {
    width: 124px;
    height: 124px;
    object-fit: cover;
    border-radius: 999px;
    border: 3px solid rgba(255,255,255,0.14);
    display: block;
    margin: 0 auto 14px auto;
}

.team-photo-placeholder {
    background: rgba(255,255,255,0.06);
}

.team-name {
    font-size: 1.1rem;
    font-weight: 800;
    text-align: center;
    margin-top: 2px;
}

.linkedin-link {
    margin-top: 12px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 999px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.09);
    color: #d8eeff;
    text-decoration: none;
    transition: transform 0.15s ease, background 0.15s ease, color 0.15s ease;
}

.linkedin-link:hover {
    background: rgba(130, 218, 203, 0.18);
    color: var(--aqua);
    transform: translateY(-1px);
}

.linkedin-icon {
    width: 18px;
    height: 18px;
    display: block;
}

.github-box {
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.03));
    border: 1px solid var(--line);
    border-radius: 22px;
    padding: 1.4rem;
    box-shadow: 0 16px 32px rgba(0,0,0,0.14);
}

.github-link {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    color: var(--text);
    background: rgba(255,255,255,0.06);
    border: 1px solid var(--line);
    padding: 0.9rem 1.1rem;
    border-radius: 999px;
    font-weight: 700;
    margin-top: 0.6rem;
}

.github-link:hover {
    color: var(--aqua);
    background: rgba(130, 218, 203, 0.12);
}

@media (max-width: 900px) {
    .hero-title {
        font-size: 3.2rem;
    }
    .hero-copy {
        text-align: center;
        padding-top: 0;
    }
    .hero-body {
        margin: 0 auto;
    }
    .hero-shell {
        min-height: 24vh;
        padding-top: 0;
    }
}

@media (max-width: 640px) {
    .section-title {
        font-size: 2.2rem;
    }
    .hero-title {
        font-size: 2.7rem;
    }
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TOP NAVIGATION - SAME PAGE
# -----------------------------
nav_container = st.container()
with nav_container:
    st.markdown('<div class="nav-shell">', unsafe_allow_html=True)
    page = st.radio(
        "Navigation",
        NAV_ITEMS,
        horizontal=True,
        label_visibility="collapsed",
        key="top_nav",
    )
    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# PAGE CONTENT
# -----------------------------
if page == "Home":
    left, right = st.columns([0.9, 1.6], gap="large")
    with left:
        st.markdown('<div class="hero-shell"><div class="hero-logo-wrap"><div class="hero-logo-card">', unsafe_allow_html=True)
        st.image("assets/logo.png", width=280)
        st.markdown('</div></div></div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="hero-shell"><div class="hero-copy">', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Phish<span class="accent">Net</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-tagline">Clear. Real-time. Scam detection inside Gmail.</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="hero-body">
            PhishNet is a Chrome extension that helps users identify phishing emails in real time.
            Instead of relying on black-box spam filters, it explains why a message is risky and helps users make informed decisions with confidence.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="hero-footer">UC Berkeley MIDS Capstone • Spring 2026 Section 3</div>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

elif page == "Motivation":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Motivation")
    section_title("Existing tools leave users guessing")
    section_body(
        "Email scams are becoming increasingly sophisticated, especially for older adults who face disproportionate financial and emotional harm."
    )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        render_card(
            "Where current tools fail",
            """
            <ul>
                <li>They provide binary classifications with no explanation</li>
                <li>They rely on static patterns that fail on modern scams</li>
                <li>They do not help users understand why something is risky</li>
            </ul>
            """
        )
    with c2:
        render_card(
            "The transparency gap",
            """
            Users are forced to rely on intuition at exactly the moment scams are most convincing.
            PhishNet is built to close that gap with clear, plain-language guidance.
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Demo":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Demo")
    section_title("What the product experience looks like")
    section_body(
        "PhishNet runs directly inside Gmail. Emails are labeled automatically, and opening a message shows the risk level and explanation."
    )

    demo_left, demo_right = st.columns([1.7, 1], gap="large")
    with demo_left:
        st.video("https://www.youtube.com/watch?v=y5IShB9ihds&list=PLhMnuBfGeCDPtyC9kUf_hG_QwjYzZ0Am1")
    with demo_right:
        render_card(
            "User workflow",
            """
            <ul>
                <li>Email arrives in Gmail</li>
                <li>PhishNet assigns a risk label</li>
                <li>User opens the email and sees the explanation</li>
                <li>User decides whether to trust, ignore, or escalate</li>
            </ul>
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Data":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Data")
    section_title("Grounded in real scam patterns")
    section_body(
        "PhishNet combines retrieval-based context with structured storage so the system can generalize beyond simple keywords."
    )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        render_card(
            "Retrieval and grounding",
            """
            <ul>
                <li>AARP scam content is stored in S3</li>
                <li>Documents are embedded into a vector store</li>
                <li>Relevant context is retrieved during scoring</li>
                <li>This improves generalization beyond static keywords</li>
            </ul>
            """
        )
    with c2:
        render_card(
            "State and synchronization",
            """
            <ul>
                <li>DynamoDB stores scores, reasons, and user settings</li>
                <li>Gmail labels reflect risk status directly in the inbox</li>
                <li>Pub/Sub notifications keep incoming messages in sync</li>
                <li>The system stays current as new emails arrive</li>
            </ul>
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Architecture":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Architecture")
    section_title("End-to-end system for real-time scam detection")
    section_body(
        "PhishNet is built as a lightweight Chrome extension backed by a scalable cloud pipeline for scoring and explanation."
    )

    c1 = st.columns(1)[0]
    with c1:
        render_card(
            "System overview",
            """
            <ul>
                <li>Chrome extension reads Gmail threads in real time</li>
                <li>Requests are sent to a FastAPI backend on AWS App Runner</li>
                <li>Backend scores emails using Amazon Bedrock</li>
                <li>Results are returned to the Gmail UI in real time</li>
            </ul>
            """
        )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="arch-img">', unsafe_allow_html=True)
    st.image("assets/infra1.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    c2 = st.columns(1)[0]
    with c2:
        render_card(
            "Application stack",
            """
            <ul>
                <li>FastAPI service running on App Runner</li>
                <li>Gmail labels and Pub/Sub notifications keep state synchronized</li>
                <li>DynamoDB stores scores, reasons, and user settings</li>
                <li>S3 stores supporting scam knowledge content</li>
            </ul>
            """
        )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="arch-img">', unsafe_allow_html=True)
    st.image("assets/infra2.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Methodology":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Methodology")
    section_title("How the modeling approach evolved")

    section_body(
        "We evaluated a progression of approaches, starting with traditional feature-based models, then moving to full-email LLM classification, and finally to a retrieval-augmented framework grounded in known scam examples. The image below summarizes that progression and the tradeoffs that led us to the final approach."
    )

    st.markdown('<div class="method-img">', unsafe_allow_html=True)
    st.image("assets/modeling_approaches.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    section_body(
        "We evaluated GPT-4o-mini, Claude Haiku, Nova Lite, and Nova Pro using a two-step pipeline on ~800–1,000 emails. Nova Pro performed best, achieving 96% accuracy and 100% phishing recall with few-shot examples and retrieval of the top 3 similar scams. These metrics validate classification performance, but not whether our risk tiers are appropriate or explanations are clear to older adults. To address this, we supplemented with manual review and LLM-as-a-judge evaluation."
    )

    st.markdown('<div class="method-img">', unsafe_allow_html=True)
    st.image("assets/model_selection.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div class='metric-row'></div>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3, gap="medium")
    with m1:
        st.metric("Best Overall Accuracy", "96%")
    with m2:
        st.metric("Phishing Recall", "100%")
    with m3:
        st.metric("Selected Stack", "Nova Pro")

elif page == "About Us":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("About Us")
    section_title("Meet the PhishNet team")
    section_body(
        "We are a team of data science students in the Master of Information and Data Science program at UC Berkeley, building PhishNet as our final capstone project."
    )

    c1, c2, c3, c4 = st.columns(4, gap="medium")
    with c1:
        render_team_card("Ziyad Amer", "assets/ziyad.png", "https://www.linkedin.com/in/ziyad-amer/")
    with c2:
        render_team_card("Daniel Chung", "assets/daniel.png", "https://www.linkedin.com/in/danielchungt/")
    with c3:
        render_team_card("Neeharika Kotte", "assets/neeharika.png", "https://www.linkedin.com/in/neeharika-kotte-530a7a13a/")
    with c4:
        render_team_card("Annelise Meyer", "assets/annelise.png", "https://www.linkedin.com/in/annelise-meyer/")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "GitHub":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("GitHub")
    section_title("Project repository")
    section_body(
        "Explore the codebase, infrastructure, and supporting assets for the PhishNet capstone project."
    )

    st.markdown(
        f"""
        <div class="github-box">
            <div class="card-title">Repository link</div>
            <div class="card-body">
                This repository contains the project code and implementation details.
            </div>
            <a class="github-link" href="{GITHUB_URL}" target="_blank" rel="noopener noreferrer">
                Open GitHub Repository
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )