import streamlit as st

# 1. Cấu hình trang (Tiêu đề tab trình duyệt + Cấu hình căn giữa)
st.set_page_config(
    page_title="Robot Toán Học Lớp 5",
    page_icon="🤖",
    layout="centered"
)

# 2. Tùy chỉnh CSS để làm đẹp giao diện
st.markdown("""
    <style>
    /* Ẩn bớt footer mặc định của Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Thiết lập font chữ và tiêu đề chính */
    .main-title {
        text-align: center;
        color: #1E88E5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    
    /* Làm đẹp khung gợi ý câu hỏi */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #E0E0E0;
        background-color: #F9F9F9;
        color: #333333;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        border-color: #1E88E5;
        background-color: #E3F2FD;
        color: #1E88E5;
    }
    </style>
""", unsafe_allow_html=True)

# Header giao diện
st.markdown("<h1 class='main-title'>🤖 ROBOT TOÁN HỌC - BẠN ĐỒNG HÀNH LỚP 5</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>📘 <b>Bài học:</b> Khái niệm Số Thập Phân (Bài 10)</p>", unsafe_allow_html=True)

# Khởi tạo lịch sử chat trong Session State nếu chưa có
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Chào các bạn học sinh lớp 5 đáng yêu! Thầy là **Robot Toán Học** đây. Hôm nay chúng ta cùng khám phá **Bài 10: Khái niệm số thập phân** nhé! Các em có câu hỏi nào chưa hiểu không? 🌟"
        }
    ]

# 3. Khu vực Gợi ý câu hỏi nhanh (Interactive Quick Prompts)
st.markdown("##### 💡 **Gợi ý câu hỏi nhanh cho em:**")

col1, col2 = st.columns(2)

prompt_selected = None

with col1:
    if st.button("❓ Số thập phân là gì vậy Robot?"):
        prompt_selected = "Số thập phân là gì vậy Robot?"
    if st.button("❓ Hãy chỉ chọn để tạo cấu hình của số 9,17?"):
        prompt_selected = "Hãy chỉ chọn để tạo cấu hình của số 9,17?"

with col2:
    if st.button("❓ Làm sao để đổi 3,2 m thành mm?"):
        prompt_selected = "Làm sao để đổi 3,2 m thành mm?"
    if st.button("❓ Làm sao để đổi 1 kg thành tấn?"):
        prompt_selected = "Làm sao để đổi 1 kg thành tấn?"

st.divider()

# 4. Hiển thị lịch sử trò chuyện với Avatar riêng biệt
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🎒"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 5. Xử lý khi học sinh nhập câu hỏi hoặc chọn từ gợi ý
user_input = st.chat_input("Nhập câu hỏi của em tại đây...")

# Nếu nhấn nút gợi ý hoặc nhập từ chat_input
final_prompt = prompt_selected or user_input

if final_prompt:
    # Thêm câu hỏi học sinh vào lịch sử
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    
    # Hiển thị ngay lập tức lên màn hình
    with st.chat_message("user", avatar="🎒"):
        st.markdown(final_prompt)

    # Xử lý phản hồi từ Robot (Nơi xử lý logic AI)
    with st.chat_message("assistant", avatar="🤖"):
        # Viết câu trả lời mẫu hoặc gọi API AI của bạn tại đây
        response = f"Cảm ơn em đã hỏi! Dưới đây là giải đáp cho câu hỏi: *'{final_prompt}'*..."
        st.markdown(response)
        
    # Lưu câu trả lời của Robot vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": response})
