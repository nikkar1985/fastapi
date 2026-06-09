!pip install gradio




import gradio as gr

def greet(name):
  return f"Hello {name}. Έτοιμο το πρώτο Interface"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()






