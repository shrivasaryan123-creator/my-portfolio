import streamlit as st
import json
import os

# --- 1. पेज सेटअप ---
st.set_page_config(
    page_title="Video Editor & Motion Designer Portfolio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

DATA_FILE = "portfolio_data.json"

# डिफ़ॉल्ट डेटा (जिसे आप बाद में वेबसाइट के एडमिन पैनल से बदल सकते हैं)
DEFAULT_DATA = {
    "profile": {
        "name": "आपका नाम (Your Name)",
        "channel_brand": "आपके चैनल / ब्रांड का नाम",
        "tagline": "Professional Video Editor | Viral Reels & High-Retention Edits",
        "bio": "नमस्ते! मैं यूट्यूबर्स, पॉडकास्टर्स और ब्रांड्स के लिए हाई-रिटेंशन वीडियो एडिटिंग, मोशन ग्राफिक्स और साउंड डिज़ाइन करता हूँ।",
        "email": "youremail@gmail.com",
        "whatsapp": "+91XXXXXXXXXX",
        "channel_url": "https://youtube.com"
    },
    "payment": {
        "upi_id": "yourname@upi",
        "rates": [
            {"service": "10x Instagram Reel / Short (0-120 sec)", "price": "₹4,000 - ₹8,500 monthly"},
            {"service": "1x YouTube Long-form (8-15 min)", "price": "₹2,500 - ₹5,000"},
            {"service": "मंथली पैकेज (15 Reels / 4 Videos)", "price": "₹15,000 / महीना"}
        ]
    },
    "videos": [
        {
            "id": 1,
            "title": "Cinematic YouTube Travel Vlog",
            "category": "YouTube Long-form",
            "url": "https://www.youtube.com/watch?v=ScMzIvxBSi4",
            "desc": "सिनेमैटिक कलर ग्रेडिंग, डायनामिक कट्स और ऑडियो लेवलिंग।"
        },
        {
            "id": 2,
            "title": "Viral Short / Reel (Hook & Captions)",
            "category": "Shorts / Reels",
            "url": "https://www.youtube.com/watch?v=ysz5S6PUM-U",
            "desc": "एनिमेटेड सबटाइटल्स, साउंड इफेक्ट्स (SFX) और हाई-एंगेजमेंट पेसिंग।"
        }
    ]
}

def load_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_DATA, f, ensure_ascii=False, indent=4)
        return DEFAULT_DATA
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DATA

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = load_data()
prof = data.get("profile", DEFAULT_DATA["profile"])
pay = data.get("payment", DEFAULT_DATA["payment"])

# --- 2. मॉडर्न डार्क स्टाइल और एनिमेशन्स ---
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at 50% 10%, #1e1b4b 0%, #09090b 100%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #38bdf8, #a855f7, #ec4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
        line-height: 1.2;
    }
    .hero-channel {
        text-align: center;
        font-size: 1.2rem;
        color: #38bdf8;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .hero-sub {
        font-size: 1.1rem;
        text-align: center;
        color: #cbd5e1;
        max-width: 650px;
        margin: 0 auto 25px auto;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 16px;
        padding: 16px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    .badge {
        background: #6366f1;
        color: white;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .pay-box {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
        border: 1px solid #6366f1;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. हेडर सेक्शन ---
st.markdown(f"<div class='hero-channel'>🎬 {prof.get('channel_brand', '')}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='hero-title'>{prof.get('name', 'Video Editor')}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='hero-sub'>{prof.get('tagline', '')}</div>", unsafe_allow_html=True)

# संपर्क बटन्स
c1, c2, c3 = st.columns(3)
with c1:
    clean_phone = prof.get('whatsapp', '').replace('+', '').replace(' ', '')
    st.link_button("💬 WhatsApp चैट", f"https://wa.me/{clean_phone}", use_container_width=True)
with c2:
    st.link_button("📧 ईमेल भेजें", f"mailto:{prof.get('email', '')}", use_container_width=True)
with c3:
    st.link_button("📺 चैनल देखें", prof.get('channel_url', 'https://youtube.com'), use_container_width=True)

st.markdown("---")

# --- 4. वीडियो पोर्टफोलियो ---
st.subheader("🔥 मेरे वीडियो प्रोजेक्ट्स (Portfolio)")

filter_cat = st.radio("कैटेगरी:", ["सभी (All)", "Shorts / Reels", "YouTube Long-form", "Commercial / Ads"], horizontal=True)

videos_to_show = data.get("videos", [])
if filter_cat != "सभी (All)":
    videos_to_show = [v for v in videos_to_show if v.get("category") == filter_cat]

if not videos_to_show:
    st.info("इस सेक्शन में अभी कोई वीडियो नहीं है। नीचे एडमिन पैनल से जोड़ें।")
else:
    cols = st.columns(2)
    for i, vid in enumerate(videos_to_show):
        with cols[i % 2]:
            st.markdown(f"""
            <div class='glass-card'>
                <span class='badge'>{vid.get('category', 'Video')}</span>
                <h3 style='margin: 10px 0 5px 0;'>{vid.get('title', '')}</h3>
                <p style='color:#94a3b8; font-size:14px; margin-bottom: 12px;'>{vid.get('desc', '')}</p>
            </div>
            """, unsafe_allow_html=True)
            try:
                st.video(vid.get("url"))
            except Exception:
                st.caption("वीडियो लोड करने में समस्या।")

st.markdown("---")

# --- 5. पेमेंट और सर्विस रेट्स ---
st.subheader("💳 सर्विस चार्ज और पेमेंट (Hire & Pay)")

pay_col1, pay_col2 = st.columns([1.2, 1])

with pay_col1:
    st.write("### 📌 पैकेज और रेट्स:")
    for rate in pay.get("rates", []):
        st.markdown(f"- **{rate['service']}:** `{rate['price']}`")
    st.info("💡 **नोट:** काम शुरू करने के लिए 50% एडवांस देना होगा।")

with pay_col2:
    upi = pay.get('upi_id', 'yourname@upi')
    name_encoded = prof.get('name', 'Editor').replace(' ', '%20')
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=upi://pay?pa={upi}%26pn={name_encoded}"
    
    st.markdown(f"""
    <div class='pay-box'>
        <h3 style='margin-bottom:5px;'>QR कोड स्कैन करके पे करें</h3>
        <p style='color:#a855f7; font-weight:bold; margin-bottom:10px;'>UPI ID: {upi}</p>
        <img src='{qr_url}' width='190' style='border-radius:12px; margin-bottom:10px; background:white; padding:8px;'/>
        <p style='font-size:12px; color:#94a3b8;'>Google Pay • PhonePe • Paytm</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 6. एडमिन पैनल (फोन से नया वीडियो जोड़ने / हटाने के लिए) ---
with st.expander("⚙️ वेबसाइट एडमिन पैनल (यहाँ से वीडियो जोड़ें, हटाएं या डिटेल्स बदलें)"):
    pin = st.text_input("पासवर्ड डालें (डिफ़ॉल्ट पासवर्ड: 1234):", type="password")

    if pin == "1234":
        st.success("सफलतापूर्वक लॉगिन हुआ!")
        tab_v_add, tab_v_del, tab_prof = st.tabs(["➕ नया वीडियो जोड़ें", "🗑️ वीडियो हटाएं", "✏️ नाम & UPI बदलें"])

        # नया वीडियो जोड़ना
        with tab_v_add:
            with st.form("new_video_form"):
                n_title = st.text_input("वीडियो का टाइटल:")
                n_cat = st.selectbox("कैटेगरी:", ["Shorts / Reels", "YouTube Long-form", "Commercial / Ads"])
                n_url = st.text_input("यूट्यूब लिंक (YouTube URL):")
                n_desc = st.text_area("छोटा विवरण (Short Description):")
                add_sub = st.form_submit_button("🚀 वेबसाइट पर जोड़ें")

                if add_sub:
                    if n_title and n_url:
                        new_id = max([v.get("id", 0) for v in data.get("videos", [])], default=0) + 1
                        data["videos"].append({
                            "id": new_id,
                            "title": n_title,
                            "category": n_cat,
                            "url": n_url,
                            "desc": n_desc
                        })
                        save_data(data)
                        st.success(f"'{n_title}' वेबसाइट पर जुड़ गया!")
                        st.rerun()
                    else:
                        st.error("टाइटल और यूट्यूब लिंक भरना ज़रूरी है।")

        # वीडियो हटाना
        with tab_v_del:
            if not data.get("videos"):
                st.info("हटाने के लिए कोई वीडियो नहीं है।")
            else:
                for v in data.get("videos", []):
                    c_del1, c_del2 = st.columns([3, 1])
                    with c_del1:
                        st.write(f"• **{v.get('title')}** ({v.get('category')})")
                    with c_del2:
                        if st.button("हटाएं ❌", key=f"del_{v.get('id')}"):
                            data["videos"] = [item for item in data.get("videos", []) if item.get("id") != v.get("id")]
                            save_data(data)
                            st.success("वीडियो हटा दिया गया!")
                            st.rerun()

        # प्रोफाइल और UPI बदलना
        with tab_prof:
            with st.form("edit_profile_form"):
                u_name = st.text_input("आपका नाम:", value=prof.get("name", ""))
                u_brand = st.text_input("चैनल / ब्रांड नाम:", value=prof.get("channel_brand", ""))
                u_tagline = st.text_input("टैगलाइन:", value=prof.get("tagline", ""))
                u_whatsapp = st.text_input("WhatsApp नंबर (+91 के साथ):", value=prof.get("whatsapp", ""))
                u_email = st.text_input("ईमेल आईडी:", value=prof.get("email", ""))
                u_channel = st.text_input("यूट्यूब चैनल लिंक:", value=prof.get("channel_url", ""))
                u_upi = st.text_input("UPI ID:", value=pay.get("upi_id", ""))
                
                save_prof_btn = st.form_submit_button("💾 जानकारी सेव करें")

                if save_prof_btn:
                    data["profile"]["name"] = u_name
                    data["profile"]["channel_brand"] = u_brand
                    data["profile"]["tagline"] = u_tagline
                    data["profile"]["whatsapp"] = u_whatsapp
                    data["profile"]["email"] = u_email
                    data["profile"]["channel_url"] = u_channel
                    data["payment"]["upi_id"] = u_upi
                    save_data(data)
                    st.success("डिटेल्स अपडेट हो गईं!")
                    st.rerun()

    elif pin != "":
        st.error("गलत पासवर्ड! कृपया 1234 डालें।")
