from functions.get_file_content import get_file_content

test_cases = [
{
    "dir": "calculator",
    "file": "lorem.txt"
},
{
    "dir": "calculator",
    "file": "main.py"
},
{
    "dir": "calculator",
    "file": "pkg/calculator.py"
},
{
    "dir": "calculator",
    "file": "/bin/cat"
},
{
    "dir": "calculator",
    "file": "pkg/does_not_exist.py"
}

]

for case in test_cases:
    result = get_file_content(case["dir"],case["file"])
    if "truncated at" in result:
        print(f"{case["file"]} length: {len(result)}")
        print(f"{case["file"]} truncated: {'truncated' in result}")
    else:
        print(result)
