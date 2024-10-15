# -*- coding: utf-8 -*-
import time
import os

# Kiểm tra và cài đặt các thư viện cần thiết nếu chưa có
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from colorama import Fore, Back, Style, init
    import pyautogui
    import random
    import getpass

except ImportError:
    os.system("pip install seleniumbase")
    os.system("pip install selenium")
    os.system("pip install pyautogui")
    os.system("pip install colorama")
    from colorama import Fore, Back, Style, init
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import pyautogui
    import random
    import getpass


from time import sleep

"""HÀM XỬ LÝ CỨNG"""

"""chuyển tap"""


def ChuyenTab1():
    driver.switch_to.window(driver.window_handles[0])


def ChuyenTab2():
    driver.switch_to.window(driver.window_handles[1])


# Khởi tạo trình duyệt với tùy chọn ẩn hoặc hiện
def khoi_tao_trinh_duyet(che_do_an=False):
    chrome_options = Options()

    if che_do_an:
        # Chế độ headless (ẩn trình duyệt)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(
            "--window-size=1920x1080"
        )  # Đảm bảo kích thước hiển thị đúng
        # print("Trình duyệt đang chạy ở chế độ ẩn.")
    else:
        # print("Trình duyệt đang chạy ở chế độ hiển thị.")
        pass

    # Khởi tạo trình duyệt Chrome với các tùy chọn đã thiết lập
    driver = webdriver.Chrome(options=chrome_options)
    return driver


# Ví dụ sử dụng:
# Khởi tạo trình duyệt ở chế độ ẩn
# driver = khoi_tao_trinh_duyet(che_do_an=True)

# Khởi tạo trình duyệt ở chế độ hiển thị
# driver = khoi_tao_trinh_duyet(che_do_an=False)


# Upload file
def upload_file(file_name):
    # Đợi hộp thoại tải lên mở ra
    time.sleep(2)

    # Lấy đường dẫn đầy đủ của tệp trong thư mục hiện hành
    current_directory = os.getcwd()  # Lấy thư mục hiện hành
    file_path = os.path.join(current_directory, file_name)  # Kết hợp thư mục và tên tệp

    # Nhập đường dẫn tệp vào hộp thoại
    pyautogui.write(file_path)

    # Nhấn Enter để xác nhận tải file lên
    pyautogui.press("enter")


"""HÀM XỬ LÝ VÙNG CHỌN TỰ ĐỘNG HÓA"""


# - - - Nếu phần tử có sẵn có thể click được thì dùng hàm này
def autoKhiPhanTuCoTheClickDuoc_ID(boXuLy, thoiGianXuLy, idd):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.element_to_be_clickable((By.ID, idd))
    )


def autoKhiPhanTuCoTheClickDuoc_CLASS_NAME(boXuLy, thoiGianXuLy, className):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.element_to_be_clickable((By.CLASS_NAME, className))
    )


def autoKhiPhanTuCoTheClickDuoc_XPATH(boXuLy, thoiGianXuLy, xPath):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.element_to_be_clickable((By.XPATH, xPath))
    )


def autoKhiPhanTuCoTheClickDuoc_CSS_SELECTOR(boXuLy, thoiGianXuLy, cssSelector):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, cssSelector))
    )


"""# - - - Nếu đợi phần tử cần hiển thị thì dùng hàm này"""


def autoDoiPhanTuHienThi_ID(boXuLy, thoiGianXuLy, idd):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.visibility_of_element_located((By.ID, idd))
    )


def autoDoiPhanTuHienThi_CLASS_NAME(boXuLy, thoiGianXuLy, className):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.visibility_of_element_located((By.CLASS_NAME, className))
    )


def autoDoiPhanTuHienThi_XPATH(boXuLy, thoiGianXuLy, xPath):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.visibility_of_element_located((By.XPATH, xPath))
    )


def autoDoiPhanTuHienThi_CSS_SELECTOR(boXuLy, thoiGianXuLy, cssSelector):
    return WebDriverWait(boXuLy, thoiGianXuLy).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, cssSelector))
    )


""" Hàm LOGIN"""


# Nhap Hashcode
def NhapHashcodeVaLamBai():
    os.system("cls")
    #
    print("Nhập Hashcode cho bài cần làm (Chưa biết lấy hãy xem trong hướng dẫn):")
    hashcode = input("[HASHCODE]: ")

    ChuyenTab1()
    driver.get(f"https://lms.ictu.edu.vn/assignment/weekly?hashcode={hashcode}")
    # test()

    try:
        checkbox = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 10, ".p-checkbox-label"
        ).click()  # checkbox

        batDauLam = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 2, ".p-button-label"
        ).click()  # làm bài
    except:
        os.system("cls")
        for i in range(4, 0, -1):
            print(
                Fore.RED
                + "[LỖI]: Hashcode không hợp lệ hoặc có thể đã hết hạn. Vui lòng kiểm tra lại hướng dẫn để biết thêm thông tin và thử lại sau nhé!"
            )
            print(f"[HÃY THỬ LẠI SAU {i} GIÂY]")
            sleep(1)
            os.system("cls")
        NhapHashcodeVaLamBai()


# Login BingAI
def LoginBingAI():
    ### Đăng nhập
    driver.execute_script("window.open('');")  # motap2
    # driver.switch_to.window(driver.window_handles[1])  # dieukhientap2
    ChuyenTab2()
    driver.get("https://copilot.microsoft.com")
    print(
        Fore.RED
        + "[PHẢN HỒI]: Tool Auto không thể thực hiện được các bước xác minh này. Để đảm bảo an toàn và thành công \ntrong việc đăng nhập, bạn cần thực hiện bằng tay những bước xác minh tài khoản của MICROSOFT."
    )
    print(
        "- - - - - - - - - - - - - - - - - - -* * * - - - - - - - - - - - - - - - - - - -"
    )
    xacNhan = input("[ẤN ENTER NẾU BẠN ĐĂNG NHẬP THÀNH CÔNG]...")


def LoginBlackBoxAI():
    driver.execute_script("window.open('');")  # motap2
    # ChuyenTab2()
    # driver.get("https://www.blackbox.ai/")


"""Hàm Xử Lý Làm Bài"""

"""======================================== [QUÁ TRÌNH LÀM BÀI] ========================================"""


# chon đáp án
def ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi):
    # test()
    ChuyenTab1()
    # Tính toán chỉ số CSS Selector dựa trên số câu hỏi
    codeCauTraLoi = 2 + (cauSo - 1) * 4  # trích xuất css_selector từ câu hỏi
    dapAnA = f"#mat-radio-{codeCauTraLoi} .mdc-label"
    dapAnB = f"#mat-radio-{codeCauTraLoi + 1} .mdc-label"
    dapAnC = f"#mat-radio-{codeCauTraLoi + 2} .mdc-label"
    dapAnD = f"#mat-radio-{codeCauTraLoi + 3} .mdc-label"
    # chọn a b c d
    if cauTraLoi == "A" or cauTraLoi == "a" or cauTraLoi == "1":
        ChonDapAn = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 300, dapAnA)
        ChonDapAn.click()
    elif cauTraLoi == "B" or cauTraLoi == "b" or cauTraLoi == "2":
        ChonDapAn = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 300, dapAnB)
        ChonDapAn.click()
    elif cauTraLoi == "C" or cauTraLoi == "c" or cauTraLoi == "3":
        ChonDapAn = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 300, dapAnC)
        ChonDapAn.click()
    elif cauTraLoi == "D" or cauTraLoi == "d" or cauTraLoi == "4":
        ChonDapAn = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 300, dapAnD)
        ChonDapAn.click()
    else:
        pass
        # Bạn hoàn thiện giúp tôi nếu không chọn được đáp án thì gọi lại hàm tracuuBingAI ra để gọi lại
    # bấm câu hỏi tiếp theo
    cauHoiTiepTheo = autoDoiPhanTuHienThi_CSS_SELECTOR(
        driver, 30, ".ictu-page-test__test-panel__single-nav__btn-control"
    )
    cauHoiTiepTheo.click()


# chụp màn hình câu hỏi hiện tại, dán vào là chụp tap đó
def ChupManHinhCauHoiHienTai(cauHoiHienTai):
    setTime = time.localtime()

    ChuyenTab1()
    # test()
    sleep(2)
    tep = f"{setTime.tm_min}_{cauHoiHienTai}.png"
    tep1 = f"{setTime.tm_min}_{cauHoiHienTai}(1).png"
    tep2 = f"{setTime.tm_min}_{cauHoiHienTai}(2).png"
    tep3 = f"{setTime.tm_min}_{cauHoiHienTai}(3).png"

    # nếu tẹp trùng
    if os.path.exists(tep):  # nếu tệp tồn tại thì thêm số đằng sau
        driver.save_screenshot(tep1)
        return tep1
    if os.path.exists(tep1):
        driver.save_screenshot(tep2)
        return tep2
    if os.path.exists(tep2):
        driver.save_screenshot(tep3)
        return tep3
    # Nếu không có tệp trùng trả về text câu hỏi hiện tại là bao nhiêu
    driver.save_screenshot(tep)
    return tep


# tra con chat bing - return câu trả lời khi AI trả lời
def TraCuuBingAI(fileCanUpload, khongTimDuocCauTraLoi=0, max_attempts=3):
    ChuyenTab2()
    driver.refresh()
    # test()
    # giới hạn số lần thử để tránh vòng lặp vô hạn
    if khongTimDuocCauTraLoi >= max_attempts:
        return (
            Fore.RED
            + "[LỖI]: Đã thử nhiều lần nhưng không nhận được câu trả lời hợp lệ."
        )

    try:
        # upload file len bing
        upAnh = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".relative:nth-child(2) > .absolute .size-6"
        )
        upAnh.click()
        sleep(2)
        upload_file(fileCanUpload)

        # gửi yêu cầu trả lời
        userInput = autoDoiPhanTuHienThi_ID(driver, 30, "userInput")
        userInput.click()
        userInput.send_keys(
            "Vui lòng chú ý cau hỏi trong ảnh mà tôi gửi và chỉ trả lời duy nhất một ký tự đại diện cho đáp án chính xác (A, B, C hoặc D). Không thêm bất kỳ văn bản nào khác hoặc ký tự nào khác vào câu trả lời. Chỉ xuất ra duy nhất ký tự."
        )
        userInput.send_keys(Keys.SHIFT, Keys.ENTER)

        userInput.send_keys(
            "Tôi rõ ràng đã bảo là quan sát kỹ ảnh, chỉ trả lời đúng một ký tự: A, B, C hoặc D. Không thêm văn bản thừa. Không thêm bất kỳ từ ngữ hoặc dấu câu nào khác (Không thêm dấu chấm đằng sau nha ví dụ: B. (không hợp lệ)). Chỉ xuất ra đúng một ký tự."
        )

        # click gui
        send = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".text-foreground-800 > .size-6"
        )
        sleep(2.5)
        send.click()

        sleep(2.5)

        # lay cau tra loi
        answer = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".space-y-3:nth-child(2) > .space-y-3 span"
        )
        cauTraLoi = answer.text.strip()

        # xcheck xem cau hoi hop le chua
        if cauTraLoi in ["A", "B", "C", "D"]:
            return cauTraLoi
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBingAI(fileCanUpload, khongTimDuocCauTraLoi, max_attempts)

    except Exception as e:
        print(
            Fore.RED
            + f"[LỖI]: Ơ có lỗi gì thế nhỉ, bạn đăng nhập thành công BingAI chưa, phải đăng nhập mới làm được nhé^^"
        )
        return TraCuuBingAI(fileCanUpload, khongTimDuocCauTraLoi + 1, max_attempts)

    # searchbox = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 30, "searchbox")
    # searchbox.send_keys(
    #     "Bạn chỉ cần hiện thị đáp án không cần hiện thị câu trả lời ví dụ: \nCâu hỏi: 1+1 = ?\nA.1\nB.2\nC.3\nD.4\nBạn chỉ cần trả lời là : A (không có kí tự gì đằng sau)\n---"
    #     + cauHoi
    # )


def test():
    c = input("testing to ok: ")


def TraCuuBlackBoxAI(fileCanUpload, khongTimDuocCauTraLoi=0, max_attempts=3):
    ChuyenTab2()
    driver.get("https://www.blackbox.ai/")

    # driver.get("https://www.blackbox.ai/")
    if khongTimDuocCauTraLoi >= max_attempts:
        return (
            Fore.RED
            + "[LỖI]: Đã thử nhiều lần nhưng không nhận được câu trả lời hợp lệ."
        )
    try:  #:
        clickDeUpFile = autoDoiPhanTuHienThi_XPATH(
            driver,
            30,
            "/html/body/div[2]/main/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/form/div[4]/div[1]/div[3]",
        ).click()

        clickDeUpFile2 = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".cursor-default:nth-child(1)"
        ).click()
        sleep(2)
        upload_file(fileCanUpload)

        input = autoDoiPhanTuHienThi_ID(driver, 30, "chat-input-box")
        input.click()
        input.send_keys(
            "@@GPT-4o "
            + "Vui lòng chú ý cau hỏi trong ảnh mà tôi gửi và chỉ trả lời duy nhất một ký tự đại diện cho đáp án chính xác (A, B, C hoặc D). Không thêm bất kỳ văn bản nào khác hoặc ký tự nào khác vào câu trả lời. Chỉ xuất ra duy nhất ký tự."
        )
        input.send_keys(Keys.SHIFT, Keys.ENTER)
        input.send_keys(
            "Tôi rõ ràng đã bảo là quan sát kỹ ảnh, chỉ trả lời đúng một ký tự: A, B, C hoặc D. Không thêm văn bản thừa. Không thêm bất kỳ từ ngữ hoặc dấu câu nào khác (Không thêm dấu chấm đằng sau nha ví dụ: B. (không hợp lệ)). Chỉ xuất ra đúng một ký tự."
        )
        sleep(1)
        # send

        # pyautogui.press("enter")
        input.send_keys(Keys.ENTER)

        nhanCauTraLoi = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".prose:nth-child(3) > .mb-2"
        )
        answer = nhanCauTraLoi.text
        cauTraLoi = answer.strip()
        # print(cauTraLoi)
        # xcheck xem cau hoi hop le chua
        if cauTraLoi in ["A", "B", "C", "D"]:
            return cauTraLoi
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBlackBoxAI(fileCanUpload, khongTimDuocCauTraLoi, max_attempts)
    except Exception as e:
        print(Fore.RED + f"[LỖI]: {e} Có một vài lỗi tại BlackBoxAI bạn hãy thử lại^^")
        return TraCuuBlackBoxAI(fileCanUpload, khongTimDuocCauTraLoi + 1, max_attempts)


""" =================================== [THỰC THI LÀM BÀI] ===================================="""


def QuaTrinhLamBai():  # BẢN DÀNH CHO BINGAI -------------- BINGAI
    cauSo = 0  # khoitao
    cauTraLoi = ""  # khoitao
    print(
        "===================================== [PHẢN HỒI] ====================================="
    )
    while True:
        if cauSo == 15:
            break
        else:
            cauSo += 1  # tăng câu hỏi mỗi lần hoàn thành, lần đầu sẽ = 1
            fileCauHoi = ChupManHinhCauHoiHienTai(cauSo)  # lấy file câu hỏi
            sleep(1)
            cauTraLoi = TraCuuBingAI(fileCanUpload=fileCauHoi)  # tra cứu câu hỏi đó
            sleep(1)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            sleep(1)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


def QuaTrinhLamBai_2():  # BẢN DÀNH CHO BLACKBOX -------------- BLACKBOX---
    cauSo = 0  # khoitao
    cauTraLoi = ""  # khoitao
    print(
        "===================================== [PHẢN HỒI] ====================================="
    )
    while True:
        if cauSo == 15:
            break
        else:
            cauSo += 1  # tăng câu hỏi mỗi lần hoàn thành, lần đầu sẽ = 1
            fileCauHoi = ChupManHinhCauHoiHienTai(cauSo)  # lấy file câu hỏi
            sleep(1)
            cauTraLoi = TraCuuBlackBoxAI(fileCanUpload=fileCauHoi)  # tra cứu câu hỏi đó
            sleep(1)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            sleep(1)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


# Thực thi bản BingAI    BINGAI---------------
def ThucThi_BingAI():
    LoginBingAI()
    NhapHashcodeVaLamBai()
    QuaTrinhLamBai()
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        Fore.GREEN
        + "[PHẢN HỒI]: ^^ Mình làm xong cho bạn rồi, nhưng mình sợ bạn không tin tưởng mình \ncho nên mình để bạn tự kiểm tra lại rồi bấm NỘP BÀI đó!!"
    )
    tatTrinhDuyet = input("->[Gõ ENTER để thoát trình duyệt]...")
    driver.quit()


# Thực thi bản BlackBox  BLACKBOX--------------
def ThucThi_BlackBoxAI(usern, passw):
    LoginBlackBoxAI()
    NhapHashcodeVaLamBai()
    QuaTrinhLamBai_2()
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        Fore.GREEN
        + "[PHẢN HỒI]: ^^ Mình làm xong cho bạn rồi, nhưng mình sợ bạn không tin tưởng mình \ncho nên mình để bạn tự kiểm tra lại rồi bấm NỘP BÀI đó!!"
    )
    tatTrinhDuyet = input("->[Gõ ENTER để thoát trình duyệt]...")
    driver.quit()


""" Đăng nhập và thông báo ... Của LMS"""


def ThongBao(id, name):
    os.system("cls")
    print(
        f"{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════╗"
    )
    print(
        f"{Fore.YELLOW}║ - - - - - - - - - - - - - {Fore.LIGHTCYAN_EX}[LMSHelper (BETA 1.0) - {Fore.LIGHTBLUE_EX}D{Fore.LIGHTCYAN_EX}U{Fore.LIGHTMAGENTA_EX}C{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}N{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTWHITE_EX}W{Fore.LIGHTBLUE_EX}O{Fore.LIGHTCYAN_EX}R{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTGREEN_EX}2{Fore.LIGHTRED_EX}6{Fore.YELLOW}] - - - - - - - - - - - - - - ║"
    )
    print(
        f"{Fore.YELLOW}║═════════════════════════════════════════════════════════════════════════════════════════════║"
    )
    print(
        f"{Fore.YELLOW}║ [THÔNG BÁO {setTime.tm_mday}-{setTime.tm_mon}-{setTime.tm_year}]: {Fore.WHITE}Tool Auto: Sẽ dừng ở câu 15 để tránh điểm thấp khi dùng AI.         {Fore.YELLOW}║"
    )
    print(
        f"{Fore.YELLOW}║═════════════════════════════════════════════════════════════════════════════════════════════║"
    )
    print(
        f"{Fore.YELLOW}║ - - - - - - - - - - - - - - - - - - - - - [ PANEL ] - - - - - - - - - - - - - - - - - - - - ║"
    )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[1] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt Chrome - BINGAI                    {Fore.YELLOW}║"
    )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[2] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt Chrome - BLACKBOX                  {Fore.YELLOW}║"
    )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[3] | [ADD] Thêm BUTTON Sao chép câu hỏi khi làm LMS trên trình duyệt Chrome                {Fore.YELLOW}║"
    )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[*] | [EXIT] THOÁT TOOL                                                                     {Fore.YELLOW}║"
    )
    print(
        f"{Fore.YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════╝"
    )
    print(
        f"{Fore.YELLOW}- - - - - - - - - - - - - - - - - - - - - [ THÔNG TIN ] - - - - - - - - - - - - - - - - - - - -"
    )
    print(
        f"{Fore.YELLOW} Xin chào {Fore.LIGHTYELLOW_EX}{name.text} {Fore.YELLOW}- Mã sinh viên: {Fore.LIGHTYELLOW_EX}{id.text}                                         "
    )


def KiemTraTienDoLMS():
    sleep(4)
    mon = 1
    while True:
        try:
            check = autoDoiPhanTuHienThi_CSS_SELECTOR(
                driver, 2, f".classes-item:nth-child({mon}) .circle-progress-content"
            )
            mon += 1

        except:
            break
    mon -= 1
    monHoanThanh = 1
    tenMonChuaHoanThanh = []
    for i in range(1, mon, 1):
        check = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 2, f".classes-item:nth-child({i}) .circle-progress-content"
        )
        checkHoanThanhTienDo = check.text
        if checkHoanThanhTienDo == "100%":
            monHoanThanh += 1
        else:
            tenMon = autoDoiPhanTuHienThi_CSS_SELECTOR(
                driver,
                30,
                f".classes-item:nth-child({i}) .progress-left_content__top-name",
            )
            tenMonChuaHoanThanh.append(tenMon)

    if monHoanThanh == 5:
        print(
            f" {Fore.YELLOW}Bạn đã hoàn thành {Fore.GREEN}{monHoanThanh}/{mon} {Fore.YELLOW}môn, chúc mừng bạn!!!"
        )
    else:
        print(
            f" {Fore.YELLOW}Bạn đã hoàn thành {Fore.RED}{monHoanThanh}/{mon} {Fore.YELLOW}môn, hãy làm trước khi hết hạn nhé"
        )
        for mon in tenMonChuaHoanThanh:
            print(f" {Fore.YELLOW}[Môn chưa làm]: {Fore.LIGHTYELLOW_EX}{mon.text}")


def ButtonSaoChepCauHoiLMS():
    try:
        # Phần 1: Tạo button và lưu vào window
        js_part_1 = """
        window.copyButton = document.createElement('button');
        window.copyButton.innerHTML = 'Sao chép câu hỏi';
        window.copyButton.style.position = 'fixed';
        window.copyButton.style.bottom = '20px';
        window.copyButton.style.right = '20px';
        window.copyButton.style.padding = '10px 20px';
        window.copyButton.style.backgroundColor = '#007BFF'; // Màu xanh da trời
        window.copyButton.style.color = '#fff'; // Màu chữ trắng
        window.copyButton.style.border = 'none';
        window.copyButton.style.borderRadius = '5px';
        window.copyButton.style.boxShadow = '0px 4px 10px rgba(0, 0, 0, 0.2)';
        window.copyButton.style.cursor = 'pointer';
        window.copyButton.style.fontSize = '16px';
        window.copyButton.style.fontFamily = 'Arial, sans-serif';
        window.copyButton.style.zIndex = '1000';
        document.body.appendChild(window.copyButton);
        """
        driver.execute_script(js_part_1)

        # Phần 2: Thêm sự kiện hover cho button
        js_part_2 = """
        window.copyButton.addEventListener('mouseenter', function() {
        window.copyButton.style.backgroundColor = '#0056b3';
        window.copyButton.style.boxShadow = '0px 6px 12px rgba(0, 0, 0, 0.3)';
        });
        window.copyButton.addEventListener('mouseleave', function() {
        window.copyButton.style.backgroundColor = '#007BFF';
        window.copyButton.style.boxShadow = '0px 4px 10px rgba(0, 0, 0, 0.2)';
        });
        """
        driver.execute_script(js_part_2)

        # Phần 3: Hàm sao chép câu hỏi
        js_part_3 = """
        function gH(cN) {
        var e = document.querySelector('.' + cN);
        return e ? e.outerHTML : null;
        }

        function hT(h) {
        var d = document.createElement('div');
        d.innerHTML = h;
        var t = d.innerHTML.replace(/&nbsp;/g, ' ')
            .replace(/<br\\s*\\/?>/gi, '\\n')
            .replace(/<\/p>/gi, '\\n')
            .replace(/<p>/gi, '\\n')
            .replace(/<\/?[^>]+(>|$)/g, '\\n');
        t = t.replace(/\\n\\s*\\n/g, '\\n').trim();
        return t.replace(/Câu này cần xem lại/g, '');
        }

        window.copyButton.addEventListener('click', function() {
        var html = gH('present-single-question');
        if (html) {
            var text = hT(html);
            navigator.clipboard.writeText(text).then(function() {
            console.log('Đã sao chép câu hỏi vào clipboard!');
            }).catch(function(err) {
            console.error('Không thể sao chép', err);
            });
        } else {
            console.log('Không tìm thấy câu hỏi để sao chép!');
        }
        });
        """
        driver.execute_script(js_part_3)

    except Exception as e:
        print(f"{Fore.RED}[LỖI]: KHÔNG THỂ KHỞI CHẠY JAVASCRIPT! {str(e)}")

    # Để giữ trình duyệt mở cho đến khi đóng bằng tay
    print(
        f"{Fore.GREEN}[PHẢN HỒI]: {Fore.LIGHTWHITE_EX} Khởi tạo BUTTON sao chép câu hỏi khi làm bài LMS thành công!"
    )
    input(f"{Fore.YELLOW}[GÕ 'ENTER' ĐỂ VỀ PANEL]...")


# Login LMS
def MAIN(usernameLog, passwordLog):
    ChuyenTab1()
    driver.get("https://lms.ictu.edu.vn/dashboard/classes")

    try:
        tenTaiKhoan = autoKhiPhanTuCoTheClickDuoc_ID(driver, 20, "mat-input-0")
        tenTaiKhoan.send_keys(usernameLog + "@ictu.edu.vn")  # tk

        matKhau = autoKhiPhanTuCoTheClickDuoc_ID(driver, 20, "mat-input-1")
        matKhau.send_keys(passwordLog)  # mk

        dangNhap = autoKhiPhanTuCoTheClickDuoc_CLASS_NAME(driver, 20, "grid")
        dangNhap.click()  # click đăng nhập
    except:
        pass

    try:
        xacNhanDangNhapThanhCong = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 10, ".header-button__feature__node"
        )
    except:
        os.system("cls")
        for i in range(3, 0, -1):
            print(Fore.RED + "[LỖI]: Đăng nhập thất bại!!")
            print(f"{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]")
            sleep(1)
            os.system("cls")
        # os.system()
        exit()
    while True:
        name = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 20, "h6")
        id = autoDoiPhanTuHienThi_CSS_SELECTOR(driver, 20, "small")
        if xacNhanDangNhapThanhCong.text == "LỚP HỌC PHẦN":
            ThongBao(id=id, name=name)
        KiemTraTienDoLMS()
        print(
            f"{Fore.YELLOW}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
        )
        select = input(f"{Fore.LIGHTYELLOW_EX}[SELECT]: ")
        if select == "1":
            ThucThi_BingAI()
        elif select == "2":
            ThucThi_BlackBoxAI()
        elif select == "3":
            ButtonSaoChepCauHoiLMS()
        elif select == "*":
            os.system("cls")
            for i in range(3, 0, -1):
                print(Fore.GREEN + "[PHẢN HỒI]: THOÁT TOOL!!")
                print(f"{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]")
                sleep(1)
                os.system("cls")
                # os.system()
                exit()
        else:
            print(f"{Fore.RED}[LỖI]: Chức năng bạn chọn không hợp lệ, vui lòng thử lại")


setTime = time.localtime()  # Settime
os.system("cls")
# làm đẹp
init(autoreset=True)  # cái này để không bị lặp màu, tha hồ tùy chỉnh

print(
    f"{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════╗"
)
print(
    f"{Fore.YELLOW}║ - - - - - - - - - - - - - {Fore.LIGHTCYAN_EX}[LMSHelper (BETA 1.0) - {Fore.LIGHTBLUE_EX}D{Fore.LIGHTCYAN_EX}U{Fore.LIGHTMAGENTA_EX}C{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}N{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTWHITE_EX}W{Fore.LIGHTBLUE_EX}O{Fore.LIGHTCYAN_EX}R{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTGREEN_EX}2{Fore.LIGHTRED_EX}6{Fore.YELLOW}] - - - - - - - - - - - - - - ║"
)
print(
    f"{Fore.YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════╝"
)
usern = input(f" {Fore.LIGHTYELLOW_EX}Mã sinh viên [LMS/ICTU]: ")
passw = getpass.getpass(
    f" {Fore.LIGHTYELLOW_EX}Mật khẩu [LMS/ICTU](tàng hình ghi nhập): "
)

chrome_option = Options()
chrome_option.add_argument("--log-level=3")  # Tắt log từ Selenium
chrome_option.add_argument("--silent")  # Giảm thiểu các thông báo không cần thiết
driver = webdriver.Chrome(options=chrome_option)

MAIN(usernameLog=usern, passwordLog=passw)
# ThongBao()
