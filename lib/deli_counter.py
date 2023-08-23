def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_str = " ".join(f"{i + 1}. {person}" for i, person in enumerate(queue))
        print(f"The line is currently: {line_str}")

def take_a_number(queue, person):
    queue.append(person)
    position = len(queue)
    print(f"Welcome, {person}. You are number {position} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        serving_person = queue.pop(0)
        print(f"Currently serving {serving_person}.")