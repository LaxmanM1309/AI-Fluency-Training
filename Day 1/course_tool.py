def read_course_fees():
    try:
        with open("fees.txt", "r", encoding="utf-8") as file:
            return file.read()
    except Exception as error:
        return f"Tool error: {error}"


if __name__ == "__main__":
    print(read_course_fees())