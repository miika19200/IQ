from tkinter import *
from PIL import Image, ImageTk
import random

names_list = []
global questions_answers
asked = []
score = 0

question_answers = {
1:["Which word in the dictionary is spelled incorrectly?", #item 1, index 0 will be the questions
    'a. temparature', #item 2, index 1 will be the first choice
    'b. damged', #item 3, index 2 will be the second choice
    'c. incorrectly', #item 4, index 3 will be the third choice
    'd. focus' #item 4, index 4 will be the write statement we need to display the right statement if the user eneters wrong choice
    ,3] #item 7, index 5 will be the position of the right answer index where right answer sits), this will be our check if answer correct or no

  ,2:["Which of the following can be arranged into a English word?",
    'a. H R G S T',
    'b. R I L S A',
    'c. T O O M T',
    'd. W Q R G S'
    ,2]

  ,3:["The day before, the day before yesterday after Saturday. What day is it today?",
    'a. Thursday',
    'b. Friday',
    'c. Sunday',
    'd. Saturday'
    ,2]
  
  ,4:["When counting from 1-100, how many times will you come across the number 7?",
    'a. 18',
    'b. 19',
    'c. 20',
    'd. 21'
    ,3]
      
  ,5:["What's the 9th shape going to be?",
    'a.',
    'b.',
    'c.',
    'd.'
    ,2]
  
  ,6:["If you rearrange the letter “CIFAIPC” you would have the name of an:",
    'a.City',
    'b.Animal',
    'c.Ocean',
    'd.River'
    ,3]
 
  ,7:["Which one of the five is least like the other four?",
    'a.Dog',
    'b.Mouse',
    'c.Lion',
    'd.Snake'
    ,4]

  ,8:["What's next?",
    'a.',
    'b.',
    'c.',
    'd.'
    ,3]

  ,9:["What's the next pattern?",
    'a.',
    'b.',
    'c.',
    'd.'
    ,2]

 ,10:["What word is the opposite of happy",
    'a.unfortunate',
    'b.lucky',
    'c.joyful',
    'd.contended'
    ,1]
}

def ran():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    ran()

class QuizStarter:
  def __init__(self, parent):
    background_color = "darkslategray4"
    self.bg_image = Image.open("1.png") #need to use Image if need to resize 
    self.bg_image = self.bg_image.resize((450, 350), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image) 
    self.bg_image = PhotoImage(file="1.png") 

    #frame setup
    self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()

    #label for image
    self.image_label= Label(self.quiz_frame, image=self.bg_image)
    self.image_label.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always


    self.user_label = Label ( self.quiz_frame, text = "Please enter your name below",  font = ("Tw Cen", "16"), bg = background_color)
    self.user_label.grid(row = 1, pady = 20)

    self.entry_box = Entry(self.quiz_frame)
    self.entry_box.grid(row = 2, pady = 20)

    self.continue_button = Button (self.quiz_frame, text = "Continue", bg = "darkseagreen1", command=self.name_collection)
    self.continue_button.grid(row = 3, pady = 20)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.quiz_frame.destroy()
    Quiz(root)

class Quiz:
  def __init__(self, parent):
    background_color = "darkslategray4"
    self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()

    ran()
   
    self.question_label = Label(self.quiz_frame, text = question_answers[qnum][0], font = ("Tw Cen", "18", "bold"), bg = background_color)
    self.question_label.grid(row = 0)

    self.var1 = IntVar()
   
    #self button 1
    self.rb1 = Radiobutton (self.quiz_frame, text = question_answers[qnum][1], font = ("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, padx = 10, pady = 10
)
    self.rb1.grid(row=1, sticky = W)

    #self button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = question_answers[qnum][2], font = ("Helvetica", "12"), bg=background_color, value=2, variable=self.var1,
 padx = 10, pady = 10,
)
    self.rb2.grid(row=2, sticky = W)

    #self button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = question_answers[qnum][3], font = ("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, padx = 10, pady = 10
)
    self.rb3.grid(row=3, sticky = W)

    #self button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = question_answers[qnum][4], font = ("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, padx = 10, pady = 10
)
    self.rb4.grid(row=4, sticky = W)

    #confrim button
    self.confirm_button = Button(self.quiz_frame, text="Confirm", font=("Helvetica", 12 ,"bold"), bg = "SpringGreen3", )#command=self.test_progress)
    self.confirm_button.grid(row=7, padx=5, pady=5)
                   
  #editing the labeland radio buttoon to show the next question_answers
  def question_setup(self):
    ran()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])

  #confirm button command
  def test__progress(self):#can pass on users choice as an argument here as well
    global score#this score needs to be accessible to all
    scr_label=self.score_label #renaming the score label each time the score is different
    choice=self.var1.get()#get the users choice, remeber our var1 is the Intvar() menthod that stores the number chosen
    if len(asked)>9:#to determine if its the last question and just end the quiz after
      if choice== questions_answer[qnum][6]:#checking that the key (qnum) has the correct answer which is stored in the index 6 of the value array
        score+=1#will add one point to the score
        scr_label.configure(text=score)#will change the test button confirm (its a good idea to rename this variable)
        self.endscreen() #to open endscreen when the quiz is done
      else:
        score+=0 #score will stay the same, no points ould be added
        scr_label.configure(text="the correct answer would be:" + questions_answer[qnum][5]) #right answer would be given instead of thier score
        self.endscreen()
    else:
      if choice == 0:
        self.quiz_instance.config(text="Try Again, You havent chosen an option") #error message
        choice=self.var1.get()
      else:#if choice is made
        if  choice == questions_answer[qnum][6]: #ifi choice had been made correctly
          score+=1
          scr_label.configure(text=score)
          self.quiz_instance.config(text="Confirm")
        else: #if the score was incorrect
          score+=0
          scr_label.configure("The answer was:" +questions_answers[qnum][5])
          self.quiz_instance.config(text="Confirm")
          self.questions_setup()#move to the next question

  def end_screen(self):
    root.withdraw()
    open_endscrn=End()

class End:
  def __init__(self):
    background="OldLace"
    self.end_box= TopLevel(root)#toplevel widgets work as windows that are directly managed by the window manager.
    self.end_box.title("End Box")

    self.end_frame =Frame ( self.end_frame, widtih=1000, height=1000, bg=background)
    self.end_frame=grid()

    end_heading = Label (self.end_frame, text="Well Done", font=('Tw, Cen Mt', 22, 'bold'), bg=background, pady=15)
    end_heading.grid(row=0)

    exit_button = Button (self.end_frame, text="Exit", width=10,bg="Indianred1", font=('Tw Cen MT', 12, bold),command=self.close_end)
    exit_button.grid(row=4, pady=20)

#quit Button
    self.quit = Button (self.end_frame, text="quit", width=10,bg="red2", font=('Helvetica', 12, 'bold'),command=self.endScreen)
    self.quit.grid(row=7, column=3, sticky=E, padx=5, pady=5)
  def close_end(self):
    self.end_box.destroy()
    root.withdraw()
    
if __name__=="__main__":
  root = Tk()
  root.title("IQ Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()
