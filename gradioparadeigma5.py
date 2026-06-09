!pip install gradio



import gradio as gr

def calculator(num1, num2, operation):
  try:
    n1=float(num1)
    n2=float(num2)
  except:
    return "Εισάγετε έγκυρους αριθμούς"


  if operation == "+":
    return f"Αποτέλεσμα : {n1+n2}"
  elif operation == "-":
    return f"Αποτέλεσμα : {n1-n2}"
  elif operation == "*":
    return f"Αποτέλεσμα {n1*n2}"
  elif operation == "/":
    if n2 == 0:
      return "Δεν γίνεται διαίρεση με το 0"
    return f"Αποτέλεσμα {n1/n2}"

  


demo = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Number(label="1ος Αριθμός", value=10),
        gr.Number(label="2ος Αριθμός",value = 5),
        gr.Radio(["+","-", "*", "/"],
                label = "Διάλεξε πράξη",
               value = " + ")],
    outputs=gr.Textbox(label="Απάντηση"),
    title="Calculator",
    description = " Ενας απλός calculator για απλές πράξεις")

demo.launch()
