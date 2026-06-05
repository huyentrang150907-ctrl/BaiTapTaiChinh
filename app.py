import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Đọc dữ liệu từ file CSV
# Đảm bảo file 'financial_anomaly_data.csv' nằm cùng thư mục với file code này
try:
    print("Đang đọc dữ liệu... vui lòng đợi...")
    df = pd.read_csv('financial_anomaly_data.csv')
    print("--- Đã nạp dữ liệu thành công! ---")
    
    # 2. Tiền xử lý: Chỉ chọn các cột chứa con số để tính toán
    # AI không hiểu được chữ, nên ta chỉ lấy các cột số (float, int)
    data_numeric = df.select_dtypes(include=['float64', 'int64'])
    
    # Xử lý nếu có ô trống (điền bằng số 0 hoặc giá trị trung bình)
    data_numeric = data_numeric.fillna(0)

    # 3. Khởi tạo mô hình Isolation Forest (Rừng cô lập)
    # contamination=0.05 nghĩa là ta nghi ngờ có khoảng 5% dữ liệu là bất thường
    model = IsolationForest(contamination=0.05, random_state=42)

    # 4. Yêu cầu AI học và tìm điểm bất thường
    # Kết quả: 1 là bình thường, -1 là bất thường (điểm lạ)
    df['ket_qua'] = model.fit_predict(data_numeric)

    # 5. Thống kê kết quả
    so_luong_bat_thuong = len(df[df['ket_qua'] == -1])
    print(f"==> Kết quả: Phát hiện {so_luong_bat_thuong} giao dịch bất thường.")

    # 6. Hiển thị giao dịch đáng nghi nhất ra màn hình
    print("\nDanh sách giao dịch bất thường :")
    print(df[df['ket_qua'] == -1].head())

    # 7. LƯU BIỂU ĐỒ THÀNH FILE ẢNH (Giải pháp thay thế khi không hiện cửa sổ)
    print("Dang ve bieu do va luu thanh file 'ketqua_bai5.png'...")
    plt.figure(figsize=(10, 6))
    
    # Vẽ các điểm bình thường (màu đỏ) và bất thường (màu xanh)
    plt.scatter(range(len(df)), data_numeric.iloc[:, 0], c=df['ket_qua'], cmap='coolwarm', s=10)
    
    plt.title("Ket qua phat hien bat thuong - Bai thuc hanh 5")
    plt.xlabel("STT Giao dich")
    plt.ylabel("Gia tri")
    
    # Lưu file ảnh ngay tại thư mục hiện tại
    plt.savefig('ketqua_bai5.png')
    print("DA XONG! Ban hay mo file 'ketqua_bai5.png' o cot ben trai de xem.")

except FileNotFoundError:
    print("LOI: Khong tim thay file 'financial_anomaly_data.csv'.")
    print("Ban hay chac chan da giai nen file archive.zip va copy file CSV vao dung thu muc chua code.")
except Exception as e:
    print(f"Co loi xay ra: {e}")