def SplitLine(line: str, separator: str) -> list:
    print(f"i_line: {line}, separator {separator}")
    lines = line.split(separator)
    if "" not in lines:
        return lines
    lines = RemovEmptyStrings(lines)    
    return lines


def CalcItemInList(i_list: list) -> dict:
    o_dict = {}
    for item in i_list:
        if item in o_dict:
            o_dict[item] = o_dict[item] + 1
        else:
            o_dict[item] = 1
    return o_dict


def RemovEmptyStrings(list_str):
    i_max = len(list_str)
    i_cur = 0
    while i_cur < i_max:
        if list_str[i_cur].strip(" \n\r\t") == "":
            del list_str[i_cur]
            i_max = i_max - 1
        else:
            i_cur = i_cur + 1
    return list_str


def CompareLines(line_list_left: list, line_list_right: list, ignore_duplicates: bool) -> tuple:
    line_dict_left = CalcItemInList(line_list_left)
    line_dict_right = CalcItemInList(line_list_right)

    only_right = {}
    only_left = {}
    in_both = {}

    for key in line_dict_left.keys():
        count_left = 1 if ignore_duplicates else line_dict_left[key]
        count_right = 1 if ignore_duplicates and key in line_dict_right else line_dict_right.get(key, 0) 

        diff = count_left - count_right
        common = min(count_left, count_right)

        if (diff > 0):
            only_left[key] = diff
        elif (diff < 0):
            only_right[key] = -1 * diff
        if common > 0:
            in_both[key] = common 

        if count_right > 0:
            del line_dict_right[key]
    
    for key in line_dict_right.keys():
        count_right = 1 if ignore_duplicates else line_dict_right[key]
        only_right[key] = count_right
    
    return (only_left, only_right, in_both)
    

    

    