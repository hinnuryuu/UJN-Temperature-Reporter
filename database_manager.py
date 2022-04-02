# 用户数据库管理工具
import os
import json


def find_database() -> bool:
    for filename in os.listdir():
        if filename == "users.json":
            return True
    return False


def read_database() -> str:
    if find_database():
        with open("users.json", "r", encoding="utf-8") as f:
            info = f.read()
    else:
        info = "N/A"
    return info


def parse_database() -> dict:
    info = read_database()
    if info == "N/A":
        return {'data': []}
    else:
        try:
            information = json.loads(info)
        except json.JSONDecodeError:
            return {'data': []}
        else:
            return eval(str(information))


def write_database(info: dict) -> None:
    if find_database():
        with open("users.json", "w", encoding="utf-8") as f:
            information = json.dumps(info, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ':'))
            f.write(information)
        print("数据库更新成功!")
    else:
        print("数据库更新失败!")


def append_database(username: str, password: str) -> None:
    if search_database(username)[0]:
        print("该用户已在此数据库中!")
        exit(0)
    else:
        new_user = {'username': username, 'password': password}
        information = parse_database()
        information['data'].append(new_user)
        write_database(information)


def remove_database(username: str) -> None:
    information = parse_database()
    search_answer = search_database(username)
    if search_answer[0]:
        del(information['data'][search_answer[1]])
    else:
        print("该用户没有在此数据库中!")
        exit(0)
    write_database(information)


def search_database(username: str) -> tuple[bool, int]:
    information = parse_database()
    length = len(information['data'])
    for index in range(length):
        if information['data'][index]['username'] == username:
            return True, index
    return False, -1


def update_database(username: str, password: str) -> None:
    search_answer = search_database(username)
    information = parse_database()
    if search_answer[0]:
        information['data'][search_answer[1]]['username'] = username
        information['data'][search_answer[1]]['password'] = password
    else:
        print("该用户没有在此数据库中!")
        exit(0)
    write_database(information)


if __name__ == '__main__':
    print("1.增加用户成员\n2.删除用户成员\n3.更新用户成员\n4.查询用户成员")
    choice = input("输入选项以确定要进行的操作:")
    if choice == '1':
        append_username = input("输入新增的username:")
        append_password = input("输入新增的password:")
        append_database(append_username, append_password)
    elif choice == '2':
        remove_username = input("输入即将删除的username,以删除其用户信息:")
        remove_database(remove_username)
    elif choice == '3':
        update_username = input("输入更新的username:")
        update_password = input("输入更新的password:")
        update_database(update_username, update_password)
    else:
        search_username = input("输入即将查询的username:")
        search_feedback = search_database(search_username)
        if search_feedback[0]:
            data = parse_database()
            print("该用户在数据库中,其信息如下:")
            print("username:%s  password:%s" % (
                data['data'][search_feedback[1]]['username'],
                data['data'][search_feedback[1]]['password']
            ))
        else:
            print("该用户不在数据库中")
