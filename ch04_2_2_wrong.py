pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

print("# 우리 동네 애완 동물들")
for element in pets:
    for key in element : 
        print(key["name"], f'{key["age"]}살') 