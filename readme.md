# very-simple-guestbook v0.1.0

A simple guestbook application built with Flask that allows users to post comments on their own website.

## Features
- User can post a comment
- Uses flatfile `guests.db` as a comment database

## Requirements
- Python 3.x
- Flask

## Installation
1. Download the code from Github.
2. Install the required dependencies using `pip install -r requirements.txt`
3. Edit the `guestbook.html` template and `main.css` style to match the style of your own website. (They are located under templates and static/style folders)
4. Ensure the `guests.db` file is writeable by the Flask application.
5. Run the Flask application to start the guestbook.

## Usage
1. Load the page where you integrated the code.
2. Fill in the form and submit to post a comment.

## Limitations
- Currently does not include anti-spam protection.

## Contributing
If you would like to contribute to this project, please submit a pull request.
