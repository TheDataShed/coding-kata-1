def add(numbers_string):
    if not numbers_string:
        return 0

    elif len(numbers_string) == 1:
        return int(numbers_string)

    elif numbers_string.startswith("//"):
        result = 0
        delim = ""
        split_newline = numbers_string.split("\n")
        for char in range(2, len(split_newline[0])):
            delim = delim + split_newline[0][char]
        numbers = split_newline[1].split(delim)
        for num in numbers:
            if int(num) >= 0 and int(num) <= 1000:
                result += int(num)
        return result

    else:
        result = 0
        delim = ","
        if numbers_string[1] != ",":
            delim = "\n"
        numbers = numbers_string.split(delim)
        for num in numbers:
            if int(num) >= 0 and int(num) <= 1000:
                result += int(num)
        return result
