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
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.webdriver.edge.options import Options as EdgeOptions
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
    from selenium.webdriver.edge.service import Service as EdgeService
    from selenium.webdriver.edge.options import Options as EdgeOptions
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


# Tự động lấy text câu hỏi hiện tại đang làm
def LayTextCauHoiLMS():
    # Chuyển đến tab chứa câu hỏi
    ChuyenTab1()

    # Lấy nội dung câu hỏi
    question_text = driver.execute_script(
        """
        var questionLegend = document.querySelector('legend');
        var questionContent = document.querySelector('.present-single-question__direction');
        if (questionLegend && questionContent) {
            return `${questionLegend.innerText.trim()} ${questionContent.innerText.trim()}`;
        }
        return '';
        """
    )

    # Lấy nội dung đáp án
    answers_text = driver.execute_script(
        """
        var answersText = "";
        var answerElements = document.querySelectorAll('.question-type-radio__option');
        if (answerElements.length) {
            answerElements.forEach((answerElement) => {
                var label = answerElement.getAttribute('data-ictu-question-prefix');
                var answerText = answerElement.querySelector('.question-type-radio__answer-content').innerText.trim();
                answersText += `${label}. ${answerText} `;
            });
        }
        return answersText.trim();
        """
    )

    # Kết hợp câu hỏi và đáp án
    question_data = f"{question_text} {answers_text}"
    return question_data


# chon đáp án khi có câu trả lời (A,B,C,D)
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
        # Bạn hoàn thiện giúp tôi nếu không chọn được đáp án thì gọi lại hàm tracuuBingAI_HinhAnh ra để gọi lại
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


# kiểm thử
def test():
    c = input("testing to ok: ")


# tra con chat bing (dạng hình ảnh) - return câu trả lời khi AI trả lời
def TraCuuBingAI_HinhAnh(fileCanUpload, khongTimDuocCauTraLoi=0, max_attempts=3):
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
            "Tôi rõ ràng đã bảo là quan sát kỹ ảnh, chỉ trả lời đúng một ký tự: A, B, C hoặc D. Không thêm văn bản thừa. Không thêm bất kỳ từ ngữ hoặc dấu câu nào khác, không thêm khoảng trống trước và sau hay dòng trên hoặc dòng dưới (Không thêm dấu chấm đằng sau nha ví dụ: B. (không hợp lệ)) Chỉ xuất ra đúng một ký tự duy nhất A B C D đừng thêm gì đằng sau, làm ơn."
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
        if cauTraLoi.strip().upper() in ["A", "B", "C", "D"]:
            return cauTraLoi.strip().upper()
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBingAI_HinhAnh(
                fileCanUpload, khongTimDuocCauTraLoi, max_attempts
            )

    except Exception as e:
        print(
            Fore.RED
            + f"[LỖI]: Ơ có lỗi gì thế nhỉ, bạn đăng nhập thành công BingAI chưa, phải đăng nhập mới làm được nhé^^"
        )
        return TraCuuBingAI_HinhAnh(
            fileCanUpload, khongTimDuocCauTraLoi + 1, max_attempts
        )


def TraCuuBingAI_Text(cauHoi, khongTimDuocCauTraLoi=0, max_attempts=3):
    ChuyenTab2()
    driver.refresh()
    if khongTimDuocCauTraLoi >= max_attempts:
        return (
            Fore.RED
            + "[LỖI]: Đã thử nhiều lần nhưng không nhận được câu trả lời hợp lệ."
        )

    try:
        userInput = autoDoiPhanTuHienThi_ID(driver, 30, "userInput")
        userInput.click()
        userInput.send_keys(
            "Vui lòng chú ý cau hỏi trong ảnh mà tôi gửi và chỉ trả lời duy nhất một ký tự đại diện cho đáp án chính xác (A, B, C hoặc D). Không thêm bất kỳ văn bản nào khác hoặc ký tự nào khác vào câu trả lời. Chỉ xuất ra duy nhất ký tự."
        )
        userInput.send_keys(Keys.SHIFT, Keys.ENTER)

        userInput.send_keys(
            "Tôi rõ ràng đã bảo là quan sát kỹ ảnh, chỉ trả lời đúng một ký tự: A, B, C hoặc D. Không thêm văn bản thừa. Không thêm bất kỳ từ ngữ hoặc dấu câu nào khác, không thêm khoảng trống trước và sau hay dòng trên hoặc dòng dưới (Không thêm dấu chấm đằng sau nha ví dụ: B. (không hợp lệ)) Chỉ xuất ra đúng một ký tự duy nhất A B C D đừng thêm gì đằng sau, làm ơn."
        )
        userInput.send_keys(Keys.SHIFT, Keys.ENTER)
        # dán câu hỏi
        userInput.send_keys(cauHoi)

        # click gui
        try:
            send = autoDoiPhanTuHienThi_CSS_SELECTOR(
                driver, 10, ".text-foreground-800 > .size-6"
            )
            send.click()
        except:
            input.send_keys(Keys.ENTER)

        sleep(2.5)

        # lay cau tra loi
        answer = autoDoiPhanTuHienThi_CSS_SELECTOR(
            driver, 30, ".space-y-3:nth-child(2) > .space-y-3 span"
        )
        cauTraLoi = answer.text.strip()
        # xcheck xem cau hoi hop le chua
        if cauTraLoi.strip().upper() in ["A", "B", "C", "D"]:
            return cauTraLoi.strip().upper()
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBingAI_Text(cauHoi, khongTimDuocCauTraLoi, max_attempts)
    except Exception as e:
        print(
            Fore.RED
            + f"[LỖI]: Ơ có lỗi gì thế nhỉ, bạn đăng nhập thành công BingAI chưa, phải đăng nhập mới làm được nhé^^"
        )
        return TraCuuBingAI_Text(cauHoi, khongTimDuocCauTraLoi + 1, max_attempts)


# Auto tra cứu bằng blackbox- dạng hình ảnh
def TraCuuBlackBoxAI_HinhAnh(fileCanUpload, khongTimDuocCauTraLoi=0, max_attempts=3):
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
        if cauTraLoi.strip().upper() in ["A", "B", "C", "D"]:
            return cauTraLoi.strip().upper()
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBlackBoxAI_HinhAnh(
                fileCanUpload, khongTimDuocCauTraLoi, max_attempts
            )
    except Exception as e:
        print(Fore.RED + f"[LỖI]: {e} Có một vài lỗi tại BlackBoxAI bạn hãy thử lại^^")
        return TraCuuBlackBoxAI_HinhAnh(
            fileCanUpload, khongTimDuocCauTraLoi + 1, max_attempts
        )


def TraCuuBlackBoxAI_Text(cauHoi, khongTimDuocCauTraLoi=0, max_attempts=3):
    ChuyenTab2()
    driver.get("https://www.blackbox.ai/?model=gemini-pro")

    # driver.get("https://www.blackbox.ai/")
    if khongTimDuocCauTraLoi >= max_attempts:
        return (
            Fore.RED
            + "[LỖI]: Đã thử nhiều lần nhưng không nhận được câu trả lời hợp lệ."
        )

    try:
        input = autoDoiPhanTuHienThi_ID(driver, 30, "chat-input-box")
        input.click()
        input.send_keys(
            "@Gemini-PRO "
            + "Vui lòng chú ý cau hỏi trong ảnh mà tôi gửi và chỉ trả lời duy nhất một ký tự đại diện cho đáp án chính xác (A, B, C hoặc D). Không thêm bất kỳ văn bản nào khác hoặc ký tự nào khác vào câu trả lời. Chỉ xuất ra duy nhất ký tự."
        )
        input.send_keys(Keys.SHIFT, Keys.ENTER)
        input.send_keys(
            "Tôi rõ ràng đã bảo là quan sát kỹ ảnh, chỉ trả lời đúng một ký tự: A, B, C hoặc D. Không thêm văn bản thừa. Không thêm bất kỳ từ ngữ hoặc dấu câu nào khác, không thêm khoảng trống trước và sau hay dòng trên hoặc dòng dưới (Không thêm dấu chấm đằng sau nha ví dụ: B. (không hợp lệ)) Chỉ xuất ra đúng một ký tự duy nhất A B C D đừng thêm gì đằng sau, làm ơn."
        )
        input.send_keys(Keys.SHIFT, Keys.ENTER)
        input.send_keys("[Câu hỏi như sau]: ")
        input.send_keys(cauHoi)
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
        if cauTraLoi.strip().upper() in ["A", "B", "C", "D"]:
            return cauTraLoi.strip().upper()
        else:
            khongTimDuocCauTraLoi += 1
            print(
                Fore.RED
                + f"[LỖI]: Câu trả lời không hợp lệ, thử lại lần {khongTimDuocCauTraLoi}..."
            )
            return TraCuuBlackBoxAI_Text(cauHoi, khongTimDuocCauTraLoi, max_attempts)

    except Exception as e:
        print(Fore.RED + f"[LỖI]: {e} Có một vài lỗi tại BlackBoxAI bạn hãy thử lại^^")
        return TraCuuBlackBoxAI_Text(cauHoi, khongTimDuocCauTraLoi + 1, max_attempts)


""" =================================== [THỰC THI LÀM BÀI] ===================================="""


# BẢN DÀNH CHO BINGAI -------------- BINGAI (Hình ảnh)
def QuaTrinhLamBai():
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
            cauTraLoi = TraCuuBingAI_HinhAnh(
                fileCanUpload=fileCauHoi
            )  # tra cứu câu hỏi đó
            sleep(1)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            sleep(1)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


# BẢN DÀNH CHO BLACKBOX -------------- BLACKBOX (Hình ảnh)--
def QuaTrinhLamBai_2():
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
            cauTraLoi = TraCuuBlackBoxAI_HinhAnh(
                fileCanUpload=fileCauHoi
            )  # tra cứu câu hỏi đó
            sleep(1)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            sleep(1)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


# BẢN DÀNH CHO BLACKBOX -------------- BLACKBOX (TEXT)--
def QuaTrinhLamBai_3():
    cauSo = 0  # khoitao
    cauTraLoi = ""  # khoitao
    print(
        f"{Fore.GREEN}===================================== [KẾT QUẢ] ====================================="
    )
    try:
        xacMinh = autoDoiPhanTuHienThi_XPATH(
            driver, 30, "//*[@id='mat-mdc-checkbox-1']/div/label"
        )
    except:
        print(f"{Fore.RED}[LỖI]: CHƯA LOAD ĐƯỢC BÀI ")
        print(Fore.GREEN + "[PHẢN HỒI]: ĐANG THOÁT TOOL!!")
        for i in range(3, 0, -1):
            print(f"\r{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]", end="")
            sleep(1)
            # os.system("cls")
            # os.system()
        exit()
    while True:
        if cauSo == 15:
            break
        else:
            cauSo += 1
            cauHoi = LayTextCauHoiLMS()
            sleep(1)
            cauTraLoi = TraCuuBlackBoxAI_Text(cauHoi)
            # sleep(0.4)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            # sleep(0.4)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


# BẢN DÀNH CHO BINGAI -------------- BINGAI (TEXT)--
def QuaTrinhLamBai_4():
    cauSo = 0  # khoitao
    cauTraLoi = ""  # khoitao
    print(
        "===================================== [PHẢN HỒI] ====================================="
    )
    try:
        xacMinh = autoDoiPhanTuHienThi_XPATH(
            driver, 30, "//*[@id='mat-mdc-checkbox-1']/div/label"
        )
    except:
        print(f"{Fore.RED}[LỖI]: CHƯA LOAD ĐƯỢC BÀI ")
        print(Fore.GREEN + "[PHẢN HỒI]: ĐANG THOÁT TOOL!!")
        for i in range(3, 0, -1):
            print(f"\r{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]", end="")
            sleep(1)
            # os.system("cls")
            # os.system()
        exit()
    while True:
        if cauSo == 15:
            break
        else:
            cauSo += 1  # tăng câu hỏi mỗi lần hoàn thành, lần đầu sẽ = 1
            cauHoi = LayTextCauHoiLMS()
            cauTraLoi = TraCuuBingAI_Text(cauHoi)
            sleep(1)
            ChonDapAnVaChuyenCauHoi(cauSo, cauTraLoi)
            sleep(1)
            print(Fore.GREEN + f"---> [HOÀN THÀNH]: CÂU {cauSo} | Đáp án {cauTraLoi}")


# Thực thi bản BingAI (Hình ảnh)   BINGAI---------------
def ThucThi_BingAI_UpHinhAnh():
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
    while True:
        tatTrinhDuyet = input("->[Gõ 'OK' để thoát trình duyệt]...")
        if tatTrinhDuyet in ["OK", "ok", "Ok", "Oki", "*"]:
            driver.quit()
            break
        else:
            continue


# Thực thi bản BlackBox (Hình ảnh)  BLACKBOX--------------
def ThucThi_BlackBoxAI_UpHinhAnh():
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
    while True:
        tatTrinhDuyet = input("->[Gõ 'OK' để thoát trình duyệt]...")
        if tatTrinhDuyet in ["OK", "ok", "Ok", "Oki", "*"]:
            driver.quit()
            break
        else:
            continue


# Thực thi bản BlackBox (Text)
def ThucThi_BlackBoxAI_Text():
    LoginBlackBoxAI()
    NhapHashcodeVaLamBai()
    QuaTrinhLamBai_3()
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        Fore.GREEN
        + "[PHẢN HỒI]: ^^ Mình làm xong cho bạn rồi, nhưng mình sợ bạn không tin tưởng mình \ncho nên mình để bạn tự kiểm tra lại rồi bấm NỘP BÀI đó!!"
    )
    while True:
        tatTrinhDuyet = input("->[Gõ 'OK' để thoát trình duyệt]...")
        if tatTrinhDuyet in ["OK", "ok", "Ok", "Oki", "*"]:
            driver.quit()
            break
        else:
            continue


# Thực thi bản BingAI (Text)
def ThucThi_BingAI_Text():
    LoginBingAI()  # Đăng nhập vào BingAI
    NhapHashcodeVaLamBai()  # Bắt đầu quá trình làm bài
    QuaTrinhLamBai_4()
    print(
        "----------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        Fore.GREEN
        + "[PHẢN HỒI]: ^^ Mình làm xong cho bạn rồi, nhưng mình sợ bạn không tin tưởng mình \ncho nên mình để bạn tự kiểm tra lại rồi bấm NỘP BÀI đó!!"
    )
    while True:
        tatTrinhDuyet = input("->[Gõ 'OK' để thoát trình duyệt]...")
        if tatTrinhDuyet in ["OK", "ok", "Ok", "Oki", "*"]:
            driver.quit()
            break
        else:
            continue


""" Đăng nhập và thông báo ... Của LMS"""


# noti
def ThongBao(id, name):
    os.system("cls")
    print(
        f"{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════╗"
    )
    print(
        f"{Fore.YELLOW}║ - - - - - - - - - - - - - {Fore.LIGHTCYAN_EX}[LMSHelper (BETA 1.2) - {Fore.LIGHTBLUE_EX}D{Fore.LIGHTCYAN_EX}U{Fore.LIGHTMAGENTA_EX}C{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}N{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTWHITE_EX}W{Fore.LIGHTBLUE_EX}O{Fore.LIGHTCYAN_EX}R{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTGREEN_EX}2{Fore.LIGHTRED_EX}6{Fore.YELLOW}] - - - - - - - - - - - - - - ║"
    )
    print(
        f"{Fore.YELLOW}║═════════════════════════════════════════════════════════════════════════════════════════════║"
    )
    print(
        f"{Fore.YELLOW}║ [TB 15-10-2024]: {Fore.WHITE}Tool Auto: Sẽ dừng ở câu 15 để tránh điểm thấp khi dùng AI.           {Fore.YELLOW}     ║"
    )
    # print(
    #     f"{Fore.YELLOW}║ [TB 16-10-2024]: {Fore.WHITE}BingAI đang lỗi không gửi ảnh được, đợi fix rồi dùng chức năng 2 nhé. {Fore.YELLOW}     ║"
    # )
    print(
        f"{Fore.YELLOW}║ [TB 18-10-2024]: {Fore.WHITE}BingAI hiện tại đang bị dính captcha hãy dùng tạm BlackBoxAI nha. {Fore.YELLOW}         ║"
    )
    print(
        f"{Fore.YELLOW}║═════════════════════════════════════════════════════════════════════════════════════════════║"
    )
    print(
        f"{Fore.YELLOW}║ - - - - - - - - - - - - - - - - - - - - - [ PANEL ] - - - - - - - - - - - - - - - - - - - - ║"
    )
    # print(
    #     f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[1] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt - BINGAI(TEXT) (BETA)              {Fore.YELLOW}║"
    # )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[1] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt - BLACKBOX(TEXT) (BETA)            {Fore.YELLOW}║"
    )
    # print(
    #     f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[3] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt - BINGAI(ẢNH) (BETA)               {Fore.YELLOW}║"
    # )
    print(
        f"{Fore.YELLOW}║ {Fore.LIGHTWHITE_EX}[2] | [AUTO] Làm bài tập ở lớp học phần trên trình duyệt - BLACKBOX(ẢNH) (BETA)             {Fore.YELLOW}║"
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
        f"{Fore.YELLOW}Xin chào {Fore.LIGHTYELLOW_EX}{name.text} {Fore.YELLOW}- Mã sinh viên: {Fore.LIGHTYELLOW_EX}{id.text}                                         "
    )


# Kiem tra tien do lms
def KiemTraTienDoLMS():
    print(f"{Fore.YELLOW}Đang kiểm tra tiến độ học tập...", end="")
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

    print("\r" + " " * 50, end="\r")
    if monHoanThanh == 5:
        print(
            f"{Fore.YELLOW}Bạn đã hoàn thành {Fore.LIGHTGREEN_EX}{monHoanThanh}/{mon} {Fore.YELLOW}môn, chúc mừng bạn!!!"
        )
    else:
        print(
            f"{Fore.YELLOW}Bạn đã hoàn thành {Fore.LIGHTRED_EX}{monHoanThanh}/{mon} {Fore.YELLOW}môn, hãy làm trước khi hết hạn nhé"
        )
        for mon in tenMonChuaHoanThanh:
            print(f" {Fore.YELLOW}[Môn chưa làm]: {Fore.LIGHTYELLOW_EX}{mon.text}")


# Login LMS
def MAIN(usernameLog, passwordLog, driver):
    ChuyenTab1()
    driver.get("https://lms.ictu.edu.vn/dashboard/classes")

    try:
        tenTaiKhoan = autoKhiPhanTuCoTheClickDuoc_ID(driver, 20, "mat-input-0")
        tenTaiKhoan.send_keys(usernameLog)  # tk

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
        print(Fore.RED + "[LỖI]: ĐĂNG NHẬP THẤT BẠI!!")
        for i in range(3, 0, -1):
            print(f"\r{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]", end="")
            sleep(1)
            # os.system("cls")
        # os.system()
        exit()
    # while True:
    #     test()
    #     LayTextCauHoiLMS()
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
        if select == "----sadjklf":
            ThucThi_BingAI_Text()

        elif select == "1":
            ThucThi_BlackBoxAI_Text()

        elif select == "1230948283094":
            ThucThi_BingAI_UpHinhAnh()
        elif select == "2":
            ThucThi_BlackBoxAI_UpHinhAnh()
        elif select == "*":
            os.system("cls")
            print(Fore.GREEN + "[PHẢN HỒI]: ĐANG THOÁT TOOL!!")
            for i in range(3, 0, -1):
                print(f"\r{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]", end="")
                sleep(1)
                # os.system("cls")
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
    f"{Fore.YELLOW}║ - - - - - - - - - - - - - {Fore.LIGHTCYAN_EX}[LMSHelper (BETA 1.2) - {Fore.LIGHTBLUE_EX}D{Fore.LIGHTCYAN_EX}U{Fore.LIGHTMAGENTA_EX}C{Fore.LIGHTGREEN_EX}A{Fore.LIGHTRED_EX}N{Fore.LIGHTYELLOW_EX}H{Fore.LIGHTWHITE_EX}W{Fore.LIGHTBLUE_EX}O{Fore.LIGHTCYAN_EX}R{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTGREEN_EX}2{Fore.LIGHTRED_EX}6{Fore.YELLOW}] - - - - - - - - - - - - - - ║"
)
print(
    f"{Fore.YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════╝"
)
usern = input(f" {Fore.LIGHTYELLOW_EX}Mã sinh viên [LMS/ICTU]: ")
passw = getpass.getpass(
    f" {Fore.LIGHTYELLOW_EX}Mật khẩu [LMS/ICTU](tàng hình ghi nhập): "
)
os.system("cls")
print(
    f"{Fore.YELLOW}╔═════════════════════════════════════════════════════════════════════════════════════════════╗"
)
print(
    f"{Fore.YELLOW}║ - - - - - - - - - - - - - [CHỌN CẤU HÌNH CHO TRÌNH DUYỆT CỦA BẠN] - - - - - - - - - - - - - ║"
)
print(
    f"{Fore.YELLOW}║ [1] | GOOGLE CHROME                                                                         ║"
)
print(
    f"{Fore.YELLOW}║ [2] | EDGE (ẤN 'ENTER' hoặc SỐ SAI AUTO là EDGE)                                            ║"
)
print(
    f"{Fore.YELLOW}╚═════════════════════════════════════════════════════════════════════════════════════════════╝"
)
cauHinh = input(f" {Fore.LIGHTYELLOW_EX}[1 HOẶC 2]: ")
if cauHinh == "1" or cauHinh.lower() == "mot":
    try:
        chrome_option = Options()
        chrome_option.add_argument(
            "--log-level=3"
        )  # Giảm thiểu mức log của trình duyệt
        chrome_option.add_argument("--silent")  # Giảm thiểu thông báo không cần thiết
        chrome_option.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )  # Ẩn thông báo DevTools
        chrome_option.add_argument("--disable-extensions")  # Tắt các tiện ích mở rộng
        chrome_option.add_argument(
            "--disable-infobars"
        )  # Tắt các thanh thông tin tự động
        driver = webdriver.Chrome(options=chrome_option)
    except:
        print(f"{Fore.RED}[LỖI]: TRÊU TUI À :(( BẠN CHƯA TẢI CHROME MÀ")
        print(Fore.GREEN + "[PHẢN HỒI]: ĐANG THOÁT TOOL!!")
        for i in range(3, 0, -1):
            print(f"\r{Fore.LIGHTWHITE_EX}[TỰ ĐỘNG THOÁT SAU {i} GIÂY]", end="")
            sleep(1)
            # os.system("cls")
            # os.system()
        exit()
elif cauHinh == "2" or cauHinh.lower() == "hai":
    edge_option = EdgeOptions()
    edge_option.add_argument("--log-level=3")
    edge_option.add_argument("--silent")
    edge_option.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )  # Ẩn thông báo DevTools
    edge_option.add_argument("--disable-extensions")
    edge_option.add_argument("--disable-infobars")
    service = EdgeService()
    driver = webdriver.Edge(service=service, options=edge_option)
else:
    edge_option = EdgeOptions()
    edge_option.add_argument("--log-level=3")
    edge_option.add_argument("--silent")
    edge_option.add_experimental_option("excludeSwitches", ["enable-logging"])
    edge_option.add_argument("--disable-extensions")
    edge_option.add_argument("--disable-infobars")
    service = EdgeService()  # Edge driver
    driver = webdriver.Edge(service=service, options=edge_option)


# driver = khoi_tao_trinh_duyet(che_do_an=True)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
MAIN(usernameLog=usern, passwordLog=passw, driver=driver)

# ThongBao()
