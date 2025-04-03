import base64

def main():
    input_string = input("Nhap thong tin ma hoa: ")
    
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    print("Thong tin da duoc ma hoa: ", encoded_string)
    
    with open("data.txt", "w") as file:
        file.write(encoded_string)
        
    print("da ma hoa va ghi vao tet data.txt")
    
if __name__ == "__main__":
    main()