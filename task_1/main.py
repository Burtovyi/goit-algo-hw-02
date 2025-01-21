from queue import Queue
import time

# Створення черги з максимальним розміром 5
queue = Queue(maxsize=5)

# Унікальний номер заявки
request_id = 0

def generate_request():
    global request_id
    if not queue.full():
        request_id += 1
        queue.put(f"Request #{request_id}")
        print(f"Generated: Request #{request_id}")
    else:
        print("Queue is full! Cannot add more requests.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processed: {request}")
    else:
        print("Queue is empty! No requests to process.")

if __name__ == '__main__':
    while True:
        print("\nMenu:")
        print("1. Generate new request")
        print("2. Process request")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")
        
        # Імітація паузи для зручності перегляду
        time.sleep(1)
