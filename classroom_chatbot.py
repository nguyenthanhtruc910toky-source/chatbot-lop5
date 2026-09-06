import streamlit as st

# Tiêu đề ứng dụng
st.title("🤖 ROBOT TOÁN HỌC - KẾ ĐỒNG HÀNH LỚP 5")
st.subheader("Học về: Khái niệm Số Thập Phân (Bài 10)")

st.write("💡 **Gợi ý câu hỏi nhanh cho bạn:**")

# Tạo 4 nút gợi ý câu hỏi
col1, col2 = st.columns(2)

prompt_selected = None

with col1:
    if st.button("❓ Số phân tích là gì vậy Robot?"):
        prompt_selected = "Số phân tích là gì vậy Robot?"
    if st.button("❓ Hãy chỉ chọn để tạo cấu hình của số 9,17?"):
        prompt_selected = "Hãy chỉ chọn để tạo cấu hình của số 9,17?"

with col2:
    if st.button("❓ Làm sao để đổi 3,2 m thành mm?"):
        prompt_selected = "Làm sao để đổi 3,2 m thành mm?"
    if st.button("❓ Làm sao để đổi 1 kg thành tấn?"):
        prompt_selected = "Làm sao để đổi 1 kg thành tấn?"

# Khởi tạo lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "🤖 **Robot Toán Học:**\n\nChào các bạn học sinh lớp 5 đáng yêu! Thầy là Robot Toán học đây. Hôm nay chúng tôi cùng khám phá **Bài 10: Khái niệm số thập phân (Tiết 1)** nhé! Các em có câu hỏi về phân tích số liệu hay bài tập nào cần trợ giúp không nào? 🌟"
        }
    ]

# Hiển thị lịch sử tin nhắn
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Ô nhập câu hỏi
user_input = st.chat_input("Import câu hỏi của em tại đây...")

# Xử lý khi chọn nút hoặc nhập câu hỏi
final_prompt = prompt_selected or user_input

if final_prompt:
    # Lưu câu hỏi của học sinh
    st.session_state.messages.append({"role": "user", "content": final_prompt})
    with st.chat_message("user"):
        st.markdown(final_prompt)

    # Phản hồi từ Robot
    response = f"🤖 **Robot Toán Học:**\n\nCảm ơn em đã hỏi! Dưới đây là giải đáp cho câu hỏi *'{final_prompt}'*..."
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
