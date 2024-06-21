f = open("yesterday.txt", "r")
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
# n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")  #대소문자 구분제거
"""_summary_
    """# print("Number of a word 'Yesterday'", n_of_yesterday)


#윈도우 사용자 컨트롤 + 쉬프트 + p
# 맥 사용자 command + shift + p