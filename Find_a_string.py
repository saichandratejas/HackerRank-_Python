def count_substring(string, sub_string):
    character = 0
    len_str = len(string)
    len_sub_str = len(sub_string)
    for i in range(len_str):
        if string[i:i + len_sub_str] == sub_string:
            character += 1
    return character


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
