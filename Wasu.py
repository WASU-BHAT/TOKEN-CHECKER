from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝑷𝑹𝑰𝑵𝑪𝑬-𝑻𝑶𝑲𝑬𝑵-𝑪𝑯𝑬𝑨𝑲𝑬𝑹</title>
    <style>
        /* CSS for styling elements */
        .error {
            color: red;
            font-weight: italic;
        }
        h1{
            text-align: center;
            border: double 2px white;
            font-family: cursive;
            font-size: 25px;
        }
        .btn, input {
            height: 33px;
            width: 100%;
            margin-top: 20px;
            background-color: blue;
            border: double 2px white;
            color: white;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            box-sizing: border-box;
        }
        input {
            outline: green;
            border: double 2px white;
            padding: 10px;
            background-color: black;
            color: white;
        }
        h2{
            text-align: center;
            font-size: 15px;
            border-radius: 20px;
            color: white;
            background-color: black;
            border: double 2px white;
        }
        label{
            color: white;
        }
        body{
            background-image: url('https://i.ibb.co/sWrxFqn/2c3896ef289c07f31387973c3d6acb7d.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            color: white;
            height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            max-width: 350px;
            width: 100%;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
            box-shadow: 0 0 15px white;
            border: double 2px white;
            resize: none;
            background: rgba(0, 0, 0, 0.5);
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗧⃪𝗢⃪𝗞⃪𝗘⃪𝗡⃪ 𝗖⃪𝗛⃪𝗘⃪𝗖⃪𝗞⃪𝗘⃪𝗥⃪</h1>
    <form method="post">
        <input type="text" name="access_token" placeholder="𝐁𝐒𝐃𝐊-𝐓𝐎𝐊𝐄𝐍-𝐃𝐀𝐀𝐋
" required>
        <button class="btn" type="submit">𝗕⃪𝗦⃪𝗗⃪𝗞⃪ 𝗧⃪𝗢⃪𝗞⃪𝗘⃪𝗡⃪ 𝗖⃪𝗛⃪𝗘⃪𝗖⃪𝗞⃪ 𝗞⃪𝗔⃪𝗥⃪
</button>
    </form>
    
    {% if result %}
        <h2 style="color: {{ color }};">{{ result }}</h2>
    {% endif %}
    
    <footer>
        <h2>𝗕⃪𝗔⃪𝗗⃪𝗠⃪𝗔⃪𝗦⃪𝗛⃪𝗢⃪ 𝗞⃪𝗔⃪ 𝗕⃪𝗔⃪𝗔⃪𝗣⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗜⃪𝗡⃪𝗫⃪𝗜⃪𝗗⃪𝗘⃪</h2>
    </footer>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    color = "white"
    
    if request.method == "POST":
        access_token = request.form.get("access_token")
        url = f"https://graph.facebook.com/me?access_token={access_token}"

        try:
            response = requests.get(url).json()
            
            if "id" in response:
                result = f"Valid Token ✅ - User: {response['name']} (ID: {response['id']})"
                color = "green"
            else:
                result = "Invalid Token ❌"
                color = "red"
        except:
            result = "Error Checking Token ❌"
            color = "red"

    return render_template_string(html_template, result=result, color=color)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
