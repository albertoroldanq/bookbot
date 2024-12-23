# bookbot
BookBot is my first project!

After you've cloned the repository to your local machine, you'll need to create a `books/` directory in the root level of the project and add a new file `books/frankenstein.txt`

You can paste the content of the book from [https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt) or download the book from the same link or generate a

Or run this in your terminal from the root of the project to generate the books directory and file automatically
```commandline
mkdir books
curl -sS https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt > books/frankenstein.txt
```

## Testing steps

### For Windows (WSL 2) / Linux users
If you're on Linux (or Windows WSL 2), you may already have python installed. Verify this by running:

```python3 --version```  

If that worked, you can skip ahead. If not, run this command to install python3:  
```
sudo apt update
sudo apt install -y python3
```
Make sure to read the installation logs in case there's some step you're missing!

When you're done, close your terminal and re-open it to ensure the changes have taken effect.

### For Mac OS
You can use the Homebrew package manager to install Python. If you don't already have it installed you can install homebrew by running the following command:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Open your `~/.zshrc`  or `~/.bashrc` file (or whatever your shell config file is) and add this line to the bottom:
```
export PATH="/opt/homebrew/bin:$PATH"
```

Restart your terminal to ensure the changes have taken effect.

Once brew is added to the path, you can install python by simply running the command:

```
brew install python3
```
### Check Installation
Finally, make sure that it worked:

```python3 --version```

Once you have Python installed, you can run the follwoing command to run the project:
```commandline
# navigate to the project directory
cd bookbot
# run the project
python3 main.py
```
