function Send()
{
    sl = document.getElementById('sl').value
    sw = document.getElementById('sw').value
    pl = document.getElementById('pl').value
    pw = document.getElementById('pw').value

    var data = {
        'sepal_length' : sl,
        'sepal_width' : sw,
        'petal_length' : pl,
        'petal_width' : pw
    }
    
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/predict",
        headers: {
            'Content-Type': 'application/json'
        },
        data : JSON.stringify(data),
        dataType: 'json'

    }).done(function(response) {
        var output = document.getElementById('txtOut');
        output.innerText = 'prediction : ' + response.prediction + "일 확률: " + response.probability
    }).fail(function(response) {
        alert("fail" + JSON.stringify(response))
    }).always(function() {
        
    })
}