def length_of_last_word(s: str) -> int:
    i = len(s) - 1

    while i >= 0 and s[i] == " ":
        i -= 1

    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


def length_of_last_word_split(s: str) -> int:
    return len(s.strip().split()[-1])


# 测试代码
if __name__ == "__main__":
    # 测试用例：(输入字符串, 预期结果)
    test_cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),  # 单个单词无空格
        ("   hello   ", 5),  # 单词前后全是空格
        ("test  case  ", 4),  # 末尾多个空格
    ]

    func_list = [
        ("双指针遍历", length_of_last_word),
        ("split简洁写法", length_of_last_word_split),
    ]

    print("===== 最后一个单词长度 测试结果 =====\n")
    all_pass = True

    for case_idx, (s, expect) in enumerate(test_cases, 1):
        print(f"测试用例 {case_idx}")
        print(f"输入: '{s}'")
        print(f"预期结果: {expect}")

        for name, func in func_list:
            res = func(s)
            status = "✅ 通过" if res == expect else "❌ 失败"
            if res != expect:
                all_pass = False
            print(f"  {name}: 输出 {res} | {status}")
        print("-" * 40)

    print("\n全部测试完成，结果：", "所有用例通过" if all_pass else "存在用例失败")
