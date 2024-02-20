from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for content recommendation
content_data = {
    '1': {'title': 'Content 1', 'genre': 'Action', 'rating': 4.5},
    '2': {'title': 'Content 2', 'genre': 'Comedy', 'rating': 3.8},
    '3': {'title': 'Content 3', 'genre': 'Drama', 'rating': 4.2},
    # Add more content items as needed
}

# Dummy user preferences
user_preferences = {
    'user1': ['Action', 'Drama'],
    'user2': ['Comedy'],
    # Add more users and their preferences
}

@app.route('/')
def index():
    return render_template('index.html', content=content_data)

@app.route('/recommendations/<username>')
def get_recommendations(username):
    user_pref = user_preferences.get(username, [])

    recommendations = []

    # Simple content-based recommendation: Recommend content with matching genre
    for content_id, content in content_data.items():
        if content['genre'] in user_pref:
            recommendations.append(content)

    return render_template('recommendations.html', username=username, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
