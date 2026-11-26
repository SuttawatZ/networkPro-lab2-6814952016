import requests

url = "http://localhost:8000"

# 1. ทดสอบส่ง HTTP GET
print("--- ทดสอบ HTTP GET ---")
res_get = requests.get(url, params={"msg": "Hello from Client GET"})
print("Status Code:", res_get.status_code)
print("Response:", res_get.text)

print("\n" + "="*30 + "\n")

# 2. ทดสอบส่ง HTTP POST
print("--- ทดสอบ HTTP POST ---")
payload = {"student_name": "Sutthiwat", "message": "ทดสอบส่งข้อมูลแบบ POST"}
res_post = requests.post(url, data=payload)
print("Status Code:", res_post.status_code)
print("Response:", res_post.text)