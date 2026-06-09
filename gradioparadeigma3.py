!pip install gradio




import gradio as gr

def chess_move_validator(piece, current_square, target_square):
  try:
    curr_file, curr_rank = current_square[0].lower(), int(current_square[1])
    target_file, targ_rank = target_square[0].lower(), int(target_square[1])
  except:
    return "Λάθος μορφή τετραγώνων βαλε πχ e2"


  if current_square.lower() == target_square.lower():
    return "Το κομμάτι είναι ήδη εκεί"

  if piece == "Rook": 
    if curr_file == target_file or curr_rank == targ_rank:
      return f"Νόμιμη κίνηση, ο πύργος κινείται ευθεία από το {current_square} στο {target_square}"
    else:
      return "Μή νόμιμη κίνηση"
    
  elif piece == "Bishop":
    file_dist = abs(ord(curr_file) - ord(target_file))
    rank_dist = abs(curr_rank - targ_rank) 
    if file_dist == rank_dist:
      return f"Νόμιμη κίνηση. Ο Αξιωματικός κουνιέται διαγώνια από {current_square} σε {target_square}"
    else:
      return "Μη νόμιμη κίνηση"



demo = gr.Interface (
    fn=chess_move_validator,
    inputs=[gr.Dropdown(["Rook", "Bishop"], label="Επίλεξε κομμάτι", value="Rook"),
            gr.Textbox(label="Τρέχον τετράγωνο", value = "e2"),
            gr.Textbox(label="Τετράγωνο στόχος", value = "e4")
            ],
    outputs=gr.Textbox(label="Αποτέλεσμα Ελέγχου"),
    title = "Chess move validator",
    description ="Δοκίμασε εαν οι κινήσεις του πύργου ή του αξιωματικού είναι νόμιμες"
)

demo.launch()
