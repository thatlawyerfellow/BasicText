# BasicText 

**BasicText v.1 is a lightweight, intuitive text editor designed to provide an efficient and straightforward writing experience.** This editor is built with Python and the powerful PyQt5 framework, offering a clean, user-friendly interface along with essential functionalities that cater to your basic text editing needs.

With BasicText, users can create, open, and save text files effortlessly. It supports fundamental text formatting features such as font customization and alignment options, including left, center, right, and justified alignment. Additionally, BasicText features an integrated Find & Replace utility, allowing users to easily navigate and refine their documents. The text editor also includes a word count feature for those who keep track of their document length.

It is released under the GNU General Public License v.3 (GNU GPL v.3 accordingly BasicText v.1 is free software. Users are encouraged to modify and redistribute it in accordance with the terms of the license. Despite its simplicity, BasicText does not compromise on performance and reliability. However, it is provided 'as is' without any warranty; users should note that they assume all responsibility for any necessary servicing, repair, or correction.

BasicText is written in python. The BasicText.py file can be run as a .py script or it can be made an executable. 

**To run it as a script:

```bash
cd /path/to/your/script/directory
python3 BasicText.py

```

**To make P"BasicText.py," an executable using PyInstaller, follow these step-by-step instructions, including commands:

**Step 1: Install PyInstaller (if not already installed)**

If you haven't already installed PyInstaller, you can do so using pip:

```bash
pip install pyinstaller
```

**Step 2: Navigate to the directory containing your script**

Open a terminal and change the directory to where your "BasicText.py" file is located. You can use the `cd` command to navigate to the directory.

```bash
cd /path/to/your/script/directory
```

**Step 3: Create the Executable**

Run the following command to create the executable:

```bash
pyinstaller --onefile --noconsole BasicText.py
```

- `--onefile`: This option bundles everything into a single executable file.
- `--noconsole`: This option is used to hide the console window when your app runs.

PyInstaller will now start the process of analyzing your script and its dependencies.

**Step 4: Locate the Executable**

Once PyInstaller completes the process, you can find the executable in the "dist" directory within your script's directory. The executable will have the same name as your script but without the ".py" extension. In this case, it will be named "BasicText."

**Step 5: Run the Executable**

You can now run the executable by executing it from the terminal:

```bash
./dist/BasicText
```

Or on Windows:

```bash
.\dist\BasicText.exe
```

asicText should now run as an executable without the need for a Python interpreter. Copy the binary from the ./dist/ folder and move them into your Applications/Programs folder and then make a shortcut as per your liking. 
