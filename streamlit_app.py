import streamlit as st

def monster_card(name, img, rarity, element, power, desc):
    card_html = f"""
    <div style="
        background:#1c1c1c;
        border-radius:15px;
        padding:12px;
        text-align:center;
        width:200px;
        color:white;
        font-family:Arial;
        box-shadow:0 0 12px rgba(255,255,255,0.2);
    ">
        <img src="{img}" style="width:100%;border-radius:10px;">
        <h3 style="margin:6px 0;">{name}</h3>
        <span style="
            background:#ffdd00;
            padding:4px 8px;
            border-radius:6px;
            font-weight:bold;
            color:black;
        ">{rarity}</span>
        <p>屬性：{element}</p>
        <p>戰力：{power}</p>
        <small style="opacity:0.7;">{desc}</small>
    </div>
    """
    st.html(card_html)

st.title("🔮 Monster Lab｜高級怪獸展示卡")

cols = st.columns(3)

with cols[0]:
    monster_card("夜影狐", "https://placekitten.com/202/202", "SSR", "暗", 95, "夜影狐能吸收月光並化為黑炎。")

with cols[1]:
    monster_card("焰尾龍", "https://placekitten.com/203/203", "SR", "火", 88, "喜歡戰鬥，能吐出灼熱火焰。")

with cols[2]:
    monster_card("深海歌者", "https://placekitten.com/204/204", "R", "水", 72, "歌聲具有催眠能力。")
