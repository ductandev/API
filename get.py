import requests

url = 'https://gateway.systemkul.com/api/Tests/getListByPlace6438'
x = requests.get(url)

print(x.text)                   # text : Đưa ra yêu cầu tới một trang web và in văn bản phản hồi
print(x.status_code)            # Trả về một số cho biết trạng thái (200 là OK, 404 là không tìm thấy)
print(x.apparent_encoding)      # Trả về mã hóa rõ ràng
x.close()                       # Đóng kết nối tới máy chủ
print(x.content)                # Trả về nội dung của phản hồi, tính bằng byte
print(x.cookies)                # Trả về một đối tượng CookieJar với các cookie được gửi lại từ máy chủ
print(x.elapsed)                # Trả về một đối tượng theo thời gian với thời gian trôi qua từ khi gửi yêu cầu đến khi phản hồi đến
print(x.encoding)               # Trả về mã hóa được sử dụng để giải mã r.text
print(x.headers)                # Trả về từ điển các tiêu đề phản hồi
print(x.history)                # Trả về danh sách các đối tượng phản hồi có lịch sử yêu cầu (url)
print(x.is_permanent_redirect)  # Trả về True nếu phản hồi là url được chuyển hướng vĩnh viễn, nếu không thì False
print(x.is_redirect)            # Trả về Đúng nếu phản hồi được chuyển hướng, nếu không, Sai
#=======================================================
#return an iterator, one item for each character:
print(x.iter_content())         # Lặp lại phản hồi
#looping through the iterator:
for c in x.iter_content():
  print(c)
#=======================================================
#return an iterator, one item for each line:
print(x.iter_lines())           # Lặp lại các dòng của phản hồi
#looping through the iterator:
for c in x.iter_content():
  print(c)
#=======================================================
print(x.json())                 # Trả về một đối tượng JSON của kết quả (nếu kết quả được viết ở định dạng JSON, nếu không, nó gây ra lỗi)
print(x.links)                  # Trả về các liên kết tiêu đề
print(x.next)                   # Trả về đối tượng Yêu cầu được chuẩn bị trước cho yêu cầu tiếp theo trong chuyển hướng
print(x.ok)                     # Trả về True nếu status_code nhỏ hơn 400, ngược lại là False
print(x.raise_for_status())     # Nếu xảy ra lỗi, phương thức này trả về đối tượng HTTPError
print(x.reason)                 # Trả về một văn bản tương ứng với mã trạng thái
print(x.request)                # Trả về đối tượng yêu cầu đã yêu cầu phản hồi này
print(x.status_code)            # Trả về một số cho biết trạng thái (200 là OK, 404 là không tìm thấy)
print(x.text)                   # Trả về nội dung của phản hồi, dưới dạng unicode
print(x.url)                    # Trả về URL của phản hồi