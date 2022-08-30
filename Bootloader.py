import os, sys, wget

args = sys.argv

if len(args) >= 1:
    if args[1].lower() == "--help":
        print("Usage: Bootloader.py [--help] | [--update] | [package] | [output]")
        print("--help: Show this help")
        print("--update: Update poof to the latest version")
        print("--remove [r]: remove a spefiic package")
        print("--install [i]: install a spefiic package")
        sys.exit(0)
    elif args[1].lower() == "--update":
        wget.download("https://raw.githubusercontent.com/SK3-4121/Poof/main/poof.py", "poof.py")
        print("[🙄] You go update the bootloader")
        sys.exit(0)
    elif args[1].lower() == "--install" or args[1].lower() == "i":
        if len(args) >= 2:
            print(f"[🚀] instaling install {args[2]}")
            os.system(f"C:\poof\Python\wpy.exe -m pip install {args[2]}")
            sys.exit(0)
        elif len(args) == 2:
            print("[🎯] You need to specify the package to install")
            sys.exit(0)
    elif args[1].lower() == "--remove" or args[1].lower() == "r":
        if len(args) >= 2:
            print(f"[💣] removing {args[2]}")
            os.system(f"C:\poof\Python\wpy.exe -m pip uninstall {args[2]}")
            sys.exit(0)
        elif len(args) == 1:
            print("[🎯] You need to specify the package to remove")
            sys.exit(0)
    else:
        print("[🚗] Running poof")
        if len(args) != 2:
            os.system(f"C:\poof\Python\wpy.exe C:\poof\poof.py {args[1]} {args[2]}")
        elif len(args) != 1:
            os.system(f"C:\poof\Python\wpy.exe C:\poof\poof.py {args[1]}")
        else:
            print("[❌] Please provide a poof file and an output file")
            sys.exit()
