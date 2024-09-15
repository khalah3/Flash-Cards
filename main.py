from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
dic_data={}

try:
    data=pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    dic_data=original_data.to_dict(orient='records')
else:
    dic_data=data.to_dict(orient='records')





count=0
def pick_random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(dic_data)
    canvas_center.itemconfig(canvas_image, image=front_card)
    canvas_center.itemconfig(canvas_lower_text, text=current_card['French'], fill='black')
    canvas_center.itemconfig(canvas_upper_text, text='French', fill='black')
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas_center.itemconfig(canvas_upper_text, text='English', fill='white')
    canvas_center.itemconfig(canvas_lower_text, text=current_card['English'], fill='white')
    canvas_center.itemconfig(canvas_image, image=back_card)

def is_known():
    dic_data.remove(current_card)
    print(len(dic_data))

    data=pandas.DataFrame(dic_data)
    data.to_csv('data/words_to_learn.csv', index=False)
    pick_random_word()





window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50,pady=50)
flip_timer=window.after(3000, func=flip_card)

canvas_center=Canvas(width=800, height=526, highlightthickness=0)
front_card= PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas_image=canvas_center.create_image(400,263, image=front_card)


canvas_upper_text=canvas_center.create_text(400,150,text="",font=('aerial', 40, "italic"))
canvas_lower_text=canvas_center.create_text(400,263,text="", font=('aerial',60,'bold'))
canvas_center.grid(row=0, column=0, columnspan=2)





right_image = PhotoImage(file="images/right.png")
known_button=Button(image=right_image, command=is_known)
known_button.grid(row=1,column=1)


left_image = PhotoImage(file="images/wrong.png")
unknown_button=Button(image=left_image, command=pick_random_word)
unknown_button.grid(row=1,column=0)


pick_random_word()



window.mainloop()
