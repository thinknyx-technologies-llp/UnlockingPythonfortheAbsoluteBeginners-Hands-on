input_file_path = 'input_file.txt'
output_file_path = "output_file.txt"

initial_message = "This is the initial content written to the input file."

try:
    with open(input_file_path, 'w+') as file:
        file.write(initial_message)
        file.seek(0)
        read_content = file.read()
        print("Successfully wrote and read content from the input file: ")
        print(read_content)
except IOError as e:
    print(f"An error occured while handling {input_file_path}: {e}")

new_message = "This is a new message written to the output file."

try:
    with open(input_file_path, 'r+') as input_file:
        content = input_file.read()
        print("Successfully read content from the input file: ")
        print(content)
        input_file.seek(0)
        input_file.write("Updated content in the input file.\n")
        print("Successfully updated content in the input file.")
        

        with open(output_file_path, 'w+') as output_file:
            output_file.write(new_message)
            output_file.seek(0)
            written_content = output_file.read()
            print("Successfully wrote and read content from the output file: ")
            print(written_content)

except FileNotFoundError as e:
    print(f"File not found error: {e}")
except IOError as e:
    print(f"An error occured while handling files: {e}")