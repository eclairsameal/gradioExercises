import gradio as gr


def greet(name):
  return f"Hello , {name}!"

demo = gr.Interface(greet, "text", "text")
demo.launch(server_name="0.0.0.0")
