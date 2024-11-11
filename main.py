        from flask import Flask, request
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        app = Flask(__name__)
        engine = create_engine('your_database_connection_string')
        Session = sessionmaker(bind=engine)

        @app.route('/cakes', methods=['POST'])
        def create_cake():
            session = Session()
            data = request.get_json()

            name = data.get('name')
            description = data.get('description')
            weight = data.get('weight')

            cake = Cake(name=name, description=description, weight=weight)
            session.add(cake)
            session.commit()

            return 'Cake created successfully', 201

        if __name__ == '__main__':
            app.run()
