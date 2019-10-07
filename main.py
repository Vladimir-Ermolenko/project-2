# Simple text quest, controlled by user giving one of the answers to the question

print('Квет-игра "-30"',
      "\n", 'Вы проснулись в глухом зимнем лесу и ничего не помните.',
      "\n", 'Вы осмотрелись и нашли зажигалку и котелок.',
      "\n", "\n", 'В ходе прохождения вам будет предложено выбрать '
                  'один из вариантов ответа, выбор производится вводом цифры,'
                  ' соответствующей желаемому варианту, цифра вводится без скобок', "\n", )

a = input('1. (1)Разжечь костёр и растопить воду или'
          ' (2)Создать укрытие')
if a == '1':
    print('Теперь у вас есть питьевая вода и источник тепла.', "\n")
    b = input('2. (1)Пойти на поиски пищи или (2)Изучить территорию в поисках укрытия')

    if b == '1':
        print('Помимо пригоршни ягод вы нашли чей-то рюкзак,'
              ' в котором есть сигнальный пистолет, нарисованная карта и 2 банки консервов.', "\n")
        d = input('3. (1)Пойти к ближайшей хижине, отмеченной на карте или'
                  ' (2)Перекусить')

        if d == '1':
            print('Вы успешно дошли до хижины, познакомились с её обитателем,'
                  ' который отпоил вас горячим чаем и позвонил куда следует',
                  "\n", "\n", 'Поздравляю, вы выжили!')

        elif d == '2':
            print('Вы решили начать трапезу с аппетитных ягод, но они, к сожалению, оказались ядовитыми.',
                  "\n", "\n", 'Вам не удалось выжить.')

    elif b == '2':
        print('Вы нашли заброшенную хижину, в которой есть'
              ' зимняя одежда и непонятные запчасти', "\n")
        e = input('2. (1)Попробовать собрать передатчик из запчастей или'
                  ' (2)Одеться и выйти вытаптывать надпись SOS на снегу,'
                  ' в надежде, что её заметят с самолёта')

        if e == '1':
            print('В результате бесцельного комбинирования неизвестных'
                  ' вам запчастей вы собрали бомбу,'
                  ' которая в тот же момент сдетанировала прямо у вас в руках.',
                  "\n", "\n", 'К сожалению, вам не удалось выжить')

        elif e == '2':
            print('У вас получилась восхитительная надпись,'
                  ' но никаких самолётов в ближайшее время не предвидится', "\n")
            f = input('3. (1)Вернуться в хижину или'
                      ' (2)Попробовать выстрелить из сигнального пистолета,'
                      ' который только что нащупали в кармане своей новенькой куртки')

            if f == '1':
                print('Вы настолько устали вытаптывать SOS на снегу,'
                      ' что упали замертво на полпути к своему укрытию.',
                      "\n", "\n", 'К сожалению, Вы не выжили.')

            elif f == '2':
                print('Удивительно, но на этот раз вам повезло.'
                      ' Вашу сигнальную ракету увидел лесник,'
                      ' который позвонил куда следует и за вами'
                      ' прилетел вертолёт со спасателями.',
                      "\n", "\n", 'Поздравляю, вы выжили!')

elif a == '2':
    print('Теперь у вас укрытие от холода и зверей.', "\n")
    c = input('2. (1)Пойти на поиски пищи или'
              ' (2)Попробовать разжечь большой костёр,'
              ' в надежде, что его заметят с самолёта')

    if c == '1':
        print('Готовой пищи не оказалось рядом, но зато вы встретили хромого оленя', "\n")
        g = input('3. (1)Попробовать догнать его и зажарить в последствии или'
                  ' (2)Поискать растительной пищи тщательнее')

        if g == '1':
            print('К вашему удивлению, даже хромой олень бегает быстрее вас.'
                  ' Теперь вы не только голодны, но еще и заблудились', "\n")
            h = input('4. (1)Пойти по неизвестной тропинке в неизвестном направлении или'
                      ' (2)Постараться найти своё укрытие')

            if h == '1':
                print('Неизвестная тропинка привела вас к домику с телефоном для экстренной связи.'
                      ' Вы позвонили своей бабуле и она обещала вызвать спасателей.',
                      "\n", "\n", 'Поздравляю, вы выжили!')

            elif h == '2':
                print('Пока вы искали своё укрытие вы настолько вымотались,'
                      ' что решили лечь отдохнуть прямо в сугробе.',
                      "\n", "\n", 'Очевидно, вы не выжили.')

        elif g == '2':
            print('В результате тщательных поисков вы нашли несколько'
                  ' ягодок и сумку с мобильным телефоном и плюшевым мишкой', "\n")
            m = input('4. (1)Перекусить или'
                      ' (2)Попобовать позвонить в службу спасения')

            if m == '1':
                print('Вы восхитительно пообедали и готовы к новым свершениям', "\n")
                j = input('5. (1)Вернуться поспать в убежище или'
                          ' (2)Пойти на дым вдалеке')
                if j == '1':
                    print('Вы отлично выспались, однако проснулись в'
                          ' компании с белым медведем. Выходит, ваше укрытие'
                          ' не защищает от зверей, впрочем, уже не важно.',
                          "\n", "\n", 'Конечно же, вы не выжили.')
                elif j == '2':
                    print('Дым вдалеке оказался от разбившегося неподалёку вертолёта.'
                          ' Главное, на борту оказалась рация и теперь'
                          ' вы вместе с пилотом будете спасены.',
                          "\n", "\n", 'Поздавляю, вы выжили!')

            elif m == '2':
                print('Пока вы пытались куда-то позвонить по игрушеному'
                      ' телефону к вам подкрался медведь.'
                      ' Убежать не удалось.',
                      "\n", "\n", 'Понятное дело, вы не выжили.')

    elif c == '2':
        print('Костёр получился отменный, скорее всего к вам уже вылетели'
              ' на помощь. Однако помимо возможной помощи вы привлекли голодного медведя', "\n")
        n = input('3. (1)Достать горящую палку из костра и отпугивать медведя ею или'
                  ' (2)Залезть на ближайшее дерево')
        if n == '1':
            print('Сначала всё шло неплохо, однако в самый'
                  ' неподходящий момент ваша палка потухла.'
                  ' Последствия можете предугадать сами.',
                  "\n", "\n", 'Понятное дело, вы не выжили.')
        elif n == '2':
            print('Вы смогли просидеть на дереве достаточно долго'
                  ' и вертолёт спасателей забрал вас прямо с него.',
                  "\n", "\n", 'Поздравляю, вы выжили.')
pass
