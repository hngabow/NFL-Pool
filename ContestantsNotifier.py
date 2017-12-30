class SpyNotifier():
    def alert(self, error_message):
        print error_message
    def notify(self, afc_info, nfc_info):
        for info in afc_info:
            print info[0], info[1], info[2]
        for info in nfc_info:
            print info[0], info[1], info[2]

