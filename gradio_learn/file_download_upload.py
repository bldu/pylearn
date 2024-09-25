import gradio as gr
import os

def download_file():
    # 这里可以是你生成文件的逻辑，例如从数据库读取数据并保存为文件
    # 这里我们简单地创建一个文本文件
    with open("example.txt", "w") as f:
        f.write("This is an example file for download.")
    # 返回文件路径
    return "example.txt"


def download_file2(name):
    with open(f"{name}.txt", "w") as f:
        f.write("This is an example file for download.")
    return f"{name}.txt"


def upload_file(file_path):
    gr.Info(f"file to be uploaded to {file_path}")
    return  file_path


def ui(host, port):
# 创建 Gradio 界面
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                # 创建一个按钮，点击后触发下载
                download_button = gr.Button("Download File")
                # 创建一个 File 组件，用于显示下载的文件
                output_file = gr.File(label="file is here")
            # 将按钮与下载函数绑定
            download_button.click(download_file, outputs=output_file)

            with gr.Column():
                d = gr.DownloadButton(label="download | set value for download button", value="example.txt")

            with gr.Column():
                filename = gr.Textbox(label="file name")
                d2 = gr.DownloadButton(label="download | event trigger")
            d2.click(fn=download_file2, inputs=[filename], outputs=[d2])

        with gr.Row():
            with gr.Column():
                u = gr.UploadButton()
                display_file = gr.File()
            u.upload(fn=upload_file, inputs=[u], outputs=[display_file])


    # 启动 Gradio 界面
    demo.launch(server_name=host, server_port=port)


if __name__ == "__main__":
    ui("0.0.0.0", 7860)
