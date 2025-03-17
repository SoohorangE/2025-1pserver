function Send()
{
    var data = {
        'sepal_length' : 8.0,
        'sepal_width' : 1.0,
        'petal_length' : 8.0,
        'petal_width' : 1.0
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
        output.innerHTML = 'prediction : ' + response.prediction;
    }).fail(function(response) {
        alert("fail" + JSON.stringify(response))
    }).always(function() {
        
    })
}