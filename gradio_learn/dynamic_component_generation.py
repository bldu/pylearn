import gradio as gr
from gradio_toggle import Toggle
import json

TOTAL_TOGGLE_NUM = 20

def show_components(eqp_chamber):
    eqp_chamber_list = eqp_chamber.split(",")
    if len(eqp_chamber_list) > TOTAL_TOGGLE_NUM:
        raise gr.Error("too many eqp_chambers")
    update_show = [gr.update(visible=True, label=f"{eqp_chamber}", value=False) for eqp_chamber in eqp_chamber_list]
    update_hide = [gr.update(visible=False, value=False) for _ in range(TOTAL_TOGGLE_NUM-len(eqp_chamber_list))]
    return update_show + update_hide


def save_toggle_state(eqp_chamber, *toggle_list):
    eqp_chamber_list = eqp_chamber.split(",")
    state_dict = {eqp_chamber_list[i]:toggle_list[i] for i in range(len(eqp_chamber_list))}
    with open("state.json", "w") as f:
        json.dump(state_dict, f, indent=4)



def ui(host, port):
    with gr.Blocks() as demo:
        with gr.Column():
            eqp_chamber = gr.Textbox(label="EQP Chamber")
            toggle_list = []
            for i in range(TOTAL_TOGGLE_NUM):
                toggle = Toggle(visible=False, value=False, info="if enable FB", interactive=True)
                toggle_list.append(toggle)

        eqp_chamber.change(fn=show_components, inputs=[eqp_chamber], outputs=toggle_list)

        with gr.Column():
            save_button = gr.Button(value="save")
        save_button.click(fn=save_toggle_state, inputs=[eqp_chamber]+toggle_list)

    demo.launch(server_name=host, server_port=port)


def main():
    ui("0.0.0.0", 8888)


if __name__ == "__main__":
    main()
