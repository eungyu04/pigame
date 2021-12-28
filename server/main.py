from os import name
from flask import Flask, request, render_template, redirect


user_Data ={
    'users':['박범준', '이은규', '문재인'], # 유저의 이름만을 담은 리스트
    'inform':{# 유저의 세부 정보
        '박범준':{'grade': 3 , 'class': 4, 'score': 5},
        '이은규':{'grade': 3 , 'class': 2, 'score': 2},
        '문재인':{'grade': 3 , 'class': 1, 'score': 4}
        } 
}

user_list = list(user_Data.values()) # 유저 리스트화 (1명당)

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        return redirect('/userrank/')

@app.route('/userlist')
def index():
    item2 = user_Data['inform'] # user_Data 에서 inform 부분만가져오기 
    return render_template('index.html', 
            data = user_Data, items = user_list, items2 = item2)

@app.route('/userrank')
def sort_Scores():
    global user_Data
    all_score_list = [] # 중복을 포함한 모든 요소들이 저장되는 리스트 ( 유저와 점수 일대일대응용 리스트 )
    sorted_user = [] # 높은 점수인 유저부터 저장되는 리스트 ( 유저와 점수 일대일대응용 리스트 )

    for i in user_Data['users']: # 유저목록들 돌면서 이름 하나씩 가져옴
        all_score_list.append(user_Data['inform'][i]['score']) # 가져온 이름에 해당하는 점수를 리스트에 추가
        
    
    all_score_list.sort(reverse=True) # 내림차순 정렬
    print(str(all_score_list))
    set_score_list = set(all_score_list) # 중복 요소 제거 ( 점수에 해당하는 유저 찾기용 리스트 )

    for k in set_score_list: # 각각의 점수에 해당하는 유저를 알아냄
        for t in user_Data['users']:
            if user_Data['inform'][t]['score'] == k: # 내림차순 정렬된 점수 리스트에 해당하는 유저라면
                sorted_user.append(t) # 차곡차곡 쌓기

    sorted_user.reverse() # 리스트 뒤집어서 내림차순 정렬
    print(str(sorted_user))

    dictionary = dict(zip(sorted_user, all_score_list)) # 사람 : 점수 딕셔너리 만들음 > html작업하기 편하게
    print(str(dictionary))
    
    return render_template('ranking.html',
            data = dictionary)

@app.route('/userclear')
def userclear(): # 유저 초기화
    user_Data = {}

@app.route('/clientmsg', methods=['GET']) # GET요청 받음
def clientmsg(): # ex) http://localhost:5000/clientmsg?msg=ㅇㅅㅇ
    msg = request.args["msg"]
    print('[piGame Client] ' + str(msg))
    return msg
    
@app.route('/userupdate', methods=['GET']) # GET요청 받음 
def userupdate(): # ex) http://localhost:5000/useradd?user_name='박범준'&user_grade=2&user_class=7&user_score=0
    user_name = request.args["user_name"]
    user_grade = request.args["user_grade"]
    user_class = request.args["user_class"]
    user_score = request.args["user_score"]

    if user_name not in user_Data['users']: # 처음 가입한 유저일 경우 리스트에 추가.
        user_Data['users'].append(user_name)

    user_Data['inform'][user_name] = {} # 새로운 유저 추가
    user_Data['inform'][user_name]['grade'] = int(user_grade) # 학년 설정
    user_Data['inform'][user_name]['class'] = int(user_class) # 반 설정
    user_Data['inform'][user_name]['score'] = int(user_score) # 점수 설정
    print('[유저데이터] ' + str(user_Data))
    return user_Data
    

@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name}({user_id})!'

            
if __name__ == '__main__':
    app.run(debug=True)
