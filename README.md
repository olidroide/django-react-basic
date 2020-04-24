Based in blog post: https://www.valentinog.com/blog/drf/

```
sudo apt install npm

mkdir test_django_react
cd test_django_react/
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject configuration .
django-admin startapp core
cd test_django_react/

pip install coverage
pip freeze > requirements.txt
coverage run --source='.' manage.py test
coverage html
coverage report
django-admin startapp front


mkdir -p ./front/src/components
mkdir -p ./front/{static,templates}/front
cd ./front
npm init -y
npm i webpack webpack-cli --save-dev
```

package.json

```json
"scripts": {
  "dev": "webpack --mode development ./src/index.js --output ./static/front/main.js",
  "build": "webpack --mode production ./src/index.js --output ./static/front/main.js"
}
```

babel

```shell script
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
```

.babelrc

```json
{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

webpack.config.js

```
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
```

```
npm run dev
cd ..
python manage.py runserver
```
