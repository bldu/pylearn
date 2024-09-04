import gradio as gr

def show_date(date_type, start_date1, end_date1, start_date2, end_date2):
    if date_type == "date1":
        return f"start_date1:{start_date1}, end_date1:{end_date1}"
    if date_type == "date2":
        return f"start_date2:{start_date2}, end_date2:{end_date2}"
    else:
        return "please choose date type first"

def main():
    with gr.Blocks() as demo:
        with gr.Column():
            date_type = gr.Dropdown(choices=["date1", "date2"], label="choose the date type")
            with gr.Row(visible=False) as line1:
                start_date1 = gr.DateTime(type="datetime", label="start1")
                end_date1 = gr.DateTime(type="datetime", label="end1")
            with gr.Row(visible=False) as line2:
                start_date2 = gr.DateTime(type="datetime", label="start2")
                end_date2 = gr.DateTime(type="datetime", label="end2")
            date_show = gr.Textbox(placeholder="date shown here", interactive=True)
        date_type.change(fn=lambda x: [gr.update(visible=x=="date1"), gr.update(visible=x=="date2")],
                         inputs=[date_type], outputs=[line1, line2])
        date_show.focus(fn=show_date, inputs=[date_type, start_date1, end_date1, start_date2, end_date2], outputs=[date_show])

    demo.launch(server_name="0.0.0.0", server_port=8000, root_path="/demo")

if __name__ == "__main__":
    main()
