from flask import Flask, jsonify, request, render_template
import random

# 创建Flask应用
app = Flask(__name__)

# 词库：英文单词为键，中文翻译为值
word_bank = {
    "apple": "苹果",
    "banana": "香蕉",
    "cat": "猫",
    "dog": "狗",
    "elephant": "大象",
    "fish": "鱼",
    "grape": "葡萄",
    "house": "房子",
    "ice cream": "冰淇淋",
    "jungle": "丛林"
}

# 获取随机题目
@app.route('/get_question')
def get_question():
    # 从词库中随机选择一个单词
    word = random.choice(list(word_bank.keys()))
    # 获取该单词的正确翻译
    correct_translation = word_bank[word]
    # 从词库中随机选择3个错误翻译
    wrong_translations = random.sample([v for k, v in word_bank.items() if v != correct_translation], 3)
    # 将正确翻译和错误翻译合并，并打乱顺序
    options = wrong_translations + [correct_translation]
    random.shuffle(options)
    # 返回JSON格式的题目数据
    return jsonify({
        "word": word,  # 当前单词
        "options": options,  # 4个选项
        "correct_answer": correct_translation  # 正确答案
    })

# 检查答案
@app.route('/check_answer', methods=['POST'])
def check_answer():
    # 获取前端发送的JSON数据
    data = request.json
    # 提取用户选择的答案和正确答案
    user_answer = data.get("answer")
    correct_answer = data.get("correct_answer")
    # 判断用户答案是否正确
    is_correct = (user_answer == correct_answer)
    # 返回JSON格式的结果
    return jsonify({"is_correct": is_correct})

# 首页
@app.route('/')
def index():
    # 渲染前端页面
    return render_template('index.html')

# 启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)