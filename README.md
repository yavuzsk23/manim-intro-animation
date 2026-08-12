# Manim Intro Animation

A first introductory animation built with **Manim**, the mathematical animation engine popularized by 3Blue1Brown. Renders a circle that draws itself, gets labeled, and transitions color.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Manim](https://img.shields.io/badge/Manim-Animation-purple)

---

## 🇬🇧 English

### Overview
This scene demonstrates the core building blocks of a Manim animation: creating a shape, styling it, adding text, and animating a property change — all rendered to a video file.

### Features
- A circle drawn with a smooth "create" animation
- Cyan outline with a semi-transparent blue fill
- A text label that appears with a "write" (typing-style) animation
- A color transition animation (`.animate` syntax)
- Structured logging via Loguru to track render progress

### Requirements
- Python 3.10 or higher
- `manim`
- `loguru`
- FFmpeg (required by Manim for rendering video)

### Installation
```bash
pip install manim loguru
```
> Note: Manim also requires a working FFmpeg installation and, on some systems, a LaTeX distribution. See the [official Manim installation guide](https://docs.manim.community/en/stable/installation.html) for OS-specific instructions.

### Usage
```bash
manim -pql manim_first_animation.py FirstAnimation
```
- `-p` previews the video automatically after rendering
- `-ql` renders in low quality for faster iteration (use `-qh` for high quality)

### How it works
The scene is defined as a class inheriting from `Scene`, with all animation logic inside `construct()`. Each `self.play(...)` call renders one animation step: `Create` draws the circle's outline progressively, `Write` animates the text as if being typed, and `circle.animate.set_color(...)` smoothly interpolates the fill color. `self.wait(2)` holds the final frame for two seconds before the render ends.

---

## 🇩🇪 Deutsch

### Überblick
Diese Szene demonstriert die grundlegenden Bausteine einer Manim-Animation: das Erstellen einer Form, deren Gestaltung, das Hinzufügen von Text und die Animation einer Eigenschaftsänderung — alles gerendert in eine Videodatei.

### Funktionen
- Ein Kreis, gezeichnet mit einer sanften "Create"-Animation
- Cyanfarbener Umriss mit halbtransparenter blauer Füllung
- Ein Textlabel, das mit einer "Write"-Animation (im Schreibstil) erscheint
- Eine Farbübergangsanimation (`.animate`-Syntax)
- Strukturiertes Logging über Loguru zur Verfolgung des Render-Fortschritts

### Voraussetzungen
- Python 3.10 oder höher
- `manim`
- `loguru`
- FFmpeg (von Manim für das Rendern von Videos benötigt)

### Installation
```bash
pip install manim loguru
```
> Hinweis: Manim benötigt außerdem eine funktionierende FFmpeg-Installation und auf manchen Systemen eine LaTeX-Distribution. Siehe die [offizielle Manim-Installationsanleitung](https://docs.manim.community/en/stable/installation.html) für betriebssystemspezifische Hinweise.

### Verwendung
```bash
manim -pql manim_first_animation.py FirstAnimation
```
- `-p` zeigt das Video automatisch nach dem Rendern an
- `-ql` rendert in niedriger Qualität für schnellere Iteration (verwende `-qh` für hohe Qualität)

### Funktionsweise
Die Szene ist als Klasse definiert, die von `Scene` erbt, mit der gesamten Animationslogik innerhalb von `construct()`. Jeder `self.play(...)`-Aufruf rendert einen Animationsschritt: `Create` zeichnet den Umriss des Kreises schrittweise, `Write` animiert den Text, als würde er getippt, und `circle.animate.set_color(...)` interpoliert sanft die Füllfarbe. `self.wait(2)` hält das letzte Bild zwei Sekunden lang, bevor das Rendering endet.

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu sahne, bir Manim animasyonunun temel yapı taşlarını gösterir: bir şekil oluşturma, stillendirme, metin ekleme ve bir özellik değişikliğini animasyonlu hale getirme — hepsi bir video dosyasına render edilir.

### Özellikler
- Yumuşak bir "create" animasyonuyla çizilen bir çember
- Yarı saydam mavi dolgulu, camgöbeği renkli dış çizgi
- "Write" (yazma tarzı) animasyonuyla beliren bir metin etiketi
- Bir renk geçiş animasyonu (`.animate` syntax'ı)
- Render ilerlemesini takip etmek için Loguru üzerinden yapılandırılmış loglama

### Gereksinimler
- Python 3.10 veya üzeri
- `manim`
- `loguru`
- FFmpeg (Manim'in video render etmesi için gerekli)

### Kurulum
```bash
pip install manim loguru
```
> Not: Manim ayrıca çalışan bir FFmpeg kurulumu ve bazı sistemlerde bir LaTeX dağıtımı gerektirir. İşletim sistemine özgü talimatlar için [resmi Manim kurulum rehberine](https://docs.manim.community/en/stable/installation.html) bakabilirsin.

### Kullanım
```bash
manim -pql manim_first_animation.py FirstAnimation
```
- `-p` render işleminden sonra videoyu otomatik olarak önizler
- `-ql` daha hızlı deneme için düşük kalitede render eder (yüksek kalite için `-qh` kullan)

### Nasıl çalışır?
Sahne, `Scene`'den miras alan bir sınıf olarak tanımlanır, tüm animasyon mantığı `construct()` içinde yer alır. Her `self.play(...)` çağrısı bir animasyon adımını render eder: `Create` çemberin dış çizgisini kademeli olarak çizer, `Write` metni sanki yazılıyormuş gibi canlandırır, ve `circle.animate.set_color(...)` dolgu rengini yumuşak bir şekilde geçiş yaptırır. `self.wait(2)`, render sona ermeden önce son kareyi iki saniye boyunca tutar.
