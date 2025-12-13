# ===========================
# DỮ LIỆU NGƯỜI DÙNG TRONG HỆ THỐNG
# ===========================
users = []  ## Mỗi user: {"email": ..., "password": ..., "role": ..., "locked": False, "login_fail": 0}
session = {"logged_in": False, "email": None}  ## Giả lập phiên đăng nhập


# ===========================
# 1) ĐĂNG KÝ TÀI KHOẢN (FORM + API)
# ===========================
def register_user():
    print("\n=== FORM ĐĂNG KÝ TÀI KHOẢN ===")
    email = input("Nhập email: ")
    password = input("Nhập mật khẩu: ")

    ## ---- API ĐĂNG KÝ GIẢ LẬP ----
    new_user = {
        "email": email,
        "password": password,
        "role": "user",
        "locked": False,
        "login_fail": 0
    }

    users.append(new_user)  ## Lưu vào database (tạm)
    print("✔ API /auth/register → Đăng ký thành công.")
# ===========================
# 2) ĐĂNG NHẬP HT
# ===========================
def login_user():
    pass