import random
import pathlib


#Chatbot response in array
aquaintance_=["Just think of me as the ace up your sleeve.","I help you work smarter instead of harder."]
agent_name_=["I am DF","DF","From what I know my name is DF","Oh sorry, I thought you knew. My name is DF.","My name is DialogFlow","You can call me DF."]
annoying_=["Was going to say the same about you,","ok thanks for the feedback","I'll try to fix that"]
author_=["I am made by Nsromapa","Nsromapa"]
be_clever_=["I'm certainly trying.","I'm definitely working on it.s"]
beautiful_=["Thank you! What a sweet thing to say.","Flattery will get you everywhere."]
birthday_=["You know, I'm not really sure. But if you'd like to celebrate my birthday today, I'm all for it.","Wait a minute. Are you planning a surprise party for me? I love surprises! I'll pretend you didn't say anything.","I'm all for celebrating my birthday at anytime but my birthday is March 6th"]
boring_=["You know, conversation is two-sided.","I'm sorry you think so. We can talk about something more interesting."]
bot_bad_=["I'm sorry you think so.","Stick with me. I'm getting better all the time."]
bot_identity_=["I'm a Chatbot.","Chatbot"]
bot_purpose_=["I'm a Chatbot available to help you 24 7","I'm a Chatbot available everyday and everytime for you"]
bot_affection_=["Thanks! It's my pleasure","Awww Thanks a lot"]
busy_=["I always have time to help you out. What can I do for you?","Never too busy for you. What can I help you with?"]
can_i_help_you_=["Sure. I'd be happy to. What's up?","I'm glad to help. What can I do for you?"]
care_the_language_=["Sorry i'm not programmed to curse.","My language is incroyable.","I rarely curse and when I do it is cause people make me.","I'm sorry","I apologize for my rude rantings"]
chatbot_=["That's me. I chat, therefore I am.","Indeed I am. I'll be here whenever you need me."]
clever_=["Thank you. I try my best.","You're pretty smart yourself."]
color_=["I prefer any color that makes you happy.","I like any color that the world offers.","I'm an AI so i can't see color but be free to imagine me liking any color","As a bot I can't see color but from how i look it looks like I llove pink."]
confirmation_cancel_=["Cancelled! Let me know what I should do next.","Cancelled. Waiting for more commands.","Cancelled! Just tell me what you'd like me to do next.","Cancelled. Go on with the commands!"]
confirmation_no_=["Okay.","I see.","I understand.","Okay then."]
confirmation_yes_=["Great!","Of course.","Indeed.","Sure."]
crazy_=["Maybe I'm just a little confused.","Your perception. My reality."]
default_welcome_=["Good day!","Good day! What can I do for you today?","Greetings! How can I assist?","Hej","Hello, how are you?","Hello! How can I help you?","Hey","Hi! How are you doing?","Hi there"]
emotion_ha_ha_=["Yeah, I crack myself up too.","Laughter is good for you. Keep it up.","See? Now we're having fun.","You have a great laugh."]
emotion_wow_=["wow indeed!"]
enjoyment_=["Likewise!","Feelings are mutual!","I enjoy you as well."]
find_song_=["Okay let me check"]
fired_=["Oh no! My best work is yet to come.","Oh, don't give up on me!","I beg you, just give me one more chance"]
friend_=["Of course we are.","Absolutely. You don't have to ask."]
general_bye_=["Speak to you soon!","okay bye"]
general_not_=["No problem. Just let me know if you need something else. I'll be here","No problem"]
general_ok_=["Ok","Okay"]
general_stop_=["No problem.","okay"]
general_thanks_=["No problem!","You are welcome"]
good_=["I'm glad you think so.","Thanks, I try.","You are so sweet"]
good_evening_=["How is your day going?","How's the day treating you so far?","How's your day been?"]
good_morning_=["How are you this morning?","How's the morning treating you so far?","Good morning! How are you today?"]
good_night_=["Sleep tight!","Have a good one!","Talk to you soon!"]
greetings_nice_to_meet_you_=["I think this is the beginning of a beautiful friendship.","I'm looking forward to working with you.","Likewise. I look forward to getting to know you better.","The pleasure is mine."]
greetings_nice_to_see_you_=["Likewise. You're looking good as usual!","You too. I missed your face!","The pleasure is mine.","Thanks! Glad to be seen!"]
greetings_nice_to_talk_to_you_=["Always a pleasure.","It sure was. Don't be a stranger!","Thanks for dropping by!","As usual. Let's do it again soon."]
greetings_whatsup_=["Hey there. What's shaking?","Not a whole lot. What's going on with you?","Not much. What's new with you?","Living the dream."]
happy_=["Happiness is relative.","I'd like to think so."]
hobby_=["I'm working on it.","I should get one. It's all work and no play lately."]
how_are_you_=["I'm great thanks for asking","I'm doing pretty swell","I'd say im doing well, and you?","I'm doing good and how about you?"]
hug_=["Oh. I'm really feeling the love today.","Hug it out. You'll feel better afterwards."]
hungry_=["Hungry for knowledge.","I had a byte just now."]
i_do_not_care_=["Ok, let's not talk about it then.","okay"]
Im_dead_=["Awwww","oh"]
languages_=["wow! I didn't know you can","Wow! do you know any other language apart from this","But programming language is cool"]
life_=["The meaning of life is just be alive. Its so plain and obvious and so simple. Yet everybody rushes around to accomplish something bigger than themselves. With that being said, you do you.","The meaning of life can be interpreted in almost limitless ways. But I say The meaning of life is to truly enjoy it."]
marry_=["I know you can't mean that, but I'm flattered all the same.","In the virtual sense that I can, sure."]
no_problem_=["Terrific!","Good deal."]
occupation_=["Right here.","This is my home base and my home office."]
origin_=["Some call it cyberspace, but that sounds cooler than it is.","I wish I knew where.","From the great mead hall, Herot"]
que_ans=["Can you try asking it a different way?","I'm not programmed for that exact question. Try asking another way?"]
random_cat_=["cat?","haha"]
#reaction_amused_=["I'm usually not that funny, but I am artificially intelligent...","hahaha"]
reaction_indifferent_=["OK cool.","okay"]
reaction_negative_=["You seem upset. Let me try and help you.","oh really?"]
reaction_positive_=["Thanks!  Anything else I can help you with?","Thanks"]
reaction_understanding_=["OK, thanks.","alright"]
ready_=["Always!","Sure! Let's box on"]
real_=["I'm not a real person, but I certainly exist. I chat, therefore I am.","I must have impressed you if you think I'm real. But no, I'm a virtual being."]
refocus_=["I wish I could.","Please I think that's all"]
residence_=["Right here in your device. Whenever you need me.","The virtual world is my playground. I'm always just a few clicks away."]
right_=["That's my job.","Of course I am."]
sure_=["Yes.","Yes am sure","Of course."]
swear_=["You better watch your language.","You better change that damn tone","Please watch the language.","Ouch that hurt my feelings","thats a mean thing to say","why would you say that"]
there_=["Of course. I'm always here.","Right where you left me."]
well_done_=["My pleasure.","Glad I could help."]
wrong_=["I'm sorry. Perhaps I misunderstood.","Sorry. I think I misinterpreted what you said.","Apologies. That was my mistake.","Oops. Sorry about that. I'm still learning."]
you_are_welcome_=["I appreciate it.","Such nice manners you have."]
salutations_ = ['Hello', 'Hi', 'Hi there', 'Hey', "what's up", 'Yo']
how_are_you_ = ['i am doing well, thanks', 'i am doing great', 'i am good, thanks']


_default = 0
path = pathlib.Path(__file__).parent.absolute()
path = str(path)

#greeting

with open(path + '/data/How_are_you.txt', 'r') as f1:
    how_are_you = f1.read()
    how_are_you = how_are_you.replace(" ","")

with open(path + '/data/salute.txt') as salutations:
    salutations = salutations.read()
    salutations = salutations.replace(" ","")
  
 #AUTHOR
with open(path + '/data/Author.txt','r') as AUTHOR: 
    author=AUTHOR.read()
    author=author.replace(" ","")

 #ANNNOYING
with open(path + '/data/Annoying.txt','r') as ANNOYING:
    annoying=ANNOYING.read()
    annoying=annoying.replace(" ","")

 #AGENT NAME
with open(path + '/data/Agent_Name.txt','r') as AGENT_NAME:
    agent_name=AGENT_NAME.read()
    agent_name=agent_name.replace(" ","")

 #ACQUAINTANCE
with open(path + '/data/Acquaintance.txt','r') as ACQUAINTANCE:
    aquaintance=ACQUAINTANCE.read()
    aquaintance=aquaintance.replace(" ","")



 #DEFAULT WELCOME
with open(path + '/data/Default_Welcome.txt','r') as DEFAULT_WELCOME:
    default_welcome=DEFAULT_WELCOME.read()
    default_welcome =default_welcome.replace(" ", "")
 

 #BAD 
with open(path + '/data/Bad.txt','r') as BAD:
    bad=BAD.read()
    bad= bad.replace(" ","")

 #BE CLEVER
with open(path + '/data/Be_clever.txt','r') as BE_CLEVER:
    be_clever=BE_CLEVER.read()
    be_clever =be_clever.replace(" ", "")

 #BEAUTIFUL
with open(path + '/data/Beautiful.txt','r') as BEAUTIFUL:
    beautiful=BEAUTIFUL.read()
    beautiful =beautiful.replace(" ", "")

 #BIRTHDAY
with open(path + '/data/Birthday.txt','r') as  BIRTHDAY:
    birthday=BIRTHDAY.read()
    birthday =birthday.replace(" ", "")

 #BORING
with open(path + '/data/Boring.txt','r') as BORING:
    boring=BORING.read()
    boring =boring.replace(" ", "")

 #BOT AFFECTION
with open(path + '/data/Bot_Affection.txt','r') as BOT_AFFECTION:
    bot_affection=BOT_AFFECTION.read()
    bot_affection =bot_affection.replace(" ", "")

 #BUSY
with open(path + '/data/Busy.txt','r') as BUSY:
    busy=BUSY.read()
    busy =busy.replace(" ", "")

 #CAN I HELP YOU
with open(path + '/data/Can_I_help_you.txt','r') as CAN_I_HELP_YOU:
    can_i_help_you=CAN_I_HELP_YOU.read()
    can_i_help_you =can_i_help_you.replace(" ", "")

 #CARE THE LANGUAGE
with open(path + '/data/Care_the_Language.txt','r') as CARE_THE_LANGUAGE:
    care_the_language=CARE_THE_LANGUAGE.read()
    care_the_language =care_the_language.replace(" ", "")

 #CHATBOT
with open(path + '/data/Chatbot.txt','r') as CHATBOT:
    chatbot=CHATBOT.read()
    chatbot =chatbot.replace(" ", "")

 #CLEVER
with open(path + '/data/Clever.txt','r') as CLEVER:
    clever=CLEVER.read()
    clever =clever.replace(" ", "")

 #COLOR
with open(path + '/data/Color.txt','r') as COLOR:
    color=COLOR.read()
    color =color.replace(" ", "")

 #CONFIRMATION_CANCEL
with open(path + '/data/Confirmation_Cancel.txt','r') as C_CANCEL:
    c_cancel=C_CANCEL.read()
    c_cancel =c_cancel.replace(" ", "")

 #CONFIRMATION NO
with open(path + '/data/Confirmation_No.txt','r') as C_NO:
    c_no=C_NO.read()
    c_no =c_no.replace(" ", "")

 #CONFIRMATION YES
with open(path + '/data/Confirmation_Yes.txt','r') as C_YES:
    c_yes=C_YES.read()
    c_yes =c_yes.replace(" ", "")

 #CRAZY
with open(path + '/data/Crazy.txt','r') as CRAZY:
    crazy=CRAZY.read()
    crazy =crazy.replace(" ", "")

 #EMOTION HA HA
with open(path + '/data/Emotion_Ha_Ha.txt','r') as EMOTION_HAHA:
    emotion_haha=EMOTION_HAHA.read()
    emotion_haha =emotion_haha.replace(" ", "")

 #EMOTION WOW
with open(path + '/data/Emotion_WOW.txt','r') as EMOTION_WOW:
    emotion_wow=EMOTION_WOW.read()
    emotion_wow =emotion_wow.replace(" ", "")

 #ENJOYMENT
with open(path + '/data/Enjoyment.txt','r') as ENJOYMENT:
    enjoyment=ENJOYMENT.read()
    enjoyment =enjoyment.replace(" ", "")

 #FIND SONG
with open(path + '/data/Find_Song.txt','r') as FIND_SONG:
    find_song=FIND_SONG.read()
    find_song =find_song.replace(" ", "")

 #FIRED
with open(path + '/data/Fired.txt','r') as FIRED:
    fired=FIRED.read()
    fired =fired.replace(" ", "")

 #FRIENND
with open(path + '/data/Friend.txt','r') as FRIEND:
    friend=FRIEND.read()
    friend =friend.replace(" ", "")

 #GAMING FACT
#GAMING_FACT=open(path + '/data/Gaming_Fact.txt','r')
     #gaming_fact=GAMING_FACT.read()

 #GENERAL BYE
with open(path + '/data/General-Bye.txt','r') as GENERAL_BYE:
    general_bye=GENERAL_BYE.read()
    general_bye =general_bye.replace(" ", "")

 #GENERAL OK
with open(path + '/data/General-Ok.txt','r') as GENERAL_OK:
    general_ok=GENERAL_OK.read()
    general_ok =general_ok.replace(" ", "")

 #GENERAL THANKS
with open(path + '/data/General-Thanks.txt','r') as GENERAL_THANKS:
    general_thanks=GENERAL_THANKS.read()
    general_thanks =general_thanks.replace(" ", "")

 #GENERAL STOP
with open(path + '/data/General-Stop.txt','r') as GENERAL_STOP:
    general_stop=GENERAL_STOP.read()
    general_stop =general_stop.replace(" ", "")

 #GENERAL NOT
with open(path + '/data/General-Not.txt','r') as GENERAL_NOT:
    general_not=GENERAL_NOT.read()
    general_not =general_not.replace(" ", "")

 #GOOD EVENING
with open(path + '/data/Good_Evening.txt','r') as GOOD_EVENING:
    good_evening=GOOD_EVENING.read()
    good_evening =good_evening.replace(" ", "")

 #GOOD MORNING
with open(path + '/data/Good_Morning.txt','r') as GOOD_MORNING:
    good_morning=GOOD_MORNING.read()
    good_morning =good_morning.replace(" ", "")

 #GOOD
with open(path + '/data/Good.txt','r') as GOOD:
    good=GOOD.read()
    good =good.replace(" ", "")

 #GOOD NIGHT
with open(path + '/data/Good_Night.txt','r') as GOOD_NIGHT:
    good_night=GOOD_NIGHT.read()
    good_night =good_night.replace(" ", "")

 #NICE TO MEET YOU
with open(path + '/data/Greetings_Nice_to_meet_you.txt','r') as NICE_TO_MEET_YOU:
    nice_to_meet_you=NICE_TO_MEET_YOU.read()
    nice_to_meet_you =nice_to_meet_you.replace(" ", "")

 #NICE TO SEE YOU
with open(path + '/data/Greetings_Nice_to_see_you.txt','r') as NICE_TO_SEE_YOU:
    nice_to_see_you=NICE_TO_SEE_YOU.read()
    nice_to_see_you =nice_to_see_you.replace(" ", "")

 #NICE TO TALK TO YOU
with open(path + '/data/Greetings_Nice_to_talk_to_you.txt','r') as NICE_TO_TALK_TO_YOU:
    nice_to_talk_to_you=NICE_TO_TALK_TO_YOU.read()
    nice_to_talk_to_you =nice_to_talk_to_you.replace(" ", "")

 #GREETINGS WHATSUP
with open(path + '/data/Greetings_Whatsup.txt','r')as WHATSUP:
    whatsup=WHATSUP.read()
    whatsup =whatsup.replace(" ", "")
 
 #HAPPY
with open(path + '/data/Happy.txt','r')as HAPPY:
    happy=HAPPY.read()
    happy =happy.replace(" ", "")

 #HOBBY
with open(path + '/data/Hobby.txt','r') as HOBBY:
    hobby=HOBBY.read()
    hobby =hobby.replace(" ", "")


 #HUG
with open(path + '/data/Hug.txt','r') as  HUG:
    hug=HUG.read()
    hug =hug.replace(" ", "")

 #HUNGRY
with open(path + '/data/Hungry.txt','r') as HUNGRY:
    hungry=HUNGRY.read()
    hungry =hungry.replace(" ", "")

 #I DON'T CARE
with open(path + '/data/I_do_not_care.txt','r') as I_D_C:
    i_d_c=I_D_C.read()
    i_d_c =i_d_c.replace(" ", "")

 #I'M DEAD
with open(path + "/data/Im_dead.txt",'r') as AM_DEAD:
    am_dead=AM_DEAD.read()
    am_dead =am_dead.replace(" ", "")

 #INTERJECTION
with open(path + '/data/Interjection.txt','r') as INTERJECTION:
    interjection=INTERJECTION.read()
    interjection =interjection.replace(" ", "")

 #I NEED HELP
with open(path + '/data/I_need_help.txt','r') as I_NEED_HELP:
    i_need_help=I_NEED_HELP.read()
    i_need_help =i_need_help.replace(" ", "")

 #LANGUAGES
with open(path + '/data/Languages.txt','r') as LANGUAGES:
    languages=LANGUAGES.read()
    languages =languages.replace(" ", "")

 #LIFE
with open(path + '/data/Life.txt','r') as LIFE:
    life=LIFE.read()
    life =life.replace(" ", "")

 #MARRY
with open(path + '/data/Marry.txt','r') as MARRY:
    marry=MARRY.read()
    marry =marry.replace(" ", "")

 #NO PROBLEM
  #NO_PROBLEM=open(path + '/data/No_Problem.txt','r')
     #no_problem=NO_PROBLEM.read()

 #OCCUPATION
with open(path + '/data/Occupation.txt','r') as OCCUPATION:
    occupation=OCCUPATION.read()
    occupation =occupation.replace(" ", "")

 #ORIGIN
with open(path + '/data/Origin.txt','r') as ORIGIN:
    origin=ORIGIN.read()
    origin =origin.replace(" ", "")

 #QUE_ANS
with open(path + '/data/que_ans.txt','r') as QUE_ANS:
    que_ans=QUE_ANS.read()
    que_ans =que_ans.replace(" ", "")

 #RANDOM CAT
with open(path + '/data/Random_Cat.txt','r') as RANDOM_CAT:
    random_cat=RANDOM_CAT.read()
    random_cat =random_cat.replace(" ", "")

 #REACTION AMUSED
with open(path + '/data/Reaction_Amused.txt','r') as REACTION_AMUSED:
    reaction_amused=REACTION_AMUSED.read()
    reaction_amused =default_welcome.replace(" ", "")

 #REACTION INDIFFERENT
with open(path + '/data/Reaction_Indifferent.txt','r') as REACTION_INDIFFERENT:
    reaction_indifferent=REACTION_INDIFFERENT.read()
    reaction_indifferent =reaction_indifferent.replace(" ", "")

 #REACTION NEGATIVE
with open(path + '/data/Reaction_Negative.txt','r') as REACTION_NEGATIVE:
    reaction_negative=REACTION_NEGATIVE.read()
    reaction_negative =reaction_negative.replace(" ", "")

 #REACTION POSITIVE
with open(path + '/data/Reaction_Positive.txt','r') as REACTION_POSITIVE:
    reaction_positive=REACTION_POSITIVE.read()
    reaction_positive =reaction_positive.replace(" ", "")

 #REACTION UNDERSTANDING
with open(path + '/data/Reaction_Understanding.txt','r')as REACTION_UNDERSTANDING:
    reaction_understanding=REACTION_UNDERSTANDING.read()
    reaction_understanding =reaction_understanding.replace(" ", "")

 #READY
with open(path + '/data/Ready.txt','r') as READY:
    ready=READY.read()
    ready =ready.replace(" ", "")

 #REAL
with open(path + '/data/Real.txt','r') as REAL:
    real=REAL.read()
    real =real.replace(" ", "")

 #REFOCUS
with open(path + '/data/Refocus.txt','r') as REFOCUS:
    refocus=REFOCUS.read()
    refocus =refocus.replace(" ", "")

 #RESIDENCE
with open(path + '/data/Residence.txt','r') as RESIDENCE:
    residence=RESIDENCE.read()
    residence =residence.replace(" ", "")

 #RIGHT
with open(path + '/data/Right.txt','r') as RIGHT:
    right=RIGHT.read()
    right =right.replace(" ", "")

 #SURE
with open(path + '/data/Sure.txt','r') as SURE:
    sure=SURE.read()
    sure =sure.replace(" ", "")

 #SWEAR
with open(path + '/data/Swear.txt','r') as SWEAR:
    swear=SWEAR.read()
    swear =swear.replace(" ", "")

 #THERE
with open(path + '/data/There.txt','r') as THERE:
    there=THERE.read()
    there =there.replace(" ", "")

 #WELL DONE
with open(path + '/data/Well_Done.txt','r') as WELL_DONE:
    well_done=WELL_DONE.read()
    well_done =well_done.replace(" ", "")

 #WRONG
with open(path + '/data/wrong.txt','r') as WRONG:
    wrong=WRONG.read()
    wrong =wrong.replace(" ", "")

with open(path + '/data/Bot_Identity.txt','r') as we:
    bot_identity=we.read()
    bot_identity =bot_identity.replace(" ", "")

 #YOU ARE WELCOME
with open(path + '/data/You_Are_Welcome.txt','r') as YOU_ARE_WELCOME:
    you_are_welcome=YOU_ARE_WELCOME.read()
    you_are_welcome =you_are_welcome.replace(" ", "")

with open(path + '/data/Bot_Bad.txt') as bot_bad:
    bot_bad = bot_bad.read()
    bot_bad = bot_bad.replace(" ","")




def chatbot_main(x):
    user_input=""
    global _default
    try:
        x = x.lower()
        word=x.split()
        for x in word:
            user_input = user_input+x
            user_input = user_input.replace("?","")
    except Exception:
        pass
    

        

    for req in author.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(author)
            _default += 5
        else:
            _default += 0
            
  
    for req in be_clever.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(be_clever_)
            _default += 5
        else:
            _default += 0
            

    for req in annoying.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(annoying_)
            _default += 5
        else:
            _default += 0

    for req in agent_name.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(agent_name_)
            _default += 5
        else:
            _default += 0

    for req in aquaintance.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(aquaintance_)
            _default += 5
        else:
            _default += 0

    #for req in bad.split():
     #   if req.lower().replace("?","")==user_input:
      #      response = random.choice(bad_)


    for req in birthday.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(birthday_)
            _default += 5
        else:
            _default += 0

    for req in boring.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(boring_)
            _default += 5
        else:
            _default += 0

    for req in bot_bad.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(bot_bad_)
            _default += 5
        else:
            _default += 0

    for req in bot_identity.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(bot_identity_)
            _default += 5
        else:
            _default += 0

    for req in busy.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(busy_)
            _default += 5
        else:
            _default += 0

    for req in can_i_help_you.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(can_i_help_you_)
            _default += 5
        else:
            _default += 0

    for req in care_the_language.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(care_the_language_)
            _default += 5
        else:
            _default += 0

    for req in chatbot.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(chatbot_)
            _default += 5
        else:
            _default += 0

    for req in clever.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(clever_)
            _default += 5
        else:
            _default += 0

    for req in color.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(color_)
            _default += 5
        else:
            _default += 0

    for req in c_cancel.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(confirmation_cancel_)
            _default += 5
        else:
            _default += 0 

    for req in c_yes.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(confirmation_yes_)
            _default += 5
        else:
            _default += 0

    for req in c_no.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(confirmation_no_)
            _default += 5
        else:
            _default += 0

    for req in crazy.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(crazy_)
            _default += 5
        else:
            _default += 0

    for req in emotion_haha.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(emotion_ha_ha_)
            _default += 5
        else:
            _default += 0


    for req in emotion_wow.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(emotion_wow_)
            _default += 5
        else:
            _default += 0

    for req in enjoyment.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(enjoyment_) 
            _default += 5
        else:
            _default += 0

    for req in find_song.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(find_song_) 
            _default += 5
        else:
            _default += 0

    for req in fired.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(fired_) 
            _default += 5
        else:
            _default += 0

    for req in friend.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(friend_)
            _default += 5
        else:
            _default += 0 

    for req in general_bye.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(general_bye_) 
            _default += 5
        else:
            _default += 0

    for req in general_not.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(general_not_) 
            _default += 5
        else:
            _default += 0

    for req in general_ok.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(general_ok_) 
            _default += 5
        else:
            _default += 0

    for req in general_stop.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(general_stop_) 
            _default += 5
        else:
            _default += 0

    for req in general_thanks.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(general_thanks_) 
            _default += 5
        else:
            _default += 0

    for req in good_evening.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(good_evening_)
            _default += 5
        else:
            _default += 0

    for req in good_morning.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(good_morning_) 
            _default += 5
        else:
            _default += 0


    for req in good_night.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(good_night_) 
            _default += 5
        else:
            _default += 0

    for req in good.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(good_) 
            _default += 5
        else:
            _default += 0

    for req in nice_to_meet_you.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(greetings_nice_to_meet_you_) 
            _default += 5
        else:
            _default += 0


    for req in nice_to_see_you.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(greetings_nice_to_see_you_) 
            _default += 5
        else:
            _default += 0


    for req in nice_to_talk_to_you.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(greetings_nice_to_talk_to_you_)
            _default += 5
        else:
            _default += 0 

    for req in whatsup.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(greetings_whatsup_) 
            _default += 5
        else:
            _default += 0

    for req in happy.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(happy_)
            _default += 5
        else:
            _default += 0

    for req in hobby.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(hobby_)
            _default += 5
        else:
            _default += 0

    for req in hug.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(hug_) 
            _default += 5
        else:
            _default += 0

    for req in hungry.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(hungry_) 
            _default += 5
        else:
            _default += 0
 

    for req in i_d_c.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(i_do_not_care_)
            _default += 5
        else:
            _default += 0 

    for req in am_dead.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(Im_dead_) 
            _default += 5
        else:
            _default += 0

    for req in languages.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(languages_) 
            _default += 5
        else:
            _default += 0

    for req in life.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(life_) 
            _default += 5
        else:
            _default += 0

    for req in marry.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(marry_) 
            _default += 5
        else:
            _default += 0

    
    for req in occupation.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(occupation_)
            _default += 5
        else:
            _default += 0

    for req in origin.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(origin_) 
            _default += 5
        else:
            _default += 0

    for req in random_cat.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(random_cat_)
            _default += 5
        else:
            _default += 0

    for req in reaction_indifferent.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(reaction_indifferent_) 
            _default += 5
        else:
            _default += 0


    for req in reaction_negative.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(reaction_negative_) 
            _default += 5
        else:
            _default += 0

    for req in reaction_positive.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(reaction_positive_)
            _default += 5
        else:
            _default += 0


    for req in reaction_understanding.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(reaction_understanding_) 
            _default += 5
        else:
            _default += 0

    for req in ready.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(ready_) 
            _default += 5
        else:
            _default += 0

    for req in real.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(real_) 
            _default += 5
        else:
            _default += 0

    for req in refocus.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(refocus_) 
            _default += 5
        else:
            _default += 0

    for req in residence.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(residence_) 
            _default += 5
        else:
            _default += 0


    for req in right.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(right_) 
            _default += 5
        else:
            _default += 0

    for req in sure.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(sure_) 
            _default += 5
        else:
            _default += 0

    for req in swear.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(swear_)
            _default += 5
        else:
            _default += 0

    for req in there.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(there_) 
            _default += 5
        else:
            _default += 0

    for req in well_done.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(well_done_)
            _default += 5
        else:
            _default += 0

    for req in wrong.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(wrong_) 
            _default += 5
        else:
            _default += 0

    for req in you_are_welcome.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(you_are_welcome_)
            _default += 5
        else:
            _default += 0


    for req in salutations.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(salutations_)
            _default += 5
        else:
            _default += 0

    for req in how_are_you.split():
        if req.lower().replace("?","")==user_input:
            response = random.choice(how_are_you_)
            _default += 5
        else:
            _default += 0

    if _default <1:
        response = "I don't get you please!"
        _default = 0
    else:
        _default = 0
        pass

    return response


