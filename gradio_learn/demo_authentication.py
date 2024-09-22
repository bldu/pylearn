import gradio as gr

# 模拟用户数据库
users = {
    "user1": "password1",
    "user2": "password2"
}

# 认证函数
def authenticate(username, password):
    if username in users and users[username] == password:
        return True
    return False

# 创建一个简单的Gradio界面
def greet(name):
    return f"Hello, {name}!"

# 创建Gradio Blocks
with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Enter your name")
    greet_button = gr.Button("Greet")
    output = gr.Textbox(label="Output")

    # 绑定Greet按钮的回调函数
    greet_button.click(greet, inputs=[name_input], outputs=[output])

# 启动Gradio应用，并设置认证函数
demo.launch(auth=authenticate, server_name="0.0.0.0", server_port=8888)
