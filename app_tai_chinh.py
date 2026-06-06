import streamlit as st
import math

# 1. Cấu hình trang web Streamlit
st.set_page_config(page_title="Hệ Thống Phân Tích Tài Chính", page_icon="💰", layout="wide")
st.title("💰 HỆ THỐNG PHÂN TÍCH GIAO DỊCH VÀ TIỆN ÍCH TOÁN HỌC")
st.write("Bài tập tổng hợp: Tự nhập dữ liệu phát hiện bất thường & Tính toán tài chính")

# Tạo các tab phân chia chức năng
tab1, tab2 = st.tabs(["🔍 Kiểm Tra Giao Dịch Bất Thường", "🧮 Tiện Ích Toán Học & Lợi Nhuận"])

# ==========================================
# TAB 1: PHÁT HIỆN GIAO DỊCH TỰ NHẬP BẤT THƯỜNG
# ==========================================
with tab1:
    st.header("🔍 Kiểm Tra Giao Dịch Bất Thường (Nhập Tay)")
    st.write("Hãy điền thông tin giao dịch dưới đây để hệ thống tự động phân tích dấu hiệu rủi ro.")

    # Tạo form nhập liệu cho 1 giao dịch
    col_a, col_b = st.columns(2)
    
    with col_a:
        ma_gd = st.text_input("Mã giao dịch:", value="GD1024")
        loai_gd = st.selectbox("Loại giao dịch:", ["Chuyển khoản thường", "Thanh toán hóa đơn", "Rút tiền mặt", "Chuyển khoản quốc tế"])
    
    with col_b:
        so_tien = st.number_input("Số tiền giao dịch (VND):", min_value=0, value=20000000, step=500000)
        nguong_canh_bao = st.number_input("Cài đặt ngưỡng cảnh báo rủi ro (VND):", min_value=0, value=50000000, step=1000000)

    # Nút bấm kiểm tra
    if st.button("🚀 Kiểm tra giao dịch này"):
        st.markdown("---")
        st.subheader("📊 Kết quả phân tích giao dịch:")
        
        # Hiển thị lại thông tin
        st.write(f"- Mã giao dịch: **{ma_gd}**")
        st.write(f"- Hình thức: **{loai_gd}**")
        st.write(f"- Số tiền: **{so_tien:,.0f} VND**")
        
        # Thuật toán kiểm tra bất thường (Lý do 1: Vượt ngưỡng | Lý do 2: Giao dịch quốc tế số tiền lớn)
        if so_tien > nguong_canh_bao:
            st.error(f"🚨 CẢNH BÁO: Giao dịch có dấu hiệu BẤT THƯỜNG! Số tiền đã vượt ngưỡng an toàn {so_tien - nguong_canh_bao:,.0f} VND.")
        elif loai_gd == "Chuyển khoản quốc tế" and so_tien > 30000000:
            st.warning("⚠️ CẢNH BÁO RỦI RO: Giao dịch chuyển khoản quốc tế có giá trị cao (> 30 triệu VND). Cần xác minh danh tính!")
        else:
            st.success("✅ Giao dịch AN TOÀN! Không phát hiện dấu hiệu bất thường.")

# ==========================================
# TAB 2: CÁC TIỆN ÍCH TOÁN HỌC & LÃI SUẤT
# ==========================================
with tab2:
    st.header("🧮 Khối Tiện Ích Tính Toán Tích Hợp")
    st.markdown("---")
    
    # --- Chức năng 1: Tính Giai Thừa ---
    st.subheader("1. 🔢 Tính Giai Thừa (n!)")
    n_input = st.number_input("Nhập số nguyên dương n (0 <= n <= 100):", min_value=0, max_value=100, value=5, step=1)
    if st.button("Tính Giai Thừa"):
        result_factorial = math.factorial(n_input)
        st.success(f"Kết quả: **{n_input}! = {result_factorial}**")
        
    st.markdown("---")
    
    # --- Chức năng 2: Tính Giá Trị Trung Bình ---
    st.subheader("2. 📈 Tính Giá Trị Trung Bình Danh Sách Số")
    numbers_str = st.text_input("Nhập dãy số (cách nhau bằng dấu phẩy, ví dụ: 10, 20, 30, 40):", value="10, 20, 30, 40")
    if st.button("Tính Trung Bình"):
        try:
            num_list = [float(x.strip()) for x in numbers_str.split(",") if x.strip() != ""]
            if len(num_list) > 0:
                avg_value = sum(num_list) / len(num_list)
                st.success(f"Danh sách số đã nhập: {num_list}")
                st.info(f"👉 Giá trị trung bình là: **{avg_value:.2f}**")
            else:
                st.warning("Vui lòng nhập danh sách số hợp lệ.")
        except ValueError:
            st.error("Lỗi: Vui lòng chỉ nhập số và ngăn cách bằng dấu phẩy.")

    st.markdown("---")
    
    # --- Chức năng 3: Tính Lợi Nhuận Sau 12 Tháng (Lãi kép) ---
    st.subheader("3. 💵 Tính Lợi Nhuận Sau 12 Tháng (Vốn ban đầu + Lãi suất)")
    
    principal = st.number_input("Nhập số tiền gốc ban đầu (VND):", min_value=0.0, value=10000000.0, step=500000.0)
    interest_rate_year = st.number_input("Nhập tỷ lệ lãi suất năm (% / năm):", min_value=0.0, max_value=100.0, value=6.0, step=0.1)
    
    if st.button("Tính Lợi Nhuận Dự Kiến"):
        rate_per_month = (interest_rate_year / 100) / 12
        final_amount = principal * math.pow((1 + rate_per_month), 12)
        profit = final_amount - principal
        
        st.subheader("💰 Bảng tổng kết dòng tiền sau 12 tháng:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Vốn gốc ban đầu", value=f"{principal:,.0f} VND")
        with col2:
            st.metric(label="Tiền lãi nhận được", value=f"{profit:,.0f} VND", delta=f"+{interest_rate_year}% /năm")
        with col3:
            st.metric(label="Tổng số tiền nhận về (Gốc + Lãi)", value=f"{final_amount:,.0f} VND")