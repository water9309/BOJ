'''
입력된 영단어 내에서 최대로 사용된 알파벳 찾기
'''
T = list(map(str, input())) # 영단어입력
data = [0]*26 # 개수 체크용 배열
count = 0
for i in range(97, 123): # 알파벳(소문자) 체크
    for j in range(len(T)): #단어 체크
        #알파벳 존재 여부
        if(i == ord(T[j].lower())):
           data[i-97] += 1

#알바펫 최대개수 중복 확인
for i in range(len(data)):
    if(data[i] == max(data)):
        count += 1

if(count == 1):
    print((chr(data.index(max(data))+97).upper()))
else:
    print("?")

#a = 97, z = 122 26개
#A = 65, Z = 90
