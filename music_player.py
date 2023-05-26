from client.app import App
from model.admin_db import Admin


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    Admin()
    main()
