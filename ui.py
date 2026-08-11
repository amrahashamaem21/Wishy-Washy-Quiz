from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#FFE8B0"

class QuizInterface:

    def get_next_question(self):
        quiz_txt = self.quiz.next_question()
        return quiz_txt

    def start_quiz(self):
        self.canvas.delete("all")
        self.question_box_img = PhotoImage(file="quiz-images/ui/question_box.png")
        self.canvas.create_image(400, 200, image=self.question_box_img)
        quiz_txt = self.get_next_question()
        self.canvas.create_text(400,200,text=quiz_txt, width=350,justify="center",font=("Chewy", 16))

        self.true_option_img = PhotoImage(file="quiz-images/option_buttons/option_pink.png")
        self.true_button = Button(
            self.canvas,
            image=self.true_option_img,
            text="True",
            compound="center",
            font=("Chewy", 16),
            fg="black",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.quiz.check_answer("True")
        )
        self.canvas.create_window(300, 400, window=self.true_button)

        self.false_option_img = PhotoImage(file="quiz-images/option_buttons/option_blue.png")
        self.false_button = Button(
            self.canvas,
            image=self.false_option_img,
            text="False",
            compound="center",
            font=("Chewy", 16),
            fg="black",
            bg=THEME_COLOR,
            activebackground=THEME_COLOR,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.quiz.check_answer("False")
        )
        self.canvas.create_window(500, 400, window=self.false_button)
        self.canvas.create_text(500, 400, text="False", font=("Chewy", 16), fill="black")



    def __init__(self,quiz_brain: QuizBrain):


        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Wishy_Washy Quiz")

        self.canvas=Canvas(self.window,width=800,height=600,bg=THEME_COLOR,highlightthickness=0)
        self.canvas.pack()

        self.quiz_title=PhotoImage(file="quiz-images/ui/quiz_title.png")
        self.canvas.create_image(400,100,image=self.quiz_title)

        self.sun_img = PhotoImage(file="quiz-images/decorations/sun.png")
        self.sun_img = self.sun_img.subsample(4, 4)
        self.canvas.create_image(700, 90, image=self.sun_img)

        self.cloud_01_img = PhotoImage(file="quiz-images/decorations/cloud_01.png")
        self.canvas.create_image(80, 60, image=self.cloud_01_img)


        self.fence_img = PhotoImage(file="quiz-images/decorations/fence.png")
        fence_x_positions = [100, 300, 500, 700]
        for x in fence_x_positions:
            self.canvas.create_image(x, 560, image=self.fence_img)


        self.grass_flowers_img = PhotoImage(file="quiz-images/decorations/grass_flowers.png")
        grass_x_positions = [60, 180, 300, 420, 540, 660]
        for x in grass_x_positions:
            self.canvas.create_image(x, 580, image=self.grass_flowers_img)

        self.mailbox_img = PhotoImage(file="quiz-images/decorations/mailbox.png")
        self.canvas.create_image(730, 545, image=self.mailbox_img)


        self.charlie_img = PhotoImage(file="quiz-images/characters/charlie/charlie_normal.png")
        self.canvas.create_image(190, 350, image=self.charlie_img)

        self.frieda_img = PhotoImage(file="quiz-images/characters/frieda/frieda_happy.png")
        self.canvas.create_image(320, 350, image=self.frieda_img)


        self.answer_note_img = PhotoImage(file="quiz-images/speech_bubbles/how_much_you_know.png")
        self.answer_note_img = self.answer_note_img.subsample(4, 4)
        self.canvas.create_image(620, 280, image=self.answer_note_img)

        self.start_button_img = PhotoImage(file="quiz-images/buttons/start_button.png")
        self.canvas.create_image(620, 420, image=self.start_button_img)
        self.start_button = Button(self.canvas,image=self.start_button_img,bg=THEME_COLOR,activebackground=THEME_COLOR,borderwidth=0,highlightthickness=0,command=self.start_quiz)
        self.canvas.create_window(620, 420, window=self.start_button)

        self.sparkle_01_img = PhotoImage(file="quiz-images/decorations/sparkle_large_01.png")
        self.sparkle_02_img = PhotoImage(file="quiz-images/decorations/sparkle_large_02.png")

        self.canvas.create_image(500, 200, image=self.sparkle_01_img)
        self.canvas.create_image(50, 300, image=self.sparkle_02_img)

        self.canvas.create_text(395, 200,text="Oh, Charlie!!", font=("Comic Sans MS", 20, "italic"),fill="black")



        self.window.mainloop()





