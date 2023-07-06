def append_t0_list(text: str, a: list[str]):
    a.append(text.casefold())
    return a
a = []
print(append_t0_list("dyg",a))