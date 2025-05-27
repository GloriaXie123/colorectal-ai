
# 肠癌智筛宝开发部署文档 / Development and Deployment Documentation for Colorectal Cancer Smart Screening

## 项目简介 / Project Overview

肠癌智筛宝是一款用于根据ctDNA值推荐中医药治疗方案的Web应用。当前版本包含前端展示页面和后端推荐逻辑，数据来源为用户输入并进行内存模拟存储。

Colorectal Cancer Smart Screening is a web application designed to recommend Traditional Chinese Medicine (TCM) treatments based on ctDNA values. The current version includes a frontend display page and backend recommendation logic, with data simulated in-memory from user input.

## 技术栈 / Tech Stack

- 前端 / Frontend: HTML, CSS, JavaScript
- 后端 / Backend: Python, Flask
- 跨域支持 / CORS: flask_cors
- 内网穿透 / Tunneling: ngrok

## 项目结构 / Project Structure

```
project_root/
├── templates/
│   ├── index.html       # 主页面 Main page
│   ├── style.css        # 样式文件 Style file
│   └── script.js        # 前端逻辑 Frontend logic
├── app.py               # Flask 后端主程序 Flask backend main app
└── requirements.txt     # 依赖文件 Dependencies
```

## 部署步骤 / Deployment Steps

### 1. 创建虚拟环境 / Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. 安装依赖 / Install Dependencies

```bash
pip install flask flask_cors
```

### 3. 启动后端服务 / Start Backend Service

```bash
python app.py
# 或使用后台运行方式 / Or run in background:
nohup python app.py > backend.log 2>&1 &
```

### 4. 启动前端服务器 / Start Frontend Server

```bash
cd templates
python3 -m http.server 8080
# 或后台运行 / Or run in background:
nohup python3 -m http.server 8080 > frontend.log 2>&1 &
```

### 5. 使用 Ngrok 暴露端口 / Expose Port via Ngrok

```bash
ngrok http 8080
# 记录生成的网址 / Note the generated public URL
```

### 6. 修改前端接口地址 / Modify Frontend API URL

在 `script.js` 中，将 `fetch` 请求的地址改为 ngrok 的 https 地址：

```js
fetch('https://your-ngrok-url.ngrok-free.app/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ patient_id: ..., ctDNA: ... })
})
```

### 7. 访问与测试 / Access and Test

- 打开浏览器访问 ngrok 提供的网址 / Visit the ngrok public URL in your browser.
- 输入信息并点击推荐按钮 / Fill in the information and click the recommendation button.

## 注意事项 / Notes

- 请确保前后端接口使用 HTTPS，避免混合内容导致请求失败。
- 当前系统为测试版，仅做演示用途。
- 如果 ngrok 报错 “同时在线数超过限制”，请升级账户或关闭其他实例。

## 版本说明 / Version Info

版本: v0.1 Beta  
日期: 2025年5月  
作者: 项目发起人 + ChatGPT 协助  
Version: v0.1 Beta  
Date: May 2025  
Author: Project Owner + ChatGPT Collaboration
