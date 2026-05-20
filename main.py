import streamlit as st
st.title('경민김의 웹앱!!!')
st.write('안녕하세요!!!😎')
import streamlit as st
import time

# 1. 페이지 기본 설정 및 기깔나는 테마 적용
st.set_page_config(
    page_title="경민김의 웹앱",
    page_icon="😎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 2. 커스텀 CSS로 스타일링 (폰트 및 애니메이션 효과)
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem !important;
        font-weight: 800;
        background: linear-gradient(90deg, #FF4B4B, #FF8533);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.5rem;
        color: #4A4A4A;
        font-weight: 500;
        margin-bottom: 2rem;
    }
    .highlight {
        background-color: #FFF0F0;
        padding: 20px;
        border-left: 5px solid #FF4B4B;
        border-radius: 5px;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 사이드바 (프로필 및 메뉴)
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500", use_container_width=True) # 세련된 추상화 이미지
    st.markdown("### 👤 Creator. 경민김")
    st.caption("고객을 사로잡는 기깔나는 웹앱을 만듭니다.")
    st.markdown("---")
    
    # 인터랙티브 소셜 링크 버튼
    st.markdown("**Contact & Link**")
    st.link_button("🌐 GitHub 바로가기", "https://github.com")
    st.link_button("✉️ 이메일 보내기", "mailto:kyungmin@example.com")

# 4. 메인 화면 상단 (타이틀 & 환영 인사)
st.markdown('<h1 class="main-title">경민김의 웹앱!!! 😎</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Streamlit으로 구현한 힙하고 멋진 공간입니다.</p>', unsafe_allow_html=True)

# 5. 메인 콘텐츠 (카드 형태의 레이아웃)
st.markdown('<div class="highlight"><h3>✨ Welcome!</h3>안녕하세요!!! 방문해 주셔서 진심으로 감사드립니다. 본 앱은 Streamlit의 강력한 기능을 활용하여 기깔나게 커스텀되었습니다.</div>', unsafe_allow_html=True)

# 6. 인터랙티브 기능 (재미 요소 추가)
st.markdown("### 🚀 무엇을 도와드릴까요?")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎉 환영 폭죽 터뜨리기", use_container_width=True):
        st.balloons()
        st.success("경민김의 웹앱에 오신 것을 환영합니다!")

with col2:
    if st.button("🔥 오늘의 응원 한마디", use_container_width=True):
        with st.spinner("생각 중..."):
            time.sleep(0.8)
        st.info("오늘도 당신의 하루는 기깔나게 멋질 겁니다! 화이팅! 💪")

# 7. 추가 위젯 (방문자 발자국 남기기)
st.markdown("---")
st.markdown("### 📝 방명록")
user_name = st.text_input("닉네임을 입력하세요", placeholder="홍길동")
user_comment = st.text_area("경민김에게 한마디 남겨주세요!", placeholder="웹앱 너무 멋져요...")

if st.button("제출하기", type="primary"):
    if user_name and user_comment:
        st.toast(f"✅ {user_name}님의 소중한 의견이 등록되었습니다!")
        st.markdown(f"**💬 {user_name}**: {user_comment}")
    else:
        st.warning("닉네임과 내용을 모두 입력해 주세요!")
