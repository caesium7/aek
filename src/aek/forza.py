import sys

if sys.stdout.isatty():
    print("\033[1;30;103m FORZA AEKARA! \033[0m")
else:
    print("🟡⚫ FORZA AEKARA! 🟡⚫")
