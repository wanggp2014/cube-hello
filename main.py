def greet(name: str) -> str:
    """生成问候语"""
    return f"Hello, {name}! Welcome to CubeHello."

def farewell(name: str) -> str:
    """生成告别语"""
    return f"Goodbye, {name}! See you next time."

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))