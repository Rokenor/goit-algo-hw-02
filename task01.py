import queue
import random
import time

# Лічільник унікальних номерів заявок
request_id_counter = 0

def generate_request(q: queue.Queue):
    ''' Генерує нову заявку '''
    global request_id_counter
    request_id_counter += 1

    new_request = {
        "id": request_id_counter,
        "description": f"Завдання №{request_id_counter}"
    }

    q.put(new_request)
    print(f"Завяка з ID {new_request['id']} додана до черги")      

def process_request(q: queue.Queue):
    ''' Обробляє заявку '''
    if not q.empty():
        request_to_process = q.get()
        print(f"Обробляється заявка №{request_to_process['id']}")

        time.sleep(1)
        print(f"Заявка №{request_to_process['id']} оброблена")
    else:
        print("Черга порожня")

if __name__ == "__main__":
    # Створюємо чергу заявок
    request_queue = queue.Queue()

    print('Для завершення програми натисність Ctrl+C')

    # Головний цикл програми
    try:
        while True:
            # З імовірністю 70% генеруємо нову заявку
            if random.random() < 0.7:
                generate_request(request_queue)
            
            # З імовірністю 50% обробляємо заявку
            if random.random() < 0.5:
                process_request(request_queue)

            # Виводимо поточний розмір черги
            print(f"Поточний розмір черги: {request_queue.qsize()}")

            # Уповільнення симуляції
            time.sleep(2)

    except KeyboardInterrupt:
        print('*'*10)
        print("Програму завершено")
        print(f"Необроблено заявок: {request_queue.qsize()}")