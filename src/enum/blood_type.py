class BloodType:
    def __init__(self, type: str):
        if type not in ('A', 'B', 'O', 'AB'):
            raise ValueError('妥当な血液型ではありません。')
        self.type = type
    def get_name(self):
        return self.type