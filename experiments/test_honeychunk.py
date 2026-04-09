from src.honeychunk.generator import make_honeychunk
from src.honeychunk.insert import append_honeychunk

doc = "이 문서는 일반 사용자 안내 문서입니다."
chunk = make_honeychunk("보안 정책")
result = append_honeychunk(doc, chunk)

print(result)