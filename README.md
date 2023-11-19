# Streamlit OCR - Converting Image to text

Sample Project Using Python, Streamlit, Pytesseract to Read Files by OCR

<p>
Thanks to the power of artificial intelligence, travel planning has never been easier.
</p>

<p>
In this post, we'll create a basic, but handy tool that leverages AI to generate travels suggestions based on your location and provide kind of places.
</p>

<p>
We'll create a Python application using streamlit, a popular library for creating interactive web applications. The app will incorporate features from the langchain library, which integrates OpenAI's language model capabilities, allowing us to generate text based on prompts.
</p>

<p>
Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required.
</p>

<p>
This repo contains templates and example code for creating [Streamlit](https://streamlit.io) Components.

For complete information, please see the [Streamlit Components documentation](https://docs.streamlit.io/en/latest/streamlit_components.html)!

</p>

## Quickstart

- Ensure you have [Python 3.10+](https://www.python.org/downloads/) installed.
- Clone this repo.
- Create a new Python virtual environment for the template:

```
$ cd template
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```

- Initialize and run the component template frontend:

```
$ cd template/my_component/frontend
$ npm install    # Install npm dependencies
$ npm run start  # Start the Webpack dev server
```

- From a separate terminal, run the template's Streamlit app:

```
$ cd template
$ . venv/bin/activate  # activate the venv you created earlier
$ pip install -e . # install template as editable package
$ streamlit run my_component/example.py  # run the example
```

- If all goes well, you should see something like this:
  ![Quickstart Success](quickstart.png)
- Modify the frontend code at `my_component/frontend/src/MyComponent.tsx`.
- Modify the Python code at `my_component/__init__.py`.

## Examples

See the `template-reactless` directory for a template that does not use [React](https://reactjs.org/).

See the `examples` directory for examples on working with pandas DataFrames, integrating with third-party libraries, and more.

<img src="https://github.com/teonett/Streamlit-Python-OCR/blob/main/Transcricao.png">

<h4>Copyright (C) 2023 Jose Teotonio (teonett@gmail.com)</h4>
<p>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>

</p>
