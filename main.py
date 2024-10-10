import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


with gr.Blocks() as demo:
    gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
    )
    gr.Markdown(
        "If you liked this space, please give me a star on GitHub 😉: [Github repo](https://github.com/jorge-armando-navarro-flores/Translator)"
    )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
