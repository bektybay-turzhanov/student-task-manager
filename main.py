def main():
    print("Student Task Manager")
    task = input("Enter a task: ").strip()

    if not task:
        print("Task cannot be empty")
    else:
        print("Task added:", task)


if __name__ == "__main__":
    main()
