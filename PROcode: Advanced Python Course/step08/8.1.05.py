import json

def solve():
    try:
        line1 = input().strip()
        decryption_dict = json.loads(line1)
        
        line2 = input().strip()
        encrypted_passwords = line2.split()
        
        garbage_chars = "*#@!$"
        
        results = []
        
        for item in encrypted_passwords:
            clean_hash = ""
            for char in item:
                if char not in garbage_chars:
                    clean_hash += char
            
            if clean_hash in decryption_dict:
                results.append(decryption_dict[clean_hash])
            else:
                results.append("Не удалось расшифровать пароль")
        
        print(" ".join(results))
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
