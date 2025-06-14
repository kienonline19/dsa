def search(dic, value):
    for key in dic:
        if dic[key] == value:
            return key, value

    return f"The {value} does not exist!"


if __name__ == "__main__":
    person = {
        "name": "Edy",
        "age": 26,
        "address": "London"
    }

    print(search(person, "Edy"))
