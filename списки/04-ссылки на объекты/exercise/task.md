Реализуйте функцию `make_list`, которая возвращает список из пустых списков(Количество вложенных списков определяется параметром, передаваемым в функцию).

Причем добавление любого элемента во вложенный список приводит к тому, что он добавляется во все остальные списки


    l = make_list(2)   #      [
                       #         [],
                       #         [],
                       #      ]
    
    l[1].append(a)     # l -> [
                       #         [1],
                       #         [1],
                       #      ]     