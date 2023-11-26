import tkinter as tk
from tkinter import filedialog
import subprocess
import os

selected_codec = "libvpx"  # По умолчанию выбран VP8

def convert_video():
    input_file = filedialog.askopenfilename(title="Select your no hud videofile",
                                            filetypes=(("Video files", "*.mp4;*.avi;*.mkv;*.webm"), ("All files", "*.*")))
    if input_file:
        output_format = "VP8" if selected_codec == "libvpx" else "VP9"
        output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Output")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + f'_converted_{output_format}.webm')
        
        command = [
            'ffmpeg',
            '-i', input_file,
            '-c:v', selected_codec, '-b:v', '5M',  # Использование выбранного кодека и битрейта
            '-f', 'webm',
            output_file
        ]

        status_label.config(text="We are working on your file..... freezes are possible.")
        root.update()  # Обновление интерфейса для отображения текста

        subprocess.run(command)  # Запуск процесса конвертации без вывода информации о прогрессе

        status_label.config(text="the conversion was completed. the file is saved in this directory: " + output_file)
        format_label.config(text="Webm type: " + output_format)

def select_codec(codec):
    global selected_codec
    selected_codec = codec
    output_format = "VP8" if selected_codec == "libvpx" else "VP9"
    format_label.config(text="Webm type: " + output_format)

def exit_program():
    root.destroy()

# Создание окна
root = tk.Tk()
root.title("Just Dance Video2Webm Tools by kezo")

# Установка размера окна
root.geometry("1024x512")
root.resizable(False, False)

# Установка фонового изображения, если файл существует
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "Data", "background.png")

if os.path.isfile(image_path):
    background_image = tk.PhotoImage(file=image_path)
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

# Кнопка выбора файла
select_button = tk.Button(root, text="Chose your videofile and start convertion...", command=convert_video)
select_button.pack(pady=20)

# Кнопки выбора кодека
vp8_button = tk.Button(root, text="Convert to webm VP8", command=lambda: select_codec("libvpx"))
vp8_button.pack(side="left", padx=20)
vp9_button = tk.Button(root, text="Convert to webm VP9", command=lambda: select_codec("libvpx-vp9"))
vp9_button.pack(side="right", padx=20)

# Метка для вывода статуса
status_label = tk.Label(root, text="")
status_label.pack()

# Метка для отображения выбранного формата
format_label = tk.Label(root, text="Webm type: VP8")
format_label.pack()

# Кнопка для выхода из программы
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

# Текст в правом нижнем углу
text_label = tk.Label(root, text="Just Dance Video2webm", fg="white", bg="black")
text_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
