'''
사용된알파벳 체크
'''

S = input() # 알파벳 입력
data = [] # 알파벳 체크
position = [0]*26

for i in range(97, 123): # 알파벳을 아스키코드순으로 확인
    if chr(i) not in S: #알파벳 없으면 -1처리
        position[i-97] = -1
    else:
        for j in range(len(S)): # 입력한 알파벳 체크
            if(i == ord(S[j])):
                if S[j] in data:
                    continue
                else:
                    data.append(S[j])
                    position[i-97] = j

print(position, end=' ')
#a = 97, z = 122 26개
