from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# 访问主页，返回 HTML 页面
@app.route('/')
def index():
    return render_template('index.html')

# 绑定病例信息（模拟存储）
patients = {}

@app.route('/bind_patient', methods=['POST'])
def bind_patient():
    data = request.json
    patient_id = data.get('patient_id')
    if not patient_id:
        return jsonify({'error': 'Missing patient_id'}), 400

    # 模拟绑定一些信息
    patients[patient_id] = {
        'name': data.get('name', ''),
        'age': data.get('age', ''),
        'gender': data.get('gender', ''),
        'other_info': data.get('other_info', '')
    }
    return jsonify({'message': 'Patient bound successfully'})

# 推荐中医治疗方案
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
         data = request.json
         ctDNA = data.get('ctDNA')
         patient_id = data.get('patient_id')

         if ctDNA is None:
             return jsonify({'error': 'Missing ctDNA value'}), 400

         risk_level = get_risk_level(ctDNA)
         recommendation = get_recommendation(risk_level)

         # 返回推荐内容
         response = jsonify({
                 'risk_level': risk_level,
            'recommendation': recommendation
        })

         response.headers.add('Content-Type', 'application/json; charset=utf-8')  # 设置编码为 UTF-8
         return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_risk_level(ctDNA):
    if 70 <= ctDNA <= 99:
        return '高风险'
    elif 50 <= ctDNA < 70:
        return '中风险'
    else:
        return '低风险'

def get_recommendation(risk_level):
    # 这里是固定的文本方案，先模拟
    if risk_level == '高风险':
        return {
            '中药药剂': '处方A：XX中药组合。',
            '食疗': '推荐食谱：鲫鱼汤、山药粥。',
            '辅助疗法': '针灸疗法，每周2次。',
            '养生操/打坐': '太极拳每日练习20分钟。'
        }
    elif risk_level == '中风险':
        return {
            '中药药剂': '处方B：调理脾胃，健脾益气。',
            '食疗': '推荐食谱：红枣莲子粥。',
            '辅助疗法': '推拿疗法，每周1次。',
            '养生操/打坐': '八段锦，每天早晚各一次。'
        }
    else:
        return {
            '中药药剂': '处方C：保养肝肾，益气养血。',
            '食疗': '推荐食谱：银耳百合汤。',
            '辅助疗法': '足浴放松，每周3次。',
            '养生操/打坐': '静坐冥想，每晚15分钟。'
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

