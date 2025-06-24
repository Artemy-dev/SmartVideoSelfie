# 🚀 [SmartVideoSelfie](https://github.com/Artemy-dev/SmartVideoSelfie) — Sharp Frame Extractor from Video  
A simple and effective Python CLI tool to extract sharp frames from videos.  
(Простой и эффективный CLI-инструмент на Python для извлечения чётких кадров из видео.)

---

## 💻 Supported Platforms

- ✅ Windows  
- ✅ macOS  
- ✅ Linux  

---

## 📦 Features / Возможности

- 🔹 Automatic extraction of every N-th frame from video / Автоматическое извлечение каждого N-го кадра из видео  
- 🔹 Sharpness evaluation using multiple metrics / Оценка резкости каждого кадра по нескольким метрикам  
- 🔹 Saves only high-quality sharp frames / Сохраняет только качественные, чёткие кадры  
- 🔹 Removes temporary files after processing / Удаление временных файлов после обработки  
- 🔹 Supports `.mp4`, `.mov`, `.avi`, `.mkv` video formats / Поддержка популярных видеоформатов

---

## ❓ Why this project? / Зачем этот проект?

This tool helps quickly get the best photos from video clips without manual frame-by-frame search.  
Инструмент позволяет быстро получать лучшие фото из видео без ручного перебора кадров.

---

## 🚀 Installation / Установка

```bash
git clone https://github.com/Artemy-dev/SmartVideoSelfie.git
cd SmartVideoSelfie
pip install -r requirements.txt
````

---

## ⚙️ Usage / Пример использования

```bash
python main.py --threshold 800 --skip 3
```

**Parameters / Параметры:**

| Parameter     | Description / Описание                                          | Default / По умолчанию | Allowed / Допустимо |
| ------------- | --------------------------------------------------------------- | ---------------------- | ------------------- |
| `--threshold` | Frame sharpness threshold (higher = stricter)                   | `700`                  | `100` – `2000`      |
| `--skip`      | Extract every N-th frame (e.g., 1 = every frame, 5 = every 5th) | `5`                    | `1` – `100`         |

---

## 📁 Project Structure / Структура проекта

```
├── photo/            # Saved sharp frames
├── video/            # Input videos
├── .gitignore
├── main.py           # Main script
├── README.md         # This file
└── requirements.txt  # Dependencies
```

---

## 👤 Author / Автор

**Artem Grachev**<br>
Python/Golang Developer | ML & DevOps Enthusiast<br>
Telegram: [@Artemy\_Develop](https://t.me/Artemy_Develop)<br>
GitHub: [Artemy-dev](https://github.com/Artemy-dev)

---

## 🌍 SEO Keywords

* video frame extraction
* sharp frame detection
* python cli video tool
* opencv frame extractor
* video photo grabber
* automatic frame selection
* python video processing
* selfie video snapshot
