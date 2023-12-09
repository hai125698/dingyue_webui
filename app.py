import base64

from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)

# 指定的文件路径
file_path = "node_info"
password_file = "password"
app.secret_key = '123456'


# 读取文件内容
def read_file():
    with open(file_path, "r") as file:
        content = file.read().splitlines()
    return content


# 保存文件内容
def save_file(content):
    with open(file_path, "w") as file:
        file.write("\n".join(content))


# 读取密码
def read_password():
    with open(password_file, "r") as file:
        password = file.read().strip()
    return password


# 保存密码
def save_password(password):
    with open(password_file, "w") as file:
        file.write(password)


# 进入主页
@app.route('/')
def index():
    print(isLoggedIn())
    # 如果未登录，重定向到登录页面
    if not isLoggedIn():
        return redirect(url_for('login'))

    # 读取文件内容
    content = read_file()

    # 检查是否有错误消息
    error_message = request.args.get('error_message', None)

    return render_template('index.html', content=content, error_message=error_message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 获取提交的密码
        password = request.form.get('password')

        # 读取正确的密码
        correct_password = read_password()

        # 检查密码是否正确
        if password == correct_password:
            # 设置会话变量以指示成功登录
            session['isLoggedIn'] = True
            # 重定向到主页
            return redirect(url_for('/'))
        else:
            # 密码错误，显示错误消息
            return render_template('login.html', error_message="密码错误")

    # 显示登录页面
    return render_template('login.html', error_message=None)


@app.route('/check_password', methods=['POST'])
def check_password():
    # 获取前端提交的密码
    password = request.form.get('password')

    # 读取正确的密码
    correct_password = read_password()

    # 验证密码是否正确
    if password == correct_password:
        session['isLoggedIn'] = True
        return redirect(url_for('index'))
    else:
        # 密码错误，重定向到登录页面，并附带错误消息
        return redirect(url_for('login', error_message='密码错误'))


@app.route('/change_password', methods=['POST'])
def change_password():
    if not isLoggedIn():
        return "请先登录"

    # 获取前端提交的新密码
    new_password = request.form.get('newPassword')

    # 保存新密码
    save_password(new_password)

    # 读取文件内容
    content = read_file()
    return jsonify(content=content, message="密码修改成功")


@app.route('/save', methods=['POST'])
def save():
    if not isLoggedIn():
        return "请先登录"

    # 获取前端提交的内容
    new_content = request.form.getlist('content[]')

    # 保存文件内容
    save_file(new_content)

    # 返回 JSON 格式的消息和文件内容
    return jsonify(message="保存成功", content=new_content)


@app.route('/get_node')
def get_node():
    # 获取前端提交的token
    token = request.args.get('token')

    # 读取正确的密码
    correct_password = read_password()

    # 检查token是否与正确的密码匹配
    if token == correct_password:
        # 执行文件内容的处理
        path = 'node_info'
        with open(path, 'rb') as file:
            file_content = file.read()
            base64_content = base64.b64encode(file_content).decode('utf-8')
            return base64_content
    else:
        # 返回token错误提示
        return "Token 错误"


# 检查登录状态的路由
@app.route('/check_login_status', methods=['GET'])
def check_login_status():
    # 检查 session 中是否存在 'isLoggedIn' 键
    isLoggedIn = 'isLoggedIn' in session and session['isLoggedIn']

    # 返回 JSON 格式的响应，表示登录状态
    return jsonify({'isLoggedIn': isLoggedIn})


# 新增一个函数来检查是否已经登录
def isLoggedIn():
    return 'isLoggedIn' in session and session['isLoggedIn']


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
