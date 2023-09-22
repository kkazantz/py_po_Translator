from googletrans import Translator

# Initialize the Translator
translator = Translator()

# Function to translate text to Greek
def translate_to_greek(text):
    try:
        translation = translator.translate(text, dest='el')
        return translation.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return str(e)

# Read the entire .po file
with open('wp-plugins-woo-gutenberg-products-block-stable-el.po', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# To hold the modified lines
modified_lines = []

# Flags to keep track of msgctxt, msgid, and msgstr lines
current_msgctxt = None
current_msgid = ""

for line in lines:
    # Remove trailing spaces and newlines
    line = line.rstrip()

    # Identify msgctxt lines
    if line.startswith("msgctxt"):
        current_msgctxt = line
        
    # Identify msgid lines
    elif line.startswith("msgid"):
        current_msgid = line.split('"')[1]
        
    # Identify msgstr lines and translate msgid
    elif line.startswith("msgstr") and line == 'msgstr ""':
        translated_text = translate_to_greek(current_msgid)
        line = f'msgstr "{translated_text}"'

        # If msgctxt exists, include it in the modified lines
        if current_msgctxt:
            modified_lines.append(current_msgctxt)
            current_msgctxt = None  # Reset msgctxt

    # Add the (possibly modified) line to the new list
    modified_lines.append(line)

# Join the modified lines into a single string
modified_content = "\n".join(modified_lines)

# Write the modified content to a new .po file
with open('wp-plugins-woo-gutenberg-products-block-stable-el-updated.po', 'w', encoding='utf-8') as file:
    file.write(modified_content)
