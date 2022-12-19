from app import create_app

# 访问 127.0.0.1:9521/todolist

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9521)
