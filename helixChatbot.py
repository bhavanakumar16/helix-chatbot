from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

#creating the chatbot with required logic adaptors
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
            "chatterbot.logic.MathematicalEvaluation",
        {
            'import_path': 'chatterbot.logic.BestMatch'
            
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.8,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter"
)
import pandas as pd

# Importing the database
database = pd.read_csv('student.csv', sep=',')

rollno = database['Roll_No']
name = database['Name']
age = database['Age']
gender = database['Gender']
marks = database['Marks']
lowest_name = ''
lowest_rollno = ''
topper_name = ''
topper_rollno = ''
no_of_failures = 0
ppl_over_95=0
ppl_over_90=0
ppl_over_80=0

for i in range(0,len(marks)):

  if marks[i] == min(marks):
    lowest_name = name[i]
    lowest_rollno = rollno[i]

  if marks[i] == max(marks):
    topper_name =topper_name+','+name[i]
    
  if marks[i] <= 33 :
    no_of_failures = no_of_failures + 1

  if marks[i] >= 95:
    ppl_over_95 = ppl_over_90 + 1

  if marks[i] >= 90:
    ppl_over_90 = ppl_over_80 + 1

  if marks[i] >= 80:
    ppl_over_80 = ppl_over_80 + 1

#training of bot
#trainer = ChatterBotCorpusTrainer(bot)
#trainer = ListTrainer(bot)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
bot.set_trainer(ListTrainer)

for i in range(0,len(marks)):
    
  bot.train([
            "give me the complete details of roll number {}".format(rollno[i]),
            "\nHere are the details:Roll No.: {}; Name: {}  Age: {}  Gender: {}  Marks: {}  ".format(rollno[i], name[i], age[i], gender[i], marks[i]),
            "complete details of roll number {}".format(rollno[i]),
            "\nHere are the details:Roll No.: {}; Name: {}  Age: {}  Gender: {}  Marks: {} ".format(rollno[i], name[i], age[i], gender[i], marks[i]),
            "full details of roll number {}".format(rollno[i]),
            "\nHere are the details : Roll No.: {}; Name: {}  Age: {}  Gender: {}  Marks: {} ".format(rollno[i], name[i], age[i], gender[i], marks[i]),
            "give all details of roll number {}".format(rollno[i]),
            "\nHere are the details : Roll No.: {}; Name: {}  Age: {}  Gender: {}  Marks: {}  ".format(rollno[i], name[i], age[i], gender[i], marks[i])
    ])
  bot.train([
        "what is the marks of roll number {}".format(rollno[i]),
        "Marks of {} - {} is {}".format(rollno[i], name[i], marks[i]),
        "tell me marks of roll number {}".format(rollno[i]),
        "Marks of {} - {} is {}".format(rollno[i], name[i], marks[i]) ])
    
  bot.train([
        "what is the marks of {}".format(name[i]),
        "Marks of {} is {}".format(name[i], marks[i]),
        "tell me marks of {}".format(rollno[i]),
        "Marks of {} is {}".format(name[i], marks[i]),
        "how much did {} score?".format(rollno[i]),
        "{} scored {}".format(name[i], marks[i])
         ])
    
  bot.train([
        "what is the age of roll number {}".format(rollno[i]),
        "Age of {}, roll no. {} is {}".format(name[i], rollno[i], age[i])])
    
  bot.train([
        "what is the marks of {}".format(name[i]),
        "Marks of {} - {} is {} ".format(rollno[i], name[i], marks[i])])
  bot.train([
        "what is the age of {}".format(name[i]),
        "Age of {} - {} is {}".format(name[i], rollno[i], age[i])
        ])

bot.train(["what is the class average?",
           "The class average is {}".format(sum(marks)/len(marks)),
           "what is average score of class?",
           "The class average is {}".format(sum(marks)/len(marks)),
           "what is average marks of class?",
           "The class average is {}".format(sum(marks)/len(marks))
          ])    
    
bot.train([
          "what is the lowest marks?",
          "The Lowest marks is {}.!".format(min(marks)),
          "who scored the lowest marks?",
          "{} scored the lowest marks.".format(lowest_name)
          ])    

bot.train([
           "how many failures?",
           "Thankfully, No one failed. Phew ! ",
           "how many failed?",
           "Thankfully, No one failed. Phew !"
          ])
bot.train([
  "what is the highest marks?",
  "The highest marks is {}. Wow!".format(max(marks)),
  "how much did the topper score?",
  "The topper scored {}. Congratulations!".format(max(marks))
])

bot.train([
  "who got the highest marks?",
  "The highest marks is {}. Well done {}! ".format(max(marks), topper_name)
])
    
bot.train([
  "who got the lowest marks?",
  "The lowest marks is {}, obtained by {}, roll number {} - Feel sad for the chap".format(min(marks), lowest_name, lowest_rollno),
  "who got the lowest marks?",
  "The lowest marks is {}, obtained by {}, roll number {} - Feel sad for the chap".format(min(marks), lowest_name, lowest_rollno)
])

bot.train([
           "who are you?",
           "Hey there! I am Helix, the ChatBot! To know how I can help you, ask me! ",
            "what is your name?",
           "My name is Helix, the ChatBot! Here to help!",
           "what do you do?",
           "I am your personal assistant, so I'll try my best to help you!\n I can solve any mathematical equation, provide you with data from a database or even tell you a joke! ",
           "how can you help me?",
           "I am your personal assistant, so I'll try my best to help you!\n I can solve any mathematical equation, provide you with data from a database or even tell you a joke! ",
          ])


bot.train([
   "Who all got above ninety five percent"
   "{} people got over 95%.".format(ppl_over_95),
   "people over ninety five percent"
   "{} people got over 95%.".format(ppl_over_95)
        ])

bot.train([
   "Who all got above ninety percent"
   "{} people got over 90%.".format(ppl_over_90),
   "people over ninety percent"
   "{} people got over 90%.".format(ppl_over_90)
        ])

bot.train([
   "Who all got above eighty percent"
   "{} people got over 80%.".format(ppl_over_80),
   "people over eighty percent"
   "{} people got over 80%.".format(ppl_over_80)
        ])
print("Training Complete")

bot.train("chatterbot.corpus.english")

CONVERSATION_ID = bot.storage.create_conversation()


'''def get_feedback():
  from chatterbot.utils import input_function
  text = input_function()
  if 'yes' in text.lower():
    return False
  elif 'no' in text.lower():
    return True
  else:
    print('Please type either "Yes" or "No"')
    return get_feedback()'''


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHi, I'm Helix - The Chatbot\nThe sole reason Helix was made,\nwas to provide you with aid!\n\nAsk me something!")
from chatterbot.utils import input_function

while True:
    try:
        input_statement = bot.input.process_input_statement()
        statement, response = bot.generate_response(input_statement, CONVERSATION_ID)
        bot.output.process_response(response)
        print('\n')
       
    except (KeyboardInterrupt, EOFError, SystemExit):
        break