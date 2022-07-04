import website


if __name__ == "__main__":
    app = website.create_app()
    app.run("127.0.0.1", debug=True)