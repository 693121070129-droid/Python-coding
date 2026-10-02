from grade import cal_grade

while True:
    user = input("ป้อนคะแนน = ")
    if user == 'ปิด':
        print("ปิดโปรแกรม")
        break
    try:
        score = float(user)
        if score <0 or score > 100:
            print("คะแนนต้องอยู่ระหว่าง 0 - 100")
            continue
    
        grade_result = cal_grade(score)
        print(f"คะแนน {score} ได้เกรด {grade_result}")
        print("-" * 30)
    
    except ValueError:
        print("ใส่ได้แค่เฉพาะตัวเลข หรือ พิมย์ปิดเท่านั้น")
        print("-" * 30)