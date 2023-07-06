def sum_string(*params: str):
    result = ""
    for element in params:
        result = result + element
    return result
print(sum_string("gjg", "fuuyf"))