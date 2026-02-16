#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Args:
        text: must be a string
    
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Karakterleri bul ve işaretle
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            # Sonraki boşlukları atla
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    
    # Fazla boşlukları temizle ve yazdır
    lines = result.split("\n")
    for j, line in enumerate(lines):
        if j > 0 and line == "" and lines[j-1] == "":
            continue
        print(line.strip() if line else "", end="")
        if j < len(lines) - 1:
            print()

# Alternatif daha temiz çözüm:
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Noktalama işaretlerinden sonra iki yeni satır ekle
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    
    # Satırları ayır ve her satırdaki baştaki/sondaki boşlukları temizle
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "":
            if i > 0 and lines[i-1].strip() == "":
                continue
            print()
        else:
            print(line.strip())
