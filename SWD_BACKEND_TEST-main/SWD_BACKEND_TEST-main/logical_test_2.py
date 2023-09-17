
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def arabic_to_roman(number):
    # Define lists of Roman numeral symbols and their corresponding values
    roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Check if the input number is within the range
    if number < 1 or number > 1000:
        return "Invalid input. Please enter a number between 1 and 1000."

    # Initialize an empty string to store the Roman numeral
    roman_numeral = ""

    # Iterate through the Roman numeral symbols and their values
    index = 0
    while number > 0:
        # Check if the current Roman symbol can be subtracted from the number
        while number >= roman_values[index]:
            # Subtract the Roman value and add the symbol to the Roman numeral
            number -= roman_values[index]
            roman_numeral += roman_symbols[index]
        # Move to the next Roman symbol
        index += 1

    return roman_numeral

try:
    user_input = int(input("Enter a number between 1 and 1000: "))
    result = arabic_to_roman(user_input)
    print("Roman numeral:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")
