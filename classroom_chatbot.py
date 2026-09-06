import streamlit as st

# 1. Cấu hình trang (Tiêu đề, Icon, Bố cục)
st.set_page_config(
    page_title="Robot Toán Học Lớp 5 - Bạn Đồng Hành",
    page_icon="🤖",
    layout="centered"
)

# 2. Tùy chỉnh CSS để làm đẹp toàn bộ giao diện
st.markdown("""
    <style>
    /* Ẩn các thành phần mặc định của Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Thiết lập font chữ chung, thân thiện trẻ em */
    * {font-family: 'Open Sans', 'Segoe UI', sans-serif;}
    
    /* Tiêu đề chính */
    .main-title {
        text-align: center;
        color: #1E88E5; /* Màu xanh chủ đạo */
        font-size: 2.2rem;
        font-weight: 800;
        margin-top: -30px;
        margin-bottom: 5px;
    }
    
    /* Tiêu đề phụ */
    .sub-title {
        text-align: center;
        color: #555555;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    
    /* Làm đẹp khu vực "Gợi ý câu hỏi nhanh" */
    .section-title {
        color: #333333;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 15px;
    }
    
    /* Phong cách cho nút gợi ý tương tác */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #E0E0E0;
        background-color: #F8FBFF; /* Màu nền nhẹ của thẻ gợi ý */
        color: #333333;
        font-weight: 600;
        padding: 10px 15px;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
    }
    
    /* Hiệu ứng khi rê chuột vào nút gợi ý */
    div.stButton > button:hover {
        border-color: #1E88E5;
        background-color: #E3F2FD; /* Màu nền đậm hơn một chút */
        color: #1E88E5;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header giao diện
st.markdown("<h1 class='main-title'>🤖 ROBOT TOÁN HỌC - BẠN ĐỒNG HÀNH LỚP 5</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>📘 <b>Bài học:</b> Khái niệm Số Thập Phân (Bài 10)</p>", unsafe_allow_html=True)

# 4. Khu vực "Gợi ý câu hỏi nhanh" với các Thẻ tương tác
st.markdown("<p class='section-title'>💡 **Gợi ý câu hỏi nhanh cho em:**</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Nút bấm gợi ý, nhấn vào là tự gửi câu hỏi
prompt_selected = None

with col1:
    if st.button("❓ Số thập phân là gì vậy Robot?"):
        prompt_selected = "Số thập phân là gì vậy Robot?"
    if st.button("❓ Chỉ chọn để tạo cấu hình của số 9,17?"):
        prompt_selected = "Hãy chỉ chọn để tạo cấu hình của số 9,17?"

with col2:
    if st.button("❓ Làm sao để đổi 3,2 m thành mm?"):
        prompt_selected = "Làm sao để đổi 3,2 m thành mm?"
    if st.button("❓ Làm sao để đổi 1 kg thành tấn?"):
        prompt_selected = "Làm sao để đổi 1 kg thành tấn?"

st.divider()

# Khởi tạo lịch sử chat trong Session State nếu chưa có
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Chào các bạn học sinh lớp 5 đáng yêu! Thầy là **Robot Toán Học** đây. Hôm nay chúng ta cùng khám phá **Bài 10: Khái niệm số thập phân** nhé! Các em có câu hỏi nào chưa hiểu không? 🌟"
        }
    ]

# 5. Hiển thị lịch sử trò chuyện với Avatar riêng biệt
for message in st.session_state.messages:
    # Đặt avatar: Robot hoạt hình cho assistant, Học sinh hoạt hình cho user
    avatar = "https://raw.githubusercontent.com/tienthanh8495/img-host/main/robot_avatar.png" if message["role"] == "assistant" else "🎒"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 6. Xử lý khi học sinh nhập câu hỏi hoặc chọn từ gợi ý
user_input = st.chat_input("Nhập câu hỏi của em tại đây...")

# Nếu nhấn nút gợi ý hoặc nhập từ chat_input
final_prompt = prompt_selected or user_input

if final_prompt:
    # Thêm câu hỏi học sinh vào lịch sử
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    
    # Hiển thị ngay lập tức lên màn hình
    with st.chat_message("user", avatar="🎒"):
        st.markdown(final_prompt)

    # 7. Xử lý phản hồi từ Robot (Nơi xử lý logic AI của bạn)
    with st.chat_message("assistant", avatar="https://raw.githubusercontent.com/tienthanh8495/img-host/main/robot_avatar.png"):
        # Viết câu trả lời mẫu hoặc gọi API AI của bạn tại đây
        response = f"Cảm ơn em đã hỏi! Dưới đây là giải đáp cho câu hỏi *'{final_prompt}'* của em..."
        st.markdown(response)
        
    # Lưu câu trả lời của Robot vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": response})
