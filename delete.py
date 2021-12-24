from requests import get, post, delete
from json import dumps, loads, dump, load

# '''Các delete()phương pháp gửi một yêu cầu DELETE để url được chỉ định.
# Yêu cầu DELETE được thực hiện để xóa tài nguyên được chỉ định (tệp, bản ghi, v.v.)
# CÚ PHÁP: requests.delete(url, args) '''


url = 'https://gateway-staging.systemkul.com/api/Unit/DeleteUnit?id='

# data_request_new = {
#     "id" : "cace4b76-4b35-47ef-97d0-a4f9e32b9cf0"
# }
strtt = str("cace4b76-4b35-47ef-97d0-a4f9e32b9cf0")
r = delete(url+strtt, timeout=2.5, headers={'Content-Type': 'application/octet-stream', })
print(r.status_code)
print(r.text)
print(r.json())
print(r.url)


    

# url = 'https://gateway.systemkul.com/api/Tests/DeleteByList'

# x = requests.delete(url)    # Thực hiện yêu cầu XÓA đối với một trang web và trả lại văn bản phản hồi
# print(x.text)
# #===============================================================================
# # Đôi khi máy chủ chuyển hướng một yêu cầu, có thể là tệp ko tồn tại, v.v., Hãy đặt thông số 'allow_redirects' thành "False" để từ chối chuyển hướng
# x = requests.delete(url, allow_redirects=False)         # allow_redirects: Tùy chọn. Một Boolean để bật / tắt chuyển hướng.True mặc định (cho phép chuyển hướng)
# # In văn bản phản hồi (Nội dung của tệp được yêu cầu):
# print(x.text)


# #use the 'auth' parameter to send requests with HTTP Basic Auth:
# x = requests.delete(url, auth = ('user', 'pass'))       # Tùy chọn. Một bộ để kích hoạt xác thực HTTP nhất định. Mặc định Không có
# print(x.status_code)

# #specify a cert to use as a client side certificate by setting the 'cert' parameter:
# x = requests.delete(url, cert='folder/myclient.cert')
# print(x.status_code)

# #use the 'cookies' parameter to send cookies to the server:
# x = requests.delete(url, cookies = {"favcolor": "Red"})
# print(x.status_code)

# #use the 'headers' parameter to set the HTTP headers:
# x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(x.status_code)

# #find a free proxy address and send your request via that proxy:
# x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(x.status_code)

# #allow the response to be streamed by setting the 'stream' parameter to True:
# x = requests.delete(url, stream=True)
# print(x.status_code)

# #to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
# x = requests.delete(url, timeout=0.001)
# print(x.text)

# #make the request with the path to a TLS certificate:
# x = requests.delete(url, verify='folder/tlscertificate')
# print(x.status_code)

# #make the request and specify that there will be no verifying:
# x = requests.delete(url, verify=False)
# print(x.status_code)

# list  = [ '6', '8' ]
# json_object = json.dumps(list, indent = 4)
# print(json_object)

# url = 'https://gateway.systemkul.com/api/Tests/DeleteByList'

# x = requests.delete(url, auth  = list )
# print(x.status_code)


