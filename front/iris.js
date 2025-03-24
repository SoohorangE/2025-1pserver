function drawChart(probability, pid)
{
        var data = google.visualization.arrayToDataTable([
          ['iris species', 'probability'],
          ['setosa',     probability[0][0]],
          ['versicolor',      probability[0][1]],
          ['virginica',  probability[0][2]],
        ]);

        var options = {
          title: '붓꽃 품종 확률',
            is3d: true,
            pieHole: 0.41
        };

        var chart = new google.visualization.PieChart(pid);

        chart.draw(data, options);
}

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

        google.charts.setOnLoadCallback(drawChart(response.probability, document.getElementById('piechart')))

    }).fail(function(response) {
        alert("fail" + JSON.stringify(response))
    }).always(function() {
        
    })
}