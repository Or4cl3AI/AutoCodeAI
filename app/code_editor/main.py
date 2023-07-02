import sys

def run_code(code):
    try:
        exec(code)
    except Exception as e:
        sys.stderr.write(str(e))

if __name__ == '__main__':
    code = input("Enter your code: ")
    run_code(code)