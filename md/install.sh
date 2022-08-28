echo Installing Poof!;
# echo NOTE: MAKE SURE YOUR ON ROOT;

ClearDirectory() {
    rm -r C:/poof;
}

ClearDirectory;
mkdir C:/poof;

touch C:/poof/Settings.json;
echo "{\"Silent_Mode\": true, \"Auto_Clear\": true}" > C:/poof/Settings.json;

powershell -ExecutionPolicy Bypass -Command 'wget "https://github.com/SK3-4121/Poof/releases/download/Purple/poof.exe" -o C:\poof\poof.exe';

set PATH=$PATH:~C:/poof

echo Installed Poof!;
read -t 5;
