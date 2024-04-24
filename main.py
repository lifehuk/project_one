
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Выучи китайский')
background = transform.scale(image.load('background.jpg'), (700, 500))

game = True
finish = False
while game:
    window.blit(background, (0, 0))

    for i in event.get():
        if i.type == QUIT:
            game = False
    
    display.update()
    if finish != True:
       window.blit(background, (0, 0))


mixer.init()
mixer.music.load('China.ogg')
mixer.music.play()

    





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



    
}

# if finish != True:
#        window.blit(background, (0, 0))


# mixer.init()
# mixer.music.load('China.ogg')
# mixer.music.play()


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
#             monster = Enemy('ufo.png', 50, 50, randint(20, 480),  randint(-200, -65), randint(1,5))
#             Student2.add(Student2)
        
#         if sprite.spritecollide(Student1, Student2, False) or missing >= 20:
#             finish = True
#             window.blit(win, (350, 250))

#         if score >= 15:
#             finish = True
#             window.blit(lose, (350, 250))
            



#         text1 = font2.render('Счёт' + str(score), 1, (255, 255, 255))
#         text2 = font2.render('Пропущено' + str(missing), 1, (255, 255, 255))
#         window.blit(text1, (10, 20))
#         window.blit(text2, (10, 50))
        


#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         if e.type == MOUSEBUTTONDOWN:
#             if e.button == 1:
#                 fire_sound.play()
#                 Student.fire()


