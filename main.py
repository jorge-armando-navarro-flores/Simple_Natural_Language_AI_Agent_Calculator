import gradio as gr
from app import set_api_key, response


with gr.Blocks() as demo:

    api_key_textbox = gr.Textbox(type="password")
    message_textbox = gr.Textbox(value="add 2 and 5, then multiply it by 7")
    gr.Interface(
        fn=response,
        inputs=[message_textbox],
        outputs=["text"],
    )
    api_key_textbox.change(set_api_key, inputs=[api_key_textbox])

    gr.Markdown(
        "If you liked this space, please give me a star on GitHub 😉: [Github repo](https://github.com/jorge-armando-navarro-flores/Translator)"
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
