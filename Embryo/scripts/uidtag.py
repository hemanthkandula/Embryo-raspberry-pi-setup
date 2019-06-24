from pirc522 import RFID
import RPi.GPIO as GPIO


TAGS = ['484341F49','48434B94D8','4843457E3C','484427F28','484347D090','48433B526E','484346B9F8','4843422B6E','484345DC9E','48434B266A']

IDS = ['embryo1','embryo2','embryo3', 'embryo4','embryo5','embryo6','embryo7','embryo8','embryo9','embryo10','embryo11','embryo12','embryo13','embryo14']



class RC522Reader:
    def __init__(self):
        self.reader = RFID()

    def force_read_id(self):
        while True:
            self.reader.wait_for_tag()
            (error, tag_type) = self.reader.request()
            if error:
                continue

            #print("Tag detected")
            (error, uid) = self.read_uid()
            if error:
                continue

            card_uid = ''
            for part in uid:
                card_uid += ("%X" % part)
            return IDS[TAGS.index(card_uid)]


            #IDS[TAGS.index(card_uid)]
            #return card_uid

    def read_uid(self):
        # https://www.nxp.com/docs/en/application-note/AN10927.pdf
        (error, uid) = self.reader.anticoll()
        if error:
            return error, None

        if uid[0] is not 0x88:
            return False, uid
        
        error = self.reader.select_tag(uid)  

        full_uid = uid[1:3]

        #print("UID is not yet complete")
        (error, cl2) = self.read_cl2()
        if error:
            return error, None

        if cl2[0] is not 0x88:
            full_uid.extend(cl2)
            return False, full_uid

        full_uid.extend(cl2[1:3])
        (error, cl3) = self.read_cl3()
        if error:
            return error, None

        full_uid.extend(cl3)
        return False, full_uid

    def read_cl2(self):
        back_data = []
        serial_number = []

        serial_number_check = 0

        self.reader.dev_write(0x0D, 0x00)
        serial_number.append(0x95)
        serial_number.append(0x20)

        (error, back_data, back_bits) = self.reader.card_write(self.reader.mode_transrec, serial_number)
        if not error:
            if len(back_data) == 5:
                for i in range(4):
                    serial_number_check = serial_number_check ^ back_data[i]

                if serial_number_check != back_data[4]:
                    error = True
            else:
                error = True

        return error, back_data

    def read_cl3(self):
        back_data = []
        serial_number = []

        serial_number_check = 0

        self.reader.dev_write(0x0D, 0x00)
        serial_number.append(0x97)
        serial_number.append(0x20)

        (error, back_data, back_bits) = self.reader.card_write(self.reader.mode_transrec, serial_number)
        if not error:
            if len(back_data) == 5:
                for i in range(4):
                    serial_number_check = serial_number_check ^ back_data[i]

                if serial_number_check != back_data[4]:
                    error = True
            else:
                error = True

        return error, back_data

# rdr = RC522Reader()
# try:
#     while True:
    



#         uid = rdr.force_read_id()
#         print(uid)
#         input()

# finally:
#         GPIO.cleanup()
