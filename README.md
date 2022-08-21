# Poof
_Custom syntax highlighting_
    https://github.com/SK3-4121/Poof/raw/main/poof%20syntax%20highlight.7z
    cp -r poof ~/.vscode/extensions

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
