# -*- coding: utf-8 -*-
import time
import lora_setting


# LoRa送信用クラス
class radio:

    def __init__(self, lora_device, channel):
        self.sendDevice = lora_setting.LoraSettingClass(lora_device)
        self.channel = channel
        #self.channel = 15

    # ES920LRデータ送信メソッド
    #def lora_send(self):
    def sendData(self):
        # LoRa初期化
        self.sendDevice.reset_lora()
        # LoRa設定コマンド
        set_mode = ['1', 'd', self.channel, 'e', '0001', 'f', '0001', 'g', '0000',
                    'l', '2', 'n', '1', 'p', '1', 'y', 'z']
        # LoRa設定
        self.sendDevice.setup_lora(set_mode)
        
        #開始時間の記録
        self.startTime = time.time()
        self.timer = 0
        
        # LoRa(ES920LR)データ送信
        while True:
            try:
                self.timer = 1000*(time.time() - self.startTime) #経過時間 (ms)
                self.timer = int(self.timer)
                #ログデータ作成。\マークを入れることで改行してもコードを続けて書くことができる
                data = str(self.timer) + ","\
                          + 'aaaa'
                """
                # 送るデータ
                data = 'aaaa'
                """
                print('<-- SEND -- [ {} ]'.format(data))
                self.sendDevice.cmd_lora('{}'.format(data))
            except KeyboardInterrupt:
                self.sendDevice.close()
            # 1秒待機
            time.sleep(1)
