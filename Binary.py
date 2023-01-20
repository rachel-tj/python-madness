class Binary:


    # from decimal to anything
    def dec_to(self, num, base):
        if base > 36 or base < 2:
            print("no can do")
            return
        answer = ""
        try:
            num = int(num)
        except ValueError:
            print("there's something other than numbers here.")
            return;
        while num != 0:
            digit = num % base
            if digit > 9:
                digit = chr(digit + 87)
            answer += str(digit)
            num //= base
        answer = answer[::-1]
        return answer
    

    # from anything to decimal
    def to_dec(self, num, base):
        if base > 36 or base < 2 or " " in num:
            print("no can do")
            return
        sum = 0
        num = str(num)
        place = 0
        while len(num) > 0:
            digit = num[-1]
            if ord(digit) >= 97 and ord(digit) <= 122:
                digit = ord(digit) - 87
            add = int(digit) * (base ** place)
            num = num[:-1]
            sum += int(add)
            place += 1
        return sum

    def hex_to_rgb(self, hex):
        arr = []
        for i in range (0, len(hex), 2):
            arr.append(hex[i : i + 2])
        answer = "rgb("
        for num in arr:
            answer += str(self.to_dec(num, 16)) + ", "
        return answer[:-2] + ")"

    def rgb_to_hex(self, rgb):
        arr = rgb.split(", ")
        answer = "#"
        for color in arr:
            answer += self.dec_to(color, 16)
        return answer
