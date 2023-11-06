# **Project Description**

## **TechTalk: Ignite Conversations, Amplify Ideas.** <br>

![image](TechTalkBanner.png)


## **What is it ?**
**TechTalk** Blog App is an intuitive and user-friendly web application created with Flask, aimed at enhancing your blogging experience. Whether you're a professional tech enthusiast or just getting started, **TechTalk** empowers you to effortlessly create, update, and manage your posts. The app provides a secure user authentication system, ensuring a personalized and trustworthy blogging journey.

With its sleek and responsive design, **TechTalk** adapts seamlessly to various devices, allowing users to share their thoughts on technology with the world. Let's unite on TechTalk, a platform that encourages the free expression of ideas and strengthens the core principle of freedom of speech. Join us as we build a community where tech discussions thrive and diverse voices are celebrated.

---------------------------
---------------------------

## **Table of Contents**

- [Project Architecture](#architecture)
- [Features](#features)
- [Getting Started](#getting-started)
   - [Window Users](#windows)
   - [macOS Users](#macOS)
   - [Linux Users](#linux)
- [Usage](#usage)
    + [Name Patterns](#name-patterns)
    + [Star Patterns](#star-patterns)
      * [Pyramid](#pyramid)
      * [Triangle](#triangle)
      * [Diamond](#diamond)
    + [Number Patterns](#number-patterns)
      * [Pascal's Triangle](#pascal)
      * [Triangle1](#triangle1)
      * [Triangle2](#triangle2)
      * [Pyramid1](#pyramid1)
    + [Alphabet Patterns](#alphabet-patterns)
      * [Triangle](#alpha-triangle)
      * [Pyramid1](#alpha-pyramid1)
      * [Pyramid2](#alpha-pyramid2)
   + [Pattern Code](#pattern-code)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)


------------------------------
------------------------------

## **Project Architecture** <a name = 'architecture'></a>

```
WORKSPACE
    |
    |--> TechTalk
    |        |
    |        |--> instance
    |        |         |
    |        |         |--> blog.db
    |        |
    |        |--> static
    |        |         |
    |        |         |--> profile_images
    |        |         |        |
    |        |         |        |--> ....
    |        |         |
    |        |         |--> basic.css
    |        |
    |        |--> templates
    |        |         |
    |        |         |--> about.html
    |        |         |
    |        |         |--> basic.html
    |        |         |
    |        |         |--> create_post.html
    |        |         |
    |        |         |--> index.html
    |        |         |
    |        |         |--> login.html
    |        |         |
    |        |         |--> post.html
    |        |         |
    |        |         |--> profile.html
    |        |         |
    |        |         |--> register.html
    |        |         |
    |        |         |--> user_posts.html
    |        |
    |        |--> __init__.py
    |        |
    |        |--> forms.py
    |        |
    |        |--> models.py
    |        |
    |        |--> routes.py
    |   
    |
    |--> .gitignore
    |
    |--> LICENSE
    |
    |--> TechTalkBanner.png
    |
    |--> README.md
    |
    |--> requirements.txt
    |
    |--> app.py
```

---------------------------
---------------------------

# **Key Features** <a name="features"></a>

## **User Authentication:** 
Securely register an account, log in, and manage your profile with ease. **TechTalk** Blog App provides a secure user authentication system, allowing you to manage your account with confidence. Register an account, log in securely, and explore the full range of features available to you.

## **Effortless Blogging:** 
Create, update, and delete your posts effortlessly through a clean and intuitive interface.Manage your blog content effortlessly with TechTalk's CRUD operations. Create new posts, update existing ones, and remove posts you no longer need. The intuitive interface ensures a hassle-free content management experience.

## **Project Structure** 
**TechTalk** follows a well-organized project structure, making it easy for developers to understand and contribute to the project. The codebase is clean and modular, with separate components for models, forms, and the main application logic.

## **User-Friendly Interface:** 
**TechTalk** is designed with simplicity in mind, ensuring a smooth and enjoyable user experience.

## **Responsive Design:** 
Access your blog on any device with our responsive design, ensuring a seamless experience on desktops, tablets, and smartphones.


---------------------------
---------------------------

# **Getting Started** <a name="getting-started"></a>

- **Python:**
 Make sure you have Python installed on your machine. This application is developed using Python 3.7 and above. You can download Python from [python.org](https://www.python.org/downloads/).

```python
# Check Python version
python --version
```

- **Virtual Environment (optional but recommended):**
It is good practice to use a virtual environment to manage dependencies for your project.

```python
# Install virtualenv using pip
pip install virtualenv
```

- **Dependencies:**
Install project dependencies using the provided requirements.txt file.


```python
# Inside the project directory
pip install -r requirements.txt
```

- **Database Setup:** 
This application uses SQLAlchemy as the default database. To use it you need to install it first using pip command or it will be installed in your venv if you run ```pip install -r requirements.txt```

```python
# Install SQLAlcemy using pip
pip install SQLAlchemy
```

- **Running the Application:** 
Execute the following command to run the Flask application.

```python
# Install SQLAlcemy using pip
python app.py
```

- **Optional Configuration**
  + **Web Server:** For production deployment, consider using a production-ready web server (e.g., Nginx or Apache) in conjunction with a WSGI server (e.g., Gunicorn).

  + **Database Configuration:** If you prefer using a different database, update the database URL install the corresponding database driver.

  + **Additional Dependencies:** Depending on your needs, you may want to install additional dependencies for features like authentication, forms, etc.


---------------------------
---------------------------


# **Contributing** <a name = 'contributing'></a>

Contributions to the **TechTalk** package are welcome! Whether you've found a bug, have suggestions for improvements, or want to add new features, your contributions can make this package even better.

## **How to Contribute**

1. **Open an Issue:** If you come across a bug or have an idea for an improvement, start by opening an issue on the [GitHub repository](https://github.com/Saqibs575/techtalk/issues). Provide as much detail as possible about the issue or suggestion.

2. **Fork the Repository:** If you plan to work on a fix or enhancement, fork the repository by clicking the "Fork" button on the top right of the repository page.

3. **Clone the Fork:** Clone your forked repository to your local machine using the following command, replacing `<your-username>` with your GitHub username:

```sh
git clone https://github.com/<your-username>/techtalk.git
```

## **Create a Branch**:
Before making changes, create a new branch to work on. This helps keep your changes isolated from the main codebase. Use a descriptive branch name related to the feature or bug you're addressing:

```sh
git checkout -b feature/my-new-feature
```

## **Make Changes**: 
Write your code and make the necessary changes. Follow any coding style guidelines and keep the changes focused on a single issue or feature.

## **Test Your Changes**: 
Before submitting a pull request, make sure your changes work as intended and do not introduce new issues. Run tests if available and perform manual testing if needed.

## **Commit and Push**: 
Commit your changes and push them to your forked repository:

```python
git commit -m "Add a descriptive commit message"
git push origin feature/my-new-feature
```

## **Submit a Pull Request**: 
Go to the [original repository](https://github.com/Saqibs575/techtalk) and click the "New Pull Request" button. Select your branch and provide a detailed description of your changes. A team member will review your pull request and provide feedback.

-------------------------------------
-------------------------------------


# **License** <a name = 'license'></a>

**Copyright &copy; 2023 Saqib Shaikh**

This software package, named "**TechTalk**," is distributed under the terms of the GNU General Public License version 3.0 (GPLv3). This license grants you the freedom to use, modify, and distribute this software according to the conditions set forth in the license text.

### License Summary

The GNU General Public License v3.0 (GPLv3) is an open-source license that ensures software remains free and open for all users. It provides the following key permissions and restrictions:

- **Permissions:** You are free to use, share, and modify the software.
- **Copyleft:** Any modified versions of the software must also be distributed under the GPLv3 license terms.
- **Distribution:** If you distribute the software, you must include the source code or a written offer to provide it.
- **Patents:** The license explicitly deals with patents, ensuring users can use the software without concerns about potential patent claims.

### License Text

For the full text of the GNU General Public License v3.0 (GPLv3), please refer to the [LICENSE](https://github.com/Saqibs575/techtalk/blob/main/LICENSE) file located in the repository. This license outlines the complete terms and conditions that apply to this software.

It's important to carefully read and understand the license terms before using or distributing this software.

For any questions or inquiries regarding the license, please contact Saqib Shaikh at saquibs575@gmail.com.


-------------------------------------
-------------------------------------

# **Acknowledgments** <a name="acknowledgements">
This project wouldn't have been possible without the guidance, tutorials, and resources provided by the following individuals and organizations:

- **Corey Schafer (@coreyms):** A big thank you to Corey Schafer for his excellent tutorial on building a blog app with Flask. The tutorial served as a valuable learning resource and provided insights into creating a robust Flask application. You can find the tutorial [here](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).

- **Bootstrap:** The frontend of this blog app is powered by Bootstrap, a free and open-source CSS framework. Bootstrap made it easy to create a responsive and visually appealing user interface. [Visit Bootstrap's official website](https://getbootstrap.com/docs/5.3/getting-started/introduction/) for more information.

- **Flask:** The web framework used for building this blog app is Flask. Flask's simplicity and flexibility were instrumental in the development process. Learn more about Flask at [Flask's official website](https://flask.palletsprojects.com/en/3.0.x/).




