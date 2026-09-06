import streamlit as st
import google.generativeai as genai

# 1. Cấu hình khóa API Gemini AI
# Dán API Key mới của bạn vào giữa 2 dấu ngoặc kép dưới đây
GEMINI_API_KEY = "AQ.Ab8RN6Kc1aAOseG2qY_VWad7VnfDCojF6lGpn-HWumHOU_HcZA"

# Khởi tạo mô hình AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=(
        "Bạn là Robot Toán Học thân thiện, kiên nhẫn, chuyên giảng dạy môn Toán cho học sinh lớp 5 tại Việt Nam. "
        "Hãy giải thích chi tiết, dễ hiểu, trình bày rõ ràng từng bước và dùng ngôn ngữ vui tươi, động viên học sinh."
    )
)

# 2. Cấu hình giao diện Streamlit
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

# 3. Lịch sử trò chuyện
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Chào các bạn học sinh lớp 5 đáng yêu! Thầy là **Robot Toán Học** đây. Hôm nay chúng ta cùng khám phá **Bài 10: Khái niệm số thập phân (Tiết 1)** nhé! Các em có câu hỏi hay bài tập nào chưa hiểu cứ hỏi thầy nhé! 🌟"
        }
    ]

# Hiển thị lịch sử chat
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🎒"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 4. Xử lý khi học sinh đặt câu hỏi
user_input = st.chat_input("Viết câu hỏi của em tại đây...")
final_prompt = prompt_selected or user_input

if final_prompt:
    # Hiển thị câu hỏi của học sinh
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    with st.chat_message("user", avatar="🎒"):
        st.markdown(final_prompt)

    # Robot suy luận và trả lời
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Robot đang suy nghĩ câu trả lời..."):
            try:
                response = model.generate_content(final_prompt)
                bot_reply = response.text
                
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error("Robot đang kết nối lại với hệ thống AI, em hãy thử bấm gửi lại câu hỏi nhé!")
