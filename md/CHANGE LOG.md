# Poof
_Custom syntax highlighting_

    https://github.com/SK3-4121/Poof/raw/main/poof%20syntax%20highlight.7z
    cp -r poof ~/.vscode/extensions

# Version 1.0.8
    Fixed requirements not working by using a python as a extrnal pip and python env for exec()
    New commands added to poof.exe; To fix it i added a new BootLoader.py which you can find in the root.
    
    Usage: Bootloader.py [--help] | [--update] | [package] | [output]
    --help: Show this help
    --update: Update poof to the latest version
    --remove [r]: remove a spefiic package
    --install [i]: install a spefiic package

# Version 1.0.7
    func test() {
        tabel={
            "Test": "Testing sucks dude.",
        }!;
        print(tabel["Test"]);
    }

    test(); -> Testing sucks dude.


# Version 1.0.6
Fixed comments after line script

# Version 1.0.5
Added switches
Example

    ask = inp("[*]: Whats your number: ");

    switch (int(ask)) {
        case 1 {
            print("You choose 1");
        }
        case 2 {
            print("You choose 2");
        }
        case 3 {
            print("You choose 3");
        }
        case 4 {
            print("You choose 4");
        }
    }


# Version 1.0.4
Added two different types of commands & settings.json (found in C:\poof)

    poof index.pf
    or
    poof index.pf output.py

# Version 1.0.3
Fixed the try, except, finally crash issue

# Version 1.0.2
Fixed the file input type

# Version 1.0.1
    python poof.py input.pf output/file.py

# Version 1.0.0
    Poof = Parser("index.pf", "cache/output.py")
    Poof.Settings["Silent_Mode"] = True
    Poof.Compile()
    Poof.Write_Output()
    Poof.Execute()
