from functions.run_python_file import run_python_file
test_cases =[
    {
        "dir": "calculator",
        "file": "main.py",
    },
    {
        "dir": "calculator",
        "file": "main.py",
        "arg": ["3 + 5"],
    },
    {
        "dir": "calculator",
        "file": "tests.py",
    },
    {
        "dir": "calculator",
        "file": "../main.py",
    },
    {
        "dir": "calculator",
        "file": "nonexistent.py",
    },
    {
        "dir": "calculator",
        "file": "lorem.txt",
    }
]

for case in test_cases:
    arguments: list[str] | None = case.get("arg", None)
    result = run_python_file(case["dir"], case["file"], arguments)
    print(result)
