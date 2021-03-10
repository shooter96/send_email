# @author: wy
# @project:send_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def email_send(receivers, file=None):
    '''
    :param filename:
    :param receivers:
    :param file:发送的文件的路径
    :param receivers:
    '''
    # 邮件发送方
    from_addr = 'device-test@isyscore.com'
    password = 'qFy7Tp6aX44trRgb'
    sender = from_addr
    file = file
    filename = file.split('/')[-1]

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 构建附件
    att = MIMEApplication(open(file, 'rb').read())
    att["Content-Type"] = 'application/octet-stream'

    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))
    msg.attach(att)

    # 设置邮件内容
    content = 'hello,测试报告请查收，见附件！'
    textApart = MIMEText(content)
    msg.attach(textApart)

    # 主题设置
    msg['Subject'] = "自动化测试报告"

    # 发送人信息
    msg['From'] = '设备组' + '<{}>'.format(sender)

    try:
        server = smtplib.SMTP('smtp.exmail.qq.com')
        # 登录邮箱
        server.login(from_addr, password)
        # 发送邮件
        for receiver in receivers:
            msg['To'] = receiver
        server.sendmail(from_addr, receivers, msg.as_string())
        print('邮件发送成功')

        server.quit()
    except smtplib.SMTPException as e:
        print('邮件发送失败:{}'.format(e))


if __name__ == '__main__':
    # email_receivers_str = input("请输入邮件接收人邮箱号，多个邮箱使用逗号隔开:")
    # email_receivers_list = email_receivers_str.split(',')
    # send_file = input("请输入测试报告地址：")
    # filename = ''
    # try:
    #     filename = send_file.split('/')[-1]
    #     email_send(email_receivers_list, file=send_file, filename=filename)
    # except Exception as e:
    #     print("文件路径不正确:{}".format(e))
    email_send(['wangy@isyscore.com'], '/Users/shooter/Documents/网关列表.xlsx')
    # email_send(['wangy@isyscore.com'], '/Users/shooter/Desktop/log.html')

