
import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("TaskForge")
app.geometry("500x700+0+0")

tasks = []
tasks_completed = 0
completed_tasks = []

# Instructions
instructions = ctk.CTkLabel(
    app,
    text="Upload, Do, Track, TaskForge.",
    font=("Helvetica", 25),
    text_color="blue"
)
instructions.place(x=100, y=650)

# Title
title = ctk.CTkLabel(
    app,
    text="TaskForge",
    font=("Helvetica", 40),
    text_color="blue"
)
title.pack(pady=(20, 1))

# Counter
counter_frame = ctk.CTkFrame(
    app,
    width=200,
    height=100,
    border_width=2,
    border_color="blue"
)
counter_frame.place(x=290, y=100)
counter_frame.propagate(False)

count_display = ctk.CTkLabel(
    counter_frame,
    text="No Tasks Completed",
    font=("Helvetica", 16),
    wraplength=150
)
count_display.pack(pady=2)

# Completed tasks section
completed_frame = ctk.CTkScrollableFrame(
    app,
    width=175,
    height=403,
    border_width=2,
    border_color="blue"
)
completed_frame.place(x=290, y=210)

completed = ctk.CTkLabel(
    completed_frame,
    text="Completed Tasks",
    font=("Helvetica", 16),
    wraplength=150
)
completed.pack(pady=2)

# Input frame
input_frame = ctk.CTkFrame(
    app,
    width=245,
    height=100,
    border_width=2,
    border_color="blue"
)
input_frame.place(x=10, y=100)
input_frame.propagate(False)

input_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Enter a task..."
)
input_entry.pack(pady=10)

warning = ctk.CTkLabel(input_frame, text="")
warning.pack()

# Active task list
list_frame = ctk.CTkScrollableFrame(
    app,
    width=220,
    height=400,
    border_width=2,
    border_color="blue"
)
list_frame.place(x=10, y=210)


def remove_task(item):
    tasks.remove(item)
    refresh_list()


def refresh_list():
    # Clear existing task rows
    for widget in list_frame.winfo_children():
        widget.destroy()

    # Rebuild active tasks
    for item in tasks:
        row = ctk.CTkFrame(list_frame)
        row.pack(fill="x", pady=2)

        label = ctk.CTkLabel(
            row,
            text=item,
            font=("Helvetica", 14),
            wraplength=75
        )
        label.pack(side="left", padx=10, pady=5)

        remove_button = ctk.CTkButton(
            row,
            text="❌",
            width=30,
            fg_color="transparent",
            hover_color="darkred",
            command=lambda i=item: remove_task(i)
        )
        remove_button.pack(side="right", padx=5)

        mark_button = ctk.CTkButton(
            row,
            text="✔️",
            width=30,
            fg_color="transparent",
            hover_color="darkgreen",
            command=lambda i=item: mark_complete(i)
        )
        mark_button.pack(side="right", padx=5)


def refresh_completed():
    # Clear existing completed rows
    for widget in completed_frame.winfo_children():
        if widget != completed:
            widget.destroy()

    # Update completed counter heading
    completed.configure(
        text="Completed Tasks"
    )

    # Rebuild completed task rows
    for item in completed_tasks:
        row = ctk.CTkFrame(completed_frame)
        row.pack(fill="x", pady=2)

        label = ctk.CTkLabel(
            row,
            text=item,
            font=("Helvetica", 14),
            wraplength=100
        )
        label.pack(padx=10, pady=5)


def mark_complete(item):
    global tasks_completed

    tasks.remove(item)
    completed_tasks.append(item)
    tasks_completed += 1

    count_display.configure(
        text=f"Completed: {tasks_completed}"
    )

    refresh_list()
    refresh_completed()


def show():
    item = input_entry.get().strip()

    if not item:
        warning.configure(
            text="Please enter a task!",
            text_color="darkred"
        )
        return

    tasks.append(item)
    warning.configure(text="")
    input_entry.delete(0, "end")
    refresh_list()


# Press Enter to add a task
input_entry.bind("<Return>", lambda event: show())

app.mainloop()




