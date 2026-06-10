import os
import sys
import time
from gtts import gTTS

# কালার কোড সেটআপ (টার্মাক্স ইন্টারফেস সুন্দর করার জন্য)
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def show_banner():
    clear_screen()
    print(CYAN + BOLD + """
 █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
 █████████╗████████╗███████╗   ██████╗  ██████╗ █
 █╚══██╔══╝╚══██╔══╝██╔════╝   ██╔══██╗██╔═══██╗█
 █   ██║      ██║   ███████╗   ██████╔╝██║   ██║█
 █   ██║      ██║   ╚════██║   ██╔═══╝ ██║   ██║█
 █   ██║      ██║   ███████║   ██║     ╚██████╔╝█
 █   ╚═╝      ╚═╝   ╚══════╝   ╚═╝      ╚═════╝ █
 █        [ TEXT TO SPEECH ADVANCED TOOL ]      █
 █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    """ + RESET)
    print(YELLOW + "      Developed for Termux | Version 2.0" + RESET)
    print("-" * 53)

def loading_animation():
    animation = [
        "[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 25%", 
        "[■■■■□□□□□□] 40%", "[■■■■■■□□□□] 65%", 
        "[■■■■■■■■□□] 85%", "[■■■■■■■■■■] 100%"
    ]
    print("\n" + YELLOW + " ⚙️ অডিও তৈরি হচ্ছে, দয়া করে অপেক্ষা করো..." + RESET)
    for i in range(len(animation)):
        time.sleep(0.4)
        sys.stdout.write("\r" + CYAN + " " + animation[i] + RESET)
        sys.stdout.flush()
    print("\n")

def main():
    show_banner()
    
    # মাল্টি-লাইন ইনপুট নেওয়ার সিস্টেম
    print(GREEN + BOLD + " 📝 তোমার বাংলা টেক্সটটি নিচে পেস্ট করো।" + RESET)
    print(WHITE + " (লেখা শেষ হলে নতুন লাইনে " + RED + "DONE" + WHITE + " লিখে Enter চাপো):\n" + RESET)
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "DONE":
                break
            lines.append(line)
        except EOFError:
            break
            
    text = "\n".join(lines)
    
    if not text.strip():
        print(RED + "\n ❌ কোনো টেক্সট দেওয়া হয়নি! টুলটি বন্ধ হচ্ছে।" + RESET)
        return

    # ফাইলের নাম ইনপুট নেওয়া
    print("\n" + "-" * 53)
    print(GREEN + " 💾 অডিও ফাইলের একটি নাম দাও (যেমন: myaudio)" + RESET)
    file_name = input(CYAN + " ❯ " + RESET).strip()
    
    if not file_name:
        file_name = "termux_audio" # নাম না দিলে ডিফল্ট নাম
        
    # ডট mp3 এক্সটেনশন না থাকলে যুক্ত করা
    if not file_name.endswith('.mp3'):
        file_name += '.mp3'
        
    save_path = f"/sdcard/Download/{file_name}"
    
    try:
        # প্রোগ্রেস বার দেখানো
        loading_animation()
        
        # gTTS প্রসেসিং
        tts = gTTS(text=text, lang='bn')
        tts.save(save_path)
        
        print(GREEN + BOLD + " ⚡ সফলভাবে সম্পন্ন হয়েছে!" + RESET)
        print(WHITE + f" 📂 ফাইলটি সেভ হয়েছে: " + YELLOW + f"Internal Storage -> Download -> {file_name}" + RESET)
        print("-" * 53 + "\n")
        
    except Exception as e:
        print(RED + f"\n ❌ একটি সমস্যা হয়েছে: {e}" + RESET)

if __name__ == "__main__":
    # স্টোরেজ পারমিশন নিশ্চিত করা
    if not os.path.exists("/sdcard"):
        print(RED + " ⚠️ স্টোরেজ পারমিশন প্রয়োজন! টার্মাক্সে 'termux-setup-storage' রান করো।" + RESET)
    else:
        main()
