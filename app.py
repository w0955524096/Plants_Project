import flask
from app.route import get_color
from app.orm import get_xlsxoutput


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def extract_imgcolor(_images):
    #_images傳進來的圖片陣列
    # get_color.get_normalcolor(_images)

    res = get_color.get_edgecolor(_images)
    
    # get_xlsxoutput.get_xlsxoutput(get_color.get_edgecolor(_images))
    
    return res


app.run(host='0.0.0.0')