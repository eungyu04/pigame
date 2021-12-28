import numpy as np
import requests
import time
import os

np.set_printoptions(precision=10000, suppress=True)

with open("pi.txt") as f:
    piData = f.read()

print(piData[0])

def main():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    progressNumber = '' # 진행 현황

    score = 0

    userName = input('당신의 "이름"을 입력해주세요: ')

    while True:
        try:
            userGrade = int(input('당신의 "학년"을 입력해주세요: '))
            userClass = int(input('당신의 "반"을 입력해주세요: '))
            break
        except ValueError:
            print('[파이게임] 숫자만 입력 가능합니다.')
    print('[파이게임] 이름: ' + userName)
    #requests.get("http://localhost:5000/userupdate" , params={'user_name': userName, 'user_grade': userGrade, 'user_class': userClass, 'user_score': 0})
    #print('[파이게임] 당신이 입력하신 정보를 서버로 전송했습니다.')
    #requests.get("http://localhost:5000/clientmsg", params={'msg': '유저 정보 업데이트.'})


    print('[파이게임] 3초 뒤에 시작됩니다.')
    time.sleep(1)
    print('[파이게임] 2초 뒤에 시작됩니다.')
    time.sleep(1)
    print('[파이게임] 1초 뒤에 시작됩니다.')
    for i in range(10000):
        inputNumber = input(str(i + 1) + '번째 원주율 숫자를 입력해주세요! : ')
        if piData[i] == inputNumber:
            progressNumber = progressNumber + inputNumber
            print('정답!')
        else:
            score = i + 1
            print('================파이게임================')
            print('틀렸습니다 ㅅㄱ')
            print(': ' + str(i + 1) + '자리')
            print('======================================')
            break

    print('[파이게임] 서버에 당신의 결과를 전송합니다.')
    requests.get("http://localhost:5000/clientmsg", params={'msg': userName + '탈락.'})
    requests.get("http://localhost:5000/clientmsg", params={'msg': '스코어: ' + str(score)})
    requests.get("http://localhost:5000/userupdate" , params={'user_name': userName, 'user_grade': userGrade, 'user_class': userClass, 'user_score': score})
    requests.get("http://localhost:5000/clientmsg", params={'msg': '스코어 등록 완료.'})
    print('[파이게임] 전송완료.')
    
    main()

main()
