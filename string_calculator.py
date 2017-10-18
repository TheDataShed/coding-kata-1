def add(numbers_string):
    if not numbers_string:
        return 0

    elif len(numbers_string) == 1:
        return int(numbers_string)

    elif numbers_string.startswith("//"):
        result = 0
        delim = numbers_string[2]
        numbers_string = numbers_string.split("\n")
        numbers = numbers_string.split(delim)
        for num in numbers:
            result += int(num)
        return result

    else:
        result = 0
        delim = ","
        if numbers_string[1] != ",":
            delim = "\n"
        numbers = numbers_string.split(delim)
        for num in numbers:
            result += int(num)
        return result
