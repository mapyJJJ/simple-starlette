import pytest

def test_allow_methods(app):
    assert app.allow_default_methods == ["get", "post"]

    with pytest.raises(TypeError):
        app.allow_default_methods = ["error", 1]

def test_app_conf(app):
    assert app.config["ENV"] == None
    app.load_conf_from_file('tests/conf.json')
    assert app.config["ENV"] == "test_json"
    app.load_conf_from_file('tests/conf.py')
    assert app.config["ENV"] == "test_py"

    app.config["ENV"] = "test"
    assert app.config["ENV"] == "test"
 
