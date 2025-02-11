![R](https://github.com/user-attachments/assets/24613d53-7778-48b9-a169-c8b65dbae9c5)
# Bankai Interpreter 🌮🔥

A custom Python-based interpreter that allows executing `.bankai` scripts with custom keywords. **Developed by lmcteam206.**

## 📌 Features
- Custom keywords mapped to Python built-ins.
- Supports `.bankai` script execution.
- Interactive interpreter with **multiline input**.
- **Syntax highlighting** with colors.
- **Script history saving** and viewing.
- **Custom file extension support**.
- **Excel-based keyword customization**.
- 

## 🛠 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/lmcteam206/Bankai-interpreter.git
   cd bankai-interpreter
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage
### **Run the Interpreter**
```sh
python main.py
```

### **Commands**
| Command       | Description                          |
|--------------|----------------------------------|
| `.exit`     | Exit the interpreter              |
| `.help`     | Show available commands           |
| `.view`     | View custom words in Excel        |
| `.script`   | Run a `.bankai` script            |
| `.reload`   | Reload keywords from Excel        |
| `.create`   | Generate a new custom words file  |
| `.history`  | View executed commands history    |
| `.ext`      | Change allowed script extension   |

### **Execute a `.bankai` Script**
```sh
.bankai> .script my_script.bankai
```

## 🔧 Customization
You can modify `customs.xlsx` to change the mappings of Python functions to custom names.

## 📚 License
This project is licensed under the MIT License.

