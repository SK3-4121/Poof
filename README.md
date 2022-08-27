# Poof
_Custom syntax highlighting_

    https://github.com/SK3-4121/Poof/raw/main/poof%20syntax%20highlight.7z
    cp -r poof ~/.vscode/extensions

# Version 1.0.7
    func test() {
        tabel={
            "Test": "Testing sucks dude.",
        }!;
        print(tabel["Test"]);
    }

    test();


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
