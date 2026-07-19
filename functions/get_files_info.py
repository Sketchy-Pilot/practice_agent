import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir) is False:
            return f'Error: "{target_dir}" is not a directory'
        dir_list: list[str] = os.listdir(target_dir)
        output = f"Result for '{directory}' directory:"
        output = output.replace("'.'", "current")
        for i in range(0,len(dir_list)):
            target = os.path.normpath(os.path.join(target_dir,dir_list[i]))
            output += f"\n  - {dir_list[i]}: file_size={os.path.getsize(target)} bytes, is_dir={os.path.isdir(target)}"
        return output
    except Exception as e:
        return f'Error: {e}'
