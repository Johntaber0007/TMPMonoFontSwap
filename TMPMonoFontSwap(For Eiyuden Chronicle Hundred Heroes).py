import json
from tkinter import Tk, filedialog, messagebox

def select_file(prompt):
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title=prompt, filetypes=[("JSON files", "*.json")])
    return file_path

def show_popup(message, title="Notification"):
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()

def main():
    try:
        file1_path = select_file("Select the Original Font MonoBehaviour JSON File")
        if not file1_path:
            raise FileNotFoundError("No file selected for the game font monobehaviour JSON file")
        
        with open(file1_path, 'r', encoding='utf-8') as file:
            json1 = json.load(file)

        file2_path = select_file("Select your Font MonoBehaviour JSON File")
        if not file2_path:
            raise FileNotFoundError("No file selected for your font monobehaviour JSON file")
        
        with open(file2_path, 'r', encoding='utf-8') as file:
            json2 = json.load(file)

        m_FamilyName = json1['m_FaceInfo']['m_FamilyName']
        m_StyleName = json1['m_FaceInfo']['m_StyleName']

        for key in json1['m_FaceInfo']:
            if key not in ['m_FamilyName', 'm_StyleName']:
                json1['m_FaceInfo'][key] = json2['m_FaceInfo'].get(key, json1['m_FaceInfo'][key])

        json1['m_GlyphTable'] = json2['m_GlyphTable']
        json1['m_CharacterTable'] = json2['m_CharacterTable']

        json1['m_FaceInfo']['m_FamilyName'] = m_FamilyName
        json1['m_FaceInfo']['m_StyleName'] = m_StyleName

        output_file_path = filedialog.asksaveasfilename(defaultextension=".json", title="Save the Font MonoBehaviour JSON File as", filetypes=[("JSON files", "*.json")])
        if not output_file_path:
            raise FileNotFoundError("No file selected to save the font monobehaviour JSON file")

        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(json1, file, ensure_ascii=False, indent=4)

        show_popup("Finish")

    except FileNotFoundError as e:
        show_popup(str(e), "Error")
    except Exception as e:
        show_popup(f"An error occurred: {e}", "Error")

if __name__ == "__main__":
    main()
