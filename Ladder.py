import random

people = ["김태린", "김지후", "이재현", "이정민"]
results = ["1번", "2번", "3번", "4번"]

# 결과 순서를 무작위로 섞기
random.shuffle(results)

print("===== 사다리 타기 결과 =====")

for person, result in zip(people, results):
    print(f"{person} → {result}")