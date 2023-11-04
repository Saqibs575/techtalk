import os
import secrets
from blog import db
from blog import app
from blog import bcrypt
from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from blog.models import User
from blog.models import Post
from blog.forms import PostForm
from blog.forms import LoginForm
from flask import render_template
from flask_login import login_user
from flask_login import logout_user
from flask.views import MethodView
from flask_login import current_user
from flask_login import login_required
from blog.forms import RegistrationForm
from blog.forms import UpdateProfileForm
from blog.forms import UpdateProfileImageForm

def save_profile(profile_image) :
    random_hex = secrets.token_hex(8)
    _, file_extension = os.path.splitext(profile_image.filename)
    image_path = os.path.join(app.root_path, "static", "profile_images", random_hex+file_extension)
    profile_image.save(image_path)
    return random_hex+file_extension

class Home(MethodView) :
    def get(self) :
        form=PostForm()
        posts = Post.query.all()
        if current_user.is_authenticated :
            return render_template("index.html", title="Home", posts=posts, form=form)
        return render_template("index.html", title="Home", posts=posts, form=form)

class About(MethodView) :
    def get(self) :
        if current_user.is_authenticated :
            return render_template("index.html", title="Home")
        return render_template("index.html", title="Home")

class Register(MethodView) :
    def get(self) :
        if current_user.is_authenticated :
            return redirect(url_for("home"))
        form = RegistrationForm()
        return render_template("register.html", title="Register", form=form)
    def post(self) :
        form = RegistrationForm()
        if form.validate_on_submit() :
            password_hashed = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(
                            username=form.username.data,
                            email=form.email.data,
                            password=password_hashed
                        )
            db.session.add(user)
            db.session.commit()
            flash(f"Account Creatd Successfully for { form.username.data }", "success")
            return redirect(url_for("home"))
        return render_template("register.html", title="Register", form=form)

class Login(MethodView) :
    def get(self) :
        if current_user.is_authenticated :
            return redirect(url_for("home"))
        form = LoginForm()
        return render_template("login.html", title="Login", form=form)
    def post(self) :
        form = LoginForm()
        if form.validate_on_submit() :
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data) :
                login_user(user, remember=form.remember.data)
                next_page = request.args.get("next")
                flash("Login successful. Welocme to blog app.", "success")
                return redirect(next_page) if next_page else redirect(url_for("home"))
            else :
                flash("Login Failed. Please check Your Email and Password", "danger")
        return render_template("login.html", title="Login", form=form)

class Logout(MethodView) :
    def get(self) :
        logout_user()
        return redirect(url_for("home"))

class Profile(MethodView) :
    decorators = [login_required]
    def get(self) :
        form = UpdateProfileForm()
        return render_template("profile.html", title="Profile", form=form)
    def post(self, id):
        return redirect(url_for("profile"))

class UpdateProfile(MethodView) :
    decorators = [login_required]
    def post(self):
        form = UpdateProfileForm()
        if form.validate_on_submit() :
            current_user.username = form.username.data; current_user.email = form.email.data
            db.session.commit()
            flash("Profile Updated Successfully", "success")
            return redirect(url_for("profile"))
        flash("Profile Update Failed. username & email should be unique and Valid", "danger")
        return redirect(url_for("profile"))

class UpdateProfileImage(MethodView) :
    decorators=[login_required]
    def post(self) :
        form = UpdateProfileImageForm()
        if form.validate_on_submit() :
            image_file = save_profile(form.profile_pic.data)
            current_user.profile_image = image_file
            db.session.commit()
            flash("Profile Image Updated Successfully", "success")
            return redirect(url_for("profile"))
        flash("Failed to Update Profile Image. Only .jpg, .jpeg and .png files are allowed", "danger")
        return redirect(url_for("profile"))

class NewPost(MethodView) :
    decorators=[login_required]
    def get(self) :
        form = PostForm()
        return render_template("create_post.html", title="New Post", form=form)
    def post(self) :
        form = PostForm()
        try :
            if form.validate_on_submit() :
                post = Post(title=form.title.data, content=form.content.data, author=current_user)
                db.session.add(post)
                db.session.commit()
                flash("Your Post has been Updated", "success")
                return redirect(url_for("home"))
        except :
            db.session.rollback()
        flash("All Posts Must be Unique", "danger")
        return redirect(url_for("new_post"))

class Posts(MethodView) :
    decorators=[login_required]
    def get(self, id) :
        post = Post.query.get_or_404(id)
        return render_template("post.html", title=post.title, post=post)

class UpdatePosts(MethodView) :
    decorators=[login_required]
    def post(self, id) :
        form = PostForm()
        post = Post.query.get_or_404(id)
        if post.author != current_user :
            flash("You are NOT allowed to update others posts", "danger")
            return redirect(url_for('home'))
        try :
            if form.validate_on_submit() :
                post.title = form.title.data; post.content = form.content.data
                db.session.commit()
                flash("Your Post has been Updated.", "success")
                return redirect(url_for("posts", id=id))
        except :
            db.session.rollback()
        flash("Duplicate Posts are NOT allowed", "danger")
        return redirect(url_for("posts", id=id))

class DeletePosts(MethodView) :
    decorators=[login_required]
    def post(self, id) :
        form = PostForm()
        post = Post.query.get_or_404(id)
        if post.author != current_user :
            flash("You are NOT allowed to delete others posts", "danger")
            return redirect(url_for('home'))
        try :
            if form.validate_on_submit() :
                db.session.delete(post)
                db.session.commit()
                flash("Your Post has been Deleted.", "warning")
                return redirect(url_for("home"))
        except :
            db.session.rollback()
        flash("Duplicate Posts are NOT allowed", "danger")
        return redirect(url_for("posts", id=id))

app.add_url_rule("/", view_func=Home.as_view("home"))
app.add_url_rule("/about", view_func=About.as_view("about"))
app.add_url_rule("/login", view_func=Login.as_view("login"))
app.add_url_rule("/logout", view_func=Logout.as_view("logout"))
app.add_url_rule("/profile", view_func=Profile.as_view("profile"))
app.add_url_rule("/register", view_func=Register.as_view("register"))
app.add_url_rule("/post/<int:id>", view_func=Posts.as_view("posts"))
app.add_url_rule("/post/<int:id>/update", view_func=UpdatePosts.as_view("update_posts"))
app.add_url_rule("/post/<int:id>/delete", view_func=DeletePosts.as_view("delete_posts"))
app.add_url_rule("/post/new", view_func=NewPost.as_view("new_post"))
app.add_url_rule("/update-profile", view_func=UpdateProfile.as_view("update_profile"))
app.add_url_rule("/update-profile-image", view_func=UpdateProfileImage.as_view("update_profile_image"))