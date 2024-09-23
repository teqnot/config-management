import tkinter as tk

class ShellGUI:
    def __init__(self, shell):
        self.shell = shell
        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.insert_prompt()
        self.text.bind("<Return>", self.execute_command)
        self.text.bind('<Key>', self.prevent_editing)

    def insert_prompt(self):
        self.text.insert(tk.END, self.shell.get_prompt())
        self.text.see(tk.END)

    def execute_command(self, event):
        lines = self.text.get("1.0", tk.END).splitlines()
        input_line = lines[-1].replace(self.shell.get_prompt(), '').strip()

        self.text.insert(tk.END, "\n")

        result = self.shell.run_command(input_line)
        if not input_line.startswith("cd"):
            self.text.insert(tk.END, f"{result}\n")
        self.insert_prompt()

        return "break"
    
    def run_init_script(self, init_script):
        self.text.insert(tk.END, f"[ Executing startup script {init_script} ]\n")
        self.insert_prompt()
        with open(init_script, 'r') as file:
            commands = file.readlines()
            for command in commands:
                command = command.strip()
                if command:
                    self.text.insert(tk.END, f"{command}\n")
                    result = self.shell.run_command(command)
                    self.text.insert(tk.END, f"{result}\n")
                    self.insert_prompt()
    
    def prevent_editing(self, event):
        if int(self.text.index(tk.INSERT).split('.')[1]) < len(self.shell.get_prompt()):
            self.text.insert(tk.END, " ")

    def run(self):
        self.root.mainloop()