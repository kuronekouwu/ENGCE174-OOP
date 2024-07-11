def generate_pattern01(n, current=0, result=""):
    if current == n:
        return result
    line = "* " * (current + 1)
    return generate_pattern01(n, current + 1, result + line + "\n")


def generate_pattern02(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "* " * (current + 1)
    return generate_pattern02(n, current + 1, result + line + "\n")


def generate_pattern03(n, current=0, result=""):
    if current == n:
        return result
    line = "* " * (n - current)
    return generate_pattern03(n, current + 1, result + line + "\n")


def generate_pattern04(n, current=0, result=""):
    if current == n:
        return result
    line = " " * (n - current - 1) + "* " * (current + 1)
    return generate_pattern04(n, current + 1, result + line + "\n")


def generate_pattern05(n, current=0, result=""):
    if current == n:
        return result
    line = " " * current + "* " * (n - current)
    return generate_pattern05(n, current + 1, result + line + "\n")


# รับค่า x จากผู้ใช้
x = int(input("Enter height pyramid: "))

# แสดงผลลัพธ์สำหรับแต่ละฟังก์ชัน generate_pattern
pattern = generate_pattern01(x)
print(pattern, end="")
print("-" * 15)

pattern = generate_pattern02(x)
print(pattern, end="")
print("-" * 15)

pattern = generate_pattern03(x)
print(pattern, end="")
print("-" * 15)

pattern = generate_pattern04(x)
print(pattern, end="")
print("-" * 15)

pattern = generate_pattern05(x)
print(pattern, end="")
print("-" * 15)
