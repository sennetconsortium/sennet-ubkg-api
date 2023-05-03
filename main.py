from ubkg_api.app import app


@app.route('/sennet', methods=['GET'])
def sennet():
    return "Hello from the SenNet UBKG-API :)"


def main():
    app.run(debug=True, port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()