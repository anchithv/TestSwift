
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""


def number_to_thai_text(number):
    # Define a list of Thai digit words
    thai_digits = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    # Initialize an empty string to store the Thai text
    thai_text = ""

    # Check if the input number is valid
    if number < 0 or number >= 10000000:
        return "Invalid input. Please enter a number between 0 to 9,999,999."

    # Handle the case when the input number is 0
    if number == 0:
        return thai_digits[0]

    # Define a function to convert three digits to Thai text
    def convert_three_digits(num):
        text = ""
        hundreds = num // 100
        if hundreds > 0:
            text += thai_digits[hundreds] + "ร้อย"
            num %= 100
        tens = num // 10
        if tens > 0:
            if tens == 1:
                text += "สิบ"
            else:
                text += thai_digits[tens] + "สิบ"
            num %= 10
        if num > 0:
            text += thai_digits[num]
        return text

    # Convert millions
    millions = number // 1000000
    if millions > 0:
        thai_text += thai_digits[millions] + "ล้าน"
        number %= 1000000
    
    # Convert hundred thousands
    hundredthousands = number // 100000
    if hundredthousands > 0:
        thai_text += convert_three_digits(hundredthousands) + "แสน"
        number %= 100000
    
    # Convert ten thousands
    tenthousands = number // 10000
    if tenthousands > 0:
        thai_text += convert_three_digits(tenthousands) + "หมื่น"
        number %= 10000
    
    # Convert thousands
    thousands = number // 1000
    if thousands > 0:
        thai_text += convert_three_digits(thousands) + "พัน"
        number %= 1000

    # Convert the remaining digits (if any)
    if number > 0:
        thai_text += convert_three_digits(number)

    return thai_text

try:
    user_input = int(input("Enter a number between 0 and 9,999,999: "))
    result = number_to_thai_text(user_input)
    print("Thai text:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
