import streamlit as st

st.set_page_config(
    page_title="MBTI 게임 추천소 🎮",
    page_icon="🎮",
    layout="centered",
)

# ---------------------------------------------------------
# 커스텀 스타일 (귀엽고 고급진 + 부드러운 느낌)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Gowun Dodum', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #fdf6f0 0%, #f3e8ff 50%, #e8f0ff 100%);
    }

    .main-title {
        font-family: 'Jua', sans-serif;
        text-align: center;
        font-size: 42px;
        background: linear-gradient(90deg, #b28dff, #ff9ecb, #9ecbff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding-top: 10px;
        margin-bottom: 0px;
    }

    .sub-title {
        text-align: center;
        color: #8a7ca8;
        font-size: 16px;
        margin-bottom: 30px;
    }

    div[data-baseweb="select"] {
        border-radius: 20px;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.75);
        border-radius: 28px;
        padding: 30px 28px;
        margin-top: 25px;
        box-shadow: 0 8px 24px rgba(178, 141, 255, 0.18);
        border: 1px solid rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(6px);
    }

    .game-name {
        font-family: 'Jua', sans-serif;
        font-size: 28px;
        color: #6c4ab6;
        margin-bottom: 8px;
    }

    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #ffd6e8, #e0d4ff);
        color: #7a4fb5;
        padding: 5px 14px;
        border-radius: 15px;
        font-size: 13px;
        margin-right: 6px;
        margin-bottom: 10px;
    }

    .desc-text {
        color: #5c5470;
        font-size: 15.5px;
        line-height: 1.7;
    }

    .footer-note {
        text-align: center;
        color: #b3a9c9;
        font-size: 12.5px;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# MBTI별 게임 추천 데이터
# ---------------------------------------------------------
mbti_games = {
    "INTJ": {
        "emoji": "🧠",
        "game": "문명 (Civilization) 시리즈",
        "tags": ["#전략", "#장기전", "#설계의 즐거움"],
        "desc": "치밀한 계획과 큰 그림을 그리는 걸 좋아하는 INTJ에게는 나라를 처음부터 설계하고 발전시키는 '문명' 시리즈가 완벽해요. 몇 수 앞을 내다보는 전략적 사고를 마음껏 발휘할 수 있답니다.",
    },
    "INTP": {
        "emoji": "🔬",
        "game": "팩토리오 (Factorio)",
        "tags": ["#논리", "#최적화", "#탐구"],
        "desc": "복잡한 시스템을 분석하고 최적의 해법을 찾는 걸 즐기는 INTP에게는 자동화 공장을 설계하는 '팩토리오'가 딱이에요. 끝없는 최적화의 재미에 시간 가는 줄 모를 거예요.",
    },
    "ENTJ": {
        "emoji": "👑",
        "game": "스타크래프트 II (StarCraft II)",
        "tags": ["#리더십", "#승부욕", "#전략"],
        "desc": "목표 지향적이고 승부욕 넘치는 ENTJ에게는 빠른 판단력과 통솔력이 필요한 '스타크래프트 II'를 추천해요. 상대를 압도하는 전략으로 승리를 이끌어보세요.",
    },
    "ENTP": {
        "emoji": "💡",
        "game": "포탈 2 (Portal 2)",
        "tags": ["#창의력", "#퍼즐", "#유머"],
        "desc": "새로운 아이디어와 재치 있는 발상을 좋아하는 ENTP에게는 기발한 퍼즐과 유머가 가득한 '포탈 2'가 잘 어울려요. 예상 밖의 해법을 찾는 재미가 쏠쏠하답니다.",
    },
    "INFJ": {
        "emoji": "🌙",
        "game": "저니 (Journey)",
        "tags": ["#감성", "#스토리", "#힐링"],
        "desc": "깊은 의미와 감정적 교감을 소중히 여기는 INFJ에게는 신비롭고 감동적인 여정을 그린 '저니'를 추천해요. 말없이도 마음이 통하는 잔잔한 경험을 선사할 거예요.",
    },
    "INFP": {
        "emoji": "🌸",
        "game": "스타듀밸리 (Stardew Valley)",
        "tags": ["#힐링", "#감성", "#나만의 세계"],
        "desc": "따뜻한 상상력과 자기만의 세계를 소중히 여기는 INFP에게는 평화로운 농장에서 나만의 이야기를 만들어가는 '스타듀밸리'가 안성맞춤이에요.",
    },
    "ENFJ": {
        "emoji": "🤝",
        "game": "동물의 숲 (Animal Crossing)",
        "tags": ["#소통", "#커뮤니티", "#따뜻함"],
        "desc": "사람들과의 관계와 따뜻한 커뮤니티를 중요하게 여기는 ENFJ에게는 이웃들과 어울리며 마을을 가꾸는 '동물의 숲'을 추천해요. 함께하는 즐거움을 만끽할 수 있어요.",
    },
    "ENFP": {
        "emoji": "🎨",
        "game": "젤다의 전설: 야생의 숨결 (Zelda: BOTW)",
        "tags": ["#자유", "#모험", "#호기심"],
        "desc": "새로운 경험과 자유로운 탐험을 사랑하는 ENFP에게는 광활한 세계를 마음껏 누비는 '젤다의 전설: 야생의 숨결'이 잘 맞아요. 호기심을 자극하는 모험이 가득해요.",
    },
    "ISTJ": {
        "emoji": "🏛️",
        "game": "시티즈: 스카이라인 (Cities: Skylines)",
        "tags": ["#체계", "#계획", "#꾸준함"],
        "desc": "체계적이고 꼼꼼한 ISTJ에게는 도시를 차근차근 설계하고 관리하는 '시티즈: 스카이라인'을 추천해요. 규칙과 질서 속에서 안정적인 성취감을 느낄 수 있어요.",
    },
    "ISFJ": {
        "emoji": "🍞",
        "game": "동물의 숲 (Animal Crossing)",
        "tags": ["#평화", "#돌봄", "#소소함"],
        "desc": "다정하고 세심한 ISFJ에게는 소소한 일상을 가꾸며 이웃을 챙기는 '동물의 숲'이 잘 어울려요. 평화롭고 따뜻한 분위기 속에서 편안함을 느낄 수 있답니다.",
    },
    "ESTJ": {
        "emoji": "📋",
        "game": "에이지 오브 엠파이어 (Age of Empires)",
        "tags": ["#전략", "#효율", "#리더십"],
        "desc": "체계적인 관리와 효율을 중시하는 ESTJ에게는 문명을 건설하고 이끄는 '에이지 오브 엠파이어'를 추천해요. 자원 관리와 전략적 지휘를 동시에 즐길 수 있어요.",
    },
    "ESFJ": {
        "emoji": "🎉",
        "game": "잇 테이크스 투 (It Takes Two)",
        "tags": ["#협동", "#친밀함", "#재미"],
        "desc": "사람들과 함께하는 즐거움을 아는 ESFJ에게는 파트너와 협력하며 진행하는 '잇 테이크스 투'가 딱이에요. 함께 웃고 힘을 합치는 과정 자체가 즐거움이 될 거예요.",
    },
    "ISTP": {
        "emoji": "🔧",
        "game": "마인크래프트 (Minecraft)",
        "tags": ["#손기술", "#자율성", "#실험"],
        "desc": "손으로 직접 만들고 실험하는 걸 좋아하는 ISTP에게는 무엇이든 만들 수 있는 '마인크래프트'가 완벽해요. 자유롭게 도구를 다루며 나만의 방식으로 즐길 수 있어요.",
    },
    "ISFP": {
        "emoji": "🎭",
        "game": "쿠킹 마마 / 슈퍼 마리오 오디세이",
        "tags": ["#감성", "#미적감각", "#자유로움"],
        "desc": "감각적이고 자유로운 영혼의 ISFP에게는 아기자기하고 예쁜 비주얼의 '슈퍼 마리오 오디세이' 같은 게임이 잘 맞아요. 눈과 마음이 즐거운 경험을 선사해요.",
    },
    "ESTP": {
        "emoji": "⚡",
        "game": "포트나이트 (Fortnite)",
        "tags": ["#액션", "#순발력", "#스릴"],
        "desc": "즉각적인 반응과 스릴을 즐기는 ESTP에게는 빠른 판단과 액션이 필요한 '포트나이트'를 추천해요. 짜릿한 서바이벌 배틀에서 존재감을 뽐낼 수 있어요.",
    },
    "ESFP": {
        "emoji": "🎤",
        "game": "저스트 댄스 (Just Dance)",
        "tags": ["#흥", "#파티", "#에너지"],
        "desc": "밝고 에너지 넘치는 ESFP에게는 신나게 몸을 움직이며 즐기는 '저스트 댄스'가 제격이에요. 친구들과 함께라면 즐거움이 두 배가 될 거예요.",
    },
}

# ---------------------------------------------------------
# 화면 구성
# ---------------------------------------------------------
st.markdown('<div class="main-title">🎮 MBTI 게임 추천소</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">나의 MBTI에 딱 맞는 게임을 찾아드려요 ✨</div>',
    unsafe_allow_html=True,
)

st.write("")

mbti_list = list(mbti_games.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요 💫", mbti_list)

if selected_mbti:
    info = mbti_games[selected_mbti]
    badges_html = "".join(f'<span class="badge">{tag}</span>' for tag in info["tags"])

    st.markdown(
        f"""
        <div class="result-card">
            <div class="game-name">{info['emoji']} {selected_mbti}에게 추천하는 게임</div>
            <div class="game-name" style="font-size:24px; margin-top:-4px;">👉 {info['game']}</div>
            <div>{badges_html}</div>
            <div class="desc-text">{info['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="footer-note">Made with 💜 by MBTI Game Recommender</div>',
    unsafe_allow_html=True,
)
