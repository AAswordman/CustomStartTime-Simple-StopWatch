import tkinter as tk
import time

class Stopwatch(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("高级秒表")
        self.geometry("600x180")
        self.configure(bg="#F8F8F8")

        self.start_time = 0.0
        self.running = False

        self.label = tk.Label(self, text="00:00:00.00", font=("Arial", 40), bg="#F8F8F8", fg="black", pady=20)
        self.label.pack(fill=tk.X, ipadx=20, ipady=10)

        self.custom_time_entry = tk.Entry(self, font=("Arial", 14), justify=tk.CENTER, width=5)
        self.custom_time_entry.insert(0, "0")  # 默认值为0秒
        self.custom_time_entry.pack(side=tk.LEFT, padx=(10, 0))

        self.set_start_button = tk.Button(self, text="设定开始时间", font=("Arial", 14), bg="#FF9800", fg="white",
                                        command=self.set_custom_start, width=15)
        self.set_start_button.pack(side=tk.LEFT, padx=(10, 0))

        self.buttons_frame = tk.Frame(self, bg="#F8F8F8")
        self.buttons_frame.pack(fill=tk.X, pady=10)

        self.start_button = tk.Button(self.buttons_frame, text="开始", font=("Arial", 16), bg="#4CAF50", fg="white",
                                     command=self.start, width=6, state=tk.DISABLED)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.buttons_frame, text="停止", font=("Arial", 16), bg="#F44336", fg="white",
                                    command=self.stop, width=6, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.buttons_frame, text="重置", font=("Arial", 16), bg="#2196F3", fg="white",
                                    command=self.reset, width=6)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def set_custom_start(self):
        try:
            custom_seconds = int(self.custom_time_entry.get())
            if custom_seconds >= 0:
                self.start_time = time.time() - custom_seconds  # 直接更新start_time
                self.running = True
                self.update_clock()  # 立即更新显示
                self.running = False
                self.start_button.config(state=tk.NORMAL)  # 允许开始计时
            else:
                print("请输入一个非负整数作为开始时间。")
        except ValueError:
            print("请输入有效的数字。")

    def start(self):
        if not self.running:
            self.running = True
            self.update_clock()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        if self.running:
            self.update_clock()
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset(self):
        self.start_time = time.time()
        self.update_clock()
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_clock(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            hours, remainder = divmod(self.elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}."
                                  f"{int((seconds * 100) % 100):02d}")
            self.after(100, self.update_clock)

if __name__ == "__main__":
    app = Stopwatch()
    app.mainloop()