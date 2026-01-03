from functools import wraps

from flask import (
    Flask,
    render_template,
    abort,
    request,
    redirect,
    url_for,
    session,
)

from storage import list_articles, get_article, create_article, update_article, delete_article

app = Flask(__name__)

app.secret_key = "change-this-to-a-random-string"

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)

    return wrapped_view


# ---------- Admin routes ----------

@app.route("/admin")
@login_required
def admin_dashboard():
    articles = list_articles()
    return render_template("dashboard.html", articles=articles)


@app.route("/admin/articles/new", methods=["GET", "POST"])
@login_required
def add_article():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        published = request.form.get("published", "").strip()

        if not title or not content or not published:
            error = "All fields are required."
            return render_template(
                "article_form.html",
                page_title="Add Article",
                heading="Add Article",
                submit_label="Create",
                article=None,
                error=error,
            )

        article_id = create_article(title, content, published)
        return redirect(url_for("admin_dashboard"))

    # GET request
    return render_template(
        "article_form.html",
        page_title="Add Article",
        heading="Add Article",
        submit_label="Create",
        article=None,
        error=None,
    )

@app.route("/admin/articles/<article_id>/edit", methods=["GET", "POST"])
@login_required
def edit_article(article_id):
    article = get_article(article_id)
    if article is None:
        abort(404)

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        published = request.form.get("published", "").strip()

        if not title or not content or not published:
            error = "All fields are required."
            return render_template(
                "article_form.html",
                page_title="Edit Article",
                heading="Edit Article",
                submit_label="Save changes",
                article=article,
                error=error,
            )

        update_article(article_id, title, content, published)
        return redirect(url_for("admin_dashboard"))

    # GET request
    return render_template(
        "article_form.html",
        page_title="Edit Article",
        heading="Edit Article",
        submit_label="Save changes",
        article=article,
        error=None,
    )

@app.route("/admin/articles/<article_id>/delete", methods=["POST"])
@login_required
def delete_article_route(article_id):
    delete_article(article_id)
    return redirect(url_for("admin_dashboard"))


# ---------- Public routes ----------

@app.route("/")
def home():
    articles = list_articles()
    return render_template("home.html", articles=articles)


@app.route("/article/<article_id>")
def article_detail(article_id):
    article = get_article(article_id)
    if article is None:
        abort(404)
    return render_template("article.html", article=article)


# ---------- Auth routes ----------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # use .get(...) so missing fields don’t crash
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["is_admin"] = True
            return redirect(url_for("admin_dashboard"))
        else:
            error = "Invalid username or password"
            return render_template("login.html", error=error)

    # GET request
    return render_template("login.html", error=None)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
