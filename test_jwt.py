import jwt

payload = {
    "name": "장현준",
}

secret_key = "test_key"

encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")
print(encoded_jwt) # secret key를 이용해서 보내고자 하는 데이터의 payload에 인코딩되어 문자열을 출력함

decode_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
print(decode_jwt) # jwt로 만들었던 payload 데이터를 출력할 수 있음
