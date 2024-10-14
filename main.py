import gradio as gr
from app import set_api_key, response


with gr.Blocks() as demo:
    gr.Label("Natural Language Calculator", color="#6EACDA")
    api_key_textbox = gr.Textbox(
        label="Open AI API Key",
        placeholder="Set your OpenAI API key (Required)",
        type="password",
    )
    api_key_link_markdown = gr.Markdown(
        "[Get Your OpenAI API key here](https://platform.openai.com/api-keys)"
    )

    with gr.Row():

        with gr.Column():
            message_textbox = gr.Textbox(
                label="Query", placeholder="Add 2 and 5, then multiply it by 7"
            )
            submit_btn = gr.Button(value="Submit")
        with gr.Column():
            output_textbox = gr.Textbox(label="Response")

    api_key_textbox.change(
        set_api_key, inputs=[api_key_textbox], outputs=[output_textbox]
    )
    submit_btn.click(
        fn=response, inputs=[message_textbox], outputs=[message_textbox, output_textbox]
    )

    gr.Markdown(
        "If you liked this space, please give me a star on GitHub 😉: [Github repo](https://github.com/jorge-armando-navarro-flores/Simple_Natural_Language_AI_Agent_Calculator)"
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
