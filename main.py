
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Выучи китайский')
background = transform.scale(image.load('China.jpg'), (700, 500))
font.init()
score = 0
missing = 0
font1 = font.Font(None, 40)
font2 = font.Font(None, 40)
font3 = font.Font(None, 26)
font4 = font.Font(None, 30)
font5 = font.Font(None, 40)
font6 = font.Font(None, 40)
font7 = font.Font(None, 40)

text_collor = (255, 0, 0)


mixer.init()
mixer.music.load('China.mp3')
mixer.music.play()

game = True
finish = False
while game:
    text1 = font1.render('Счёт:' + str(score), 1, text_collor)
    text2 = font2.render('Пропущено:' + str(missing), 1, text_collor)
    question1 = ('Кто сказал цитату: Твой дом там, где спокойны твои мысли.?')
    text3 = font3.render('Первый вопрос:' + str(question1), 1, text_collor)
    variant1 = 'Конфуций'
    variant2 = 'Лао-Цзы'
    variant3 = 'Чжуан-цзы'
    text4 = font4.render(variant1, 1, text_collor)
    text5 = font5.render(variant2, 1, text_collor)
    text6 = font6.render(variant3, 1, text_collor)




    
    window.blit(background, (0, 0))
    window.blit(text1, (10, 20))
    window.blit(text2, (10, 50))
    window.blit(text3, (30, 200))
    window.blit(text4, (70, 350))
    window.blit(text5, (450, 350))
    window.blit(text6, (250, 350))    
   
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    display.update()
    if finish != True:
       window.blit(background, (0, 0))






result = ''

if result == 5/5:
    print('Отличный результат')
if result == 4/5:
    print('Хороший результат')
if result == 3/5:
    print('Удовлетворительный результат')
if result == 2/5 or 1/5 or 0/5:
    print('Нужно много работать')




chitatas = {
    'Конфуций': 'Твой дом там, где спокойны твои мысли.',
    'Конфуций': 'Добром нужно отвечать на добро, а на зло нужно отвечать справедливостью.',
    'Конфуций': 'Правильные поступки приводят к правильному результату на их дела.',
    'Конфуций': 'У людей с красивыми словами и притворными манерами мало человеколюбия.',
    'Конфуций': 'Благородный муж безмятежени спокоен, маленький мальчик постоянно встревожен и обеспокоен.',
    'Конфуций': 'Благородный муж предъявляет требования к себе, низкий человек предъявляет требования к людям.',
    'Конфуций': 'Можно всю жизнь руководствоваться одним словом: это слово - взаимность.',
    'Конфуций': 'Легче зажечь одну свечу, чем клясть темноту.',
    'Конфуций': 'Правильные поступки приводят к правильному результату на их дела.', 
    'Лао Цзы': 'Человек, стоящий на цыпочках, не может долго стоять.',
    'Лао Цзы': 'Ходьба побеждает холод, покой побеждает жару. Спокойствие создаёт порядок в мире.',
    'Чжуан-цзы': 'То, что сделало прекрасной мою жизнь, сделает прекрасной и мою смерть.',
    'Лао Цзы': 'Тот, кто знает, не говорит. Тот, кто говорит, не знает.',
    'Конфуций': 'Знать, что нужно сделать, и не делать этого - это трусость.',
    'Конфуций': 'Когда тебе плохо - прислушайся к природе. Тишина мира успокаивает лучше, чем милионны ненужных слов.',
    'Книга изречений': 'В котле с кипящей водой нет холодного места.', 
    'Чжуан-цзы': 'Научись видеть, где всё темно, и слышать, где всё тихо.',
    'Чжуан-цзы': 'Когда знаешь, что поделать ничего нельзя, и спокойно принимаель судьбу - это высшее выражение действия силы духа.',
    'Конфуций': 'Не беспокойся о том, что люди тебя не знают, но беспокойся о том, что ты не знаешь людей.',



    
}

# if finish != True:
#        window.blit(background, (0, 0))




# class Student():
#     def__init__(self, Student1, Student2)
# while game:

#     if finish != True:
#         window.blit(background, (0, 0))
#         Student.reset()
#         Student.update()

#         .update()
#         .draw(window)
        

#         collides = sprite.groupcollide(monsters,  True, True)
#         for c in collides:
#             score += 1
#             student = Enemy('ufo.png', 50, 50, randint(20, 480),  randint(-200, -65), randint(1,5))
#             Student2.add(Student2)
        
#         if sprite.spritecollide(Student1, Student2, False) or missing >= 20:
#             finish = True
#             window.blit(win, (350, 250))


            




        


#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         if e.type == MOUSEBUTTONDOWN:
#             if e.button == 1:
#                 fire_sound.play()
#                 Student.fire()


# question2 = ('Знать, что нужно сделать, и не делать этого - это... Продолжите фразу.')
    # text7 = font4.render('Второй вопрос:' + str(question2), 1, (text_color))
    # variant1 = глупость
    # variant2 = трусость
    # variant3 = грех
    
    # question3 = ('')
    # text11 = font5.render('Третий вопрос:' + str(question3) 1, (text_color))
    # variant1 = 
    # variant2 = 
    # variant3 = 
 
    # question4 = ('Какого места, согласно цитате из Книги изречений, нет в котле с кипящей водой?')
    # text15 = font6.render('Четвёртый вопрос:' + str(question4), 1, (text_color))
    # variant1 = холодного
    # variant2 = горячего
    # variant3 = нейтрального

    # qusetion5 = ('')
    # text19 = font7.render('Пятый вопрос:' + str(question5), 1, (text_color))
    # variant1 = 
    # variant2 = 
    # variant3 = 
