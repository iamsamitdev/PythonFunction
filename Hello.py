# สร้างฟังก์ชันแบบไม่มี Return
def hello(name):
    print(f"Hello {name}")


# การเรียกใช้งานฟังก์ชัน
hello("Samit Koyom")


# สร้างฟังก์ชันแบบมี Return Value
def area(width, height):
    return width * height


# เรียกใช้งานฟังก์ชัน
print(area(10, 20))
print()


# ฟังก์ชันแบบมีการกำหนดค่าเริ่มต้นไว้
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


show_info()
print()
show_info("Samit")
print()
show_info("Samit", 20000)
print()
show_info("Samit", 20000, "Java")
