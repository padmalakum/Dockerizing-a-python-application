$(document).on('submit', '#post-form', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: 'create/',
        data: {
            text: $('#text').val(),
            start: $('#start').val(),
            end: $('#end').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            $('#validation').text(data.error)
            useReturnData(data)
            $('#validation').text("")
        }
    })
})

function useReturnData(data){
    $('#successMessage').text("");
    $('#textData').html("");
    textData = data.text;
    start = parseInt(data.start);
    end = parseInt(data.end);
    let arr=[...textData];
    let colors = ['#CD5C5C','#228B22','#F4A460','#800080','#FFD700','#32CD32','#DC143C','#66CDAA','#0000FF','#FF0000','#9ACD32','#48D1CC','#BC8F8F','#7FFF00']
    let result = '';
    for(let i = 1; i <= arr.length; i++){
        if(i >= start && i <=end){
            result += '<span style="color:' + colors[Math.floor(i % colors.length)] + '">' + arr[i-1] + '</span>';
        }
        else{
            result += arr[i-1];
        }
    }
    $('#textData').html(result);
    $('#successMessage').text(data.success_message);
};