if __name__ == "__main__":
    import os
    import vk_api 
    from vk_api.longpoll import VkLongPoll, VkEventType

    token=os.environ["VK_API_TOKEN"] 

    # Подключаем токен и longpoll
    bh = vk_api.VkApi(token = token)
    give = bh.get_api()
    longpoll = VkLongPoll(bh)

    # Создадим функцию для ответа на сообщения в лс группы
    def blasthack(id, text):
        bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

    # Слушаем longpoll(Сообщения)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
          # Чтобы наш бот не слышал и не отвечал на самого себя
           if event.to_me:
              message = event.text.lower()
              # Получаем id пользователя
              id = event.user_id
              if message == 'привет':
                blasthack(id, 'Привет, я бот!')

              elif message == 'как дела?':
                  blasthack(id, 'Хорошо, а твои как?' )

              else:
                 blasthack(id, 'Я вас не понимаю! :(')
