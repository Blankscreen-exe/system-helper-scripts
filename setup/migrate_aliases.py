import configparser
import os

def update_aliases(toml_file):
  """
  Parses a TOML file and updates the .bash_aliases file with the aliases.
  """

  # Check if the file exists
  if not os.path.exists(toml_file):
    print(f"Error: File '{toml_file}' does not exist.")
    return

  # Backup the existing .bash_aliases (optional)
  backup_file = os.path.expanduser("~/.bash_aliases.bak")
  try:
    os.rename(os.path.expanduser("~/.bash_aliases"), backup_file)
    print(f"Backed up existing aliases to '{backup_file}'.")
  except OSError:
    pass  # Ignore backup error if file doesn't exist

  # Temporary file to store new aliases
  tmp_aliases = "/tmp/aliases.tmp"

  # Clear the temporary file
  with open(tmp_aliases, "w") as f:
    f.write("")

  # Parse the TOML file
  config = configparser.ConfigParser()
  config.read(toml_file)

  for alias_name, alias_value in config.items("aliases"):
    # Check if alias name is valid
    if not alias_name:
      print(f"Warning: Empty alias name found in '{toml_file}'.")
      continue

    # Append alias to temporary file
    with open(tmp_aliases, "a") as f:
      f.write(f"alias {alias_name}='{alias_value}'\n")

  # Move temporary file to .bash_aliases (avoiding overwriting)
  new_aliases_file = os.path.expanduser("~/.bash_aliases.new")
  os.rename(tmp_aliases, new_aliases_file)

  # Check if there are any new aliases
  diff_output = os.popen(f"diff --unchanged-line-format='' ~/.bash_aliases {new_aliases_file}").read().strip()
  new_aliases_count = len(diff_output.splitlines())

  if new_aliases_count > 0:
    print(f"Updated ~/.bash_aliases with new aliases from '{toml_file}'.")
    os.rename(new_aliases_file, os.path.expanduser("~/.bash_aliases"))
  else:
    print(f"No new aliases found in '{toml_file}'.")
    os.remove(new_aliases_file)

if __name__ == "__main__":
  toml_file = input("Enter the path to your TOML file: ")
  update_aliases(toml_file)
