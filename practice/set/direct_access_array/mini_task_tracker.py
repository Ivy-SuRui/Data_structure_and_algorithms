tasks = [None] * 100

def add_task(name,index):
    tasks[index] = name

def view_task(index):
    print(tasks[index])

def mark_done(index):
    tasks[index] = f"{tasks[index]} Done."

def delete_task(index):
    tasks[index] = None

def print_tasks():
    for i in range(len(tasks)):
        if tasks[i] != None:
            print(f"{i}: {tasks[i]}")


def main():
    add_task("Write report",0)
    add_task("Buy milk",3)
    mark_done(0)
    print_tasks()

if __name__ == "__main__":
    main()