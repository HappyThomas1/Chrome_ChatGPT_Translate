window.onload = function() {
    chrome.runtime.sendMessage({from: 'popup', subject: 'loadData'}, function(response) {
        var textWithBreaks = response.text.replace(/\n/g, '<br>');
        document.getElementById('result-text').innerHTML = textWithBreaks;
    });
};