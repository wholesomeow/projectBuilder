# TODO(wholesomeow): Populate preflight_data.choices with a list generated from ../data/templates/<language>/*.json excluding ../data/templates/_generic

def validate_directory_symbols(target_path, current_directory):
    up_dir_count = 0
    split_target_path = target_path.split('/')
    new_path = []

    for item in split_target_path:
      if item == '.':
        return current_directory
      elif item == '..':
        up_dir_count += 1
      else:
         new_path.append(item)

    final_target = '/'.join(new_path)

    split_dir = current_directory.split('/')
    for count in range(up_dir_count):
       split_dir.pop()

    join_dir = '/'.join(split_dir)
    final_dir = f'{join_dir}/{final_target}'

    return final_dir