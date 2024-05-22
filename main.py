
from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Выучи китайский')
background = transform.scale(image.load('China.jpg'), (700, 500))
font.init()
score = 0
missing = 0
font1 = font.Font(None, 40)
font2 = font.Font(None, 40)
font3 = font.Font(None, 25)
font4 = font.Font(None, 30)
font5 = font.Font(None, 30)
font6 = font.Font(None, 30)

text_collor = (0, 0, 0)


mixer.init()
mixer.music.load('China.mp3')
mixer.music.play()

game = True
finish = False

q_x = 10
q_y = 200

v1_x = 250
v1_y = 250
v2_x = 250
v2_y = 300
v3_x = 250
v3_y = 350

right_answer = 'Правильный ответ'
incorrect_answer = 'Неправильный ответ'
info = 'Нажмите пробел для перехода в следующий раунд'
info_text = font3.render(info, 1, text_collor)
q = 1
round = 1
while game:
    window.blit(background, (0,0))
    text1 = font1.render('Счёт:' + str(score), 1, text_collor)
    window.blit(text1, (10, 20))
    if round == 1:
        question = ('Кто сказал цитату: Твой дом там, где спокойны твои мысли.?')
        variant1 = '1. Конфуций'
        variant2 = '3. Лао-Цзы'
        variant3 = '2. Чжуан-цзы'
        if q == 1:
            text3 = font3.render('Первый вопрос:' + str(question), 1, text_collor)
            text4 = font4.render(variant1, 1, text_collor)
            text5 = font5.render(variant2, 1, text_collor)
            text6 = font6.render(variant3, 1, text_collor)
            window.blit(text3, (q_x, q_y))
            window.blit(text4, (v1_x, v1_y))
            window.blit(text5, (v2_x, v2_y))
            window.blit(text6, (v3_x, v3_y))    
        if q == 2:
            right_answer_text = font4.render(right_answer, 1, text_collor)
            window.blit(right_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
            
        if q == 3:
            incorrect_answer_text = font4.render(incorrect_answer, 1, text_collor)
            window.blit(incorrect_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
    elif round == 2:
        question = ('Знать, что нужно сделать, и не делать этого - это... Продолжите фразу.')
        variant1 = '1. глупость'
        variant2 = '3. трусость'
        variant3 = '2. грех'
        if q == 1:
            text3 = font3.render('Второй вопрос:' + str(question), 1, text_collor)
            text4 = font4.render(variant1, 1, text_collor)
            text5 = font5.render(variant2, 1, text_collor)
            text6 = font6.render(variant3, 1, text_collor)
            window.blit(text3, (q_x, q_y))
            window.blit(text4, (v1_x, v1_y))
            window.blit(text5, (v2_x, v2_y))
            window.blit(text6, (v3_x, v3_y))    
        if q == 2:
            right_answer_text = font4.render(right_answer, 1, text_collor)
            window.blit(right_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
        if q == 3:
            incorrect_answer_text = font4.render(incorrect_answer, 1, text_collor)
            window.blit(incorrect_answer_text, (250, 250))
            window.blit(info_text, (100, 350))

    elif round == 3:
        question = ('..., покой побеждает жару. Начните фразу.')
        variant1 = '1. ходьба побеждает холод'
        variant2 = '3. покой побеждает холод'
        variant3 = '2. ходьба побеждает жару'
        if q == 1:
            text3 = font3.render('Третий вопрос:' + str(question), 1, text_collor)
            text4 = font4.render(variant1, 1, text_collor)
            text5 = font5.render(variant2, 1, text_collor)
            text6 = font6.render(variant3, 1, text_collor)
            window.blit(text3, (q_x, q_y))
            window.blit(text4, (v1_x, v1_y))
            window.blit(text5, (v2_x, v2_y))
            window.blit(text6, (v3_x, v3_y))    
        if q == 2:
            right_answer_text = font4.render(right_answer, 1, text_collor)
            window.blit(right_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
        if q == 3:
            incorrect_answer_text = font4.render(incorrect_answer, 1, text_collor)
            window.blit(incorrect_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
    elif round == 4:
        question = ('Какого места, согласно цитате из Книги изречений, нет в котле с кипящей водой?')
        variant1 = '1. холодного'
        variant2 = '3. горячего'
        variant3 = '2. нейтрального'
        if q == 1:
            text3 = font3.render('Четвёртый вопрос:' + str(question), 1, text_collor)
            text4 = font4.render(variant1, 1, text_collor)
            text5 = font5.render(variant2, 1, text_collor)
            text6 = font6.render(variant3, 1, text_collor)
            window.blit(text3, (q_x, q_y))
            window.blit(text4, (v1_x, v1_y))
            window.blit(text5, (v2_x, v2_y))
            window.blit(text6, (v3_x, v3_y))    
        if q == 2:
            right_answer_text = font4.render(right_answer, 1, text_collor)
            window.blit(right_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
        if q == 3:
            incorrect_answer_text = font4.render(incorrect_answer, 1, text_collor)
            window.blit(incorrect_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
    elif round == 5:
        question = ('Не выходя со двора, можно познать мир. Кто это сказал?')
        variant1 = '1. Конфуций'
        variant2 = '3. Чжуан-Цзы'
        variant3 = '2. Лао-Цзы'
        if q == 1:
            text3 = font3.render('Пятый вопрос:' + str(question), 1, text_collor)
            text4 = font4.render(variant1, 1, text_collor)
            text5 = font5.render(variant2, 1, text_collor)
            text6 = font6.render(variant3, 1, text_collor)
            window.blit(text3, (q_x, q_y))
            window.blit(text4, (v1_x, v1_y))
            window.blit(text5, (v2_x, v2_y))
            window.blit(text6, (v3_x, v3_y))    
        if q == 2:
            right_answer_text = font4.render(right_answer, 1, text_collor)
            window.blit(right_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
        if q == 3:
            incorrect_answer_text = font4.render(incorrect_answer, 1, text_collor)
            window.blit(incorrect_answer_text, (250, 250))
            window.blit(info_text, (100, 350))
    else:
        if score == 5:
            final_text = font1.render('Отличный результат', 1, text_collor)
        if score == 4:
            final_text = font1.render('Хороший результат', 1, text_collor)
        if score == 3:
            final_text = font1.render('Удовлетворительный результат', 1, text_collor)
        if score == 2 or score == 1 or score == 0:
            final_text = font1.render('Нужно много работать', 1, text_collor)
        window.blit(final_text, (200, 250))


    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if round == 1:
                if i.key == K_1:
                    q = 2
                    score += 1
                if i.key == K_2 or i.key == K_3:
                    q = 3
            if round == 2:
                if i.key == K_3:
                    q = 2
                    score += 1
                if i.key == K_2 or i.key == K_1:
                    q = 3
            if round == 3:
                if i.key == K_1:
                    q = 2
                    score += 1
                if i.key == K_2 or i.key == K_3:
                    q = 3

            if round == 4:
                if i.key == K_1:
                    q = 2
                    score += 1
                if i.key == K_2 or i.key == K_3:
                    q = 3
            if round == 5:
                if i.key == K_2:
                    q = 2
                    score += 1
                if i.key == K_1 or i.key == K_3:
                    q = 3

            if i.key == K_SPACE:
                round += 1
                q = 1
        





    display.update()







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




            




      
