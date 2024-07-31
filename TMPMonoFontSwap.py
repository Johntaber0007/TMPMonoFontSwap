import json
from tkinter import Tk, filedialog, messagebox
import os

def select_file(prompt):
    root = Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(title=prompt, filetypes=[("JSON files", "*.json")])
    if not file_path:
        raise FileNotFoundError(f"No file selected for {prompt}")
    return file_path

def save_file(prompt):
    root = Tk()
    root.withdraw() 
    file_path = filedialog.asksaveasfilename(defaultextension=".json", title=prompt, filetypes=[("JSON files", "*.json")])
    if not file_path:
        raise FileNotFoundError("No file selected to save the new JSON file")
    return file_path

def replace_path_id(dict1, dict2):
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        for key in dict1.keys():
            if key in dict2:
                if key == 'm_PathID':
                    dict1[key] = dict2[key]
                else:
                    replace_path_id(dict1[key], dict2[key])
    elif isinstance(dict1, list) and isinstance(dict2, list):
        for item1, item2 in zip(dict1, dict2):
            replace_path_id(item1, item2)

def show_popup(message, title="Notification"):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

def main():
    print("Welcome to the JSON Font Processor")
    
    try:
        print("Please select the font JSON file (File 1).")
        file1_path = select_file("Select your Font MonoBehaviour JSON File")

        with open(file1_path, 'r', encoding='utf-8') as file:
            json1 = json.load(file)

        print("Please select the game font JSON file (File 2).")
        file2_path = select_file("Select the Original Font MonoBehaviour JSON File")

        with open(file2_path, 'r', encoding='utf-8') as file:
            json2 = json.load(file)

        if 'm_Name' in json2:
            json1['m_Name'] = json2['m_Name']

        replace_path_id(json1, json2)

        if 'm_FaceInfo' in json2:
            json1['m_FaceInfo'] = json2['m_FaceInfo']

        print("Please choose where to save the new JSON file.")
        output_file_path = save_file("Save the Font MonoBehaviour JSON File as")

        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(json1, file, ensure_ascii=False, indent=4)

        show_popup("Finish")

    except FileNotFoundError as e:
        show_popup(str(e), "Error")
    except Exception as e:
        show_popup(f"An error occurred: {e}", "Error")

if __name__ == "__main__":
    main()
