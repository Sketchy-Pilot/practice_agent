from functions.write_file import write_file
test_cases = [
    {
        "dir": "calculator",
        "file": "lorem.txt",
        "content": "wait, this isn't lorem ipsum",
    },
    {
        "dir": "calculator",
        "file": "pkg/morelorem.txt",
        "content": "lorem ipsum dolor sit amet",
    },
    {
        "dir": "calculator",
        "file": "/tmp/temp.txt",
        "content": "this should not be allowed",
    }
]

for case in test_cases:
    result = write_file(case["dir"], case["file"], case["content"])
    print(result)
