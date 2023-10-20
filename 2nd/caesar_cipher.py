# モジュール
import sys

def make_caesar(input_char:str,shift_bit:int):
    
    output_char:str = ""
    input_bytes:int = int(hex(ord(input_char)),16) 
    output_bytes:int

    # 加算されたビットが最大値を超えた場合の対処
    def fix_difference(val,addition,max,min):
        if val + addition > max:
            val = min + ((val + addition) - max)
        else:
            val = val + addition
        return val

    # ローマ字の場合の場合
    if(input_char.isascii()):
        ALPHABET_MAX = 126
        ALPHABET_MIN = 33
        q,addition = divmod(shift_bit,ALPHABET_MAX-ALPHABET_MIN)
        output_bytes = fix_difference(input_bytes,addition,ALPHABET_MAX,ALPHABET_MIN)
    # ひらがなorカタカナの場合
    else:
        HIRAGANA_MAX = 12448
        HIRAGANA_MIN = 12353
        KATAKANA_MIN = 12449
        KATAKANA_MAX = 12542
        
        if(input_bytes>=HIRAGANA_MIN and input_bytes <= HIRAGANA_MAX):
            # ひらがな
            q,addition = divmod(shift_bit,HIRAGANA_MAX-HIRAGANA_MIN)
            output_bytes = fix_difference(input_bytes,addition,HIRAGANA_MAX,HIRAGANA_MIN)
        
        elif(input_bytes >= KATAKANA_MIN):
            # カタカナ
            q,addition = divmod(shift_bit,KATAKANA_MAX-KATAKANA_MIN)
            output_bytes = fix_difference(input_bytes,addition,KATAKANA_MAX,KATAKANA_MIN)
        
        else:
            pass
    return chr(output_bytes)
    
# メイン関数
def main():
    string = input("暗号化したい文字を入力してください>>")
    shift = input("シフトする値を入力してください>>")
    
    if (shift.isdecimal()==False):
        print("入力が正しくありません。再度やり直してください。")
        return

    output_string = ""
    for val in list(string):
        output_string += make_caesar(val,int(shift))


if __name__=="__main__":
    main()
