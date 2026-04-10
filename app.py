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
DEMO_VIDEO_URL = "https://www.youtube.com/watch?v=iMht94dYnFI"

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
    --light-text: #1F2937;
    --light-muted: #4B5563;
    --light-line: rgba(17,24,39,0.10);
    --light-accent: #0EA5A4;
}

html, body, [data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 15% 18%, rgba(130, 218, 203, 0.08), transparent 35%),
        radial-gradient(circle at 84% 18%, rgba(95, 132, 174, 0.10), transparent 40%),
        radial-gradient(circle at 50% 88%, rgba(130, 218, 203, 0.06), transparent 35%),
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
    color: #FFFFFF !important;
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
    border-bottom: 2px solid var(--aqua);
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

.arch-img img, .method-img img, .data-img img {
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

/* light mode support */
@media (prefers-color-scheme: light) {
    html, body, [data-testid="stAppViewContainer"] {
        background: #FFFFFF;
        color: var(--light-text);
    }

    .nav-shell {
        background: rgba(255,255,255,0.92);
        border: 1px solid var(--light-line);
        box-shadow: 0 10px 28px rgba(17,24,39,0.08);
    }

    div[role="radiogroup"] label {
        color: var(--light-text) !important;
    }

    div[role="radiogroup"] label:hover {
        background: rgba(17,24,39,0.04);
        color: var(--light-accent) !important;
    }

    div[role="radiogroup"] label:has(input:checked) {
        background: rgba(14,165,164,0.08);
        color: var(--light-accent) !important;
        border-color: rgba(14,165,164,0.20);
        border-bottom: 2px solid var(--light-accent);
    }

    .hero-logo-card,
    .content-card,
    .team-card,
    .github-box,
    [data-testid="metric-container"] {
        background: rgba(255,255,255,0.88);
        border: 1px solid var(--light-line);
        box-shadow: 0 12px 28px rgba(17,24,39,0.08);
    }

    .hero-tagline,
    .section-body,
    .card-body,
    .hero-footer {
        color: var(--light-muted);
    }

    .hero-body {
        color: #111827;
    }

    .section-eyebrow {
        color: var(--light-accent);
    }

    .hero-title,
    .section-title,
    .card-title,
    .team-name,
    .github-link {
        color: var(--light-text);
    }

    .hero-title .accent {
        color: var(--light-accent);
    }

    .linkedin-link {
        background: rgba(17,24,39,0.04);
        border: 1px solid var(--light-line);
        color: var(--light-text);
    }

    .linkedin-link:hover {
        background: rgba(14,165,164,0.10);
        color: var(--light-accent);
    }

    .github-link {
        background: rgba(17,24,39,0.04);
        border: 1px solid var(--light-line);
    }

    .github-link:hover {
        background: rgba(14,165,164,0.10);
        color: var(--light-accent);
    }

    .arch-img img, .method-img img, .data-img img {
        border: 1px solid var(--light-line);
        box-shadow: 0 12px 28px rgba(17,24,39,0.08);
    }
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
            PhishNet is a free Chrome extension for Gmail that helps users understand why an email is risky, not just whether it is. By surfacing interpretable signals and plain-language explanations, it helps older adults stay in control of their inbox instead of relying on black-box filters.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="hero-footer">UC Berkeley MIDS Capstone • Spring 2026 Section 3</div>', unsafe_allow_html=True)
        st.markdown('</div></div>', unsafe_allow_html=True)

elif page == "Motivation":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Problem")
    section_title("A growing crisis hiding in plain sight")
    section_body(
        "Older adults lose billions of dollars each year to phishing and email fraud, and the problem is accelerating. Reported losses for adults over 60 reached $2.4 billion in 2024, a four-fold increase since 2020, and the true figure is likely much higher because fraud is deeply underreported."
    )

    c1, c2 = st.columns(2, gap="large")
    with c1:
        render_card(
            "Why this matters",
            """
            <ul>
                <li>Scams create real mental and physical harm, not just financial loss</li>
                <li>Older adults living alone or managing cognitive decline are especially vulnerable</li>
                <li>Median losses are significantly higher than for younger groups</li>
            </ul>
            """
        )
    with c2:
        render_card(
            "Why this is underserved",
            """
            <ul>
                <li>6 in 10 older adults say technology was not designed with them in mind</li>
                <li>No widely available free tool exists to help them navigate their inbox safely</li>
                <li>63.6M U.S. adults aged 55+ use Chrome on desktop or tablet</li>
            </ul>
            """
        )

    section_eyebrow("Transparency Gap")
    section_title("Why existing tools fail")
    section_body(
        "Current solutions generally fall into three failure modes: they are too simple, too opaque, or too inaccessible. At the moment when scams are becoming hardest to distinguish from legitimate emails, users are left relying on intuition."
    )

    c3, c4 = st.columns(2, gap="large")
    with c3:
        render_card(
            "Where tools fall short",
            """
            <ul>
                <li>Binary classifiers give a label with no explanation</li>
                <li>Black-box systems hide their reasoning entirely</li>
                <li>Users cannot learn from or verify the model’s decision</li>
            </ul>
            """
        )
    with c4:
        render_card(
            "What that creates",
            """
            <ul>
                <li>Dependency instead of confidence or literacy</li>
                <li>No fallback when a scam slips through a filter</li>
                <li>Enterprise-priced or reactive products that are not senior-specific</li>
            </ul>
            """
        )

    section_eyebrow("Solution")
    section_title("Designed for clarity, not just detection")
    section_body(
        "PhishNet closes this gap by identifying scam patterns, surfacing interpretable risk signals, and keeping users in control of their own inbox. It is designed for two core personas: the independent older adult who wants protection without surveillance, and the trusted family member who wants peace of mind without being constantly on call."
    )

    c5, c6 = st.columns(2, gap="large")
    with c5:
        render_card(
            "What users see",
            """
            <ul>
                <li>Three risk tiers: safe, suspicious, dangerous</li>
                <li>A sidebar widget that explains the signals behind the verdict</li>
                <li>Psychological tactics surfaced in plain language, including authority, scarcity, and social proof</li>
            </ul>
            """
        )
    with c6:
        render_card(
            "Why it works",
            """
            <ul>
                <li>Protection without removing user agency</li>
                <li>One-click trusted contact support when needed</li>
                <li>Privacy-first design with minimal data retention</li>
            </ul>
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Demo":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Demo")
    section_title("What the product experience looks like")
    section_body(
        "PhishNet runs directly inside Gmail. Emails are labeled automatically, and opening a message shows the risk level, explanation, and next-step options in real time."
    )

    demo_left, demo_right = st.columns([1.7, 1], gap="large")
    with demo_left:
        st.video(DEMO_VIDEO_URL)
    with demo_right:
        render_card(
            "User workflow",
            """
            <ul>
                <li>Email arrives in Gmail and PhishNet checks whether the thread has already been scored</li>
                <li>The extension assigns a risk tier: safe, suspicious, or dangerous</li>
                <li>Opening the email reveals a sidebar with the explanation behind the decision</li>
                <li>The Risk Analysis tab surfaces signals such as urgency, authority, impersonation, or suspicious requests</li>
                <li>The Ask tab lets users ask follow-up questions about the message in plain language</li>
                <li>The Settings tab allows users to add a trusted contact and share a summary with one click</li>
                <li>Users can choose whether to trust, ignore, escalate, or request additional help</li>
            </ul>
            """
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Data":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Data")
    section_title("Grounded in real scams and elder-specific behavior")
    section_body(
        "A core challenge was the lack of elder-specific phishing datasets. To address this, we combined real phishing corpora, balanced ham/spam data, synthetic augmentation, and a live knowledge base of trusted scam reports."
    )

    st.markdown('<div class="data-img">', unsafe_allow_html=True)
    st.image("assets/datasets.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    render_card(
        "Key insights",
        """
        <ul>
            <li>Elder-targeted paraphrasing meaningfully shifted language toward terms like Medicare, benefits, and security</li>
            <li>SpamAssassin analysis surfaced common domain impersonation patterns, including subtle misspellings</li>
            <li>Across sources, we identified 23 distinct elder-specific scam patterns spanning healthcare, romance, prescription offers, and more</li>
        </ul>
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Architecture":
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    section_eyebrow("Architecture")
    section_title("End-to-end system for real-time scam detection")
    section_body(
        "PhishNet combines a Gmail-native Chrome extension with a cloud-based inference system that is optimized for speed, interpretability, and continuous improvement."
    )

    c1 = st.columns(1)[0]
    with c1:
        render_card(
            "System overview",
            """
            <ul>
                <li>The Chrome extension checks for untagged Gmail threads when new mail arrives or Gmail is opened</li>
                <li>Events route through a GCP Pub/Sub layer and trigger a FastAPI backend on AWS App Runner</li>
                <li>Amazon Bedrock runs the classification pipeline with retrieval from a live knowledge base</li>
                <li>Results are written back to the Gmail UI in real time</li>
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
            "Application stack and learning loop",
            """
            <ul>
                <li>Two-stage scoring keeps latency and cost low: safe emails stop after initial classification, while suspicious and dangerous emails receive full explanation generation</li>
                <li>DynamoDB stores scores, settings, feedback, and structured outputs</li>
                <li>S3 stores vectorized AARP and IC3 source material for the knowledge base</li>
                <li>A weekly scraper updates trusted scam content and incrementally refreshes the vector store</li>
                <li>Thumbs-down user feedback becomes labeled evaluation data used to improve prompts, retrieval quality, and explanation fidelity</li>
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
        "We evaluated a progression of approaches, from traditional ML on semantic features to full-email LLM classification and finally to a retrieval-augmented framework grounded in live scam reports. The goal was not just high binary accuracy, but a system that stays current, explains itself clearly, and performs well for older-adult-facing use cases."
    )

    st.markdown('<div class="method-img">', unsafe_allow_html=True)
    st.image("assets/modeling_approaches.png", width=1120)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    section_body(
        "Traditional ML reached about 85% accuracy but struggled with legitimate-email precision. Fine-tuned LLMs improved accuracy to 93% by using full email bodies, but required retraining as scams evolved. RAG delivered the strongest balance of adaptability and performance by grounding classification in a live, updatable knowledge base."
    )

    section_body(
        "We benchmarked GPT-4o-mini, Claude Haiku, Nova Lite, and Nova Pro in a two-step pipeline. Nova Pro performed best, achieving 96% overall accuracy and 100% phishing recall with few-shot examples and retrieval of the top three similar scams. Because binary metrics alone do not capture whether risk tiers and explanations are truly usable, we also layered in manual review and LLM-as-a-judge evaluation."
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

    render_card(
        "Evaluation beyond accuracy",
        """
        <ul>
            <li>Manual review assessed whether risk tiers and explanations were appropriate for older adults</li>
            <li>LLM-as-a-judge scoring measured phishing tier quality, explanation quality, faithfulness, relevance, and coherence</li>
            <li>Nova Pro achieved strong explanation quality while remaining succinct and consistent with the label</li>
        </ul>
        """
    )

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