import tkinter as tk

root = tk.Tk()
root.title("Счётчик")

text_hello = tk.Label(root, text="Нажато: 0 раз")
text_hello.pack(pady=10)

def main():
    count = 0

    def click():
        nonlocal count
        count += 1
        text_hello.config(text=f"Нажато: {count} раз")

    btn = tk.Button(root, text="Нажми меня", command=click)
    btn.pack(pady=10)

main()

root.mainloop()