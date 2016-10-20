"""
This is the internal help system of wallabag-cli.
"""


def show(startscript, command="main"):
    if command == "":
        command = "main"

    index = dict()

    # General help
    main_txt = """
Usage:
  {0} <command> [options]

Commands:
  config         Start the configuration.
  add            Add a new link to wallabag.

General Options:
  -h, --help     Show help.
  --about        Show about information.
  -v, --version  Show version No.

Use \"{0} <command> --help\" for further information.
And don't forget to be excellent to each other!
""".format(startscript)
    index['main'] = main_txt

    # config
    config_txt = """
Usage:
  {0} config [options]

Description:
  Start the configuration.

Options:
  -h, --help  Show help
""".format(startscript)
    index['config'] = config_txt

    # config
    add_txt = """
Usage:
  {0} add [options] <url>

Description:
  Add a new link to wallabag.

Options:
  -h, --help  Show help
""".format(startscript)
    index['add'] = add_txt

    if not command in index:
        print("Error: Invalid command \"{0}\"!".format(command))
        command = "main"

    print(index[command])
