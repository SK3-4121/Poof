import threading, time, sys, os

class Parser:
    def __init__(self, file, output) -> None:
        self.Settings = {
            "Silent_Mode": True,
            "Auto_Clear": True,
        }
        self.FailedPoint = False
        self.output = output
        if self.Settings["Auto_Clear"] == True:
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")
        with open(file, "r") as f: self.content = f.read()

    def run_sanitizer(self):
        script = self.content
        CheckPoints = []
        CPF = False
        Counter = 0

        for line in script.split("\n"):
            Counter += 1
            if not line == "":
                if not line.endswith(";") and not line.endswith("{") and not line.endswith("}"):
                    CheckPoints.append(f"{Counter} | {line}")
                    CPF = True

        if CPF == False:
            if self.Settings["Silent_Mode"] == False:
                print("[🚀] Sanitizer is working")
            self.FailedPoint = True
            return True
        else:
            def read():
                time.sleep(0.5)
                print("[❌] Sanitizer is not working\nPlease check the following lines:\n------------------------------")
                for i in CheckPoints:
                    print(i)
                print("------------------------------")

            threading.Thread(target=read).start()

    def Remove_Comments(self):
        script = self.content
        for line in script.split("\n"):
            if line.startswith("#"):
                if line.endswith(")"):
                    script = script.replace(line, "")
                script = script.replace(line, line[:-99999999])
        self.content = script

    def Write_Output(self):
        if self.FailedPoint == True:
            file = self.output
            with open(file, "w") as f: f.write(self.content)
            if self.Settings["Silent_Mode"] == False:
                print("[🎉] Script is written to {}".format(file))
            return True

    def Execute(self):
        if self.FailedPoint == True:
            script = self.content
            exec(script)
            return True

    def Compile(self):
        script = self.content
        self.Remove_Comments()
        if self.run_sanitizer() == True:
            for line in script.split("\n"):
                if line.endswith(" {"):
                    script = script.replace(" {", ":")
                if line.startswith("#"):
                    script = script.replace(line, "")
                if line.startswith("}"):
                    script = script.replace(line, "")

            # rules
            script = script.replace("require", "import")
            script = script.replace("inp", "input")
            script = script.replace("func", "def")
            script = script.replace("};", "")
            script = script.replace("}", "")
            script = script.replace(";", "")
            script = script.replace(" else", "else")
            script = script.replace("node", "class")
            script = script.replace("else if", "elif")

            self.content = script
            if self.Settings["Silent_Mode"] == False:
                print("[🍺] Poof is done")
            return True

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        PRS = Parser(args[1], args[2])

        if PRS.Compile() == True:
            PRS.Write_Output()
            PRS.Execute()
    else:
        print("[❌] Please provide a file and an output file")
        sys.exit()
