class Notifier:
    def __init__(self, method='email'):
        self.method = method

    def send_notification(self, message):
        if self.method == 'email':
            self.send_email(message)
        elif self.method == 'slack':
            self.send_slack(message)

    def send_email(self, message):
        # 发送邮件的逻辑
        pass

    def send_slack(self, message):
        # 发送 Slack 消息的逻辑
        pass
