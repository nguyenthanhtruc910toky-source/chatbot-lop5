import streamlit as st
import random

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="Robot Toán Học Lớp 5 - Trợ lý Số Thập Phân",
    page_icon="🤖",
    layout="centered"
)

# Thêm CSS để giao diện thân thiện với học sinh tiểu học
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #e3f2fd, #ffffff);
    }
    h1 {
        color: #1e88e5;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
    }
    .chat-bubble-robot {
        background-color: #e1f5fe;
        padding: 15px;
        border-radius: 15px 15px 15px 0px;
        margin-bottom: 10px;
        border-left: 5px solid #0288d1;
        color: #0d47a1;
    }
    .chat-bubble-user {
        background-color: #efebe9;
        padding: 15px;
        border-radius: 15px 15px 0px 15px;
        margin-bottom: 10px;
        border-right: 5px solid #8d6e63;
        color: #3e2723;
        text-align: right;
    }
    .hint-box {
        background-color: #fff9c4;
        padding: 10px;
        border-radius: 10px;
        border: 1px dashed #fbc02d;
        font-size: 0.9em;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề ứng dụng
st.title("🤖 ROBOT TOÁN HỌC - BẠN ĐỒNG HÀNH LỚP 5")
st.subheader("Học về: Khái niệm Số Thập Phân (Bài 10)")

# Khởi tạo trạng thái lịch sử trò chuyện
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Chào các bạn học sinh lớp 5 đáng yêu! Thầy là Robot Toán Học đây. Hôm nay chúng mình cùng khám phá **Bài 10: Khái niệm số thập phân (Tiết 1)** nhé! Các em có câu hỏi gì về số thập phân hay đổi đơn vị đo lường không? Cứ hỏi thầy nhé! 🌟"}
    ]

# Gợi ý một số câu hỏi nhanh cho học sinh
st.markdown("### 💡 Gợi ý câu hỏi nhanh cho bạn:")
col1, col2 = st.columns(2)
with col1:
    q1 = st.button("❓ Số thập phân là gì vậy Robot?")
    q2 = st.button("❓ Hãy chỉ cho tớ cấu tạo của số 9,17?")
with col2:
    q3 = st.button("❓ Làm sao để đổi 3,2 m thành mm?")
    q4 = st.button("❓ Làm sao để đổi 1 kg thành tấn?")

# Xử lý khi nhấn nút câu hỏi nhanh
clicked_question = None
if q1: clicked_question = "Số thập phân là gì vậy Robot?"
elif q2: clicked_question = "Hãy chỉ cho tớ cấu tạo của số 9,17?"
elif q3: clicked_question = "Làm sao để đổi 3,2 m thành mm?"
elif q4: clicked_question = "Làm sao để đổi 1 kg thành tấn?"

# Hàm xử lý câu trả lời của Robot dựa trên bài học SGK Toán 5
def get_robot_response(user_query):
    query = user_query.lower()
    
    if "số thập phân là gì" in query or "khái niệm" in query:
        return (
            "Chào bạn! **Số thập phân** là một loại số đặc biệt gồm hai phần được phân cách bởi dấu phẩy:<br><br>"
            "1. **Phần nguyên:** gồm các chữ số ở bên trái dấu phẩy.<br>"
            "2. **Phần thập phân:** gồm các chữ số ở bên phải dấu phẩy.<br><br>"
            "Ví dụ: Số $0,4$ đọc là *không phẩy bốn*; số $0,05$ đọc là *không phẩy không năm*. Thật dễ hiểu đúng không nào! 😊"
        )
    
    elif "9,17" in query or "cấu tạo số 9" in query:
        return (
            "Ôi, số $9,17$ là một ví dụ tuyệt vời trong Bài 10 đấy! Hãy cùng phân tích cấu tạo của nó nhé:<br><br>"
            "👉 Số **$9,17$** gồm:<br>"
            " - **Phần nguyên** là **$9$** (nằm bên trái dấu phẩy).<br>"
            " - **Phần thập phân** là **$17$** (nằm bên phải dấu phẩy).<br><br>"
            "Chúng mình đọc số này là: *Chín phẩy mười bảy* nhé! Bạn đã rõ chưa nào? 🦊"
        )
        
    elif "3,2 m" in query or "3,2m" in query or "đổi 3,2" in query or "mm" in query:
        return (
            "Học sinh lớp 5 tinh mắt thế! Đây là Bài tập 2.b trong SGK đúng không nào?<br><br>"
            "Để đổi **$3,2\\text{ m}$** ra **milimét (mm)**, chúng mình làm như sau:<br>"
            " - Ta biết $1\\text{ m} = 1000\\text{ mm}$.<br>"
            " - Vậy $3,2\\text{ m}$ sẽ bằng: $3,2 \\times 1000 = 3200\\text{ mm}$!<br><br>"
            "Kết quả điền vào ô trống là **$3200$**. Quá đơn giản phải không? Thử tự làm với $4,5\\text{ kg}$ xem có ra $4500\\text{ g}$ không nhé! 💪"
        )
        
    elif "1 kg" in query or "tấn" in query or "0,001" in query:
        return (
            "Thầy Robot giải đáp ngay đây! Chúng mình cùng quan sát mẫu chuyển đổi đơn vị đo nhé:<br><br>"
            " - Ta có: $1\\text{ kg} = \\frac{1}{1000}\\text{ tấn}$ (vì $1\\text{ tấn} = 1000\\text{ kg}$).<br>"
            " - Khi viết dưới dạng số thập phân, ta được: **$0,001\\text{ tấn}$**.<br><br>"
            "Tương tự, nếu có $564\\text{ m}$, ta đổi sang kilômét như sau:<br>"
            " $564\\text{ m} = \\frac{564}{1000}\\text{ km} = 0,564\\text{ km}$! Thầy chúc bạn làm tốt các bài tập tương tự nhé! 🚀"
        )
        
    elif "13,2" in query or "132 mm" in query or "1,65" in query:
        return (
            "Trùng hợp quá, đây chính là các số thực tế trong Bài tập 3 vận dụng đấy!<br><br>"
            "📏 **$132\\text{ mm} = 13,2\\text{ cm}$**<br>"
            " - Phần nguyên là **$13$**<br>"
            " - Phần thập phân là **$2$** (đọc là *Mười ba phẩy hai*).<br><br>"
            "🧍‍♂️ Chiều cao của bạn nhỏ trong hình là **$1,65\\text{ m}$**<br>"
            " - Phần nguyên là **$1$**<br>"
            " - Phần thập phân là **$65$** (đọc là *Một phẩy sáu mươi lăm*).<br><br>"
            "Những số này đều được áp dụng rất nhiều trong đo đạc thực tế đấy nhé! Cố lên bạn nhỏ! 📐"
        )
        
    else:
        return (
            "Thầy Robot chưa hiểu rõ câu hỏi này của em lắm. Em có thể hỏi về:<br>"
            "1. Cách đọc các số thập phân (như $0,4$; $0,05$...)?<br>"
            "2. Phần nguyên và phần thập phân là gì?<br>"
            "3. Cách đổi đơn vị đo lường (m sang mm, kg sang g, kg sang tấn)?<br><br>"
            "Hãy thử nhập lại hoặc nhấn vào các nút gợi ý phía trên nhé! 🤖💖"
        )

# Hiển thị lịch sử trò chuyện
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f'<div class="chat-bubble-robot"><b>🤖 Robot Toán Học:</b><br>{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble-user"><b>🧒 Học sinh:</b><br>{message["content"]}</div>', unsafe_allow_html=True)

# Gửi câu hỏi mới
user_input = st.chat_input("Nhập câu hỏi của em tại đây...")

# Nếu học sinh gõ hoặc nhấn câu hỏi nhanh
query_to_send = None
if user_input:
    query_to_send = user_input
elif clicked_question:
    query_to_send = clicked_question

if query_to_send:
    # Thêm câu hỏi của học sinh vào lịch sử
    st.session_state.messages.append({"role": "user", "content": query_to_send})
    # Nhận câu trả lời từ robot
    response = get_robot_response(query_to_send)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Reload để cập nhật màn hình
    st.rerun()

# Phần chân trang thông tin bổ sung
st.markdown("---")
st.markdown(
    '<div class="hint-box"><b>💡 Mẹo nhỏ cho học sinh:</b><br>'
    'Khi làm bài toán đổi đơn vị: Hãy nhớ mối quan hệ giữa các đơn vị đo nhé! '
    'Ví dụ: 1 m = 1000 mm; 1 kg = 1000 g; 1 tấn = 1000 kg. Nhớ xem kĩ phần nguyên và phần thập phân nhé!</div>',
    unsafe_allow_html=True
)
