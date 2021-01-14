# @author: wy
# @project:send_email
def check_email_url(email_address):
    # check '@'
    at_count = 0
    for element in email_address:
        if element == '@':
            at_count = at_count + 1

    if at_count != 1:
        return False

    # check ' '
    for element in email_address:
        if element == ' ':
            return False

    # check '.com'
    postfix = email_address[-4:]
    if postfix != '.com':
        return False

    # check char
    # isalpha函数检测字符串中是否只包含字母
    # isdigit函数检测字符串中是否只包含数字字符
    for element in email_address:
        if element.isalpha() == False and element.isdigit() == False:
            if element != '.' and element != '@' and element != '_':
                return False

    return True
