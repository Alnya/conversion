import subprocess


def main():
    # psqlをターミナルで開く
    subprocess.run("\"c:\\program files\\postgresql\\11\\bin\\psql.exe\" -U postgres -d shop", shell=True)


if __name__ == "__main__":
    main()
