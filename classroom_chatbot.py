import streamlit as st
import google.generativeai as genai

# ==========================================
# PHẦN 1: CẤU HÌNH API VÀ AI
# ==========================================
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except Exception:
    st.error("Chưa cấu hình API Key trong mục Secrets của Streamlit Cloud!")
    st.stop() # Dừng chạy ứng dụng nếu không có API key

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction=(
        "Bạn là Robot Toán Học thân thiện, kiên nhẫn, chuyên giảng dạy môn Toán cho học sinh lớp 5 tại Việt Nam. "
        "Hãy giải thích chi tiết, dễ hiểu, trình bày rõ ràng từng bước và dùng ngôn ngữ vui tươi, động viên học sinh."
    )
)
)

# ==========================================
# PHẦN 2: CẤU HÌNH GIAO DIỆN NGƯỜI DÙNG
# ==========================================
st.set_page_config(page_title="Robot Toán Học Lớp 5", page_icon="🤖")

st.title("🤖 ROBOT TOÁN HỌC - BẠN ĐỒNG HÀNH LỚP 5")
st.subheader("Học về: Khái niệm Số Thập Phân (Bài 10)")
st.write("💡 **Gợi ý câu hỏi nhanh cho bạn:**")

# Các nút gợi ý
col1, col2 = st.columns(2)
prompt_selected = None

with col1:
    if st.button("❓ Số thập phân là gì vậy Robot?"):
        prompt_selected = "Số thập phân là gì vậy Robot?"
    if st.button("❓ Hãy cho biết cấu tạo của số 9,17?"):
        prompt_selected = "Hãy cho biết cấu tạo của số 9,17?"

with col2:
    if st.button("❓ Làm sao để đổi 3,2 m thành mm?"):
        prompt_selected = "Làm sao để đổi 3,2 m thành mm?"
    if st.button("❓ Làm sao để đổi 1 kg thành tấn?"):
        prompt_selected = "Làm sao để đổi 1 kg thành tấn?"

# ==========================================
# PHẦN 3: KHỞI TẠO BỘ NHỚ (GIẢI QUYẾT LỖI CHAT_SESSION)
# ==========================================
# 3.1 Nhớ các tin nhắn hiển thị trên màn hình
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chào các bạn học sinh lớp 5 đáng yêu! Thầy là **Robot Toán Học** đây. Hôm nay chúng ta cùng khám phá **Bài 10: Khái niệm số thập phân (Tiết 1)** nhé! Các em có câu hỏi hay bài tập nào chưa hiểu cứ hỏi thầy nhé! 🌟"
        }
    ]

# 3.2 Nhớ ngữ cảnh trò chuyện cho AI (Đoạn code bạn bị thiếu)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Hiển thị lại các tin nhắn cũ mỗi khi tải lại trang
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🎒"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ==========================================
# PHẦN 4: XỬ LÝ CÂU HỎI MỚI CỦA HỌC SINH
# ==========================================
user_input = st.chat_input("Viết câu hỏi của em tại đây...")
final_prompt = prompt_selected or user_input

if final_prompt:
    # 4.1 Hiển thị câu hỏi của học sinh lên màn hình
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    with st.chat_message("user", avatar="🎒"):
        st.markdown(final_prompt)

    # 4.2 Robot gửi câu hỏi cho AI và chờ trả lời
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Robot đang suy nghĩ câu trả lời..."):
            try:
                # Gửi tin nhắn có kèm bộ nhớ
                response = st.session_state.chat_session.send_message(final_prompt)
                bot_reply = response.text
                
                # In ra câu trả lời và lưu vào lịch sử
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                # Báo lỗi chi tiết nếu mất kết nối
                st.error(f"Lỗi kết nối AI: {e}")
