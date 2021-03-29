import subprocess
from settings import get_psql_on_path


def main():
    # psqlをターミナルで開く
    subprocess.run(get_psql_on_path(), shell=True)


if __name__ == "__main__":
    main()
