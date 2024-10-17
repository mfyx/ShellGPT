import cmd
import subprocess
import sys
import os

"""
BASE TODO
- [x] base shell terminal
- [x] support cd command
- [x] support exit command
- [ ] support syntax highlighting
- [ ] use `!` to launching external command-line programs
- [ ] real time acquisition of operational output

SENIOR TODO
- [ ] explain the results of command execution
- [ ] use `TAB` to adopt command auto completion
- [ ] use `:` to convert natural language input to shell commands
- [ ] use `?` to explain how to use a certain command
- [ ] use `>` to chat with llm
- [ ] use `<your task>` or ``` <your tasks> ``` to assign tasks
"""

class FullShell(cmd.Cmd):
    intro = 'Welcome to FullShell. Type help or ? to list commands.'
    prompt = '(full_shell) '

    def do_exit(self, _):
        """Exit the shell."""
        print("Exiting the shell. Goodbye!")
        return True

    def do_cd(self, path):
        """Change the current directory."""
        try:
            os.chdir(path)
            print(f"Changed directory to {os.getcwd()}")
        except FileNotFoundError:
            print(f"No such directory: {path}")
        except Exception as e:
            print(f"Error: {e}")

    def default(self, line):
        """Execute the entered shell command."""
        try:
            # 使用 shell 执行命令
            result = subprocess.run(line, shell=True, check=True, text=True, capture_output=True)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"Error: {result.stderr}", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")

if __name__ == '__main__':
    FullShell().cmdloop()