def generate_greeting(first_name, last_name):
    if len(first_name) <= 10 and len(last_name) <= 10:
        greeting = f"Hello {first_name} {last_name}! You just developed into python."
        return greeting
    else:
        return "Error: First and last names must be 10 characters or less."
def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    greeting_message = generate_greeting(first_name, last_name)
    print("Greeting Message:")
    print(greeting_message)
if __name__ == "__main__":
    main()

