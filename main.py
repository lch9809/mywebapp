import html
import random

import streamlit as st


# ---------------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------------
st.set_page_config(
    page_title="MBTI Game Atelier",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# 디자인
# 외부 CSS·폰트·이미지 없이 main.py 안에서만 구성합니다.
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        :root {
            --ink: #2f2940;
            --muted: #756f82;
            --cream: #fffaf5;
            --rose: #f5dfe6;
            --lavender: #e9e2f4;
            --sage: #dfeae3;
            --gold: #b88a53;
            --line: rgba(77, 61, 94, 0.12);
        }

        html, body, [class*="css"] {
            font-family:
                Pretendard, -apple-system, BlinkMacSystemFont,
                "Segoe UI", "Noto Sans KR", sans-serif;
        }

        .stApp {
            color: var(--ink);
            background:
                radial-gradient(circle at 12% 8%, rgba(245, 223, 230, 0.82), transparent 28%),
                radial-gradient(circle at 88% 12%, rgba(233, 226, 244, 0.88), transparent 30%),
                radial-gradient(circle at 75% 85%, rgba(223, 234, 227, 0.76), transparent 30%),
                linear-gradient(145deg, #fffdfb 0%, #faf7fb 48%, #fffaf4 100%);
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stToolbar"] {
            right: 1rem;
        }

        .block-container {
            max-width: 880px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }

        .hero {
            position: relative;
            overflow: hidden;
            padding: 2.25rem 2.1rem;
            margin-bottom: 1.35rem;
            border: 1px solid rgba(255, 255, 255, 0.75);
            border-radius: 30px;
            background:
                linear-gradient(
                    135deg,
                    rgba(255,255,255,0.86),
                    rgba(255,250,245,0.72)
                );
            box-shadow: 0 20px 55px rgba(72, 53, 89, 0.10);
            backdrop-filter: blur(12px);
        }

        .hero::after {
            content: "✦";
            position: absolute;
            top: -42px;
            right: 34px;
            font-size: 8rem;
            color: rgba(184, 138, 83, 0.11);
            transform: rotate(12deg);
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            margin-bottom: 0.75rem;
            padding: 0.38rem 0.78rem;
            border: 1px solid rgba(184, 138, 83, 0.22);
            border-radius: 999px;
            color: #86663f;
            background: rgba(255, 248, 236, 0.76);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.09em;
        }

        .hero-title {
            position: relative;
            z-index: 1;
            margin: 0;
            color: var(--ink);
            font-size: clamp(2rem, 5vw, 3.55rem);
            line-height: 1.08;
            letter-spacing: -0.045em;
        }

        .hero-title .accent {
            color: #9a6680;
        }

        .hero-copy {
            position: relative;
            z-index: 1;
            max-width: 620px;
            margin: 0.95rem 0 0;
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.75;
            word-break: keep-all;
        }

        .soft-divider {
            width: 64px;
            height: 3px;
            margin: 1.25rem 0 0;
            border-radius: 999px;
            background: linear-gradient(90deg, #b88a53, #d8bfa2);
        }

        .section-label {
            margin: 1.5rem 0 0.55rem;
            color: #6f627b;
            font-size: 0.8rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        div[data-baseweb="select"] > div {
            min-height: 3.35rem;
            border: 1px solid rgba(91, 74, 108, 0.16);
            border-radius: 18px;
            background: rgba(255, 255, 255, 0.86);
            box-shadow: 0 10px 26px rgba(72, 53, 89, 0.07);
        }

        div[data-baseweb="select"] > div:focus-within {
            border-color: rgba(154, 102, 128, 0.55);
            box-shadow: 0 0 0 3px rgba(154, 102, 128, 0.10);
        }

        .stButton > button {
            min-height: 3rem;
            border: 0;
            border-radius: 16px;
            color: white;
            background: linear-gradient(135deg, #9b7188, #78678f);
            box-shadow: 0 10px 24px rgba(107, 84, 126, 0.20);
            font-weight: 700;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }

        .stButton > button:hover {
            color: white;
            border: 0;
            transform: translateY(-1px);
            box-shadow: 0 13px 30px rgba(107, 84, 126, 0.25);
        }

        .stButton > button:focus {
            color: white;
            border: 0;
        }

        .intro-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.9rem;
            margin-top: 1.4rem;
        }

        .mini-card {
            padding: 1.1rem;
            border: 1px solid rgba(77, 61, 94, 0.10);
            border-radius: 21px;
            background: rgba(255,255,255,0.63);
            box-shadow: 0 12px 28px rgba(72, 53, 89, 0.06);
        }

        .mini-icon {
            display: grid;
            width: 2.35rem;
            height: 2.35rem;
            margin-bottom: 0.7rem;
            place-items: center;
            border-radius: 13px;
            background: rgba(245, 223, 230, 0.78);
            font-size: 1.1rem;
        }

        .mini-title {
            margin-bottom: 0.28rem;
            font-weight: 800;
        }

        .mini-copy {
            color: var(--muted);
            font-size: 0.86rem;
            line-height: 1.55;
            word-break: keep-all;
        }

        .profile-banner {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 1.15rem 0 1rem;
            padding: 1.05rem 1.2rem;
            border: 1px solid rgba(77, 61, 94, 0.10);
            border-radius: 22px;
            background: rgba(255,255,255,0.66);
        }

        .profile-symbol {
            display: grid;
            flex: 0 0 3.15rem;
            width: 3.15rem;
            height: 3.15rem;
            place-items: center;
            border-radius: 17px;
            background: linear-gradient(145deg, #f6e5ea, #e8e1f1);
            font-size: 1.45rem;
            box-shadow: inset 0 0 0 1px rgba(255,255,255,0.65);
        }

        .profile-name {
            font-size: 1.08rem;
            font-weight: 850;
        }

        .profile-subtitle {
            margin-top: 0.2rem;
            color: var(--muted);
            font-size: 0.88rem;
        }

        .game-card {
            position: relative;
            overflow: hidden;
            height: 100%;
            padding: 1.25rem;
            border: 1px solid rgba(77, 61, 94, 0.10);
            border-radius: 24px;
            background: rgba(255,255,255,0.72);
            box-shadow: 0 14px 32px rgba(72, 53, 89, 0.07);
        }

        .game-card.primary {
            padding: 1.55rem;
            border-color: rgba(154, 102, 128, 0.18);
            background:
                linear-gradient(
                    140deg,
                    rgba(255,255,255,0.90),
                    rgba(249,239,244,0.82)
                );
            box-shadow: 0 20px 44px rgba(92, 65, 105, 0.11);
        }

        .game-card.primary::after {
            content: "";
            position: absolute;
            width: 145px;
            height: 145px;
            top: -70px;
            right: -45px;
            border-radius: 50%;
            background: rgba(232, 213, 224, 0.55);
        }

        .rank-badge {
            position: relative;
            z-index: 1;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            margin-bottom: 0.85rem;
            padding: 0.36rem 0.68rem;
            border-radius: 999px;
            color: #8b6075;
            background: rgba(245, 223, 230, 0.72);
            font-size: 0.77rem;
            font-weight: 800;
        }

        .game-head {
            position: relative;
            z-index: 1;
            display: flex;
            align-items: flex-start;
            gap: 0.85rem;
        }

        .game-icon {
            display: grid;
            flex: 0 0 3rem;
            width: 3rem;
            height: 3rem;
            place-items: center;
            border-radius: 16px;
            background: rgba(233, 226, 244, 0.74);
            font-size: 1.35rem;
        }

        .game-title {
            margin: 0;
            color: var(--ink);
            font-size: 1.25rem;
            line-height: 1.25;
            letter-spacing: -0.025em;
        }

        .game-en {
            margin-top: 0.24rem;
            color: #8a8292;
            font-size: 0.78rem;
        }

        .tag-row {
            position: relative;
            z-index: 1;
            display: flex;
            flex-wrap: wrap;
            gap: 0.42rem;
            margin: 0.92rem 0 0.85rem;
        }

        .tag {
            padding: 0.32rem 0.58rem;
            border-radius: 999px;
            color: #675c70;
            background: rgba(235, 229, 240, 0.72);
            font-size: 0.75rem;
            font-weight: 700;
        }

        .game-reason {
            position: relative;
            z-index: 1;
            margin: 0;
            color: #5f5968;
            font-size: 0.91rem;
            line-height: 1.68;
            word-break: keep-all;
        }

        .mood-line {
            position: relative;
            z-index: 1;
            margin-top: 0.9rem;
            padding-top: 0.8rem;
            border-top: 1px solid rgba(77, 61, 94, 0.09);
            color: #7b7184;
            font-size: 0.79rem;
        }

        .summary-card {
            margin-top: 1rem;
            padding: 1.25rem 1.3rem;
            border: 1px solid rgba(184, 138, 83, 0.16);
            border-radius: 23px;
            background:
                linear-gradient(
                    135deg,
                    rgba(255,251,243,0.86),
                    rgba(255,255,255,0.66)
                );
        }

        .summary-title {
            margin-bottom: 0.45rem;
            color: #775a39;
            font-weight: 850;
        }

        .summary-copy {
            margin: 0;
            color: #6a6270;
            font-size: 0.91rem;
            line-height: 1.7;
            word-break: keep-all;
        }

        .keyword-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.85rem;
        }

        .keyword {
            padding: 0.38rem 0.68rem;
            border: 1px solid rgba(184, 138, 83, 0.18);
            border-radius: 999px;
            color: #826341;
            background: rgba(255, 248, 236, 0.72);
            font-size: 0.77rem;
            font-weight: 750;
        }

        .footer-note {
            margin-top: 1.65rem;
            color: #8a8291;
            font-size: 0.77rem;
            line-height: 1.6;
            text-align: center;
        }

        [data-testid="stExpander"] {
            margin-top: 1rem;
            border: 1px solid rgba(77, 61, 94, 0.10);
            border-radius: 18px;
            background: rgba(255,255,255,0.52);
        }

        @media (max-width: 680px) {
            .block-container {
                padding-top: 1rem;
            }

            .hero {
                padding: 1.65rem 1.3rem;
                border-radius: 24px;
            }

            .intro-grid {
                grid-template-columns: 1fr;
            }

            .profile-banner {
                align-items: flex-start;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# MBTI별 게임 추천 데이터
# - 게임명, 장르, 추천 이유, 플레이 분위기를 모두 코드 안에 저장합니다.
# ---------------------------------------------------------
PROFILES = {
    "ISTJ": {
        "symbol": "📚",
        "nickname": "차분한 설계자",
        "subtitle": "규칙을 파악하고 완성도를 쌓아가는 플레이",
        "description": "명확한 목표와 탄탄한 시스템 안에서 계획을 세우고, 조금씩 결과를 완성해 가는 게임과 잘 맞아요.",
        "keywords": ["체계적인 성장", "분명한 목표", "꾸준한 성취"],
        "games": [
            {
                "title": "팩토리오",
                "english": "Factorio",
                "icon": "⚙️",
                "genres": ["자동화", "건설", "전략"],
                "reason": "복잡한 생산 과정을 직접 설계하고 효율을 개선하는 재미가 강해요. 작은 문제를 하나씩 정리하며 거대한 시스템을 완성할 수 있어요.",
                "mood": "정리하고 최적화하는 데 몰입하고 싶은 날",
            },
            {
                "title": "스타듀 밸리",
                "english": "Stardew Valley",
                "icon": "🌿",
                "genres": ["농장", "생활", "성장"],
                "reason": "하루의 루틴을 직접 정하고 농장과 마을을 꾸준히 발전시키는 과정이 편안한 성취감을 줘요.",
                "mood": "조용히 나만의 계획을 채우고 싶은 저녁",
            },
            {
                "title": "시드 마이어의 문명 VI",
                "english": "Sid Meier's Civilization VI",
                "icon": "🏛️",
                "genres": ["턴제 전략", "경영", "역사"],
                "reason": "장기적인 계획과 자원 관리가 승패를 좌우해요. 한 수씩 고민하며 안정적인 운영을 만드는 재미가 있어요.",
                "mood": "시간을 두고 큰 그림을 그리고 싶은 주말",
            },
        ],
    },
    "ISFJ": {
        "symbol": "🫖",
        "nickname": "다정한 정원사",
        "subtitle": "돌보고 꾸미며 관계를 이어가는 플레이",
        "description": "따뜻한 분위기 속에서 캐릭터와 공간을 돌보고, 작은 변화를 차곡차곡 쌓는 게임이 편안하게 어울려요.",
        "keywords": ["따뜻한 관계", "안정적인 루틴", "섬세한 꾸미기"],
        "games": [
            {
                "title": "모여봐요 동물의 숲",
                "english": "Animal Crossing: New Horizons",
                "icon": "🏝️",
                "genres": ["생활", "꾸미기", "힐링"],
                "reason": "섬 주민들과 인사를 나누고 공간을 정성껏 꾸미는 과정이 부드럽고 안정적인 즐거움을 줘요.",
                "mood": "마음이 복잡해 천천히 쉬고 싶은 날",
            },
            {
                "title": "스피릿페어러",
                "english": "Spiritfarer",
                "icon": "⛵",
                "genres": ["어드벤처", "경영", "감성"],
                "reason": "캐릭터를 세심하게 돌보며 각자의 이야기를 들어주는 게임이에요. 잔잔하지만 깊은 감정을 남겨요.",
                "mood": "따뜻하고 뭉클한 이야기가 필요한 밤",
            },
            {
                "title": "더 심즈 4",
                "english": "The Sims 4",
                "icon": "🏡",
                "genres": ["생활 시뮬레이션", "건축", "관계"],
                "reason": "가족과 집, 일상을 원하는 방식으로 보살피고 꾸밀 수 있어요. 세세한 취향을 반영하는 재미가 커요.",
                "mood": "예쁜 공간과 평온한 일상을 만들고 싶은 날",
            },
        ],
    },
    "INFJ": {
        "symbol": "🌙",
        "nickname": "고요한 이야기꾼",
        "subtitle": "상징과 감정을 천천히 음미하는 플레이",
        "description": "분위기와 서사가 깊고, 선택 뒤에 담긴 의미를 오래 생각하게 만드는 게임이 특히 잘 맞아요.",
        "keywords": ["깊은 서사", "감정의 여운", "상징과 해석"],
        "games": [
            {
                "title": "라이프 이즈 스트레인지",
                "english": "Life is Strange",
                "icon": "🦋",
                "genres": ["스토리", "선택", "미스터리"],
                "reason": "인물의 감정과 관계를 섬세하게 따라가며 중요한 선택을 내려요. 선택 이후의 여운까지 오래 남는 작품이에요.",
                "mood": "한 편의 드라마처럼 깊게 몰입하고 싶은 날",
            },
            {
                "title": "그리스",
                "english": "GRIS",
                "icon": "🎨",
                "genres": ["플랫포머", "예술", "감성"],
                "reason": "대사보다 색과 음악, 움직임으로 감정을 전달해요. 조용히 해석하며 플레이하기 좋은 아름다운 게임이에요.",
                "mood": "말보다 분위기로 위로받고 싶은 순간",
            },
            {
                "title": "투 더 문",
                "english": "To the Moon",
                "icon": "🌌",
                "genres": ["스토리", "어드벤처", "감성"],
                "reason": "한 사람의 기억을 따라가며 삶과 선택의 의미를 되짚게 해요. 짧지만 깊은 이야기를 좋아한다면 잘 맞아요.",
                "mood": "조용한 밤, 오래 남는 이야기를 만나고 싶을 때",
            },
        ],
    },
    "INTJ": {
        "symbol": "♟️",
        "nickname": "우아한 전략가",
        "subtitle": "큰 그림을 그리고 최적의 해답을 찾는 플레이",
        "description": "복잡한 규칙을 분석하고 자신만의 전략을 세워 결과를 통제할 수 있는 게임에서 강한 만족을 느껴요.",
        "keywords": ["장기 전략", "논리적 설계", "높은 숙련도"],
        "games": [
            {
                "title": "슬레이 더 스파이어",
                "english": "Slay the Spire",
                "icon": "🃏",
                "genres": ["덱빌딩", "로그라이크", "전략"],
                "reason": "카드 조합과 확률, 앞으로의 전투를 함께 계산해야 해요. 매 판 새로운 최적해를 찾는 과정이 매력적이에요.",
                "mood": "짧고 밀도 높은 전략 싸움을 하고 싶은 날",
            },
            {
                "title": "더 위트니스",
                "english": "The Witness",
                "icon": "🔍",
                "genres": ["퍼즐", "탐험", "추론"],
                "reason": "설명을 최소화한 채 규칙을 스스로 발견하게 해요. 관찰과 추론으로 세계의 원리를 이해하는 맛이 있어요.",
                "mood": "누구의 도움 없이 문제를 풀어내고 싶은 시간",
            },
            {
                "title": "시드 마이어의 문명 VI",
                "english": "Sid Meier's Civilization VI",
                "icon": "🏛️",
                "genres": ["턴제 전략", "경영", "역사"],
                "reason": "기술, 외교, 군사, 문화의 우선순위를 긴 호흡으로 설계할 수 있어요. 큰 그림을 좋아하는 성향과 잘 맞아요.",
                "mood": "오래 고민해 완벽한 판을 만들고 싶은 주말",
            },
        ],
    },
    "ISTP": {
        "symbol": "🛠️",
        "nickname": "냉정한 해결사",
        "subtitle": "직접 부딪치며 기술을 익히는 플레이",
        "description": "설명은 짧게, 조작과 실전은 깊게 들어가는 게임이 잘 맞아요. 손으로 익히며 실력이 느는 감각을 좋아해요.",
        "keywords": ["정교한 조작", "실전 학습", "즉각적인 판단"],
        "games": [
            {
                "title": "하데스",
                "english": "Hades",
                "icon": "🔥",
                "genres": ["액션", "로그라이크", "성장"],
                "reason": "빠른 판단과 손맛, 반복 플레이 속 성장의 균형이 좋아요. 실패해도 바로 다음 시도를 하고 싶게 만들어요.",
                "mood": "짧게 시작해 강하게 몰입하고 싶은 날",
            },
            {
                "title": "몬스터 헌터 라이즈",
                "english": "Monster Hunter Rise",
                "icon": "🐉",
                "genres": ["액션", "사냥", "협동"],
                "reason": "무기별 조작을 익히고 몬스터의 패턴에 대응하는 과정이 핵심이에요. 숙련이 곧 결과로 이어져요.",
                "mood": "하나의 기술을 제대로 연마하고 싶은 주말",
            },
            {
                "title": "데드 셀",
                "english": "Dead Cells",
                "icon": "🗡️",
                "genres": ["액션", "로그라이크", "플랫포머"],
                "reason": "빠르고 정확한 조작이 중요하며, 다양한 무기 조합을 직접 시험할 수 있어요. 군더더기 없는 액션이 매력적이에요.",
                "mood": "생각보다 손이 먼저 움직이는 게임이 당길 때",
            },
        ],
    },
    "ISFP": {
        "symbol": "🌷",
        "nickname": "감각적인 산책자",
        "subtitle": "아름다운 세계를 자유롭게 느끼는 플레이",
        "description": "경쟁보다는 분위기와 감각, 나만의 방식으로 표현할 수 있는 경험에서 큰 만족을 얻는 편이에요.",
        "keywords": ["아름다운 분위기", "자유로운 탐험", "감각적 표현"],
        "games": [
            {
                "title": "저니",
                "english": "Journey",
                "icon": "🏜️",
                "genres": ["탐험", "예술", "감성"],
                "reason": "복잡한 설명 없이 풍경과 음악만으로 여행의 감정을 전달해요. 짧고 아름다운 경험을 원할 때 좋아요.",
                "mood": "조용히 낯선 세계를 걷고 싶은 밤",
            },
            {
                "title": "스카이: 빛의 아이들",
                "english": "Sky: Children of the Light",
                "icon": "🕯️",
                "genres": ["탐험", "소셜", "힐링"],
                "reason": "부드러운 비행과 아름다운 공간, 말 없이 이어지는 교류가 인상적이에요. 부담 없이 감성을 채우기 좋아요.",
                "mood": "예쁜 풍경과 따뜻한 연결이 필요한 날",
            },
            {
                "title": "모여봐요 동물의 숲",
                "english": "Animal Crossing: New Horizons",
                "icon": "🏝️",
                "genres": ["생활", "꾸미기", "힐링"],
                "reason": "정답 없이 자신의 취향대로 섬과 캐릭터를 꾸밀 수 있어요. 작은 미적 선택이 곧 플레이가 돼요.",
                "mood": "나만의 예쁜 공간을 천천히 만들고 싶을 때",
            },
        ],
    },
    "INFP": {
        "symbol": "☁️",
        "nickname": "몽상하는 수집가",
        "subtitle": "독특한 세계와 진심 어린 이야기를 만나는 플레이",
        "description": "개성 있는 캐릭터와 진솔한 메시지, 상상력을 자극하는 세계를 자유롭게 탐험할 때 깊이 몰입해요.",
        "keywords": ["독창적인 세계", "진심 어린 서사", "자유로운 상상"],
        "games": [
            {
                "title": "언더테일",
                "english": "UNDERTALE",
                "icon": "❤️",
                "genres": ["RPG", "스토리", "선택"],
                "reason": "익숙한 게임 규칙을 비틀며 플레이어의 선택과 태도를 이야기로 연결해요. 캐릭터에 정을 붙이기 쉬워요.",
                "mood": "독특하고 따뜻한 이야기에 빠지고 싶은 날",
            },
            {
                "title": "커피 톡",
                "english": "Coffee Talk",
                "icon": "☕",
                "genres": ["비주얼 노벨", "대화", "힐링"],
                "reason": "비 오는 밤 카페에서 손님들의 고민을 듣는 잔잔한 게임이에요. 대화와 분위기를 좋아한다면 잘 맞아요.",
                "mood": "조용히 타인의 이야기를 듣고 싶은 밤",
            },
            {
                "title": "나이트 인 더 우즈",
                "english": "Night in the Woods",
                "icon": "🐈",
                "genres": ["어드벤처", "스토리", "인디"],
                "reason": "불안과 관계, 성장의 고민을 독특한 유머와 감성으로 풀어요. 완벽하지 않은 인물들의 이야기가 매력적이에요.",
                "mood": "조금 쓸쓸하지만 솔직한 이야기가 당길 때",
            },
        ],
    },
    "INTP": {
        "symbol": "🧩",
        "nickname": "호기심 많은 연구자",
        "subtitle": "규칙을 발견하고 가능성을 실험하는 플레이",
        "description": "기존의 생각을 뒤집는 퍼즐과 시스템을 자유롭게 실험할 수 있는 게임에서 지적 즐거움을 느껴요.",
        "keywords": ["새로운 규칙", "자유로운 실험", "지적인 퍼즐"],
        "games": [
            {
                "title": "포탈 2",
                "english": "Portal 2",
                "icon": "🌀",
                "genres": ["퍼즐", "액션", "SF"],
                "reason": "공간의 규칙을 이해하고 전혀 다른 관점에서 해답을 찾아야 해요. 재치 있는 이야기까지 더해져 지루할 틈이 없어요.",
                "mood": "똑똑하고 유쾌한 퍼즐이 필요한 날",
            },
            {
                "title": "바바 이즈 유",
                "english": "Baba Is You",
                "icon": "🔤",
                "genres": ["퍼즐", "논리", "인디"],
                "reason": "문장 자체를 움직여 게임의 규칙을 바꾸는 독특한 퍼즐이에요. 고정관념을 깨는 해법을 좋아한다면 강력 추천해요.",
                "mood": "머리가 말랑해지는 새로운 문제가 당길 때",
            },
            {
                "title": "아우터 와일즈",
                "english": "Outer Wilds",
                "icon": "🪐",
                "genres": ["탐험", "미스터리", "SF"],
                "reason": "지식이 곧 성장인 탐험 게임이에요. 우주의 단서를 스스로 연결하며 거대한 수수께끼를 이해하게 돼요.",
                "mood": "아무것도 모른 채 세계의 비밀을 파헤치고 싶을 때",
            },
        ],
    },
    "ESTP": {
        "symbol": "🏎️",
        "nickname": "대담한 플레이메이커",
        "subtitle": "속도와 긴장감을 즉시 즐기는 플레이",
        "description": "빠른 판단과 즉각적인 피드백, 매 순간 상황이 바뀌는 경쟁에서 에너지를 얻는 편이에요.",
        "keywords": ["빠른 템포", "즉각적인 승부", "화려한 액션"],
        "games": [
            {
                "title": "로켓 리그",
                "english": "Rocket League",
                "icon": "🚀",
                "genres": ["스포츠", "경쟁", "멀티플레이"],
                "reason": "조작은 직관적이지만 실력의 깊이는 매우 커요. 짧은 경기 안에서 과감한 플레이와 멋진 장면을 만들 수 있어요.",
                "mood": "지금 바로 한 판 승부를 보고 싶은 순간",
            },
            {
                "title": "에이펙스 레전드",
                "english": "Apex Legends",
                "icon": "🎯",
                "genres": ["FPS", "배틀로얄", "팀플레이"],
                "reason": "빠른 이동과 전투 판단이 중요해요. 위험을 감수한 플레이가 멋진 역전으로 이어질 수 있어요.",
                "mood": "긴장감 높은 팀 전투가 당기는 날",
            },
            {
                "title": "포르자 호라이즌 5",
                "english": "Forza Horizon 5",
                "icon": "🏁",
                "genres": ["레이싱", "오픈월드", "수집"],
                "reason": "멋진 차를 타고 자유롭게 달리며 다양한 이벤트에 즉시 참여할 수 있어요. 시원한 속도감이 강점이에요.",
                "mood": "아무 생각 없이 시원하게 달리고 싶을 때",
            },
        ],
    },
    "ESFP": {
        "symbol": "🎉",
        "nickname": "빛나는 무드메이커",
        "subtitle": "함께 웃고 바로 즐거워지는 플레이",
        "description": "화려하고 직관적이며 다른 사람과 재미를 나누기 쉬운 게임이 잘 맞아요. 순간의 즐거움을 크게 느껴요.",
        "keywords": ["즐거운 파티", "화려한 연출", "함께하는 재미"],
        "games": [
            {
                "title": "저스트 댄스",
                "english": "Just Dance",
                "icon": "💃",
                "genres": ["리듬", "파티", "음악"],
                "reason": "음악이 나오면 바로 몸을 움직이며 즐길 수 있어요. 친구들과 함께하면 분위기를 빠르게 끌어올릴 수 있어요.",
                "mood": "기분 전환이 필요하고 신나게 놀고 싶은 날",
            },
            {
                "title": "폴 가이즈",
                "english": "Fall Guys",
                "icon": "👑",
                "genres": ["파티", "경쟁", "캐주얼"],
                "reason": "규칙이 쉽고 상황이 계속 웃기게 흘러가요. 실패조차 재미있는 가벼운 경쟁을 즐길 수 있어요.",
                "mood": "부담 없이 웃으며 여러 판 하고 싶은 때",
            },
            {
                "title": "오버쿡드! 2",
                "english": "Overcooked! 2",
                "icon": "🍳",
                "genres": ["협동", "파티", "요리"],
                "reason": "친구들과 소리치고 웃으며 역할을 맞추는 게임이에요. 정신없는 상황 자체가 최고의 추억이 돼요.",
                "mood": "여럿이 모여 왁자지껄 놀고 싶은 날",
            },
        ],
    },
    "ENFP": {
        "symbol": "🌈",
        "nickname": "반짝이는 모험가",
        "subtitle": "새로운 세계와 사람을 자유롭게 만나는 플레이",
        "description": "변화가 많고 창의적인 선택이 가능하며, 예상하지 못한 이야기가 펼쳐지는 게임에서 신나게 몰입해요.",
        "keywords": ["새로운 경험", "자유로운 선택", "즐거운 교류"],
        "games": [
            {
                "title": "잇 테이크 투",
                "english": "It Takes Two",
                "icon": "🧸",
                "genres": ["협동", "어드벤처", "플랫포머"],
                "reason": "스테이지마다 완전히 다른 아이디어가 등장해 지루할 틈이 없어요. 함께 이야기하며 해결하는 재미도 커요.",
                "mood": "친한 사람과 특별한 모험을 떠나고 싶은 날",
            },
            {
                "title": "스플래툰 3",
                "english": "Splatoon 3",
                "icon": "🦑",
                "genres": ["슈팅", "경쟁", "스타일"],
                "reason": "화려한 색감과 빠른 경기, 개성 있는 꾸미기를 모두 즐길 수 있어요. 매 판 분위기가 달라 신선해요.",
                "mood": "톡톡 튀는 액션과 개성을 즐기고 싶을 때",
            },
            {
                "title": "드래곤 퀘스트 빌더즈 2",
                "english": "Dragon Quest Builders 2",
                "icon": "🧱",
                "genres": ["건설", "RPG", "탐험"],
                "reason": "모험과 건축, 주민들과의 이야기가 자연스럽게 이어져요. 떠오르는 아이디어를 마음껏 현실로 만들 수 있어요.",
                "mood": "상상한 것을 직접 만들며 모험하고 싶은 주말",
            },
        ],
    },
    "ENTP": {
        "symbol": "🎭",
        "nickname": "재치 있는 실험가",
        "subtitle": "규칙을 비틀고 색다른 전략을 시험하는 플레이",
        "description": "예측하기 어려운 상황, 기발한 시스템, 다른 사람과의 심리전처럼 생각을 계속 자극하는 게임이 잘 맞아요.",
        "keywords": ["기발한 발상", "변칙적인 전략", "유쾌한 심리전"],
        "games": [
            {
                "title": "더 스탠리 패러블: 울트라 디럭스",
                "english": "The Stanley Parable: Ultra Deluxe",
                "icon": "🚪",
                "genres": ["내러티브", "코미디", "메타"],
                "reason": "게임의 안내를 따를지 거스를지에 따라 이야기가 엉뚱하게 변해요. 규칙 자체와 장난치는 재미가 탁월해요.",
                "mood": "뻔한 전개를 벗어난 신선한 경험이 필요할 때",
            },
            {
                "title": "발라트로",
                "english": "Balatro",
                "icon": "🃏",
                "genres": ["덱빌딩", "로그라이크", "전략"],
                "reason": "익숙한 포커 규칙에 과감한 변칙을 더해 수많은 조합을 만들어요. 엉뚱한 전략이 강력해지는 쾌감이 있어요.",
                "mood": "새로운 조합을 계속 실험하고 싶은 날",
            },
            {
                "title": "어몽 어스",
                "english": "Among Us",
                "icon": "🛸",
                "genres": ["추리", "심리전", "파티"],
                "reason": "사실과 거짓을 섞어 다른 사람을 설득해야 해요. 즉흥적인 말과 심리전이 매 판 새로운 이야기를 만들어요.",
                "mood": "친구들과 떠들며 머리싸움을 하고 싶을 때",
            },
        ],
    },
    "ESTJ": {
        "symbol": "📋",
        "nickname": "확실한 지휘자",
        "subtitle": "목표를 세우고 효율적으로 운영하는 플레이",
        "description": "역할과 목표가 분명하고, 자원을 관리해 눈에 보이는 성과를 만드는 게임에서 강한 재미를 느껴요.",
        "keywords": ["효율적 운영", "명확한 성과", "주도적인 판단"],
        "games": [
            {
                "title": "투 포인트 캠퍼스",
                "english": "Two Point Campus",
                "icon": "🏫",
                "genres": ["경영", "건설", "시뮬레이션"],
                "reason": "시설과 인력, 학생 만족도를 조율해 캠퍼스를 성장시켜요. 관리 결과가 눈에 보이게 나타나 성취감이 커요.",
                "mood": "계획대로 조직이 돌아가는 기분을 느끼고 싶을 때",
            },
            {
                "title": "프로스트펑크",
                "english": "Frostpunk",
                "icon": "❄️",
                "genres": ["생존", "경영", "전략"],
                "reason": "한정된 자원과 시간 속에서 공동체를 이끌어야 해요. 어려운 결정을 내리고 결과를 책임지는 긴장감이 있어요.",
                "mood": "진지하고 밀도 높은 경영에 몰입하고 싶은 날",
            },
            {
                "title": "XCOM 2",
                "english": "XCOM 2",
                "icon": "🛰️",
                "genres": ["턴제 전술", "전략", "SF"],
                "reason": "부대를 구성하고 작전을 지휘하며 장기적인 전쟁까지 관리해요. 분명한 목표와 냉정한 판단이 중요해요.",
                "mood": "내가 직접 작전을 성공시키고 싶은 주말",
            },
        ],
    },
    "ESFJ": {
        "symbol": "🎀",
        "nickname": "따뜻한 호스트",
        "subtitle": "사람들과 공간을 돌보며 즐거움을 나누는 플레이",
        "description": "관계가 살아 있고, 다른 사람과 함께 목표를 이루거나 예쁜 공간을 가꾸는 게임이 자연스럽게 어울려요.",
        "keywords": ["즐거운 관계", "함께하는 목표", "아늑한 공간"],
        "games": [
            {
                "title": "팔리아",
                "english": "Palia",
                "icon": "🌻",
                "genres": ["생활", "온라인", "힐링"],
                "reason": "집을 꾸미고 마을 사람들과 친해지며 다른 플레이어와 편안하게 어울릴 수 있어요. 경쟁 부담도 적어요.",
                "mood": "사람 냄새 나는 편안한 세계에 머물고 싶을 때",
            },
            {
                "title": "디즈니 드림라이트 밸리",
                "english": "Disney Dreamlight Valley",
                "icon": "✨",
                "genres": ["생활", "꾸미기", "어드벤처"],
                "reason": "익숙한 캐릭터들을 돕고 마을을 예쁘게 가꿀 수 있어요. 관계와 꾸미기를 동시에 즐기기 좋아요.",
                "mood": "포근하고 반짝이는 일상을 만들고 싶은 날",
            },
            {
                "title": "오버쿡드! 2",
                "english": "Overcooked! 2",
                "icon": "🍳",
                "genres": ["협동", "파티", "요리"],
                "reason": "서로 역할을 나누고 도우며 하나의 목표를 완성해요. 함께할수록 재미가 커지는 대표적인 협동 게임이에요.",
                "mood": "친구들과 웃으며 팀워크를 맞추고 싶을 때",
            },
        ],
    },
    "ENFJ": {
        "symbol": "🌟",
        "nickname": "다정한 리더",
        "subtitle": "사람의 성장과 팀의 이야기를 이끄는 플레이",
        "description": "매력적인 동료들과 관계를 쌓고, 함께 성장해 더 큰 목표를 이루는 서사에 깊이 몰입하는 편이에요.",
        "keywords": ["동료의 성장", "관계 중심 서사", "협력과 리더십"],
        "games": [
            {
                "title": "페르소나 5 더 로열",
                "english": "Persona 5 Royal",
                "icon": "🎭",
                "genres": ["JRPG", "스토리", "관계"],
                "reason": "동료들의 고민을 이해하고 관계를 깊게 만들며 팀 전체가 성장해요. 스타일과 서사도 풍부해요.",
                "mood": "매력적인 동료들과 긴 이야기를 함께하고 싶을 때",
            },
            {
                "title": "잇 테이크 투",
                "english": "It Takes Two",
                "icon": "🧸",
                "genres": ["협동", "어드벤처", "스토리"],
                "reason": "서로 다른 능력을 가진 두 사람이 협력해야 앞으로 나아갈 수 있어요. 관계 회복이라는 주제도 따뜻해요.",
                "mood": "소중한 사람과 함께 웃고 협력하고 싶은 날",
            },
            {
                "title": "파이널 판타지 XIV",
                "english": "Final Fantasy XIV",
                "icon": "🛡️",
                "genres": ["MMORPG", "스토리", "협동"],
                "reason": "긴 서사와 다양한 동료, 역할별 협력이 어우러져요. 다른 사람을 돕고 팀을 이끄는 재미도 충분해요.",
                "mood": "오랫동안 머물 수 있는 큰 세계가 필요한 때",
            },
        ],
    },
    "ENTJ": {
        "symbol": "👑",
        "nickname": "야심 찬 사령관",
        "subtitle": "자원을 장악하고 승리의 구조를 만드는 플레이",
        "description": "큰 목표를 향해 빠르게 판단하고, 경쟁 우위를 만들며 복잡한 조직이나 국가를 이끄는 게임이 잘 맞아요.",
        "keywords": ["강력한 리더십", "거대한 목표", "경쟁 우위"],
        "games": [
            {
                "title": "프로스트펑크 2",
                "english": "Frostpunk 2",
                "icon": "🏙️",
                "genres": ["도시 건설", "정치", "전략"],
                "reason": "도시의 성장뿐 아니라 세력 간 이해관계와 장기 정책까지 조율해야 해요. 큰 결정을 내리는 맛이 강해요.",
                "mood": "복잡한 조직을 내 방식으로 이끌고 싶은 날",
            },
            {
                "title": "크루세이더 킹즈 III",
                "english": "Crusader Kings III",
                "icon": "🏰",
                "genres": ["대전략", "정치", "경영"],
                "reason": "가문과 영토, 외교와 계략을 수 세대에 걸쳐 설계해요. 야심찬 목표를 자신만의 방식으로 달성할 수 있어요.",
                "mood": "거대한 판에서 영향력을 넓히고 싶을 때",
            },
            {
                "title": "XCOM 2",
                "english": "XCOM 2",
                "icon": "🛰️",
                "genres": ["턴제 전술", "전략", "SF"],
                "reason": "장기 전략과 현장 전술을 동시에 지휘해요. 위험을 계산하고 제한된 자원으로 승리를 만드는 재미가 있어요.",
                "mood": "냉정한 판단으로 불리한 판을 뒤집고 싶은 날",
            },
        ],
    },
}

MBTI_ORDER = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]


# ---------------------------------------------------------
# HTML 렌더링 함수
# ---------------------------------------------------------
def safe(value):
    """고정 데이터라도 HTML 출력 전 이스케이프합니다."""
    return html.escape(str(value))


def render_game_card(game, primary=False):
    card_class = "game-card primary" if primary else "game-card"
    badge = '<div class="rank-badge">✦ 오늘의 1순위 추천</div>' if primary else ""
    tags = "".join(
        f'<span class="tag">{safe(genre)}</span>'
        for genre in game["genres"]
    )

    return f"""
        <div class="{card_class}">
            {badge}
            <div class="game-head">
                <div class="game-icon">{safe(game["icon"])}</div>
                <div>
                    <h3 class="game-title">{safe(game["title"])}</h3>
                    <div class="game-en">{safe(game["english"])}</div>
                </div>
            </div>
            <div class="tag-row">{tags}</div>
            <p class="game-reason">{safe(game["reason"])}</p>
            <div class="mood-line">추천 순간 · {safe(game["mood"])}</div>
        </div>
    """


def choose_another_game(game_count):
    current = st.session_state.get("recommendation_index", 0)
    candidates = [index for index in range(game_count) if index != current]
    st.session_state.recommendation_index = random.choice(candidates)


# ---------------------------------------------------------
# 화면
# ---------------------------------------------------------
st.markdown(
    """
    <section class="hero">
        <div class="eyebrow">MBTI × GAME CURATION</div>
        <h1 class="hero-title">
            나와 닮은 취향의<br>
            <span class="accent">게임을 만나보세요.</span>
        </h1>
        <p class="hero-copy">
            MBTI를 선택하면 플레이 성향에 어울리는 게임 세 편을
            부드럽고 감성적인 큐레이션으로 추천해 드려요.
        </p>
        <div class="soft-divider"></div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">01 · Select your type</div>', unsafe_allow_html=True)

selected_mbti = st.selectbox(
    "당신의 MBTI를 골라주세요",
    ["선택해주세요"] + MBTI_ORDER,
    index=0,
)

if selected_mbti == "선택해주세요":
    st.markdown(
        """
        <div class="intro-grid">
            <div class="mini-card">
                <div class="mini-icon">🎮</div>
                <div class="mini-title">취향 중심 추천</div>
                <div class="mini-copy">
                    성향과 플레이 스타일을 연결해 게임 세 편을 골라드려요.
                </div>
            </div>
            <div class="mini-card">
                <div class="mini-icon">🫧</div>
                <div class="mini-title">부드러운 큐레이션</div>
                <div class="mini-copy">
                    장르뿐 아니라 어떤 기분일 때 어울리는지도 함께 알려드려요.
                </div>
            </div>
            <div class="mini-card">
                <div class="mini-icon">✨</div>
                <div class="mini-title">가볍게 즐기기</div>
                <div class="mini-copy">
                    정답을 정하는 검사가 아니라 새로운 게임을 발견하는 작은 놀이예요.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    profile = PROFILES[selected_mbti]
    games = profile["games"]

    if st.session_state.get("last_mbti") != selected_mbti:
        st.session_state.last_mbti = selected_mbti
        st.session_state.recommendation_index = 0

    left, right = st.columns([3, 1])
    with left:
        st.markdown(
            f'<div class="section-label">02 · {safe(selected_mbti)} collection</div>',
            unsafe_allow_html=True,
        )
    with right:
        if st.button("다른 추천", use_container_width=True):
            choose_another_game(len(games))

    st.markdown(
        f"""
        <div class="profile-banner">
            <div class="profile-symbol">{safe(profile["symbol"])}</div>
            <div>
                <div class="profile-name">
                    {safe(selected_mbti)} · {safe(profile["nickname"])}
                </div>
                <div class="profile-subtitle">{safe(profile["subtitle"])}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_index = st.session_state.get("recommendation_index", 0)
    primary_game = games[selected_index]
    other_games = [
        game for index, game in enumerate(games)
        if index != selected_index
    ]

    st.markdown(render_game_card(primary_game, primary=True), unsafe_allow_html=True)

    st.markdown(
        '<div class="section-label">03 · More matches</div>',
        unsafe_allow_html=True,
    )

    game_columns = st.columns(2)
    for column, game in zip(game_columns, other_games):
        with column:
            st.markdown(render_game_card(game), unsafe_allow_html=True)

    keywords = "".join(
        f'<span class="keyword">#{safe(keyword)}</span>'
        for keyword in profile["keywords"]
    )

    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-title">왜 이런 게임이 잘 어울릴까요?</div>
            <p class="summary-copy">{safe(profile["description"])}</p>
            <div class="keyword-row">{keywords}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("MBTI 추천은 어떻게 봐야 하나요?"):
        st.write(
            "이 추천은 재미를 위한 가벼운 취향 큐레이션입니다. "
            "같은 MBTI라도 좋아하는 장르, 조작 난이도, 플레이 시간, "
            "혼자 또는 함께 플레이하는지에 따라 취향은 충분히 달라질 수 있어요."
        )

st.markdown(
    """
    <div class="footer-note">
        Made with Streamlit · 별도의 외부 라이브러리, 이미지, API 없이 동작합니다.<br>
        오늘의 기분에 맞는 게임 한 편을 가볍게 골라보세요. ♡
    </div>
    """,
    unsafe_allow_html=True,
)
