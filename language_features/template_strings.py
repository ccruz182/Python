from string import Template

def main():
    # Usual
    str1 = "Course {0}. Teacher {1}".format("Advanced Python", "Joe Marini")
    print(str1)

    # Using template
    template = Template("Course ${title}. Teacher ${teacher}")

    # Substitute - Keyword
    str2 = template.substitute(title="Advanced Python", teacher="Joe Marini")
    print("Template:", str2)

    # Substitute - Dictionary
    str_values = {
        "title": "Advanced Python",
        "teacher": "Joe Marini"
    }
    str3 = template.substitute(str_values)
    print("Template (dict):", str3)


if __name__ == "__main__":
    main()